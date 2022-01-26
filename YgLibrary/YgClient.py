import datetime
import hashlib
import json
import re

import requests

try:
    from .MysqlFunc import MysqlCommonQuery
    from .MongoFunc import DbQuery
    from .CommonFunc import CommonFunc
    from .merchantFunc import MerchantFunc
    from .Config import *
except Exception:
    from MysqlFunc import MysqlCommonQuery
    from MongoFunc import DbQuery
    from CommonFunc import CommonFunc
    from merchantFunc import MerchantFunc
    from Config import *

sport_name_id_dic = {}
for value in sport_id_dic.items():
    sport_name_id_dic[value[1]] = value[0]


class ClientFuncOfMysql(MysqlCommonQuery):
    """
    管理后台报表管理模块MYSQL相关功能
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, *args, **kwargs):
        self.cf = CommonFunc()
        self.db = DbQuery(mongo_info)
        super().__init__(mysql_info, mongo_info, args, kwargs)

    def get_unsettled_order_list_sql(self, player_name, client_type="h5"):
        """
        获取客户端交易记录
        :param player_name:
        :param client_type: 客户端类型： pc|h5
        :return:
        """
        sql = 'select distinct bet_type as "几串",a.create_time as "投注时间",a.order_no as "注单号",bet_amount as ' \
              '"投注金额",b.tournament_name_dic as "联赛名称",b.home_team_name_dic as "主队名称",b.away_team_name_dic as ' \
              '"客队名称",b.market_name_dic as "盘口名称",b.odds_type as "赔率类型",outcome_name_dic' \
              ' "投注项名称",if(odds_type=1,b.credit_odds,b.credit_odds-1) as "赔率",spliced_outcome_id,(case when ' \
              'sub_order_status=0 then "待确认" when ((bet_type=1 and status in (0,1,2,4)) or (bet_type>1 and ' \
              'sub_order_status=1)) then "未结算" when (bet_type>1 and sub_order_status=2 and sub_settlement_result=1)' \
              ' then "赢" when (bet_type>1 and sub_order_status=2 and sub_settlement_result=2) then "输" when ' \
              '(bet_type>1 and sub_order_status=2 and sub_settlement_result=3) then "半赢" when (bet_type>1 and ' \
              'sub_order_status=2 and sub_settlement_result=4) then "半输" when (bet_type>1 and sub_order_status=2 ' \
              'and sub_settlement_result=6) then "走盘" when (bet_type>1 and sub_order_status=4) then "取消" end) ' \
              'as "赛果",b.market_id,b.match_id,specifier,sub_order_status,producer,sport_id from o_account_order ' \
              'a join o_account_order_detail b on a.order_no=b.order_no where ' \
              f'a.user_name="{player_name}" and a.status in (0,1,2,4,5) order by a.create_time desc'
        print(sql)
        rsp = self.query_data(sql, 'bfty_credit')
        order_info = []
        order_no_list = []
        for item in rsp:
            tournament_name = json.loads(item[4])["zh"]
            home_name = json.loads(item[5])["zh"]
            away_name = json.loads(item[6])["zh"]
            market_name = json.loads(item[7])["zh"]
            outcome_name = json.loads(item[9])["zh"]
            odds = float(item[10])
            create_time = item[1].strftime("%Y-%m-%d %H:%M:%S")
            bet_type = int(item[0])

            score = self.db.get_order_result_score(item[14], item[13], item[15])
            if (bet_type == 1 and item[12] == "未结算") or item[12] == "待确认" or (item[16] in (0, 1)):
                score = ""

            if client_type == "h5":
                detail_data = [item[11], home_name, away_name, market_name, item[8], odds, item[12], score]
                if item[2] not in order_no_list:
                    order_no_list.append(item[2])
                    order_info.append(
                        [bet_type if bet_type > 1 else tournament_name, create_time, item[3], item[2], [detail_data]])
                else:
                    order_index = order_no_list.index(item[2])
                    order_info[order_index][-1].append(detail_data)
            else:
                detail_data = [item[11], item[4], home_name, away_name, item[17], market_name, item[8], odds,
                               item[12], score]
                if item[2] not in order_no_list:
                    order_no_list.append(item[2])
                    order_info.append(
                        [create_time, item[2], item[3], item[12], item[18], [detail_data]])
                else:
                    order_index = order_no_list.index(item[2])
                    order_info[order_index][-1].append(detail_data)

        return order_info

    def get_unsettled_order_total_sql(self, player_name):
        """
        获取客户端交易记录,总计
        :param player_name:
        :return:
        """
        sql = 'select count(1) as "总计单数",sum(bet_amount) as "投注额" from o_account_order a where a.user_name=' \
              f'"{player_name}" and a.status in (0,1,2,4,5)'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]

    def get_settled_order_history_detail_total_h5_sql(self, player_name, date_diff, sport_name=""):
        """
        获取投注记录里面的已结算按天总计
        """
        award_date = self.cf.get_md_date_by_now(diff=date_diff)
        sport_str = "" if not sport_name else f'and sport_id="{small_sport_id_dic[sport_name]}"'
        date_str = f' and DATE_FORMAT(a.award_time,"%Y-%m-%d")="{award_date}" '
        sql = 'select count(1) as "总单数",sum(bet_amount) as "投注额",sum(handicap_final_win_or_lose) as "输赢" from ' \
              '(select distinct a.* from o_account_order a join o_account_order_detail b on a.order_no=b.order_no ' \
              f'where a.user_name="{player_name}" and ' \
              f'a.status in (3,6) {date_str} {sport_str}) a'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]

    def get_settled_order_history_detail_list_sql(self, player_name, date_diff, sport_name="", client_type='h5'):
        """
        获取投注记录里面的已结算按天明细列表
        :param player_name:
        :param date_diff:
        :param sport_name:
        :param client_type: 客户端类型： pc|h5
        """
        award_date = self.cf.get_md_date_by_now(diff=date_diff)
        sport_str = "" if not sport_name else f'and sport_id="{small_sport_id_dic[sport_name]}"'
        date_str = f' and DATE_FORMAT(a.award_time,"%Y-%m-%d")="{award_date}" '
        sql = 'select distinct bet_type as "几串",a.create_time as "投注时间",a.order_no as "注单号",bet_amount as' \
              ' "投注金额",round(a.handicap_win_or_lose,2) as "输赢",round(backwater_amount,2) as "返水",' \
              'round(handicap_final_win_or_lose+bet_amount,2) as "返回金额",b.tournament_name_dic as "联赛名称",' \
              'b.home_team_name_dic as "主队名称",b.away_team_name_dic as "客队名称",' \
              'b.market_name_dic as "盘口名称",b.odds_type as "赔率类型",outcome_name_dic "投注项名称",if(odds_type=1,' \
              'b.credit_odds,b.credit_odds-1) as "赔率",spliced_outcome_id,(case when (sub_order_status=3 and ' \
              'sub_settlement_result=1) then "赢" when (sub_order_status=3 and sub_settlement_result=2) then "输" ' \
              'when (sub_order_status=3 and sub_settlement_result=3) then "半赢" when (sub_order_status=3 and ' \
              'sub_settlement_result=4) then "半输" when (sub_order_status=3 and sub_settlement_result=6) ' \
              'then "平局" when (sub_order_status=6) then "取消" end) as "赛果",b.market_id,b.match_id,specifier,' \
              'b.spliced_outcome_id,(case when a.settlement_result=1 then "赢" when a.settlement_result=2 then "输" ' \
              'when a.settlement_result=3 then "半赢" when a.settlement_result=4 then "半输" when (a.status=3 and ' \
              'a.settlement_result=6) then "走盘" when (a.status=6 and a.settlement_result=6) then "取消" end) ' \
              'as "状态",sport_id from o_account_order a join o_account_order_detail' \
              f' b on a.order_no=b.order_no where a.user_name="{player_name}" and a.status in (3,6) ' \
              f'{sport_str}{date_str} order by a.create_time desc'
        rsp = self.query_data(sql, 'bfty_credit')
        order_info = []
        order_no_list = []
        for item in rsp:
            tournament_name = json.loads(item[7])["zh"]
            home_name = json.loads(item[8])["zh"]
            away_name = json.loads(item[9])["zh"]
            market_name = json.loads(item[10])["zh"]
            outcome_name = json.loads(item[12])["zh"]
            odds = float(item[13])
            create_time = item[1].strftime("%Y-%m-%d %H:%M:%S")
            bet_type = int(item[0])
            score = self.db.get_order_result_score(item[17], item[16], item[18])
            # if int(item[-4]) in [53, 54, 58, 59]:
            #     pp = item[2]
            if item[15] == "取消":
                score = []

            if client_type == 'h5':
                detail_data = [item[19], home_name, away_name, market_name, item[11], odds, item[15], score]
                if item[2] not in order_no_list:
                    order_no_list.append(item[2])
                    order_info.append(
                        [bet_type if bet_type > 1 else tournament_name, create_time, item[3], item[4], item[5], item[6],
                         item[2], [detail_data]])
                else:
                    order_index = order_no_list.index(item[2])
                    # detail_data = [item[14], home_name, away_name, market_name, item[11], odds, item[15]]
                    order_info[order_index][-1].append(detail_data)
            else:
                detail_data = [item[14], tournament_name, home_name, away_name, market_name, item[11], odds,
                               item[15], score]
                if item[2] not in order_no_list:
                    order_no_list.append(item[2])
                    order_info.append(
                        [create_time, item[2], item[3], item[4], item[5], item[6], item[20], item[21], [detail_data]])
                else:
                    order_index = order_no_list.index(item[2])
                    order_info[order_index][-1].append(detail_data)
        return order_info

    def get_settled_order_history_total_list_sql(self, player_name, date_start_diff=-30, date_end_diff=None):
        """
        获取投注记录里面的已结算总计中的明细列表
        :param player_name:
        :param date_start_diff:
        :param date_end_diff:  不传值则为PC，传值则为H5
        """
        date_start_diff = int(date_start_diff)
        date_end_diff = int(date_end_diff) if date_end_diff is not None else ""
        start_date = self.cf.get_md_date_by_now(diff=date_start_diff) if date_start_diff else ""
        end_date = self.cf.get_md_date_by_now(diff=date_end_diff) if type(date_end_diff) == int else ""
        date_str = ""
        if start_date:
            date_str = f' and DATE_FORMAT(award_time,"%Y-%m-%d")>"{start_date}" '
        if type(date_end_diff) == int:
            date_str = f' and (DATE_FORMAT(award_time,"%Y-%m-%d")>="{start_date}" and ' \
                       f'DATE_FORMAT(award_time,"%Y-%m-%d")<"{end_date}")'
        if type(date_end_diff) != int:
            sql = 'select DATE_FORMAT(award_time,"%Y-%m-%d") as "日期",count(1) as "单数",sum(bet_amount) as "投注金额",' \
                  'sum(if(status=3,bet_amount,0)) as "有效金额",round(sum(handicap_final_win_or_lose),2) as "输赢" ' \
                  f'from o_account_order where user_name="{player_name}" and status in (3,6) {date_str} group by ' \
                  f'DATE_FORMAT(award_time,"%Y-%m-%d") order by DATE_FORMAT(award_time,"%Y-%m-%d") desc'
        else:
            sql = 'select DATE_FORMAT(award_time,"%Y-%m-%d") as "日期",sum(bet_amount) as "投注金额",' \
                  'sum(if(status=3,bet_amount,0)) as "有效金额",round(sum(handicap_final_win_or_lose),2) as "输赢",' \
                  f'round(sum(backwater_amount),2) as "返水" from o_account_order where user_name="{player_name}" ' \
                  f'and status in (3,6) {date_str} group by ' \
                  f'DATE_FORMAT(award_time,"%Y-%m-%d") order by DATE_FORMAT(award_time,"%Y-%m-%d") desc'
        rsp = self.query_data(sql, 'bfty_credit')
        return [item for item in rsp]

    def get_settled_order_history_total_sum_h5_sql(self, player_name, date_diff):
        """
        获取投注记录里面的已结算总计中的统计列表
        :param player_name:
        :param date_diff:
        """
        award_date = self.cf.get_md_date_by_now(diff=date_diff)
        date_str = f' and DATE_FORMAT(award_time,"%Y-%m-%d")>"{award_date}" '
        sql = f'select count(1) as "单数" from o_account_order where user_name="{player_name}" and status in (3,6) ' \
              f'{date_str}'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0][0]

    def get_settled_order_list_detail_sql(self, merchant_name, player_name, group, date_diff=0, sport_name=None,
                                          order_status=None):
        """
        获取客户端账户历史详情
        :param merchant_name:
        :param player_name:
        :param group:
        :param date_diff: 日期偏移
        :param sport_name:
        :param order_status: 全部注单|赢|输|半赢|半输|注单平局|注单取消
        :return:
        """
        order_status_dic = {"赢": 1, "输": 2, "半赢": 3, "半输": 4, "注单平局": 6}
        date = self.cf.get_md_date_by_now(diff=date_diff)
        sport_name_str = "" if not sport_name else f' and a.sport_category_id="{sport_id_dic[sport_name]}" '
        order_status = "全部注单" if not order_status else order_status
        if order_status == "全部注单":
            status_str = " and status in (2, 3,4,6,8)"
        elif order_status == "注单取消":
            status_str = " and status in (4, 6, 8) "
        elif order_status in ["半赢", "半输"]:
            status_str = f" and bet_type=1 and status in (2,3) and settlement_result={order_status_dic[order_status]} "
        else:
            status_str = f" and status in (2, 3) and settlement_result={order_status_dic[order_status]} "

        sql = 'select b.match_id,market_id,b.specifier,a.order_no,a.create_time,a.sport_category_id,' \
              'IF(bet_type=1,b.market_name_dic,"综合过关"),' \
              'bet_amount,(case when status in (4,6,7,8) then 0 when ISNULL(rebate_amount) and status not in ' \
              '(4,6,7,8) then -bet_amount else rebate_amount-bet_amount+ifnull(backwater_amount,0) end) as "输赢",' \
              '(case when status in (4,6,7,8) then "注单取消" when ' \
              'settlement_result=1 then "赢" when settlement_result=2 then "输" when settlement_result=3 then "半赢" ' \
              'when settlement_result=4 then "半输" when status in (2,3) and settlement_result=6 then "注单平局" when ' \
              'status ' \
              'in (4,6,7,8) then "注单取消" end) as "注单状态",b.market_name_dic,b.tournament_name_dic,home_team_name_dic,' \
              'away_team_name_dic,outcome_name_dic,bet_score,odds,b.match_time,(case when sub_order_status in (2,3) ' \
              'and sub_settlement_result="1" then "赢" when sub_order_status in (2,3) and sub_settlement_result="2" ' \
              'then "输" when sub_order_status in (2,3) and sub_settlement_result="3" then "半赢" when ' \
              'sub_order_status in (2,3) and sub_settlement_result="4" then "半输" when sub_order_status in (2,3) ' \
              'and sub_settlement_result="6" then "注单平局" when sub_order_status in (4,6,7,8) then "注单取消" end) as ' \
              '"子注单状态" from biz_order a join biz_order_detail b on a.order_no=b.order_no where ' \
              f'a.merchant_name="{merchant_name}" and a.user_name="{player_name}" and ' \
              f'a.merchant_user_group_id="{group}" and DATE_FORMAT(CONVERT_TZ(' \
              f'a.match_start_time,"+00:00","-04:00"),"%Y-%m-%d")="{date}" {sport_name_str} {status_str} ' \
              f'order by a.create_time desc'
        rsp = self.query_data(sql, 'business_order')
        order_info = []
        order_no_list = []

        # 全场、半场
        full_score_market_list = [1, 2, 3, 10, 11, 12, 13, 15, 16, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29, 31, 32,
                                  33, 34, 35, 36, 37, 45, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 186, 188,
                                  199, 219, 223, 225, 227, 228, 229, 251, 256, 258, 314, 546, 547]
        half_score_market_list = [47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 63, 64, 66, 68, 69, 70, 71, 74,
                                  75, 76, 77, 78, 79, 81, 81, 542]
        # 角球
        corner_score_market_list = [165, 166, 169, 170, 171, 172]
        half_corner_score_market_list = [176, 177, 180, 181, 182, 183]
        # 总得分
        all_score_market_list = [187, 189, 190, 191, 237, 238, 406, 410]
        # 点球
        penalty_score_market_list = [123, 127]
        # 加时
        over_time_score_market_list = [2, 3, 113, 116, 117, 119, 120, 406, 410]
        # 阶段比分
        period_score_market_list = [104, 202, 203, 204, 236, 245, 246, 247, 248, 303, 304, 756, 757, 309, 310, 311]
        # 罚牌
        card_market_list = [139, 142, 143, 144]
        half_card_market_list = [152, 155, 156, 157]
        for item in rsp:
            nr_period_score = None
            over_time_score = ""
            period_score_dic = {}
            period_score = {}
            all_score = ""
            full_score = ""
            half_score = ""
            penalty_score = ""
            # 罚牌数，角球数
            card_number_list = [0, 0]
            corner_number_list = [0, 0]
            half_corner_number_list = [0, 0]
            half_card_score_list = [0, 0]

            rtn = self.db.get_match_score_msql_new(item[0])
            match_score = rtn[0]
            sport_id = match_score["tournamentSportId"]
            if "periodScores" in match_score:
                period_data = match_score["periodScores"]
                for period in period_data:
                    period_score.update({str(period["number"]): {"zh": period['periodDescription'],
                                                                 "home": period['homeScore'],
                                                                 "away": period['awayScore']}})
                home_all_score = away_all_score = 0
                for value in match_score['periodScores']:
                    home_all_score += int(value["homeScore"])
                    away_all_score += int(value["awayScore"])
                all_score = f"{home_all_score} - {away_all_score}"

                full_score_list = [0, 0]
                half_score_list = [0, 0]
                # 遍历每一条period score
                for period_data in match_score['periodScores']:
                    # 如果是足球篮球，区分上下半场，全场不包括加时赛
                    if sport_id == small_sport_id_dic["足球"]:
                        if period_data["number"] == 1:
                            half_score_list = [period_data["homeScore"], period_data["awayScore"]]
                        if period_data["number"] in (1, 2):
                            full_score_list[0] += int(period_data["homeScore"])
                            full_score_list[1] += int(period_data["awayScore"])
                    # 篮球分上下半场，全场包括加时赛
                    elif sport_id == small_sport_id_dic["篮球"]:
                        if period_data["number"] in (1, 2):
                            half_score_list[0] += int(period_data["homeScore"])
                            half_score_list[1] += int(period_data["awayScore"])
                        full_score_list[0] += int(period_data["homeScore"])
                        full_score_list[1] += int(period_data["awayScore"])
                    # 冰棍球全场不包括加时
                    elif sport_id == small_sport_id_dic["冰上曲棍球"] and "加时" not in \
                            period_data['periodDescription']:
                        full_score_list[0] += int(period_data["homeScore"])
                        full_score_list[1] += int(period_data["awayScore"])
                    elif sport_id in [small_sport_id_dic["羽毛球"], small_sport_id_dic["乒乓球"],
                                      small_sport_id_dic["网球"], small_sport_id_dic["排球"]]:
                        if int(period_data["homeScore"]) > int(period_data["awayScore"]):
                            full_score_list[0] += 1
                        elif int(period_data["homeScore"]) < int(period_data["awayScore"]):
                            full_score_list[1] += 1
                    # 棒球全场包括加时赛
                    # elif sport_id == small_sport_id_dic["棒球"]:
                    else:
                        full_score_list[0] += int(period_data["homeScore"])
                        full_score_list[1] += int(period_data["awayScore"])

                half_score = f'{half_score_list[0]} - {half_score_list[1]}'
                full_score = f'{full_score_list[0]} - {full_score_list[1]}'
                for score in match_score["periodScores"]:
                    if score["periodDescription"] == "点球":
                        penalty_score = f"{score['homeScore']} - {score['awayScore']}"

            if "periodStatisticsMap" in match_score:
                for index, name in enumerate(["1st half", "2nd half"]):
                    # 有periodStatisticsMap字段
                    if name in match_score["periodStatisticsMap"]:
                        # 计算角球
                        for corner_data in match_score["periodStatisticsMap"][name]:
                            if corner_data["homeAway"] == "Home":
                                corner_number_list[0] += corner_data["corner"] if "corner" in corner_data else 0
                                if name == "1st half":
                                    half_corner_number_list[0] += corner_data[
                                        "corner"] if "corner" in corner_data else 0
                            else:
                                corner_number_list[1] += corner_data["corner"] if "corner" in corner_data else 0
                                if name == "1st half":
                                    half_corner_number_list[1] += corner_data[
                                        "corner"] if "corner" in corner_data else 0
                        # 计算罚牌
                        for index2, color in enumerate(["yellow", "red", "yellowRed"]):
                            for card_data in match_score["periodStatisticsMap"][name]:
                                # 若有该颜色，则相应的增加罚牌数
                                if color in card_data:
                                    if index2 == 0:
                                        if card_data["homeAway"] == "Home":
                                            card_number_list[0] += card_data[color]
                                            if name == "1st half":
                                                half_card_score_list[0] += card_data[color]
                                        else:
                                            card_number_list[1] += card_data[color]
                                            if name == "1st half":
                                                half_card_score_list[1] += card_data[color]
                                    else:
                                        if card_data["homeAway"] == "Home":
                                            card_number_list[0] += card_data[color] * 2
                                            if name == "1st half":
                                                half_card_score_list[0] += card_data[color] * 2
                                        else:
                                            card_number_list[1] += card_data[color] * 2
                                            if name == "1st half":
                                                half_card_score_list[1] += card_data[color] * 2
            card_score = f"{card_number_list[0]} - {card_number_list[1]}"
            corner_score = f"{corner_number_list[0]} - {corner_number_list[1]}"
            half_card_score = f"{half_card_score_list[0]} - {half_card_score_list[1]}"
            half_corner_score = f"{half_corner_number_list[0]} - {half_corner_number_list[1]}"

            key_list = list(period_score.keys())
            key_list.sort()
            for key in key_list:
                if "加时" in period_score[key]["zh"]:
                    over_time_score = f'{period_score[key]["home"]} - {period_score[key]["away"]}'
                else:
                    period_score_dic[key] = f'{period_score[key]["home"]} - {period_score[key]["away"]}'
            reg_result = re.search(r"nr=([\d.]+)", item[2])

            if reg_result and period_score_dic and (int(item[1]) in period_score_market_list):
                nr = str(reg_result.group(1))
                nr_period_score = period_score_dic[nr]

            if item[3] not in order_no_list:
                order_no_list.append(item[3])
                order_detail_list = list(item[3:10])
                order_detail_list[3] = json.loads(order_detail_list[3])["zh"] if order_detail_list[3] != "综合过关" \
                    else order_detail_list[3]
                order_detail_list[1] = order_detail_list[1].strftime("%Y-%m-%dT%H:%M:%S.000Z")
                order_detail_list[2] = sport_name_id_dic[int(order_detail_list[2])]
                temp_data = [[json.loads(item[10])["zh"], json.loads(item[11])["zh"], json.loads(item[12])["zh"],
                              json.loads(item[13])["zh"], item[15], item[16],
                              item[17].strftime("%Y-%m-%dT%H:%M:%S.000Z"), item[18]]]
                # 比分
                if temp_data[0][7] != "注单取消":
                    score_list = []
                    if int(item[1]) in full_score_market_list and full_score:
                        score_list.append(full_score)
                    if int(item[1]) in half_score_market_list and half_score:
                        score_list.append(half_score)
                    if int(item[1]) in corner_score_market_list and corner_score:
                        score_list.append(corner_score)
                    if int(item[1]) in penalty_score_market_list and penalty_score:
                        score_list.append(penalty_score)
                    if int(item[1]) in all_score_market_list and all_score:
                        score_list.append(all_score)
                    if int(item[1]) in over_time_score_market_list and over_time_score:
                        score_list.append(over_time_score)
                    if int(item[1]) in period_score_market_list and nr_period_score:
                        score_list.append(nr_period_score)
                    if int(item[1]) in card_market_list and card_score:
                        score_list.append(card_score)
                    if int(item[1]) in half_corner_score_market_list and half_corner_score:
                        score_list.append(card_score)
                    if int(item[1]) in half_card_market_list and half_card_score:
                        score_list.append(card_score)
                    temp_data[-1].append(score_list)
                if len(temp_data[-1]) == 8:
                    temp_data[-1].append([])

                order_detail_list.append(temp_data)
                order_info.append(order_detail_list)
            else:
                temp_data = [json.loads(item[10])["zh"], json.loads(item[11])["zh"], json.loads(item[12])["zh"],
                             json.loads(item[13])["zh"], item[15], item[16],
                             item[17].strftime("%Y-%m-%dT%H:%M:%S.000Z"), item[18]]
                if temp_data[-1] != "注单取消":
                    score_list = []
                    market_id = int(item[1])
                    if market_id in full_score_market_list and full_score:
                        score_list.append(full_score)
                    if market_id in half_score_market_list and half_score:
                        score_list.append(half_score)
                    if market_id in corner_score_market_list and corner_score:
                        score_list.append(corner_score)
                    if market_id in penalty_score_market_list and penalty_score:
                        score_list.append(penalty_score)
                    if market_id in all_score_market_list and all_score:
                        score_list.append(all_score)
                    if market_id in over_time_score_market_list and over_time_score:
                        score_list.append(over_time_score)
                    if market_id in period_score_market_list and nr_period_score:
                        score_list.append(nr_period_score)
                    temp_data.append(score_list)
                if len(temp_data) == 8:
                    temp_data.append([])
                order_info[-1][-1].append(temp_data)
        for index, item in enumerate(order_info):
            if item[2] == "其它":
                order_info[index][2] = "其他"
        return order_info

    def get_order_settled_history_sql(self, user_account, start_diff=-30, end_diff=0):
        """
        历史注单
        """
        start_day = self.cf.get_md_date_by_now(diff=start_diff)
        end_day = self.cf.get_md_date_by_now(diff=end_diff)
        sql = 'select order_no as "注单号",user_name as "会员账号",(case when sport_id="sr:sport:1" then "足球" when ' \
              'sport_id="sr:sport:2" then "篮球"when sport_id="sr:sport:5" then "网球"when sport_id="sr:sport:31" ' \
              'then "羽毛球" when sport_id="sr:sport:20" then "乒乓球" when sport_id="sr:sport:23" then "排球" when ' \
              'sport_id="sr:sport:3" then "棒球" when sport_id="sr:sport:4" then "冰上曲棍球" end) as "体育项目",' \
              'a.create_time as "投注时间",bet_amount as "投注金额",handicap_win_or_lose as "输赢",' \
              'round(backwater_amount,2) as "返水",handicap_final_win_or_lose as "最终输赢",(case when ' \
              'a.status=6 and settlement_result=6 then "注单取消" when settlement_result=1 then "赢" when ' \
              'settlement_result=2 then "输" when settlement_result=3 then "赢一半" when settlement_result=4 ' \
              'then "输一半" when settlement_result=6 then "注单平局" end) as "注单结果",c.account as "代理线",' \
              'concat(round(level0_actual_percentage*100,0),"%") as "代理线占成",if(a.status=3,round(bet_amount*' \
              'level0_retreat_proportion,2),0) as "代理线退水" from o_account_order a join u_user b on a.user_id=b.id ' \
              'join m_account c on b.proxy0_id=c.id where (DATE_FORMAT(a.create_time,"%Y-%m-%d") between ' \
              f'"{start_day}" and "{end_day}") and a.status in (3,6) and c.account="{user_account}"'
        rsp = self.query_data(sql, 'bfty_credit')
        data_list = [list(item) for item in rsp]
        for index, item in enumerate(data_list):
            item[3] = datetime.datetime.strftime(item[3], "%Y-%m-%d %H:%M:%S")
            data_list[index] = item
        return data_list

    def get_order_unsettled_history_sql(self, user_account, start_diff=-30, end_diff=0):
        """
        即时注单
        """
        start_day = self.cf.get_md_date_by_now(diff=start_diff)
        end_day = self.cf.get_md_date_by_now(diff=end_diff)
        sql = 'select order_no as "注单号",user_name as "会员账号",(case when sport_id="sr:sport:1" then "足球" when ' \
              'sport_id="sr:sport:2" then "篮球"when sport_id="sr:sport:5" then "网球" when sport_id="sr:sport:31" ' \
              'then "羽毛球" when sport_id="sr:sport:20" then "乒乓球" when sport_id="sr:sport:23" then "排球" when ' \
              'sport_id="sr:sport:3" then "棒球" when sport_id="sr:sport:4" then "冰上曲棍球" end) as "体育项目",' \
              'a.create_time as "投注时间",bet_amount as "投注金额",c.account as "代理线",' \
              'concat(round(level0_actual_percentage*100,0),"%") as "代理线占成",d.account as "一级代理",' \
              'concat(round(level1_actual_percentage*100,0),"%") as "一级代理占成",e.account as "二级代理",' \
              'concat(round(level2_actual_percentage*100,0),"%") as "二级代理占成",f.account as "三级代理",' \
              'concat(round(level3_actual_percentage*100,0),"%") as "三级代理占成" from o_account_order a join u_user ' \
              'b on a.user_id=b.id join m_account c on b.proxy0_id=c.id join m_account d on b.proxy1_id=d.id join ' \
              'm_account e on b.proxy2_id=e.id join m_account f on b.proxy3_id=f.id where ' \
              f'(DATE_FORMAT(a.create_time,"%Y-%m-%d") between "{start_day}" and "{end_day}") and a.status ' \
              f'in (0,1,2,4,5) and c.account="{user_account}"'
        print(sql)
        rsp = self.query_data(sql, 'bfty_credit')
        data_list = [list(item) for item in rsp]
        for index, item in enumerate(data_list):
            item[3] = datetime.datetime.strftime(item[3], "%Y-%m-%d %H:%M:%S")
            data_list[index] = item
        return data_list


class YgClient(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, client_host, *args, **kwargs):
        self.cf = CommonFunc()
        self.session = requests.session()
        self.db = DbQuery(mongo_info)
        self.order_no_list = []
        # self.host = 'http://192.168.10.120:6210'
        self.host = client_host
        self.head = {"Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9",
                     "Connection": "keep-alive",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/85.0.4183.102 Safari/537.36"}
        self.market_group_dic = {"足球": "100", "篮球": "200", "网球": "300", "排球": "400", "乒乓球": "600",
                                 "棒球": "700", "冰球": "900", "羽毛球": "500"}
        self.mysql = ClientFuncOfMysql(mysql_info, mongo_info)

    def login_client(self, name, password):
        url = self.host + "/creditUser/creditUserLogIn"
        hb = hashlib.md5()
        hb.update(bytes(password, encoding="utf8"))
        params = {"userName": name, "password": hb.hexdigest(),
                  "loginUrl": "http://192.168.10.120:96"}
        rsp = self.session.post(url, json=params)
        if rsp.json()["message"] != "OK":
            raise AssertionError(rsp.json()["message"])
        else:
            return rsp.json()["data"]["accessCode"]

    def get_result_score_h5(self, token, sport_name, diff_unit):
        self.head["accessCode"] = token
        url = self.host + "/creditMatchH5/queryCreditMobileMatchResultList"
        match_result_list = []
        for page in range(1, 1000):
            params = {"marketType": 1,
                      "sportCategoryId": small_sport_id_dic[sport_name],
                      "resultTime": "",
                      "dateOffset": diff_unit,
                      "page": page,
                      "limit": 50}
            print(params)
            rtn = self.session.post(url, json=params, headers=self.head).json()

            for item in rtn["data"]["data"]:
                for match in item["matchList"]:
                    period_score_list = [(period["homeTeamScore"], period["awayTeamScore"]) for period
                                         in match["scoreInfoList"]]
                    match_result_list.append([match["matchId"], match["matchEndTimeString"], item["tournamentName"],
                                              match["homeTeamName"], match["awayTeamName"], period_score_list])
            if page >= rtn["data"]["totalPage"]:
                break
        return match_result_list

    # ------------------ PC ----------------------------------
    def get_result_score_pc(self, token, sport_name, diff_unit):
        """
        PC端赛果查询
        """
        self.head["accessCode"] = token
        url = self.host + "/creditMatchPC/queryCreditMatchResultList"
        match_result_list = []
        for page in range(1, 1000):
            params = {"sportCategoryId": small_sport_id_dic[sport_name],
                      "resultTime": self.cf.get_md_date_by_now(diff=diff_unit),
                      "page": page,
                      "limit": 100}
            rtn = self.session.post(url, json=params, headers=self.head).json()

            for item in rtn["data"]["data"]:
                period_score_list = []
                for period in item["periodScore"]:
                    if (not period["homeTeamScore"] and period["homeTeamScore"] != 0) and (
                            not period["awayTeamScore"] and period["awayTeamScore"] != 0):
                        period_score_list.append("")
                    else:
                        period_score_list.append((period["homeTeamScore"], period["awayTeamScore"]))
                match_result_list.append([item["matchId"], item["matchSchedule"], item["tournamentName"],
                                          item["homeTeamName"], item["awayTeamName"], item["matchStatus"],
                                          period_score_list])
            if page >= rtn["data"]["totalPage"]:
                break
        return match_result_list

    def get_unsettled_order_history_list_pc(self, token):
        """
        获取投注记录里面的未结算列表
        :param token
        """
        url = self.host + "/creditPCOrder/unsettledBet"
        order_data_list = []
        sum_data = []
        self.head["accessCode"] = token

        for page in range(1, 100):
            params = {"page": page, "limit": 100}
            rtn = self.session.post(url, json=params, headers=self.head).json()
            for item in rtn["data"]:
                sub_order_detail = []
                for sub in item["outcomeList"]:
                    result = sub["outcomeResult"]
                    score = re.findall(r':\s*(\d+ - \d+)', str(result))
                    score = [] if not score else score
                    sub_order_detail.append([sub["splicedOutcomeId"], sub["tournamentName"], sub["homeTeamName"],
                                             sub["awayTeamName"], sub["producer"], sub["marketName"], sub["oddsType"],
                                             sub["odds"], sub["outcomeWinOrLoseName"], score])
                order_data_list.append([item["betTime"], item["orderNo"], item["betAmount"],
                                        item["settlementWinOrLoseName"], item["sportId"], sub_order_detail])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_data_list, sum_data

    def get_settled_order_history_total_list_pc(self, token, date_start_diff=-30, date_end_diff=0):
        """
        获取投注记录里面的已结算-按日统计结果
        :param token:
        :param date_start_diff:
        :param date_end_diff:
        :return:
        """
        self.head["accessCode"] = token
        url = self.host + "/creditPCOrder/accountHistoryStatistics"
        day_start = self.cf.get_md_date_by_now("日", date_start_diff)
        day_end = self.cf.get_md_date_by_now("日", date_end_diff)

        params = {"createDay": day_start, "endDay": day_end}
        rtn = self.session.post(url, json=params, headers=self.head).json()

        order_data_list = [[item["date"], item["betAmount"], item["effectiveAmount"], item["profitAmount"],
                            item["backwaterAmount"]] for item in rtn["data"] if (item["betAmount"] or
                                                                                 item["effectiveAmount"] or
                                                                                 item["profitAmount"] or
                                                                                 item["backwaterAmount"])]
        return order_data_list

    def get_settled_order_history_detail_list_pc(self, token, date_diff=0, sport_name=""):
        """
        获取投注记录里面的已结算明细列表
        :param token:
        :param date_diff:
        :param sport_name:
        """
        self.head["accessCode"] = token
        url = self.host + "/creditPCOrder/settledBet"
        order_data_list = []

        for page in range(1, 100):
            params = {"offset": date_diff,
                      "sportCategoryId": small_sport_id_dic[sport_name] if sport_name else "",
                      "page": page,
                      "limit": 100}
            rtn = self.session.post(url, json=params, headers=self.head).json()
            if not rtn["data"]:
                continue

            for item in rtn["data"]:
                sub_order_detail = []
                for sub in item["outcomeList"]:
                    result = sub["outcomeResult"]
                    score = re.findall(r':\s*(\d+ - \d+)', str(result))
                    score = [] if not score else score

                    sub_order_detail.append(
                        [sub["splicedOutcomeId"], sub["tournamentName"], sub["homeTeamName"], sub["awayTeamName"],
                         sub["marketName"], sub["oddsType"], sub["odds"], sub["outcomeWinOrLoseName"], score])
                order_data_list.append(
                    [item["betTime"], item["orderNo"], item["betAmount"], item["profitAmount"],
                     item["backwaterAmount"], item["resultAmount"], item["settlementWinOrLoseName"],
                     item["sportId"], sub_order_detail])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_data_list

    # ----------------------- H5 -----------------------------
    def get_unsettled_order_history_list_h5(self, token):
        """
        获取投注记录里面的未结算列表
        """
        url = self.host + "/creditOrder/bettingRecord"
        order_data_list = []
        sum_data = []
        self.head["accessCode"] = token

        for page in range(1, 1000):
            params = {"page": page, "limit": 50, "settleType": False}
            rtn = self.session.post(url, json=params, headers=self.head).json()
            if page == 1:
                sum_data = [rtn["data"]["totalBetNum"], rtn["data"]["totalBetAmount"]]

            for item in rtn["data"]["orderList"]:
                bet_type = len(item["outcomeList"])
                if bet_type == 1:
                    tournament_name = item["outcomeList"][0]["tournamentName"]
                else:
                    tournament_name = ""
                sub_order_detail = []

                for sub in item["outcomeList"]:
                    result = sub["outcomeResult"]
                    score = re.findall(r':\s*(\d+ - \d+)', str(result))
                    score = [] if not score else score
                    sub_order_detail.append([sub["splicedOutcomeId"], sub["homeTeamName"], sub["awayTeamName"],
                                             sub["marketName"], sub["oddsType"],
                                             sub["odds"], sub["outcomeWinOrLoseName"], score])
                order_data_list.append([bet_type if bet_type > 1 else tournament_name, item["betTime"],
                                        item["betAmount"], item["orderNo"], sub_order_detail])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_data_list, sum_data

    def get_settled_order_history_total_h5(self, token, date_diff):
        """
        获取投注记录里面的已结算总计
        """
        self.head["accessCode"] = token
        url = self.host + "/creditOrder/betSettleRecord"
        today = self.cf.get_md_date_by_now("日", 0)
        day_start = self.cf.get_md_date_by_now("日", date_diff)

        params = {"dateStart": day_start, "dateEnd": today, "settleType": True, "dateOffset": date_diff}
        print(params)
        rtn = self.session.post(url, json=params, headers=self.head).json()
        total_num = rtn["data"]["totalNum"]

        order_data_list = [[item["date"], item["effectiveCount"], item["betAmount"], item["effectiveAmount"],
                            item["profitAmount"]] for item in rtn["data"]["statisticsVOS"] if item["betAmount"]]
        return order_data_list, total_num

    def get_settled_order_history_detail_list_h5(self, token, date_diff=0, sport_name=""):
        """
        获取投注记录里面的已结算明细列表
        :param token:
        :param date_diff:
        :param sport_name:
        """
        self.head["accessCode"] = token
        url = self.host + "/creditOrder/bettingRecord"
        order_data_list = []
        sum_data = []

        for page in range(1, 1000):
            params = {"dateOffset": date_diff, "settleType": True,
                      "sportCategoryId": small_sport_id_dic[sport_name] if sport_name else "", "page": page,
                      "limit": 20}
            rtn = self.session.post(url, json=params, headers=self.head).json()
            if page == 1:
                sum_data = [rtn["data"]["totalCount"], rtn["data"]["totalBetAmount"], rtn["data"]["totalPreProfit"]]

            for item in rtn["data"]["orderList"]:
                bet_type = len(item["outcomeList"])
                if bet_type == 1:
                    tournament_name = item["outcomeList"][0]["tournamentName"]
                else:
                    tournament_name = ""
                sub_order_detail = []
                for sub in item["outcomeList"]:
                    result = sub["outcomeResult"]
                    score = re.findall(r':\s*(\d+ - \d+)', str(result))
                    score = [] if not score else score

                    sub_order_detail.append(
                        [sub["splicedOutcomeId"], sub["homeTeamName"], sub["awayTeamName"], sub["marketName"],
                         sub["oddsType"], sub["odds"], sub["outcomeWinOrLoseName"], score])
                order_data_list.append(
                    [bet_type if bet_type > 1 else tournament_name, item["betTime"], item["betAmount"],
                     item["profitAmount"],
                     item["backwaterAmount"], item["resultAmount"], item["orderNo"], sub_order_detail])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_data_list, sum_data

    def get_match_list_h5(self, token, match_type, sport_name, odds_type=1, if_all=False, diff_unit=""):
        """
        获取滚球sport列表
        :param match_type: 早盘 | 滚球 | 今日
        :param sport_name:
        :param odds_type:
        :param if_all: 是否获取所有，否为只获取每个联赛的第一个比赛
        :param diff_unit:
        :param token
        :return:
        """
        url = self.host + "/creditMatchH5/matchList"
        self.head["accessCode"] = token
        params = {"highlight": "false",
                  "marketGroupId": self.market_group_dic[sport_name],
                  "sportCategoryId": small_sport_id_dic[sport_name],
                  "oddsType": odds_type,
                  "sort": 1,
                  "tournamentIds": [],
                  "matchIds": []}
        if diff_unit:
            params["dateOffset"] = diff_unit
        if match_type == "滚球":
            params["periodId"] = "INPLAY"
        elif match_type == "早盘":
            params["periodId"] = "EARLY"
        else:
            params["periodId"] = "TODAY"
        rsp = self.session.post(url, headers=self.head, json=params, timeout=60)
        match_list = []
        for item in rsp.json()["data"]:
            if not if_all:
                if len(item["matchIds"][0]) > 10:
                    match_list.append(item["matchIds"][0][9:])
                else:
                    match_list.append(item["matchIds"][0])
            else:
                for match in item["matchIds"]:
                    if len(item["matchIds"][0]) > 10:
                        match_list.append(match[9:])
                    else:
                        match_list.append(match)
        return match_list

    def get_live_match_list_h5(self, token, sport_name, odds_type=1, if_all=False):
        """
        获取滚球sport列表
        :param sport_name:
        :param odds_type:
        :param token:
        :param if_all: 是否获取所有，否为只获取每个联赛的第一个比赛
        :return:
        """
        return self.get_match_list_h5(token, "滚球", sport_name, odds_type, if_all)

    def get_pre_match_list_h5(self, token, sport_name="足球", odds_type=1, if_all=False, diff_unit=""):
        """
        获取早盘sport列表
        :param token
        :param sport_name:
        :param odds_type:
        :param if_all: 是否获取所有，否为只获取每个联赛的第一个比赛
        :param diff_unit: 默认为0
        :return:
        """
        return self.get_match_list_h5(token, "早盘", sport_name, odds_type, if_all, diff_unit if diff_unit else -1)

    def get_today_match_list(self, token, sport_name, odds_type=1, if_all=False):
        """
        获取今日比赛列表
        :param sport_name:
        :param odds_type:
        :param token
        :param if_all: 是否获取所有，否为只获取每个联赛的第一个比赛
        :return:
        """
        match_list = self.get_match_list_h5(token, "今日", sport_name, odds_type, if_all)
        return match_list

    def get_parlay_match_list(self, token, sport_name, odds_type=1, if_all=False):
        live_list = self.get_live_match_list_h5(token, sport_name, odds_type, if_all)
        pre_list = self.get_pre_match_list_h5(token, sport_name, odds_type, if_all)
        today_list = self.get_today_match_list(token, sport_name, odds_type, if_all)
        return live_list + today_list + pre_list
