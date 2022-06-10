#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import openpyxl,xlrd
from os.path import  join,abspath,dirname
import openpyxl
from pymysql.cursors import DictCursor
import flask,json,pymysql,random,re,datetime
import requests
from concurrent.futures import ThreadPoolExecutor
import json
import re
import time
import xmltodict
import random
import datetime
from MongoFunc import DbQuery
from MyExceptions import *
from CommonFunc import CommonFunc
from MysqlFunc import MysqlCommonQuery,MysqlFunc


class BetController(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self, mysql_info, mongo_info, *args):
        """
        模拟ctrl给我司推送数据
        """
        # self.bc_host = "http://192.168.10.10:8808/mock/message"
        self.bc_host = "http://35.234.4.41:31101/mock/message"
        self.session = requests.session()
        self.dbq = DbQuery(mongo_info)
        # self.ctrl_docs = CtrlIoDocs(mysql_info, mongo_info)
        self.cf = CommonFunc()
        self.mysql = MysqlCommonQuery(mysql_info)
        self.my = MysqlFunc(mysql_info)

    def get_lll(self):
        global sort_num
        """
        通过订单号，获取注单的比赛ID
        ：param order_no:
        :param sort: 默认是0   串关中可根据sort指定某个投注项
        """

        # sql="SELECT IF(any_value(a.sport_id=c.sport_id),any_value(c.sport_name),NULL)'球类',any_value(a.tournament_name)'联赛名称',any_value(a.match_time)'开赛时间',CONCAT(CASE any_value(a.is_live)WHEN 1 THEN '滚球'WHEN 3 THEN '早盘'END,'   ',any_value(a.tournament_name),'   ',any_value(a.home_team_name),'(主队)',' VS ',any_value(a.away_team_name),'(客队)')as '赛事',any_value(a.market_name)'盘口名称',IF(a.outcome_id=1714 AND a.outcome_id=16,SUM(bet_amount*b.level0_actual_percentage)),0)'全场让球盘(主队)',IF(a.outcome_id=1715 AND a.market_id=16,SUM(bet_amount*b.level0_actual_percentage)),0)'全场让球盘(客队)',IF(a.outcome_id=12 AND a.market_id=18,SUM(bet_amount*b.level0_actual_percentage)),0)'全场大小盘(大盘)',IF(a.outcome_id=13 AND a.market_id=18,SUM(bet_amount*b.level0_actual_percentage)),0)'全场大小盘(小盘)',IF(any_value(a.outcome_id)=1 AND any_value(a.market_id)=1,SUM(bet_amount*b.level0_actual_percentage)),0)'全场独赢(1)',IF(any_value(a.outcome_id)=3 AND any_value(a.market_id)=1,SUM(bet_amount*b.level0_actual_percentage)),0)'全场独赢(2)'FROM o_account_order_match as a LEFT JOIN o_account_order as b ON a.order_no=b.order_no LEFT JOIN  s_sport as c ON a.sport_id=c.sport_id WHERE a.market_id IN (16,18,1) AND b.status=1 AND a.sport_id='sr:sport:1' AND b.proxy0_id=(SELECT id FROM m_account WHERE login_account='d0')AND a.match_id='sr:match:33730319'GROUP BY a.match_id,a.outcome_id,a.market_id ORDER BY SUM(bet_amount*b.level0_actual_percentage)) DESC"
        # sql="SELECT IF(any_value(a.sport_id=c.sport_id),any_value(c.sport_name),NULL)'球类',any_value(a.tournament_name)'联赛名称',any_value(a.match_time)'开赛时间',CONCAT(CASE any_value(a.is_live)WHEN 1 THEN '滚球'WHEN 3 THEN '早盘'END,'   ',any_value(a.tournament_name),'   ',any_value(a.home_team_name),'(主队)',' VS ',any_value(a.away_team_name),'(客队)')as '赛事',any_value(a.market_name)'盘口名称',IF(a.outcome_id=1714 AND a.outcome_id=16,SUM(bet_amount*b.level0_actual_percentage)),0)'全场让球盘(主队)',IF(a.outcome_id=1715 AND a.market_id=16,SUM(bet_amount*b.level0_actual_percentage)),0)'全场让球盘(客队)',IF(a.outcome_id=12 AND a.market_id=18,SUM(bet_amount*b.level0_actual_percentage)),0)'全场大小盘(大盘)',IF(a.outcome_id=13 AND a.market_id=18,SUM(bet_amount*b.level0_actual_percentage)),0)'全场大小盘(小盘)',IF(any_value(a.outcome_id)=1 AND any_value(a.market_id)=1,SUM(bet_amount*b.level0_actual_percentage)),0)'全场独赢(1)',IF(any_value(a.outcome_id)=3 AND any_value(a.market_id)=1,SUM(bet_amount*b.level0_actual_percentage)),0)'全场独赢(2)'FROM o_account_order_match as a LEFT JOIN o_account_order as b ON a.order_no=b.order_no LEFT JOIN  s_sport as c ON a.sport_id=c.sport_id WHERE a.market_id IN (16,18,1) AND b.status=1 AND a.sport_id='sr:sport:1' AND b.proxy0_id=(SELECT id FROM m_account WHERE login_account='d0') GROUP BY a.match_id,a.outcome_id,a.market_id ORDER BY SUM(bet_amount*b.level0_actual_percentage)) DESC"
        sql="SELECT IF (any_value (a.sport_id=c.sport_id),any_value (c.sport_name),NULL) '球类',any_value (a.match_time) '开赛时间',CONCAT(CASE any_value (a.is_live) WHEN 1 THEN '滚球' WHEN 3 THEN '早盘' END,'   ',any_value (a.tournament_name),'   ',any_value (a.home_team_name),'(主队)',' VS ',any_value (a.away_team_name),'(客队)') AS '赛事',any_value (a.market_name) '盘口名称',IF (a.outcome_id=1714 AND a.market_id=16,SUM(bet_amount*b.level0_actual_percentage)),0) '全场让球盘(主队)',IF (a.outcome_id=1715 AND a.market_id=16,SUM(bet_amount*b.level0_actual_percentage)),0) '全场让球盘(客队)',IF (a.outcome_id=12 AND a.market_id=18,SUM(bet_amount*b.level0_actual_percentage)),0) '全场大小盘(大盘)',IF (a.outcome_id=13 AND a.market_id=18,SUM(bet_amount*b.level0_actual_percentage)),0) '全场大小盘(小盘)',IF (a.outcome_id=1 AND a.market_id=1,SUM(bet_amount*b.level0_actual_percentage)),0) '全场独赢(1)',IF (a.outcome_id=2 AND a.market_id=1,SUM(bet_amount*b.level0_actual_percentage)),0) '全场独赢(X)',IF (a.outcome_id=3 AND a.market_id=1,SUM(bet_amount*b.level0_actual_percentage)),0) '全场独赢(2)',IF (a.outcome_id=1714 AND a.market_id=66,SUM(bet_amount*b.level0_actual_percentage)),0) '上半场让球盘(主队)',IF (a.outcome_id=1715 AND a.market_id=66,SUM(bet_amount*b.level0_actual_percentage)),0) '上半场让球盘(客队)',IF (a.outcome_id=12 AND a.market_id=68,SUM(bet_amount*b.level0_actual_percentage)),0) '上半场大小盘(大盘)',IF (a.outcome_id=13 AND a.market_id=68,SUM(bet_amount*b.level0_actual_percentage)),0) '上半场大小盘(小盘)',IF (a.outcome_id=1 AND a.market_id=60,SUM(bet_amount*b.level0_actual_percentage)),0) '上半场独赢(1)',IF (a.outcome_id=2 AND a.market_id=60,SUM(bet_amount*b.level0_actual_percentage)),0) '上半场独赢(X)',IF (a.outcome_id=3 AND a.market_id=60,SUM(bet_amount*b.level0_actual_percentage)),0) '上半场独赢(2)' FROM o_account_order_match AS a LEFT JOIN o_account_order AS b ON a.order_no=b.order_no LEFT JOIN s_sport AS c ON a.sport_id=c.sport_id WHERE a.market_id IN ('1','60','16','66','18','68') AND b.STATUS=1 AND a.sport_id='sr:sport:1' AND b.STATUS=1 AND a.sport_id='sr:sport:1' AND b.proxy0_id=(SELECT id FROM m_account WHERE login_account='d0') GROUP BY a.match_id,a.outcome_id,a.market_id ORDER BY SUM(bet_amount*b.level0_actual_percentage)) DESC"
        # print(sql)
        sort_num = self.my.query_data(sql, db_name='bfty_credit')
        # print(sort_num)

        new_list = []
        old_list = []
        tuple =sort_num
        print(f"元祖数量{len(tuple)}")
        for i in range(0, len(tuple)):
            old_list.append(list(tuple[i]))
            print(tuple[i])
            if i == 0:
                new_list.append(list(old_list[i]))
            else:
                for j in range(0, len(new_list)):
                    old = str(old_list[i][0]) + str(old_list[i][1]) + str(old_list[i][2]) + str(old_list[i][3])
                    new = str(new_list[j][0]) + str(new_list[j][1]) + str(new_list[j][2]) + str(new_list[j][3])
                    if old == new:
                        for yyds in range(5,len(new_list[j])):
                            new_list[j][yyds] = int(old_list[i][yyds]) + int(new_list[j][yyds])
                        break
                    else:
                        if j==len(new_list)-1:
                            new_list.append(list(old_list[i]))
                        else:
                            pass

        print(f"字典的数量{len(new_list)}")
        print(new_list)
        # for kk in new_list:
        #     print(kk)

        return sort_num



















if __name__ == "__main__":
    #120环境
    # mongo_inf = ['app', '123456', '192.168.10.120', '27017']
    # mysql_inf = ['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']
    #MDE环境
    mongo_inf = ['sport_test', 'BB#gCmqf3gTO5777', '35.194.233.30', '27017']
    mysql_inf = ['35.194.233.30', 'root', 'BB#gCmqf3gTO5b*', '3306']


    # mf = MongoFunc(mongo_inf)
    bc = BetController(mysql_inf, mongo_inf)




    yyds=bc.get_lll()











