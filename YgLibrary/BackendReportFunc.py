# -*- coding:utf-8 -*-

import re
import datetime
import time
import json

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


class ReportFuncOfMysql(MysqlCommonQuery):
    """
    管理后台报表管理模块MYSQL相关功能
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, *args, **kwargs):
        super().__init__(mysql_info, mongo_info, *args, **kwargs)
        self.cf = CommonFunc()
        self.db = DbQuery(mongo_info)

    def get_mts_report_list_sql(self, user_name="", order_no="", sport_name="", settlement_result="", order_status="",
                                bet_type="", bet_start_diff="", bet_end_diff="", award_start_diff="",
                                award_end_diff=""):
        """
        数据源对账报表 - 列表数据
        :param user_name:
        :param order_no:
        :param sport_name:
        :param settlement_result:
        :param order_status:
        :param bet_type:
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        condition_str = self.get_mts_report_condition_str_sql(user_name, order_no, sport_name, settlement_result,
                                                              order_status, bet_type, bet_start_diff, bet_end_diff,
                                                              award_start_diff, award_end_diff)

        sql = 'select order_no as "注单号",if(bet_type=1,"单关","串关") as "注单类型",(case when sport_id="sr:sport:1" ' \
              'then "足球" when sport_id="sr:sport:2" then "篮球" when sport_id="sr:sport:5" then "网球" when ' \
              'sport_id="sr:sport:31" then "羽毛球" when sport_id="sr:sport:20" then "乒乓球" when ' \
              'sport_id="sr:sport:23" then "排球" when sport_id="sr:sport:3" then "棒球" when sport_id="sr:sport:4" ' \
              'then "冰球" end) as "体育类型",user_name as "会员账号",create_time as "投注时间",bet_amount as "投注金额",' \
              'if(!isnull(award_time) and status in (3,6),award_time,"") as "结算时间",(case when status<0 then' \
              ' "投注失败" when status in (0,1,2,4,5) then "未结算" when status in (3,6) then "已结算" end) ' \
              'as "注单状态",(case when status=6 then "注单取消" when (isnull(settlement_result) or status not in ' \
              '(3,6)) then "" when settlement_result=1 then "赢" when settlement_result=2 then "输" when ' \
              'settlement_result=3 then "赢一半" when settlement_result=4 then "输一半" when settlement_result=6 ' \
              'then "注单平局" end) as "注单结果",if(status in (3,6),account_win_or_lose,"") as "输/赢(原始)",if(status ' \
              f'in (3,6),handicap_win_or_lose,"") as "输/赢(盘口)" from o_account_order {condition_str} ' \
              f'order by create_time desc'
        rsp = self.query_data(sql, 'bfty_credit')
        data_list = [list(item) for item in rsp]
        for index, item in enumerate(data_list):
            item[4] = str(item[4])
            item[6] = str(item[6])
            data_list[index] = item
        return data_list

    def get_mts_report_total_sql(self, user_name="", order_no="", sport_name="", settlement_result="", order_status="",
                                 bet_type="", bet_start_diff="", bet_end_diff="", award_start_diff="",
                                 award_end_diff=""):
        """
        数据源对账报表 - 总计数据
        :param user_name:
        :param order_no:
        :param sport_name:
        :param settlement_result:
        :param order_status:
        :param bet_type:
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        condition_str = self.get_mts_report_condition_str_sql(user_name, order_no, sport_name, settlement_result,
                                                              order_status, bet_type, bet_start_diff, bet_end_diff,
                                                              award_start_diff, award_end_diff)
        sql = 'select round(sum(`投注金额`),2) as "投注金额",round(sum(`输/赢(原始)`),2) as "输/赢(原始)",' \
              'round(sum(`输/赢(盘口)`),2) as "输/赢(盘口)" from (select order_no as "注单号",if(bet_type=1,"单关","串关") ' \
              'as "注单类型",(case when sport_id="sr:sport:1" ' \
              'then "足球" when sport_id="sr:sport:2" then "篮球" when sport_id="sr:sport:5" then "网球" when ' \
              'sport_id="sr:sport:31" then "羽毛球" when sport_id="sr:sport:20" then "乒乓球" when ' \
              'sport_id="sr:sport:23" then "排球" when sport_id="sr:sport:3" then "棒球" when sport_id="sr:sport:4" ' \
              'then "冰球" end) as "体育类型",user_name as "会员账号",create_time as "投注时间",bet_amount as "投注金额",' \
              'if(!isnull(award_time) and status in (3,6),award_time,"") as "结算时间",(case when status<0 then' \
              ' "投注失败" when status in (0,1,2,4,5) then "未结算" when status in (3,6) then "已结算" end) ' \
              'as "注单状态",(case when status=6 then "注单取消" when (isnull(settlement_result) or status not in ' \
              '(3,6)) then "" when settlement_result=1 then "赢" when settlement_result=2 then "输" when ' \
              'settlement_result=3 then "赢一半" when settlement_result=4 then "输一半" when settlement_result=6 ' \
              'then "注单平局" end) as "注单结果",if(status in (3,6),account_win_or_lose,"") as "输/赢(原始)",if(status ' \
              f'in (3,6),handicap_win_or_lose,"") as "输/赢(盘口)" from o_account_order {condition_str}) a'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]

    def get_mts_report_condition_str_sql(self, user_name="", order_no="", sport_name="", settlement_result="",
                                         order_status="", bet_type="", bet_start_diff="", bet_end_diff="",
                                         award_start_diff="", award_end_diff=""):
        """
        数据源对账报表:生成条件字符串
        :param user_name:
        :param order_no:
        :param sport_name:
        :param settlement_result:
        :param order_status:
        :param bet_type:
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        user_account_str = "" if not user_name else f" and user_name='{user_name}'"
        order_no_str = "" if not order_no else f" and order_no='{order_no}'"
        sport_name_str = "" if not sport_name else f" and sport_id='{small_sport_id_dic[sport_name]}'"

        if settlement_result == "注单平局":
            result_str = " and (status=3 and settlement_result=6) "
        elif settlement_result == "注单取消":
            result_str = " and (status=6 and settlement_result=6) "
        elif settlement_result == "赢":
            result_str = " and (status=3 and settlement_result=1) "
        elif settlement_result == "输":
            result_str = " and (status=3 and settlement_result=2) "
        elif settlement_result == "赢一半":
            result_str = " and (status=3 and settlement_result=3) "
        elif settlement_result == "输一半":
            result_str = " and (status=3 and settlement_result=4) "
        else:
            result_str = ""
        if order_status:
            if order_status == "未结算":
                result_str += " and status in (0,1,2,4,5)"
            elif order_status == "已结算":
                result_str += " and status in (3,6)"
            elif order_status == "投注失败":
                result_str += " and status in (-1,-2)"
            else:
                pass

        if not bet_type:
            bet_type_str = ""
        elif bet_type == "单注":
            bet_type_str = f" and bet_type=1"
        else:
            bet_type_str = f" and bet_type>1"
        if not bet_start_diff:
            start_day, end_day = self.cf.get_md_day_range("月", 0, "md")
        else:
            start_day = self.cf.get_md_date_by_now(diff=bet_start_diff)
            end_day = self.cf.get_md_date_by_now(diff=bet_end_diff)
        bet_time_str = f" and DATE_FORMAT(create_time,'%Y-%m-%d') between '{start_day}' and '{end_day}'"
        award_time_str = "" if not (award_start_diff and award_end_diff) \
            else f" and DATE_FORMAT(award_time,'%Y-%m-%d') between " \
                 f"'{self.cf.get_md_date_by_now(diff=award_start_diff)}' and " \
                 f"'{self.cf.get_md_date_by_now(diff=award_end_diff)}'"
        if (user_account_str or order_no_str or sport_name_str or result_str or bet_type_str or bet_time_str or
                award_time_str):
            where_str = " where 1=1"
        else:
            where_str = ""
        return f"{where_str} {user_account_str} {order_no_str} {sport_name_str} {result_str} {bet_type_str} " \
               f"{bet_time_str} {award_time_str} "

    def get_mts_report_order_count_sql(self, user_name="", order_no="", sport_name="", settlement_result="",
                                       order_status="", bet_type="", bet_start_diff="", bet_end_diff="",
                                       award_start_diff="", award_end_diff=""):
        """
        数据源对账报表 - 数量
        :param user_name:
        :param order_no:
        :param sport_name:
        :param settlement_result:
        :param order_status:
        :param bet_type:
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        condition_str = self.get_mts_report_condition_str_sql(user_name, order_no, sport_name, settlement_result,
                                                              order_status, bet_type, bet_start_diff, bet_end_diff,
                                                              award_start_diff, award_end_diff)
        sql = 'select sum(status in (3,6) ) as "已结算",sum(status in (0,1,2,4,5) ) as "未结算",count(*) as "单数总计" ' \
              f'from o_account_order {condition_str}'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]

    def get_mts_report_order_detail_sql(self, order_no):
        """
        获取数据源对账报表订单详情
        :param order_no:
        :return:
        """
        sql = 'select a.user_name as "会员账号",a.order_no,a.create_time as "投注时间",a.award_time as "结算时间",(case ' \
              'when status<0 then "投注失败" when status in (0,1,2,4,5) then "未结算" when status in (3,6) then "已结算"' \
              ' end) as "注单状态",(case when sport_id="sr:sport:1" then "足球" when sport_id="sr:sport:2" then "篮球" ' \
              'when sport_id="sr:sport:5" then "网球" when sport_id="sr:sport:31" then "羽毛球" when sport_id=' \
              '"sr:sport:20" then "乒乓球" when sport_id="sr:sport:23" then "排球" when sport_id="sr:sport:3" then ' \
              '"棒球" when sport_id="sr:sport:4" then "冰球" end) as "体育类型",if(bet_type=1,"单关",' \
              'concat(bet_type,"串1")) as "投注玩法",' \
              'bet_amount as "投注金额",(case when status=6 then "注单取消" when (isnull(settlement_result) or status ' \
              'not in (3,6)) then "" when settlement_result=1 then "赢" when settlement_result=2 then "输" when ' \
              'settlement_result=3 then "赢一半" when settlement_result=4 then "输一半" when settlement_result=6 then ' \
              '"注单平局" end) as "注单结果",if(status in (3,6),account_win_or_lose,null) as "输赢-原始",if(status ' \
              'in (3,6),handicap_win_or_lose,null) as "输赢-盘口",match_time as "开赛时间",tournament_name_dic,' \
              'home_team_name_dic,away_team_name_dic,if(producer=3,"早盘","滚球") as producer,market_name_dic,' \
              'spliced_outcome_id,bet_score,odds,award_time as "结算时间",(case when (sub_order_status in (2,3) and ' \
              'sub_settlement_result=1) then "赢" when ' \
              '(sub_order_status in (2,3) and sub_settlement_result=2) then "输" when (sub_order_status in (2,3) and ' \
              'sub_settlement_result=3) then "赢一半" when (sub_order_status in (2,3) and sub_settlement_result=4) then' \
              ' "输一半" when (sub_order_status in (2,3) and sub_settlement_result=6) then "注单平局" when ' \
              '(sub_order_status in (4,6) and sub_settlement_result=6) then "注单取消" end) as "子注单结果",' \
              'credit_odds,match_id,market_id,specifier,b.sub_order_status ' \
              'from o_account_order a' \
              f' join o_account_order_detail b on a.order_no=b.order_no where a.order_no="{order_no}"'
        rsp = self.query_data(sql, 'bfty_credit')
        order_info = []
        order_no_list = []
        for item in rsp:
            tournament_name = json.loads(item[12])["zh"]
            home_name = json.loads(item[13])["zh"]
            away_name = json.loads(item[14])["zh"]
            market_name = json.loads(item[16])["zh"]
            odds = float(item[19])
            credit_odds = float(item[22])
            create_time = item[2].strftime("%Y-%m-%d %H:%M:%S") if item[2] else ""
            award_time = item[3].strftime("%Y-%m-%d %H:%M:%S") if item[3] else ""
            match_time = item[11].strftime("%Y-%m-%d %H:%M:%S") if item[11] else ""

            if int(item[26]) in (2, 3):
                score = self.db.get_order_result_score(item[23], item[24], item[25])
            else:
                score = ""

            detail_data = [match_time, tournament_name, home_name, away_name, item[15], market_name, item[18],
                           item[17], odds, award_time, score, item[21], credit_odds]
            if item[2] not in order_no_list:
                order_no_list.append(item[2])
                order_info.append(
                    [item[0], item[1], create_time, award_time, item[4], item[5], item[6], item[7], item[8],
                     item[9], item[10], [detail_data]])
            else:
                order_index = order_no_list.index(item[2])
                order_info[order_index][-1].append(detail_data)

        return order_info[0]

    def get_order_no_list(self):
        """
        获取满足条件的注单no列表
        :return:
        """
        sql = "select order_no from o_account_order"
        return self.query_data(sql, 'bfty_credit')

    def get_day_report_list_sql(self, award_start_diff=-6, award_end_diff=0, terminal="", sport_name=""):
        """
        每日盈亏报表 - 列表数据; 另外还有 客户端盈亏、体育项盈亏列表中的某类型的明细数据
        :param award_start_diff:
        :param award_end_diff:
        :param terminal: ios-h5 | android-h5 | pc
        :param sport_name:
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        terminal_str = f' and terminal="{terminal}"' if terminal else ""
        sport_str = f' and sport_id="{small_sport_id_dic[sport_name]}"' if sport_name else ""
        sql = 'select a.`日期`,`投注人数`,`注单量`,`投注金额`,`有效投注`,`投注盈亏`,`总返水`,`净盈亏` from (select ' \
              'date_format(date_add(date_format(CONVERT_TZ(now(),"+00:00","-04:00"),"%Y-%m-%d"),interval ' \
              '-t.help_topic_id day),"%Y-%m-%d") as "日期" from mysql.help_topic t where t.help_topic_id<=12) a left ' \
              'join (select `日期`,count(*) as "投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额" from ' \
              '(select user_id,DATE_FORMAT(create_time,"%Y-%m-%d") as "日期",count(*) as "注单量",' \
              'round(sum(if(status>=0,bet_amount,0)),2) as "投注金额" from o_account_order where status>=0 and ' \
              f'DATE_FORMAT(create_time,"%Y-%m-%d") between "{start_day}" and "{end_day}" and create_time<now() ' \
              f'{terminal_str} {sport_str} group ' \
              'by `日期`,user_id) a group by `日期`) b on a.`日期`=b.`日期` left join (select DATE_FORMAT(award_time,' \
              '"%Y-%m-%d") as "日期",round(sum(if(status=3,bet_amount,0)),2) as "有效投注",sum(if(status=3,round(' \
              '-handicap_win_or_lose*level0_actual_percentage,2),0)) as "投注盈亏",sum(if(status=3,round(bet_amount*' \
              '(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "总返水",sum(if(status=3,-' \
              'round(handicap_win_or_lose*level0_actual_percentage,2)-(round(bet_amount*(level0_retreat_proportion-' \
              'level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),' \
              '2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*' \
              '(level3_retreat_proportion),2)),0)) as "净盈亏" from o_account_order where status>=0 and DATE_FORMAT' \
              f'(award_time,"%Y-%m-%d") between "{start_day}" and "{end_day}" and award_time<now() {terminal_str} ' \
              f'{sport_str} group by `日期`) c on a.`日期`=c.`日期` where a.`日期` between "{start_day}" and ' \
              f'"{end_day}" order by a.`日期` desc'
        return self.query_data(sql, 'bfty_credit')

    def get_day_report_total_sql(self, award_start_diff=-6, award_end_diff=0):
        """
        每日盈亏报表 - 总计数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        sql = 'select sum(`投注人数`) as "投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额",sum(`有效投注`) as ' \
              '"有效投注",sum(`投注盈亏`) as "投注盈亏",sum(`总返水`) as "总返水",sum(`净盈亏`) as "净盈亏" from (select ' \
              'a.`日期`,`投注人数`,`注单量`,`投注金额`,`有效投注`,`投注盈亏`,`总返水`,`净盈亏` from (select date_format(' \
              'date_add(date_format(CONVERT_TZ(now(),"+00:00","-04:00"),"%Y-%m-%d"),interval -t.help_topic_id day),' \
              '"%Y-%m-%d") as "日期" from mysql.help_topic t where t.help_topic_id<=6) a left join (select `日期`,' \
              'count(*) as "投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额" from (select user_id,' \
              'DATE_FORMAT(create_time,"%Y-%m-%d") as "日期",count(*) as "注单量",round(sum(if(status>=0,' \
              'bet_amount,0)),2) as "投注金额" from o_account_order where status>=0 and DATE_FORMAT(create_time,' \
              f'"%Y-%m-%d") between "{start_day}" and "{end_day}" and create_time<now() group ' \
              f'by `日期`,user_id) a group by `日期`) b on a.`日期`=b.`日期` left join (select DATE_FORMAT(award_time,' \
              f'"%Y-%m-%d") as "日期",round(sum(if(status=3,bet_amount,0)),2) as "有效投注",sum(if(status=3,' \
              f'round(-handicap_win_or_lose*level0_actual_percentage,2),0)) as "投注盈亏",sum(if(status=3,' \
              f'round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              f'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              f'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "总返水",' \
              f'sum(if(status=3,-round(handicap_win_or_lose*level0_actual_percentage,2)-(round(bet_amount*' \
              f'(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion' \
              f'-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              f'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2)),0)) as "净盈亏" from ' \
              f'o_account_order where status>=0 and DATE_FORMAT(award_time,"%Y-%m-%d") between "{start_day}" and ' \
              f'"{end_day}" and award_time<now() group by `日期`) c on a.`日期`=c.`日期` order by a.`日期` desc) a'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]

    def get_client_report_list_sql(self, award_start_diff=-6, award_end_diff=0, terminal=""):
        """
        客户端盈亏报表 - 列表数据
        :param award_start_diff:
        :param award_end_diff:
        :param terminal: ios-h5 | android-h5 | pc
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        terminal_str = f' where a.`客户端`="{terminal}"' if terminal else ""
        sql = 'select a.`客户端`,`投注人数`,`注单量`,`投注金额`,`有效投注`,`投注盈亏`,`总返水`,`净盈亏` from (select distinct ' \
              'terminal as "客户端" from o_account_order where status>=0) a left join (select `客户端`,count(*) as ' \
              '"投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额" from (select user_id,terminal as "客户端",' \
              'count(*) as "注单量",round(sum(bet_amount),2) as "投注金额" from o_account_order where status>=0 and ' \
              f'DATE_FORMAT(create_time,"%Y-%m-%d") between "{start_day}" and "{end_day}" and create_time<now() group' \
              ' by terminal,user_id) a group by `客户端`) b on a.`客户端`=b.`客户端` left join (select terminal as ' \
              '"客户端",round(sum(if(status=3,bet_amount,0)),2) as "有效投注",sum(if(status=3,' \
              'round(-handicap_win_or_lose*level0_actual_percentage,2),0)) as "投注盈亏",sum(if(status=3,round(' \
              'bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "总返水",' \
              'sum(if(status=3,-round(handicap_win_or_lose*level0_actual_percentage,2)-(round(bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2)),0)) as "净盈亏" from o_account_order where ' \
              f'status>=0 and DATE_FORMAT(award_time,"%Y-%m-%d") between "{start_day}" and "{end_day}" group by ' \
              f'terminal) c on a.`客户端`=c.`客户端` {terminal_str}'
        return self.query_data(sql, 'bfty_credit')

    def get_client_report_total_sql(self, award_start_diff=-6, award_end_diff=0, terminal=""):
        """
        客户端盈亏报表 - 总计数据
        :param award_start_diff:
        :param award_end_diff:
        :param terminal: ios-h5 | android-h5 | pc
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        terminal_str = f' where a.`客户端`="{terminal}"' if terminal else ""
        sql = 'select sum(`投注人数`) as "投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额",sum(`有效投注`)' \
              ' as "有效投注",sum(`投注盈亏`) as "投注盈亏",sum(`总返水`) as "总返水",sum(`净盈亏`) as "净盈亏" from (select ' \
              'a.`客户端`,`投注人数`,`注单量`,`投注金额`,`有效投注`,`投注盈亏`,`总返水`,`净盈亏` from (select distinct terminal ' \
              'as "客户端" from o_account_order where status>=0) a left join (select `客户端`,count(*) as "投注人数",' \
              'sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额" from (select user_id,terminal as "客户端",count(*) ' \
              'as "注单量",round(sum(bet_amount),2) as "投注金额" from o_account_order where status>=0 and DATE_FORMAT' \
              f'(create_time,"%Y-%m-%d") between "{start_day}" and "{end_day}" and create_time<now() group by ' \
              'terminal,user_id) a group by `客户端`) b on a.`客户端`=b.`客户端` left join (select terminal as "客户端",' \
              'round(sum(if(status=3,bet_amount,0)),2) as "有效投注",sum(if(status=3,round(-handicap_win_or_lose*' \
              'level0_actual_percentage,2),0)) as "投注盈亏",sum(if(status=3,round(bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "总返水",sum(if(status=3,-round(' \
              'handicap_win_or_lose*level0_actual_percentage,2)-(round(bet_amount*(level0_retreat_proportion-' \
              'level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),' \
              '2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(' \
              'level3_retreat_proportion),2)),0)) as "净盈亏" from o_account_order where status>=0 and DATE_FORMAT' \
              f'(award_time,"%Y-%m-%d") between "{start_day}" and "{end_day}" group by terminal) c on a.`客户端`=' \
              f'c.`客户端` {terminal_str}) a'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]

    def get_sport_report_list_sql(self, award_start_diff=-6, award_end_diff=0):
        """
        体育项盈亏报表 - 列表数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        sql = 'select a.sport_name as `体育类型`,`投注人数`,`注单量`,`投注金额`,`有效投注`,`投注盈亏`,`总返水`,`净盈亏` from ' \
              's_sport a left join (select sport_id,count(*) as "投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as ' \
              '"投注金额" from (select user_id,sport_id,count(*) as "注单量",round(sum(bet_amount),2) as "投注金额" from ' \
              f'o_account_order where status>=0 and DATE_FORMAT(create_time,"%Y-%m-%d") between "{start_day}" and' \
              f' "{end_day}" and create_time<now() group by sport_id,user_id) a group by sport_id) b on a.sport_id=' \
              f'b.sport_id left join (select sport_id,round(sum(if(status=3,bet_amount,0)),2) as "有效投注",' \
              f'sum(if(status=3,round(-handicap_win_or_lose*level0_actual_percentage,2),0)) as "投注盈亏",' \
              f'sum(if(status=3,round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+' \
              f'round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(' \
              f'level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),' \
              f'2),0)) as "总返水",sum(if(status=3,-round(handicap_win_or_lose*level0_actual_percentage,2)-' \
              f'(round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              f'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              f'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2)),0)) as "净盈亏" from ' \
              f'o_account_order where status>=0 and DATE_FORMAT(award_time,"%Y-%m-%d") between "{start_day}" and' \
              f' "{end_day}" group by sport_id) c on a.sport_id=c.sport_id'
        return self.query_data(sql, 'bfty_credit')

    def get_sport_report_total_sql(self, award_start_diff=-6, award_end_diff=0):
        """
        体育项盈亏报表 - 总计数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        sql = 'select sum(`投注人数`) as "投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额",sum(`有效投注`) ' \
              'as "有效投注",sum(`投注盈亏`) as "投注盈亏",sum(`总返水`) as "总返水",sum(`净盈亏`) as "净盈亏" from (select ' \
              'a.sport_name as `体育类型`,`投注人数`,`注单量`,`投注金额`,`有效投注`,`投注盈亏`,`总返水`,`净盈亏` from s_sport a' \
              ' left join (select sport_id,count(*) as "投注人数",sum(`注单量`) as "注单量",sum(`投注金额`) as "投注金额" ' \
              'from (select user_id,sport_id,count(*) as "注单量",round(sum(bet_amount),2) as "投注金额" from ' \
              f'o_account_order where status>=0 and DATE_FORMAT(create_time,"%Y-%m-%d") between "{start_day}" and' \
              f' "{end_day}" and create_time<now() group by sport_id,user_id) a group by sport_id) b on a.sport_id=' \
              f'b.sport_id left join (select sport_id,round(sum(if(status=3,bet_amount,0)),2) as "有效投注",' \
              f'sum(if(status=3,round(-handicap_win_or_lose*level0_actual_percentage,2),0)) as "投注盈亏",' \
              f'sum(if(status=3,round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+' \
              f'round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*' \
              f'(level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion' \
              f'),2),0)) as "总返水",sum(if(status=3,-round(handicap_win_or_lose*level0_actual_percentage,2)-' \
              f'(round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              f'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              f'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2)),0)) as "净盈亏" from ' \
              f'o_account_order where status>=0 and DATE_FORMAT(award_time,"%Y-%m-%d") between "{start_day}" and ' \
              f'"{end_day}" and create_time<now() group by sport_id) c on a.sport_id=c.sport_id) a'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]

    def get_back_water_report_list_sql(self, award_start_diff=-6, award_end_diff=0):
        """
        返水报表 - 列表数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        sql = 'select DATE_FORMAT(a.award_time,"%Y-%m-%d") as "日期",sum(if(status=3,round(bet_amount*(level0_' \
              'retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "总返水",sum(round(a.bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)) as "一级代理",sum(round(a.bet_amount*(' \
              'level1_retreat_proportion-level2_retreat_proportion),2)) as "二级代理",sum(round(a.bet_amount*(' \
              'level2_retreat_proportion-level3_retreat_proportion),2)) as "三级代理",sum(round(a.bet_amount*' \
              'level3_retreat_proportion,2)) as "会员",sum(if(sport_id="sr:sport:1",round(bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "足球",sum(if(sport_id="sr:sport:2",' \
              'round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "篮球",sum(if' \
              '(sport_id="sr:sport:5",round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+' \
              'round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(' \
              'level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),' \
              '2),0)) as "网球",sum(if(sport_id="sr:sport:31",round(bet_amount*(level0_retreat_proportion-' \
              'level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),' \
              '2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(' \
              'level3_retreat_proportion),2),0)) as "羽毛球",sum(if(sport_id="sr:sport:20",round(bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "乒乓球",sum(if(sport_id="sr:sport:23",' \
              'round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "排球",sum(' \
              'if(sport_id="sr:sport:3",round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+' \
              'round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(' \
              'level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),' \
              '2),0)) as "棒球",sum(if(sport_id="sr:sport:4",round(bet_amount*(level0_retreat_proportion-' \
              'level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),' \
              '2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(' \
              'level3_retreat_proportion),2),0)) as "冰球" from o_account_order a join o_account_order_detail b on ' \
              f'a.order_no=b.order_no where DATE_FORMAT(a.award_time,"%Y-%m-%d") between "{start_day}" and ' \
              f'"{end_day}" and status=3 group by DATE_FORMAT(a.award_time,"%Y-%m-%d") order by `日期` desc'
        return self.query_data(sql, 'bfty_credit')

    def get_back_water_report_total_sql(self, award_start_diff=-6, award_end_diff=0):
        """
        返水报表 - 总计数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        start_day = self.cf.get_md_date_by_now(diff=award_start_diff)
        end_day = self.cf.get_md_date_by_now(diff=award_end_diff)
        sql = 'select sum(if(status=3,round(bet_amount*(level0_' \
              'retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "总返水",sum(round(a.bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)) as "一级代理",sum(round(a.bet_amount*(' \
              'level1_retreat_proportion-level2_retreat_proportion),2)) as "二级代理",sum(round(a.bet_amount*(' \
              'level2_retreat_proportion-level3_retreat_proportion),2)) as "三级代理",sum(round(a.bet_amount*' \
              'level3_retreat_proportion,2)) as "会员",sum(if(sport_id="sr:sport:1",round(bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "足球",sum(if(sport_id="sr:sport:2",' \
              'round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "篮球",sum(if' \
              '(sport_id="sr:sport:5",round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+' \
              'round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(' \
              'level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),' \
              '2),0)) as "网球",sum(if(sport_id="sr:sport:31",round(bet_amount*(level0_retreat_proportion-' \
              'level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),' \
              '2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(' \
              'level3_retreat_proportion),2),0)) as "羽毛球",sum(if(sport_id="sr:sport:20",round(bet_amount*(' \
              'level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-' \
              'level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),' \
              '2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "乒乓球",sum(if(sport_id="sr:sport:23",' \
              'round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+round(bet_amount*(' \
              'level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(level2_retreat_proportion-' \
              'level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),2),0)) as "排球",sum(' \
              'if(sport_id="sr:sport:3",round(bet_amount*(level0_retreat_proportion-level1_retreat_proportion),2)+' \
              'round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),2)+round(bet_amount*(' \
              'level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(level3_retreat_proportion),' \
              '2),0)) as "棒球",sum(if(sport_id="sr:sport:4",round(bet_amount*(level0_retreat_proportion-' \
              'level1_retreat_proportion),2)+round(bet_amount*(level1_retreat_proportion-level2_retreat_proportion),' \
              '2)+round(bet_amount*(level2_retreat_proportion-level3_retreat_proportion),2)+round(bet_amount*(' \
              'level3_retreat_proportion),2),0)) as "冰球" from o_account_order a join o_account_order_detail b on ' \
              f'a.order_no=b.order_no where DATE_FORMAT(a.award_time,"%Y-%m-%d") between "{start_day}" and ' \
              f'"{end_day}" and status=3'
        rsp = self.query_data(sql, 'bfty_credit')
        return rsp[0]


class ReportFuncOfInterface(Backend):
    """
    管理后台报表管理模块接口相关功能
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, backend_url, *args, **kwargs):
        super().__init__(mysql_info, backend_url)

    def get_mts_report_list(self, user_name="", order_no="", sport_name="", settlement_result="", order_status="",
                            bet_type="", bet_start_diff="", bet_end_diff="", award_start_diff="", award_end_diff=""):
        """
        数据源对账报表 - 列表数据
        :param user_name:
        :param order_no:
        :param sport_name:
        :param settlement_result:
        :param order_status:
        :param bet_type:
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        bet_type_dic = {"单注": 1, "串关": 2}
        order_status_dic = {"已结算": 1, "未结算": 2, "投注失败": 3}
        report_settlement_result_dic = {"赢": 1, "输": 2, "赢一半": 3, "输一半": 4, "注单平局": 5, "注单取消": 6}
        url = self.auth_url + "/dataSourceCheckReport/getPage"
        order_list = []
        for page in range(1, 1000):
            params = {"page": page, "limit": 100, "sortBy": "", "sortParameter": "",
                      "betType": "" if not bet_type else bet_type_dic[bet_type],
                      "orderNo": order_no,
                      "settlementResult": [
                          report_settlement_result_dic[settlement_result]] if settlement_result else [],
                      "sportId": [small_sport_id_dic[sport_name]] if sport_name else [],
                      "status": [order_status_dic[order_status]] if order_status else [],
                      "userName": user_name if user_name else "",
                      "betStartTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                          diff=bet_start_diff) + " 00:00:00",
                      "betEndTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                          diff=bet_end_diff) + " 00:00:00",
                      "settlementStartTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                          diff=award_start_diff) + " 00:00:00",
                      "settlementEndTime": "" if not award_end_diff else self.cf.get_md_date_by_now(
                          diff=award_end_diff) + " 00:00:00",
                      "sortIndex": ""}
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            for order in rtn["data"]["data"]:
                order_list.append([order["orderNo"], order["betType"], order["sportName"], order["userName"],
                                   order["betTime"], order["betAmount"], order["settlementTime"],
                                   order["statusName"], order["settlementResult"], order["accountFinalWinOrLose"],
                                   order["handicapFinalWinOrLose"]])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list

    def get_mts_report_detail(self, order_no):
        """
        获取数据源对账报表中的明细数据
        :param order_no:
        :return:
        """
        url = self.auth_url + "/dataSourceCheckReport/getOrderDetailsByOrderNo"
        params = {"orderNo": order_no}
        rtn = self.session.get(url, params=params, headers=self.head_bd).json()["data"]

        order_detail = []
        for item in rtn["orderDetails"]:
            score = re.findall(r':\s*(\d+ - \d+)', str(item["matchResult"]))
            score = [] if not score else score
            for key in item.keys():
                if item[key] == "--":
                    item[key] = ""
            order_detail.append([item["matchTime"], item["tournamentName"], item["homeTeamName"], item["awayTeamName"],
                                 item["producer"], item["marketName"], item["betScore"], item["splicedOutcomeId"],
                                 item["odds"], item["settlementTime"], score, item["settlementResult"],
                                 item["creditOdds"]])
        order_data = [rtn["userName"], rtn["orderNo"], rtn["createTime"], rtn["settlementTime"], rtn["statusName"],
                      rtn["sportName"], rtn["betType"], rtn["betAmount"], rtn["settlementResult"],
                      rtn["accountFinalWinOrLose"], rtn["handicapFinalWinOrLose"], order_detail]
        return order_data

    def get_mts_report_list_total(self, user_name="", order_no="", sport_name="", settlement_result="", order_status="",
                                  bet_type="", bet_start_diff="", bet_end_diff="", award_start_diff="",
                                  award_end_diff=""):
        """
        数据源对账报表 - 总计数据
        :param user_name:
        :param order_no:
        :param sport_name:
        :param settlement_result:
        :param order_status:
        :param bet_type:
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        url = self.auth_url + "/dataSourceCheckReport/getTotal"
        bet_type_dic = {"单注": 1, "串关": 2}
        order_status_dic = {"已结算": 1, "未结算": 2, "投注失败": 3}
        report_settlement_result_dic = {"赢": 1, "输": 2, "赢一半": 3, "输一半": 4, "注单平局": 5, "注单取消": 6}
        params = {"betType": "" if not bet_type else bet_type_dic[bet_type],
                  "orderNo": order_no,
                  "settlementResult": [
                      report_settlement_result_dic[settlement_result]] if settlement_result else [],
                  "sportId": [small_sport_id_dic[sport_name]] if sport_name else [],
                  "status": [order_status_dic[order_status]] if order_status else [],
                  "userName": user_name if user_name else "",
                  "betStartTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                      diff=bet_start_diff) + " 00:00:00",
                  "betEndTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                      diff=bet_end_diff) + " 00:00:00",
                  "settlementStartTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                      diff=award_start_diff) + " 00:00:00",
                  "settlementEndTime": "" if not award_end_diff else self.cf.get_md_date_by_now(
                      diff=award_end_diff) + " 00:00:00"}
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()

        data = rtn["data"]
        return [data["betAmount"], data["accountFinalWinOrLose"], data["handicapFinalWinOrLose"]]

    def get_mts_report_order_count(self, user_name="", order_no="", sport_name="", settlement_result="",
                                   order_status="", bet_type="", bet_start_diff="", bet_end_diff="",
                                   award_start_diff="", award_end_diff=""):
        """
        数据源对账报表 - 数量
        :param user_name:
        :param order_no:
        :param sport_name:
        :param settlement_result:
        :param order_status:
        :param bet_type:
        :param bet_start_diff:
        :param bet_end_diff:
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        url = self.auth_url + "/dataSourceCheckReport/getBannerData"
        bet_type_dic = {"单注": 1, "串关": 2}
        order_status_dic = {"已结算": 1, "未结算": 2, "投注失败": 3}
        report_settlement_result_dic = {"赢": 1, "输": 2, "赢一半": 3, "输一半": 4, "注单平局": 5, "注单取消": 6}
        params = {"betType": "" if not bet_type else bet_type_dic[bet_type],
                  "orderNo": order_no,
                  "settlementResult": [
                      report_settlement_result_dic[settlement_result]] if settlement_result else [],
                  "sportId": [small_sport_id_dic[sport_name]] if sport_name else [],
                  "status": [order_status_dic[order_status]] if order_status else [],
                  "userName": user_name if user_name else "",
                  "betStartTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                      diff=bet_start_diff) + " 00:00:00",
                  "betEndTime": "" if not bet_start_diff else self.cf.get_md_date_by_now(
                      diff=bet_end_diff) + " 00:00:00",
                  "settlementStartTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                      diff=award_start_diff) + " 00:00:00",
                  "settlementEndTime": "" if not award_end_diff else self.cf.get_md_date_by_now(
                      diff=award_end_diff) + " 00:00:00"}
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()

        data = rtn["data"]
        return [data["settledNumber"], data["unsettlementNumber"], data["orderTotal"]]

    def get_day_report_list(self, award_start_diff="", award_end_diff="", sport_name="", terminal=""):
        """
        每日盈亏报表 - 列表数据
        :param award_start_diff:
        :param award_end_diff:
        :param sport_name:
        :param terminal: ios-h5 | android-h5 | pc
        :return:
        """
        url = self.auth_url + "/backendReport/queryDailyProfitAndLossList"
        order_list = []
        for page in range(1, 1000):
            params = {"page": page, "limit": 100,
                      "startCreateTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                          diff=award_start_diff),
                      "endCreateTime": "" if not award_end_diff else self.cf.get_md_date_by_now(diff=award_end_diff)}
            if sport_name:
                params["sportId"] = small_sport_id_dic[sport_name]
            if terminal:
                params["terminal"] = terminal
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            for order in rtn["data"]["data"]:
                order_list.append([order["dateTime"], order["bettingUserNumber"], order["bettingNumber"],
                                   order["betAmount"], order["effectiveBetAmount"], order["bettingProfitAndLoss"],
                                   order["totalRebate"], order["netProfitAndLoss"]])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list

    def get_report_total(self, report_name, award_start_diff="", award_end_diff="", terminal=""):
        """
        每日盈亏报表、客户端盈亏、体育项盈亏 - 总计数据
        :param report_name: 每日盈亏 | 客户端盈亏 | 体育项盈亏
        :param award_start_diff:
        :param award_end_diff:
        :param terminal: ios-h5 | android-h5 | pc
        :return:
        """
        if report_name == "每日盈亏":
            mark = "1"
        elif report_name == "客户端盈亏":
            mark = "2"
        else:
            mark = "3"
        url = self.auth_url + "/backendReport/totalDailyProfitAndLoss"
        params = {"startCreateTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
            diff=award_start_diff),
                  "mark": mark,
                  "endCreateTime": "" if not award_end_diff else self.cf.get_md_date_by_now(diff=award_end_diff)}
        if terminal:
            params["terminal"] = terminal
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()
        data = rtn["data"]
        return [data["bettingUserNumber"], data["bettingNumber"], data["betAmount"], data["effectiveBetAmount"],
                data["bettingProfitAndLoss"], data["totalRebate"], data["netProfitAndLoss"]]

    def get_client_report_list(self, award_start_diff="", award_end_diff="", terminal=""):
        """
        客户端盈亏报表 - 列表数据
        :param award_start_diff:
        :param award_end_diff:
        :param terminal: ios-h5 | android-h5 | pc
        :return:
        """
        url = self.auth_url + "/backendReport/queryClientProfitAndLossList"
        order_list = []
        for page in range(1, 1000):
            params = {"page": page, "limit": 100,
                      "startCreateTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                          diff=award_start_diff),
                      "endCreateTime": "" if not award_end_diff else self.cf.get_md_date_by_now(diff=award_end_diff),
                      "terminal": terminal}
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            for order in rtn["data"]["data"]:
                order_list.append([order["terminal"], order["bettingUserNumber"], order["bettingNumber"],
                                   order["betAmount"], order["effectiveBetAmount"], order["bettingProfitAndLoss"],
                                   order["totalRebate"], order["netProfitAndLoss"]])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list

    def get_sport_report_list(self, award_start_diff="", award_end_diff=""):
        """
        体育项报表 - 列表数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        url = self.auth_url + "/backendReport/sportsProfitAndLossList"
        order_list = []
        for page in range(1, 1000):
            params = {"page": page, "limit": 100,
                      "startCreateTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                          diff=award_start_diff),
                      "endCreateTime": "" if not award_end_diff else self.cf.get_md_date_by_now(diff=award_end_diff)}
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            for order in rtn["data"]["data"]:
                order_list.append([order["sportName"], order["bettingUserNumber"], order["bettingNumber"],
                                   order["betAmount"], order["effectiveBetAmount"], order["bettingProfitAndLoss"],
                                   order["totalRebate"], order["netProfitAndLoss"]])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list

    def get_back_water_report_list(self, award_start_diff="", award_end_diff=""):
        """
        返水报表 - 列表数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        url = self.auth_url + "/backendReport/rebateReportList"
        order_list = []
        for page in range(1, 1000):
            params = {"page": page, "limit": 100,
                      "startCreateTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
                          diff=award_start_diff),
                      "endCreateTime": "" if not award_end_diff else self.cf.get_md_date_by_now(diff=award_end_diff)}
            rtn = self.session.post(url, json=params, headers=self.head_bd).json()

            for order in rtn["data"]["data"]:
                order_list.append([order["dateTime"], order["totalRebate"], order["levelBackwaterAmount"],
                                   order["leve2BackwaterAmount"], order["leve3BackwaterAmount"],
                                   order["userBackwaterAmount"], order["soccer"], order["basketball"],
                                   order["tennis"], order["badminton"], order["tableTennis"], order["volleyball"],
                                   order["baseball"], order["iceHockey"]])
            if page >= rtn["data"]["totalPage"]:
                break
        return order_list

    def get_back_water_report_total(self, award_start_diff="", award_end_diff=""):
        """
        返水报表 - 总计数据
        :param award_start_diff:
        :param award_end_diff:
        :return:
        """
        url = self.auth_url + "/backendReport/totalRebateReport"
        params = {"startCreateTime": "" if not award_start_diff else self.cf.get_md_date_by_now(
            diff=award_start_diff),
                  "mark": "1",
                  "endCreateTime": "" if not award_end_diff else self.cf.get_md_date_by_now(diff=award_end_diff)}
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()
        data = rtn["data"]
        return [data["totalRebate"], data["levelBackwaterAmount"], data["leve2BackwaterAmount"],
                data["leve3BackwaterAmount"], data["userBackwaterAmount"], data["soccer"], data["basketball"],
                data["tennis"], data["badminton"], data["tableTennis"], data["volleyball"],
                data["baseball"], data["iceHockey"]]


if __name__ == "__main__":
    a = ReportFuncOfMysql(['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306'], ['app', '123456', '192.168.10.120', '27017'])
    print(a.get_mts_report_order_detail_sql("WYRWbyrpq7TS"))
