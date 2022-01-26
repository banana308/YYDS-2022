# -*- coding:utf-8 -*-
import json
import re

try:
    from .MysqlFunc import MysqlCommonQuery
    from .CommonFunc import CommonFunc
    from .MyExceptions import *
    from .Backend import Backend
    from .Config import *
    from .MongoFunc import DbQuery
except Exception:
    from MysqlFunc import MysqlCommonQuery
    from CommonFunc import CommonFunc
    from MyExceptions import *
    from Backend import Backend
    from Config import *
    from MongoFunc import DbQuery


class OrderFuncOfMysql(MysqlCommonQuery):
    """
    管理后台订单管理模块MYSQL相关功能
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, *args, **kwargs):
        super().__init__(mysql_info, *args, **kwargs)
        self.cf = CommonFunc()
        self.db = DbQuery(mongo_info)

    def get_order_condition_str_sql(self, user_login_account="", order_no="", agent_0="", agent_1="", agent_2="",
                                    agent_3="", sport_name="", settlement_result="", order_status="", bet_type="",
                                    bet_start_diff="", bet_end_diff="", award_start_diff="", award_end_diff="",
                                    sort="", sort_direct=""):
        """
        订单详情:生成条件字符串
        :param user_login_account:
        :param order_no:
        :param agent_0:
        :param agent_1:
        :param agent_2:
        :param agent_3:
        :param sport_name:
        :param settlement_result: 赢 | 输 | 赢一半 | 输一半 | 注单平局 | 注单取消
        :param order_status: 已结算 | 未结算 | 投注失败
        :param bet_type: 单注 | 串关
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :param sort: 排序：  投注时间 | 投注金额 | 输/赢 | 返水金额 | 最终输赢 | 结算时间
        :param sort_direct: 排序方向： 升序|降序
        :return:
        """

        sort_direct_dic = {"升序": "ascending", "降序": "descending"}
        sort_by_dic = {"投注时间": "create_time", "投注金额": "bet_amount", "输/赢": "handicap_win_or_lose",
                       "返水金额": "backwater_amount", "最终输赢": "handicap_final_win_or_lose",
                       "结算时间": "award_time"}
        user_account_str = "" if not user_login_account else f" and a.user_name='{user_login_account}'"
        order_no_str = "" if not order_no else f" and a.order_no='{order_no}'"
        sport_name_str = "" if not sport_name else f" and a.sport_id='{small_sport_id_dic[sport_name]}'"

        if settlement_result == "注单平局":
            result_str = " and (a.status=3 and settlement_result=6) "
        elif settlement_result == "注单取消":
            result_str = " and (a.status=6 and settlement_result=6) "
        elif settlement_result == "赢":
            result_str = " and (a.status=3 and settlement_result=1) "
        elif settlement_result == "输":
            result_str = " and (a.status=3 and settlement_result=2) "
        elif settlement_result == "赢一半":
            result_str = " and (a.status=3 and settlement_result=3) "
        elif settlement_result == "输一半":
            result_str = " and (a.status=3 and settlement_result=4) "
        else:
            result_str = ""
        if order_status:
            if order_status == "未结算":
                result_str += " and a.status in (0,1,2,4,5)"
            elif order_status == "已结算":
                result_str += " and a.status in (3,6)"
            elif order_status == "投注失败":
                result_str += " and a.status in (-1,-2)"
            else:
                pass

        if not bet_type:
            bet_type_str = ""
        elif bet_type == "单注":
            bet_type_str = f" and bet_type=1"
        else:
            bet_type_str = f" and bet_type>1"
        if not bet_start_diff:
            # start_day, end_day = self.cf.get_md_day_range("月", 0, "md")
            start_day = self.cf.get_md_date_by_now(diff=-100)
            end_day = self.cf.get_md_date_by_now(diff=1)
        else:
            start_day = self.cf.get_md_date_by_now(diff=bet_start_diff)
            end_day = self.cf.get_md_date_by_now(diff=bet_end_diff)
        bet_time_str = f" and a.create_time between '{start_day} 00:00:00' and '{end_day} 00:00:00'"
        award_time_str = "" if not (award_start_diff and award_end_diff) \
            else f" and award_time between " \
                 f"'{self.cf.get_md_date_by_now(diff=award_start_diff)} 00:00:00' and " \
                 f"'{self.cf.get_md_date_by_now(diff=award_end_diff)} 00:00:00'"
        proxy0_str = f' and a.proxy0_id="{self.get_agent_id(agent_0)}"' if agent_0 else ""
        proxy1_str = f' and a.proxy1_id="{self.get_agent_id(agent_1)}"' if agent_1 else ""
        proxy2_str = f' and a.proxy2_id="{self.get_agent_id(agent_2)}"' if agent_2 else ""
        proxy3_str = f' and a.proxy3_id="{self.get_agent_id(agent_3)}"' if agent_3 else ""
        sort_str = f' order by a.{sort_by_dic[sort]} {sort_direct_dic[sort_direct]}' if sort else ""
        if (user_account_str or order_no_str or sport_name_str or result_str or bet_type_str or bet_time_str or
                award_time_str or proxy0_str or proxy1_str or proxy2_str or proxy3_str):
            where_str = " where 1=1"
        else:
            where_str = ""
        return f"{where_str} {user_account_str} {order_no_str} {sport_name_str} {result_str} {bet_type_str} " \
               f"{bet_time_str} {award_time_str} {proxy0_str} {proxy1_str} {proxy2_str} {proxy3_str} {sort_str}"

    def get_order_list_sql(self, user_login_account="", order_no="", agent_0="", agent_1="", agent_2="", agent_3="",
                           sport_name="", settlement_result="", order_status="", bet_type="", bet_start_diff="",
                           bet_end_diff="", award_start_diff="", award_end_diff="", sort="", sort_direct=""):
        """
        订单详情获取列表数据
        :param user_login_account:
        :param order_no:
        :param agent_0:
        :param agent_1:
        :param agent_2:
        :param agent_3:
        :param sport_name:
        :param settlement_result: 赢 | 输 | 赢一半 | 输一半 | 注单平局 | 注单取消
        :param order_status: 已结算 | 未结算 | 投注失败
        :param bet_type: 单注 | 串关
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :param sort: 排序：  投注时间 | 投注金额 | 输/赢 | 返水金额 | 最终输赢 | 结算时间
        :param sort_direct: 排序方向： 升序|降序
        :return:
        """
        condition_sql = self.get_order_condition_str_sql(user_login_account, order_no, agent_0, agent_1, agent_2,
                                                         agent_3, sport_name, settlement_result, order_status,
                                                         bet_type, bet_start_diff, bet_end_diff, award_start_diff,
                                                         award_end_diff, sort, sort_direct)
        sql = 'select order_no as "注单号",if(bet_type=1,"单注","串关") as "注单类型",(case when a.sport_id="sr:sport:1" ' \
              'then "足球" when a.sport_id="sr:sport:20" then "乒乓球" when a.sport_id="sr:sport:5" then "网球" when ' \
              'a.sport_id="sr:sport:4" then "冰球" when a.sport_id="sr:sport:31" then "羽毛球" when ' \
              'a.sport_id="sr:sport:3" then "棒球" when a.sport_id="sr:sport:23" then "排球" when ' \
              'a.sport_id="sr:sport:2" then "篮球" end) as "体育项目",a.user_name as "会员账号",a.create_time as ' \
              '"投注时间",bet_amount as "投注金额",(case when a.status in (3,6) then handicap_win_or_lose else "" end)' \
              ' as "输/赢",(case when a.status=3 then round(bet_amount*level3_retreat_proportion,2) else 0 end) ' \
              'as "返水金额",if(a.status in (3,6),' \
              'handicap_final_win_or_lose,"") as "最终输赢",ifnull(award_time,"") as "结算时间",if(a.status in ' \
              '(3,6),case when settlement_result=1 then "赢" when settlement_result=2 then "输" when ' \
              'settlement_result=3 then "赢一半" when settlement_result=4 then "输一半" when (a.status=3 and ' \
              'settlement_result=6) then ' \
              '"注单平局" when a.status=6 then "注单取消" end, "") as "注单结果",(case when a.status <0 then "投注失败" ' \
              'when a.status in (3,6) then "已结算" else "未结算" end) as "注单状态" from o_account_order a left join ' \
              f'u_user b on a.user_id=b.id {condition_sql}'
        rtn = list(self.query_data(sql, 'bfty_credit'))
        for index, value in enumerate(rtn):
            value = list(value)
            value[4] = value[4].strftime("%Y-%m-%d %H:%M:%S")
            rtn[index] = value

        return rtn

    def get_order_total_sql(self, user_login_account="", order_no="", agent_0="", agent_1="", agent_2="", agent_3="",
                            sport_name="", settlement_result="", order_status="", bet_type="", bet_start_diff="",
                            bet_end_diff="", award_start_diff="", award_end_diff="", sort="", sort_direct=""):
        """
        订单详情获取列表数据
        :param user_login_account:
        :param order_no:
        :param agent_0:
        :param agent_1:
        :param agent_2:
        :param agent_3:
        :param sport_name:
        :param settlement_result: 赢 | 输 | 赢一半 | 输一半 | 注单平局 | 注单取消
        :param order_status: 已结算 | 未结算 | 投注失败
        :param bet_type: 单注 | 串关
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :param sort: 排序：  投注时间 | 投注金额 | 输/赢 | 返水金额 | 最终输赢 | 结算时间
        :param sort_direct: 排序方向： 升序|降序
        :return:
        """
        condition_sql = self.get_order_condition_str_sql(user_login_account, order_no, agent_0, agent_1, agent_2,
                                                         agent_3, sport_name, settlement_result, order_status,
                                                         bet_type, bet_start_diff, bet_end_diff, award_start_diff,
                                                         award_end_diff, sort, sort_direct)
        sql = 'select count(if(a.status in (3,6),1,NULL)) as "已结算",count(if(a.status in (0,1,2,4,5),1,NULL)) as ' \
              '"未结算",sum(bet_amount) as "投注金额总计",sum(if(a.status=3,handicap_win_or_lose,0)) as "会员输赢",' \
              f'count(1) as "单数总计" from o_account_order a join u_user b on a.user_id=b.id {condition_sql}'
        return self.query_data(sql, 'bfty_credit')[0]

    def get_order_detail_sql(self, order_no):
        """
        获取订单详情中的注单详情
        :param order_no:
        :return:
        """
        sql = 'select a.user_name as "会员账号",a.order_no,a.create_time as "投注时间",a.award_time as "结算时间",(case ' \
              'when status<0 then "投注失败" when status in (0,1,2,4,5) then "未结算" when status in (3,6) then "已结算"' \
              ' end) as "注单状态",(case when sport_id="sr:sport:1" then "足球" when sport_id="sr:sport:2" then "篮球" ' \
              'when sport_id="sr:sport:5" then "网球" when sport_id="sr:sport:31" then "羽毛球" when sport_id=' \
              '"sr:sport:20" then "乒乓球" when sport_id="sr:sport:23" then "排球" when sport_id="sr:sport:3" then ' \
              '"棒球" when sport_id="sr:sport:4" then "冰球" end) as "体育类型",if(bet_type=1,"单注",' \
              'concat(bet_type,"串1")) as "投注玩法",bet_amount as "投注金额",(case when status=6 then "注单取消" when ' \
              '(isnull(settlement_result) or status not in (3,6)) then "" when settlement_result=1 then "赢" when ' \
              'settlement_result=2 then "输" when settlement_result=3 then "赢一半" when settlement_result=4 then ' \
              '"输一半" when settlement_result=6 then "注单平局" end) as "注单结果",if(status=3,' \
              'handicap_win_or_lose,"") as "输赢",match_time as "开赛时间",tournament_name_dic,' \
              'home_team_name_dic,away_team_name_dic,if(producer=3,"早盘","滚球") as producer,market_name_dic,' \
              'spliced_outcome_id,bet_score,credit_odds,award_time as "结算时间",(case when (sub_order_status in (2,3) ' \
              'and sub_settlement_result=1) then "赢" when (sub_order_status in (2,3) and sub_settlement_result=2) ' \
              'then "输" when (sub_order_status in (2,3) and sub_settlement_result=3) then "赢一半" when ' \
              '(sub_order_status in (2,3) and sub_settlement_result=4) then "输一半" when (sub_order_status in (2,3) ' \
              'and sub_settlement_result=6) then "注单平局" when sub_order_status in (4,6) then "注单取消" end) as ' \
              '"子注单结果",match_id,market_id,specifier,b.sub_order_status,proxy0_id as "代理线",proxy1_id as "一级代理",' \
              'proxy2_id as "二级代理",proxy3_id as "三级代理",bet_ip as "投注IP",terminal as "投注终端",' \
              'handicap_win_or_lose as "输赢",round(level3_retreat_proportion*10000,0) as "返水比例",' \
              'if(status=3,backwater_amount,"") as "返水金额",if(status=3,handicap_final_win_or_lose,"") as "最终输赢",' \
              'concat(round(level0_actual_percentage*100,0),"%") ' \
              'as "代理线占成",if(status=3,round(bet_amount*' \
              '(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*level3_retreat_proportion,2),0) as ' \
              '"代理线退水",(case when status=3 then round(-handicap_win_or_lose*level0_actual_percentage-bet_amount*' \
              'level0_retreat_proportion,2) when (status=6 and settlement_result=6) then 0 else "" end) as "代理线输赢",' \
              'concat(round(level1_actual_percentage*100,0),"%") as "一级代理占成",' \
              'if(status=3,round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2),"") as ' \
              '"一级代理退水",if(status=3,round(-handicap_win_or_lose*level1_actual_percentage + ' \
              '(level0_retreat_proportion-level1_retreat_proportion)*bet_amount,2),"") as "一级代理输赢",' \
              'concat(round(level2_actual_percentage*100,0),"%") as "二级代理占成",if(status=3,round(bet_amount*' \
              '(level1_retreat_proportion-level2_retreat_proportion),2),"") as "二级代理退水",if(status=3,round(-' \
              'handicap_win_or_lose*level2_actual_percentage + (level1_retreat_proportion-level2_retreat_proportion)*' \
              'bet_amount,2),"") as "二级代理输赢",concat(round(level3_actual_percentage*100,0),"%") ' \
              'as "三级代理占成",if(status=3,' \
              'round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),2),"") as "三级代理退水",' \
              'if(status=3,round(-handicap_win_or_lose*level3_actual_percentage + ' \
              '(level2_retreat_proportion-level3_retreat_proportion)*bet_amount,2),"") as "三级代理输赢",' \
              'sub_settlement_remark as "备注" from o_account_order a join o_account_order_detail b on ' \
              f'a.order_no=b.order_no where a.order_no="{order_no}"'
        rsp = self.query_data(sql, 'bfty_credit')
        order_info = []
        order_no_list = []
        for item in rsp:
            agent0_name = self.get_agent_account_name_by_id(item[25])
            agent1_name = self.get_agent_account_name_by_id(item[26])
            agent2_name = self.get_agent_account_name_by_id(item[27])
            agent3_name = self.get_agent_account_name_by_id(item[28])
            tournament_name = json.loads(item[11])["zh"]
            home_name = json.loads(item[12])["zh"]
            away_name = json.loads(item[13])["zh"]
            market_name = json.loads(item[15])["zh"]
            credit_odds = float(item[18])
            create_time = item[2].strftime("%Y-%m-%d %H:%M:%S") if item[2] else ""
            award_time = item[3].strftime("%Y-%m-%d %H:%M:%S") if item[3] else ""
            match_time = item[10].strftime("%Y-%m-%d %H:%M:%S") if item[11] else ""

            if int(item[24]) in (2, 3):
                score = self.db.get_order_result_score(item[21], item[22], item[23])
            else:
                score = ""

            detail_data = [match_time, tournament_name, home_name, away_name, item[14], market_name, item[17],
                           item[16], credit_odds, award_time, score, item[20], item[47]]
            if item[2] not in order_no_list:
                order_no_list.append(item[2])
                order_info.append(
                    [item[0], agent0_name, agent1_name, agent2_name, agent3_name, item[29], item[30], item[1],
                     create_time, award_time, item[4], item[5], item[6], item[7], item[9], item[8], item[32], item[33],
                     item[34], item[35], item[36], item[37], item[38], item[39], item[40], item[41], item[42],
                     item[43], item[44], item[45], item[46], [detail_data]])
            else:
                order_index = order_no_list.index(item[2])
                order_info[order_index][-1].append(detail_data)

        return order_info[0]

    def check_settlement_result_with_uof_msg(self, order_no):
        """
        通过uof结算报文，验证注单结算结果是否正确
        :param order_no:
        :return:
        """
        sql = f"select match_id, market_id, specifier,outcome_id,sub_settlement_result,sub_order_status from " \
              f"o_account_order_detail where order_no='{order_no}'"
        rsp = self.query_data(sql, 'bfty_credit')
        if not rsp:
            print(f"注单{order_no}信息未找到!")
        # 遍历本注单的所有子注单
        for order_detail in rsp:
            match_id = order_detail[0]
            if match_id in ("sr:match:29481384", "sr:match:28385820", "sr:match:29458628", "sr:match:29454358"):
                break
            market_id = order_detail[1]
            specifier = order_detail[2]
            outcome_id = order_detail[3]
            outcome_id_reg = outcome_id.replace("+", "\\" + "+")
            outcome_id_reg = outcome_id_reg.replace(".", "\\" + ".")
            order_status = order_detail[5]
            sql_result = 7 if order_status == 6 and order_detail[4] == 6 else order_detail[4]
            sql_uof = f"select message from uof_message_log where match_id='{match_id}' and " \
                      f"message_type='BetSettlement' order by log_time desc"
            log_rsp = self.query_data(sql_uof, 'business_log')
            if not log_rsp:
                print(f"注单{order_no}对应的比赛{match_id} UOF信息未找到!")
                continue

            checked = False
            # 遍历所有settlement msg
            for uof_msg in log_rsp:
                market_data_list = re.findall('(<market.+?</market>)', uof_msg[0])
                # 遍历所有的market
                for market_data in market_data_list:
                    # print("---")
                    # print(f'<outcome id="{outcome_id}"' in market_data)
                    # if (f'<market id="{market_id}"' in market_data) and (
                    #         f' specifiers="{specifier}"' in market_data) and (
                    #         f'<outcome id="{outcome_id}"' in market_data):
                    #     print(market_data)
                    if (f'<market id="{market_id}"' in market_data) and (
                            f' specifiers="{specifier}"' in market_data) and (
                            f'<outcome id="{outcome_id}"' in market_data):
                        # 是否取消
                        if "void_reason" in market_data:
                            void_reason = True
                        else:
                            void_reason = False
                        # 是否赢输一半
                        if "void_factor" in market_data:
                            void_factor = float(re.search(r'void_factor="(.+?)"', market_data).group(1))
                        else:
                            void_factor = None
                        # settlement result
                        # print("=========1")
                        # print(f'outcome id="{outcome_id_reg}" result="(\\d)"')
                        # print(market_data)
                        result = re.search(f'outcome id="{outcome_id_reg}" result="(\\d)"', market_data).group(1)
                        if not result:
                            # print(1111111)
                            # print(market_data)
                            raise AssertionError(f"Err: {order_no} {match_id} {market_id} {specifier} {outcome_id} "
                                                 f"没有找到settlement result!")
                        result = int(result)
                        if void_reason:
                            uof_result = 7  # 取消
                        elif not void_factor:
                            if result == 0:
                                uof_result = 2
                            else:
                                uof_result = 1
                        elif void_factor == 0.5:
                            if result == 0:
                                uof_result = 4
                            else:
                                uof_result = 3
                        else:
                            # print(f"result is {result}, void factor is {void_factor}, void reason is {void_reason}")
                            uof_result = 6

                        if sql_result != uof_result:
                            # print(222)
                            # print(f"Err: {order_no} {match_id} {market_id} {specifier} {outcome_id} 没有找到Result!")
                            raise AssertionError(f"不一致！ sql为:{sql_result}, uof 为: {uof_result}。 {order_no} "
                                                 f"{match_id} {market_id} {specifier} {outcome_id}")
                        else:
                            print("数据一致！")
                            checked = True
                            break
                if checked:
                    break
                # else:
                #     print(f"Err: {order_no} {match_id} {market_id} {specifier} {outcome_id} 盘口没有找到！")

            else:
                print(333333)
                print(f"Err: {order_no} {match_id} {market_id} {specifier} {outcome_id} 没有找到Result!")


class OrderFuncOfInterface(Backend):
    """
    管理后台订单管理模块接口相关功能
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, backend_url="http://192.168.10.11:6100", *args, **kwargs):
        super().__init__(mysql_info, backend_url, *args, **kwargs)
        self.sql = MysqlCommonQuery(mysql_info)

    def get_order_list(self, user_account="", order_no="", agent_0="", agent_1="", agent_2="", agent_3="",
                       sport_name="", settlement_result="", order_status="", bet_type="", bet_start_diff="",
                       bet_end_diff="", award_start_diff="", award_end_diff="", sort="", sort_direct=""):
        """
        订单详情获取列表数据
        :param user_account:
        :param order_no:
        :param agent_0:
        :param agent_1:
        :param agent_2:
        :param agent_3:
        :param sport_name:
        :param settlement_result: 赢 | 输 | 赢一半 | 输一半 | 注单平局 | 注单取消
        :param order_status: 已结算 | 未结算 | 投注失败
        :param bet_type: 单注 | 串关
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :param sort: 排序：  投注时间 | 投注金额 | 输/赢 | 返水金额 | 最终输赢 | 结算时间
        :param sort_direct: 排序方向： 升序|降序
        :return:
        """
        bet_type_dic = {"单注": 1, "串关": 2}
        order_status_dic = {"已结算": 1, "未结算": 2, "投注失败": 3}
        order_settlement_result_dic = {"赢": 1, "输": 2, "赢一半": 3, "输一半": 4, "注单平局": 5, "注单取消": 6}
        sort_direct_dic = {"升序": "ascending", "降序": "descending"}
        agent_id_0 = self.sql.get_agent_id(agent_0) if agent_0 else ""
        agent_id_1 = self.sql.get_agent_id(agent_1) if agent_1 else ""
        agent_id_2 = self.sql.get_agent_id(agent_2) if agent_2 else ""
        agent_id_3 = self.sql.get_agent_id(agent_3) if agent_3 else ""

        url = self.auth_url + "/order/queryOrderDetailsList"
        order_list = []
        for page in range(1, 1000):
            params = {"page": page, "limit": 500, "sortBy": sort_direct_dic[sort_direct] if sort_direct else "",
                      "sortParameter": sort,
                      "betType": "" if not bet_type else bet_type_dic[bet_type], "level0AgentId": agent_id_0,
                      "level1AgentId": agent_id_1, "level2AgentId": agent_id_2, "level3AgentId": agent_id_3,
                      "settlementResult": "" if not settlement_result else order_settlement_result_dic[
                          settlement_result],
                      "sportCategoryId": "" if not sport_name else small_sport_id_dic[sport_name],
                      "status": "" if not order_status else order_status_dic[order_status],
                      "userName": user_account, "manageLogo": False,
                      "startCreateTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                          diff=bet_start_diff) + " 00:00:00",
                      "endCreateTime": "" if not bet_end_diff else self.cf.get_md_date_by_now(
                          diff=bet_end_diff) + " 00:00:00",
                      "startSettlementTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                          diff=award_start_diff) + " 00:00:00",
                      "endSettlementTime": "" if not award_end_diff else self.cf.get_md_date_by_now(
                          diff=award_end_diff) + " 00:00:00"}
            if order_no:
                params["orderNo"] = order_no
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            for order in rtn["data"]["data"]:
                order_list.append([order["orderNo"], order["betType"], order["sportCategoryName"],
                                   order["userName"], order["createTime"], order["betAmount"],
                                   float(order["accountWinOrLose"]) if order["accountWinOrLose"] != "--" else "",
                                   float(order["backwaterAmount"]) if order["backwaterAmount"] != "--" else "",
                                   float(order["accountFinalWinOrLose"]) if
                                   order["accountFinalWinOrLose"] != "--" else "",
                                   order["settlementTime"] if order["settlementTime"] != "--" else "",
                                   order["settlementResult"] if order["settlementResult"] != "--" else "",
                                   order["status"]])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list

    def get_order_detail(self, order_no):
        """
        订单详情 - 详情数据
        :param order_no:
        :return:
        """
        url = self.auth_url + "/order/getOrderDetailsInfo"
        params = {"orderNo": order_no}
        rtn = self.session.get(url, params=params, headers=self.head_bd).json()["data"]
        print(rtn)
        # for index, item in enumerate(rtn["orderDetails"]):
        #     for key, value in item.items():
        #         if value == "--":
        #             rtn["orderDetails"][index][key] = ""
        for key, value in rtn.items():
            if value == "--":
                value = ""
            rtn[key] = value
        order_detail = []
        for item in rtn["orderDetails"]:
            for key, value in item.items():
                if value == "--":
                    value = ""
                item[key] = value
            if item["matchResult"]:
                score = re.findall(r':\s*(\d+ - \d+)', item["matchResult"])
            else:
                score = ""
            # score = [] if not score else score
            order_detail.append([item["matchTime"], item["tournamentName"], item["homeTeamName"], item["awayTeamName"],
                                 item["producer"], item["marketName"], item["betScore"], item["splicedOutcomeId"],
                                 item["creditOdds"], item["settlementTime"], score,
                                 item["settlementResult"], item["remark"]])
        order_data = [rtn["userName"], rtn["level0AgentAccount"], rtn["level1AgentAccount"],
                      rtn["level2AgentAccount"], rtn["level3AgentAccount"], rtn["ipAddress"],
                      rtn["bettingTerminal"], rtn["orderNo"], rtn["createTime"], rtn["settlementTime"],
                      rtn["status"], rtn["sportCategoryName"], rtn["betType"], rtn["betAmount"],
                      rtn["accountWinOrLose"], rtn["settlementResult"], rtn["userRetreatProportion"],
                      rtn["backwaterAmount"], rtn["accountFinalWinOrLose"], rtn["level0Percentage"],
                      rtn["level0BackwaterAmount"], rtn["level0WinOrLose"], rtn["level1Percentage"],
                      rtn["level1BackwaterAmount"], rtn["level1WinOrLose"], rtn["level2Percentage"],
                      rtn["level2BackwaterAmount"], rtn["level2WinOrLose"], rtn["level3Percentage"],
                      rtn["level3BackwaterAmount"], rtn["level3WinOrLose"], order_detail]
        return order_data

    def get_order_sum_data(self, user_account="", order_no="", agent_0="", agent_1="", agent_2="", agent_3="",
                           sport_name="", settlement_result="", order_status="", bet_type="", bet_start_diff="",
                           bet_end_diff="", award_start_diff="", award_end_diff=""):
        """
        获取订单详情列表统计数据
        :param user_account:
        :param order_no:
        :param agent_0:
        :param agent_1:
        :param agent_2:
        :param agent_3:
        :param sport_name:
        :param settlement_result: 赢 | 输 | 赢一半 | 输一半 | 注单平局 | 注单取消
        :param order_status: 已结算 | 未结算 | 投注失败
        :param bet_type: 单注 | 串关
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        bet_type_dic = {"单注": 1, "串关": 2}
        order_status_dic = {"已结算": 1, "未结算": 2, "投注失败": 3}
        order_settlement_result_dic = {"赢": 1, "输": 2, "赢一半": 3, "输一半": 4, "注单平局": 5, "注单取消": 6}
        agent_id_0 = self.sql.get_agent_id(agent_0) if agent_0 else ""
        agent_id_1 = self.sql.get_agent_id(agent_1) if agent_1 else ""
        agent_id_2 = self.sql.get_agent_id(agent_2) if agent_2 else ""
        agent_id_3 = self.sql.get_agent_id(agent_3) if agent_3 else ""
        url = self.auth_url + "/order/queryOrderAggregateData"
        params = {"betType": "" if not bet_type else bet_type_dic[bet_type], "level0AgentId": agent_id_0,
                  "level1AgentId": agent_id_1, "level2AgentId": agent_id_2, "level3AgentId": agent_id_3,
                  "settlementResult": "" if not settlement_result else order_settlement_result_dic[
                      settlement_result],
                  "sportCategoryId": "" if not sport_name else small_sport_id_dic[sport_name],
                  "status": "" if not order_status else order_status_dic[order_status],
                  "userName": user_account, "manageLogo": False,
                  "startCreateTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                      diff=bet_start_diff) + " 00:00:00",
                  "endCreateTime": "" if not bet_end_diff else self.cf.get_md_date_by_now(
                      diff=bet_end_diff) + " 00:00:00",
                  "startSettlementTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                      diff=award_start_diff) + " 00:00:00",
                  "endSettlementTime": "" if not award_end_diff else self.cf.get_md_date_by_now(
                      diff=award_end_diff) + " 00:00:00"}
        if order_no:
            params["orderNo"] = order_no
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()["data"]
        return [rtn["settled"], rtn["unsettlement"], rtn["totalBetAmount"], rtn["membersWinOrLose"],
                rtn["singularTotal"]]
