# -*- coding:utf-8 -*-

try:
    from .MysqlFunc import MysqlCommonQuery
    from .CommonFunc import CommonFunc
    from .MyExceptions import *
    from .Backend import Backend
    from .Config import *
except Exception:
    from MysqlFunc import MysqlCommonQuery
    from CommonFunc import CommonFunc
    from MyExceptions import *
    from Backend import Backend
    from Config import *


class OperateFuncOfMysql(MysqlCommonQuery):
    """
    管理后台运营模块MYSQL相关功能
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, *args, **kwargs):
        super().__init__(mysql_info, args, kwargs)
        self.cf = CommonFunc()


class OperateFuncOfInterface(Backend):
    """
    管理后台报表管理模块接口相关功能
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, backend_url="http://192.168.10.11:6100", *args, **kwargs):
        super().__init__(mysql_info, backend_url, *args, **kwargs)

    def get_match_result(self, sport_name="足球", tournament_id="", team_id="", match_date_diff=0):
        """
        总台 - 赛果
        """
        url = self.auth_url + "/matchResult/queryCreditManagementMatchResultList"
        match_data = []
        match_date = self.cf.get_md_date_by_now(
            diff=match_date_diff) if (match_date_diff or match_date_diff == 0) else ""
        for page in range(1, 1000):
            params = {"page": page, "limit": 50, "endTime": match_date, "sportId": small_sport_id_dic[sport_name],
                      "tournamentId": tournament_id, "teamId": team_id}
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            for item in rtn["data"]["data"]:
                period_score_list = []
                for score in item["periodScore"]:
                    if (score["homeTeamScore"] or score["homeTeamScore"] == 0) or (score["awayTeamScore"] or
                                                                                   score["awayTeamScore"] == 0):
                        period_score = [score["homeTeamScore"], score["awayTeamScore"]]
                    else:
                        period_score = ""
                    period_score_list.append(period_score)
                # matchStatus: 已完成、比赛取消、比赛终止
                match_data.append([item["matchId"], item["matchSchedule"], item["tournamentName"], item["homeTeamName"],
                                   item["awayTeamName"], item["matchStatus"], period_score_list])
            if page >= rtn["data"]["totalPage"]:
                break
        return match_data

    def get_order_history(self, if_settled=True):
        """
        历史注单
        :param if_settled:   是否已结算，  历史注单True | 即时注单False
        """
        url = self.auth_url + "/order/queryOrderDetailsList"
        order_list = []

        for page in range(1, 100):
            if if_settled:
                params = {"page": page, "limit": 200, "sortBy": "", "sortParameter": "", "level1AgentId": "",
                          "level2AgentId": "", "level3AgentId": "", "orderNo": "", "settlementResult": "",
                          "sportCategoryId": "", "userName": "",
                          "status": "1", "manageLogo": True, "startCreateTime": "", "endCreateTime": ""}
            else:
                params = {"page": page, "limit": 200, "sortBy": "", "sortParameter": "", "level1AgentId": "",
                          "level2AgentId": "", "level3AgentId": "", "orderNo": "", "sportCategoryId": "",
                          "userName": "", "manageLogo": True, "startCreateTime": "", "endCreateTime": ""}
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()
            for item in rtn["data"]["data"]:
                order_list.append([item["orderNo"], item["userName"], item["sportCategoryName"], item["createTime"],
                                   item["betAmount"], item["accountWinOrLose"], item["backwaterAmount"],
                                   item["accountFinalWinOrLose"], item["settlementResult"],
                                   item["level0AgentAccount"], item["level0Percentage"], item["level0BackwaterAmount"]])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list

    def get_mts_report_list(self, user_name="", order_no="", sport_name="", settlement_result="", order_status="",
                            bet_type="", bet_start_diff="", bet_stop_diff="", award_start_diff="", award_end_diff=""):
        """
        获取数据源对账报表 - 列表数据
        """
        url = self.auth_url + "dataSourceCheckReport/getPage"
        if bet_type == "单注":
            bet_type_str = "1"
        elif bet_type == "串关":
            bet_type_str = "2"
        else:
            bet_type_str = ""

        if order_status == "已结算":
            order_status_str = ["1"]
        elif order_status == "未结算":
            order_status_str = ["2"]
        elif order_status == "投注失败":
            order_status_str = ["3"]
        else:
            order_status_str = ""

        order_list = []
        for page in range(1, 1000):
            params = {"betStartTime": f"{self.cf.get_md_date_by_now(diff=bet_start_diff)} 00:00:00",
                      "betEndTime": f"{self.cf.get_md_date_by_now(diff=bet_stop_diff)} 00:00:00",
                      "betType": bet_type_str,
                      "limit": 200,
                      "orderNo": order_no,
                      "page": page,
                      "settlementEndTime": f"{self.cf.get_md_date_by_now(diff=award_end_diff)} 00:00:00",
                      "settlementResult": "" if not settlement_result else [settlement_result_dic[settlement_result]],
                      "settlementStartTime": f"{self.cf.get_md_date_by_now(diff=award_start_diff)} 00:00:00",
                      "sortBy": "",
                      "sortIndex": "",
                      "sortParameter": "",
                      "sportId": [small_sport_id_dic[sport_name]],
                      "status": order_status_str,
                      "userName": user_name}
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            order_list = [[item["orderNo"], item["betType"], item["sportName"], item["userName"], item["betTime"],
                           item["betAmount"], item["settlementTime"], item["statusName"], item["settlementResult"],
                           item["accountFinalWinOrLose"], item["handicapFinalWinOrLose"]] for item in
                          rtn["data"]["data"]]
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list