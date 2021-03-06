#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
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





class betting_odds(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info,AB_list,dict):
        """
        实现单注：single bet、串关：stray、复式串关：Duplex
        总赔率求和：odds、可赢金额求和：win amount、返奖金额求和：Rebate amount
        """
        self.session = requests.session()
        self.dbq = DbQuery(mongo_info)
        self.cf = CommonFunc()
        self.mysql = MysqlCommonQuery(mysql_info)
        self.my = MysqlFunc(mysql_info)
        self.AB_list=AB_list
        self.dict=dict


    def single_bet(self, credit_odds_list,order_no,login_account):
        odds = credit_odds_list
        # win_amount = (int(odds[0]) * (bet_amount)) - bet_amount
        # backwater_amount = level3_retreat_proportion * bet_amount
        # rebate_amount = win_amount + backwater_amount + bet_amount

        a=credit_odds_list[0]
        single_bet_odds=str(re.findall(r"\d{1,}?\.\d{2}",str(a))[0])
        print(f"\033[34m登入账号{login_account}的注单：{order_no}，单注的总赔率：{single_bet_odds}\033[0m")
        return single_bet_odds

    def stray_bet(self, credit_odds_list,order_no,login_account):
        stray_bet_list=['2_1_0','3_1_0','4_1_0','5_1_0','6_1_0','7_1_0','8_1_0','9_1_0','10_1_0','11_1_0','12_1_0','13_1_0']
        # 计算赔率
        odds = 1
        for j in credit_odds_list:
            odds = odds*j
        if mix_num in stray_bet_list:
            odds=float(str(re.findall(r"\d{1,}?\.\d{2}",str(odds))[0]))
            print(f"\033[35m登入账号{login_account}的注单：{order_no}，串关{len(credit_odds_list)}串1的总赔率为：{odds}\033[0m")
        return odds



    def Duplex_2_3(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"3串4": [3_1_0, 2_3_0]}
        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]

        # 计算赔率：
        AB = dict['A'] * dict['B']
        BC = dict['B'] * dict['C']
        AC = dict['A'] * dict['C']
        odds_2_3 = AB + BC + AC
        return odds_2_3

    def Duplex_3_4(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"4串11": [4_1_0, 3_4_0, 2_6_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        ABC = dict['A'] * dict['B'] * dict['C']
        ACD = dict['A'] * dict['C'] * dict['D']
        ABD = dict['A'] * dict['B'] * dict['D']
        BCD = dict['D'] * dict['C'] * dict['B']
        odds_3_4 = ABC + ACD + ABD + BCD
        return odds_3_4

    def Duplex_2_6(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"4串11": [4_1_0, 3_4_0, 2_6_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        AD = dict['A'] * dict['D']
        BD = dict['B'] * dict['D']
        CD = dict['D'] * dict['C']
        AB = dict['A'] * dict['B']
        BC = dict['B'] * dict['C']
        AC = dict['A'] * dict['C']
        odds_2_6 = AB + BC + AC + CD + BD + AD

        return odds_2_6

    def Duplex_4_5(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"5串26": [5_1_0, 4_5_0, 3_10_0, 2_10_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        ABCD = dict['A'] * dict['B'] * dict['C'] * dict['D']
        ABCE = dict['B'] * dict['C'] * dict['A'] * dict['E']
        ABDE = dict['A'] * dict['B'] * dict['E'] * dict['D']
        ACED = dict['A'] * dict['C'] * dict['E'] * dict['D']
        BCDE = dict['B'] * dict['C'] * dict['D'] * dict['E']
        odds_4_5 = ABCD + ABCE + ABDE + ACED + BCDE
        return odds_4_5

    def Duplex_3_10(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"5串26": [5_1_0, 4_5_0, 3_10_0, 2_10_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        CDE = dict['D'] * dict['E'] * dict['C']
        ABE = dict['A'] * dict['B'] * dict['E']
        ACE = dict['A'] * dict['C'] * dict['E']
        ADE = dict['D'] * dict['A'] * dict['E']
        BCE = dict['E'] * dict['C'] * dict['B']

        BDE = dict['B'] * dict['D'] * dict['E']
        ABC = dict['A'] * dict['B'] * dict['C']
        ACD = dict['A'] * dict['C'] * dict['D']
        ABD = dict['A'] * dict['B'] * dict['D']
        BCD = dict['D'] * dict['C'] * dict['B']
        odds_3_10 = ABC + ACD + ABD + BCD + CDE + ABE + ACE + ADE + BCE + BDE

        return odds_3_10

    def Duplex_2_10(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"5串26": [5_1_0, 4_5_0, 3_10_0, 2_10_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        AD = dict['A'] * dict['D']
        BD = dict['B'] * dict['D']
        AE = dict['A'] * dict['E']
        BE = dict['B'] * dict['E']
        CE = dict['C'] * dict['E']
        DE = dict['D'] * dict['E']

        CD = dict['D'] * dict['C']
        AB = dict['A'] * dict['B']
        BC = dict['B'] * dict['C']
        AC = dict['A'] * dict['C']
        odds_2_10 = AB + BC + AC + CD + BD + AD + AE + BE + CE + DE
        return odds_2_10

    def Duplex_5_6(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"6串57": [6_1_0, 5_6_0, 4_15_0, 3_20_0, 2_15_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        ABCDE = dict['A'] * dict['B'] * dict['C'] * dict['D'] * dict['E']
        ABCDF = dict['B'] * dict['C'] * dict['A'] * dict['D'] * dict['F']
        ABCEF = dict['A'] * dict['B'] * dict['E'] * dict['C'] * dict['F']
        ABDEF = dict['A'] * dict['B'] * dict['E'] * dict['D'] * dict['F']
        ACDEF = dict['A'] * dict['C'] * dict['D'] * dict['E'] * dict['F']
        BCDEF = dict['B'] * dict['C'] * dict['D'] * dict['E'] * dict['F']
        odds_5_6 = ABCDE + ABCDF + ABCEF + ABDEF + ACDEF + BCDEF
        return odds_5_6

    def Duplex_4_15(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"6串57": [6_1_0, 5_6_0, 4_15_0, 3_20_0, 2_15_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        ABCF = dict['A'] * dict['B'] * dict['C'] * dict['F']
        ABDF = dict['B'] * dict['D'] * dict['A'] * dict['F']
        ABEF = dict['A'] * dict['B'] * dict['E'] * dict['F']
        CDEF = dict['F'] * dict['C'] * dict['E'] * dict['D']
        ACDF = dict['A'] * dict['C'] * dict['D'] * dict['F']

        ACEF = dict['A'] * dict['E'] * dict['C'] * dict['F']
        ADEF = dict['D'] * dict['F'] * dict['A'] * dict['E']
        BCDF = dict['C'] * dict['B'] * dict['F'] * dict['D']
        BCEF = dict['B'] * dict['C'] * dict['E'] * dict['F']
        BDEF = dict['B'] * dict['F'] * dict['D'] * dict['E']

        ABCD = dict['A'] * dict['B'] * dict['C'] * dict['D']
        ABCE = dict['B'] * dict['C'] * dict['A'] * dict['E']
        ABDE = dict['A'] * dict['B'] * dict['E'] * dict['D']
        ACED = dict['A'] * dict['C'] * dict['E'] * dict['D']
        BCDE = dict['B'] * dict['C'] * dict['D'] * dict['E']

        odds_4_15 = ABCD + ABCE + ABDE + ACED + BCDE + ABCF + ABDF + ABEF + CDEF + ACDF + ACEF + ADEF + BCDF + BCEF + BDEF
        return odds_4_15

    def Duplex_3_20(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"6串57": [6_1_0, 5_6_0, 4_15_0, 3_20_0, 2_15_0]}

        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        ABF = dict['A'] * dict['B'] * dict['F']
        ACF = dict['A'] * dict['C'] * dict['F']
        ADF = dict['A'] * dict['D'] * dict['F']
        AEF = dict['E'] * dict['A'] * dict['F']
        BCF = dict['B'] * dict['C'] * dict['F']

        BDF = dict['B'] * dict['D'] * dict['F']
        BEF = dict['E'] * dict['B'] * dict['F']
        CDF = dict['D'] * dict['C'] * dict['F']
        CEF = dict['C'] * dict['E'] * dict['F']
        DEF = dict['D'] * dict['E'] * dict['F']

        CDE = dict['D'] * dict['E'] * dict['C']
        ABE = dict['A'] * dict['B'] * dict['E']
        ACE = dict['A'] * dict['C'] * dict['E']
        ADE = dict['D'] * dict['A'] * dict['E']
        BCE = dict['E'] * dict['C'] * dict['B']

        BDE = dict['B'] * dict['D'] * dict['E']
        ABC = dict['A'] * dict['B'] * dict['C']
        ACD = dict['A'] * dict['C'] * dict['D']
        ABD = dict['A'] * dict['B'] * dict['D']
        BCD = dict['D'] * dict['C'] * dict['B']

        odds_3_20 = ABC + ACD + ABD + BCD + CDE + ABE + ACE + ADE + BCE + BDE + ABF + ACF + ADF + AEF + BCF + BDF + BEF + CDF + CEF + DEF
        return odds_3_20

    def Duplex_2_15(self,credit_odds_list,AB_list, dict,order_no):
        Duplex = {"6串57": [6_1_0, 5_6_0, 4_15_0, 3_20_0, 2_15_0]}
        for i in range(0, len(credit_odds_list)):
            dict[AB_list[i]] = credit_odds_list[i]
        # 计算赔率：
        AD = dict['A'] * dict['D']
        BD = dict['B'] * dict['D']
        AE = dict['A'] * dict['E']
        BE = dict['B'] * dict['E']
        CE = dict['C'] * dict['E']
        DE = dict['D'] * dict['E']
        AF=dict['A'] * dict['F']
        BF=dict['B'] * dict['F']
        CF=dict['C'] * dict['F']
        DF=dict['D'] * dict['F']
        EF=dict['E'] * dict['F']

        CD = dict['D'] * dict['C']
        AB = dict['A'] * dict['B']
        BC = dict['B'] * dict['C']
        AC = dict['A'] * dict['C']
        odds_2_15 = AB + BC + AC + CD + BD + AD + AE + BE + CE + DE + AF+ BF+ CF+ DF+ EF
        return odds_2_15

    def Duplex_bet(self, credit_odds_list,AB_list,dict,order_no,login_account):
        yyds = {'复式串关': [3, {"3串4": [3_1_0, 2_3_0,3_4_1]}, {"4串11": [4_1_0, 3_4_0, 2_6_0,4_11_1]},{"5串26": [5_1_0, 4_5_0, 3_10_0, 2_10_0,5_26_1]}, {"6串57": [6_1_0, 5_6_0, 4_15_0, 3_20_0, 2_15_0,6_57_1]}]}

        Duplex_bet_odds=""
        # print(mix_num)
        # 3串4赔率结算：
        if mix_num=='2_3_0':
            Duplex_bet_odds=self.Duplex_2_3(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关2串1*3的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num==str('3_4_1'):
            sum01=self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no,login_account=login_account)


            sum02=self.Duplex_2_3(credit_odds_list=credit_odds_list,  AB_list=AB_list, dict=dict,order_no=order_no)
            Duplex_bet_odds=sum01+sum02
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[34m登入账号{login_account}的m注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]}的总赔率为：{Duplex_bet_odds}\n\033[0m")

        # 4串11赔率结算：
        if mix_num == str('3_4_0'):
            Duplex_bet_odds=self.Duplex_3_4(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关3串1*4的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('2_6_0'):
            Duplex_bet_odds=self.Duplex_2_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关2串1*6的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('4_11_1'):
            sum01 = self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no,login_account=login_account)
            sum02 = self.Duplex_3_4(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum03 = self.Duplex_2_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            Duplex_bet_odds = sum01 + sum02+sum03
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[34m登入账号{login_account}的注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]+list(mix_num)[3]}的总赔率为：{Duplex_bet_odds}\n\033[0m")

        # 5串26赔率结算：
        if mix_num == str('4_5_0'):
            Duplex_bet_odds = self.Duplex_4_5(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关4串1*5的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('3_10_0'):
            Duplex_bet_odds = self.Duplex_3_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关3串1*10的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('2_10_0'):
            Duplex_bet_odds = self.Duplex_2_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关2串1*10的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('5_26_1'):
            sum01 = self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no,login_account=login_account)
            sum02 = self.Duplex_4_5(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum03 = self.Duplex_3_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum04= self.Duplex_2_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            Duplex_bet_odds = sum01 + sum02+sum03+sum04
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[34m登入账号{login_account}的注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]+list(mix_num)[3]}的总赔率为：{Duplex_bet_odds}\n\033[0m")

        # 6串57赔率结算：
        if mix_num == str('5_6_0'):
            Duplex_bet_odds = self.Duplex_5_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关5串1*6的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('4_15_0'):
            Duplex_bet_odds = self.Duplex_4_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关4串1*15的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('3_20_0'):
            Duplex_bet_odds = self.Duplex_3_20(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关3串1*20的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('2_15_0'):
            Duplex_bet_odds = self.Duplex_2_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[32m登入账号{login_account}的注单：{order_no}复式串关2串1*15的总赔率为：{Duplex_bet_odds}\033[0m")
        if mix_num == str('6_57_1'):
            sum01 = self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no,login_account=login_account)
            sum02 = self.Duplex_5_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum03 = self.Duplex_4_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum04 = self.Duplex_3_20(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum05 = self.Duplex_2_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            Duplex_bet_odds = sum01+sum02+sum03+sum04+sum05
            Duplex_bet_odds = float(str(re.findall(r"\d{1,}?\.\d{2}", str(Duplex_bet_odds))[0]))
            print(f"\033[34m登入账号{login_account}的注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]+list(mix_num)[3]}的总赔率为：{Duplex_bet_odds}\n\033[0m")

        return Duplex_bet_odds





class BetController(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self, mysql_info, mongo_info, AB_list,dict):
        """
        模拟ctrl给我司推送数据
        """
        self.session = requests.session()
        self.dbq = DbQuery(mongo_info)
        # self.ctrl_docs = CtrlIoDocs(mysql_info, mongo_info)
        self.cf = CommonFunc()
        self.mysql = MysqlCommonQuery(mysql_info)
        self.my = MysqlFunc(mysql_info)
        self.ce = betting_odds(mysql_info, mongo_info,AB_list,dict)

class SQL_report_ods(BetController):

    def order_no(self,bet_type,status,AB_list,dict,proxy3_id):
        """
        @根据条件：bet_type查询其注单：0全部、1单注、2串关、3串关、4串关和复式串关
        @根据条件：STATUS：0待确认、1待结算、2已结算、3已取消
        """
        if bet_type==0:
            sql = f"SELECT order_no FROM o_account_order WHERE STATUS='{status}' AND proxy3_id='{proxy3_id}'"
            sum = self.my.query_data(sql, db_name='bfty_credit')
        elif bet_type==4:
            sql = f"SELECT order_no FROM o_account_order WHERE STATUS='{status}' AND bet_type!=1 AND proxy3_id='{proxy3_id}'"
            sum = self.my.query_data(sql, db_name='bfty_credit')
        else:
            sql = f"SELECT order_no FROM o_account_order WHERE STATUS='{status}' AND bet_type='{bet_type}' AND proxy3_id='{proxy3_id}'"
            sum = self.my.query_data(sql, db_name='bfty_credit')

        order_no_lsit=[]
        for i in range(0,len(sum)):
            order_no_lsit.append(sum[i][0])
        print(order_no_lsit)
        print(len(order_no_lsit))

        for order in order_no_lsit:
            self.bet_type(order_no=order,AB_list=AB_list,dict=dict,proxy3_id=proxy3_id,status=status)
        return order_no_lsit


    def bet_type(self,order_no,AB_list,dict,proxy3_id,status,):
        global bet_amount,level3_retreat_proportion
        """
        @判断注单的类型：bet_type:1(单注)，bet_type:2(串关)，bet_type:3(复式串关)
        @根据类型调用相应的函数进行结算
        """
        sql =f"SELECT bet_type,bet_amount,level3_retreat_proportion FROM o_account_order WHERE STATUS='{status}' AND order_no='{order_no}'AND proxy3_id='{proxy3_id}'"
        sum = self.my.query_data(sql, db_name='bfty_credit')
        # print(sum)

        bet_type=sum[0][0]
        bet_amount = sum[0][1]
        level3_retreat_proportion=sum[0][2]

        self.credit_odds(order_no=order_no,bet_type=bet_type,AB_list=AB_list,dict=dict)

        return bet_type

    def credit_odds(self,order_no,bet_type,AB_list,dict):
        global mix_num
        """
        @根据注单类型查询其赔率
        @根据赔率进行计算
        """
        sql01 = f"SELECT mix_num,bet_type,login_account FROM o_account_order WHERE order_no='{order_no}'"
        sum01 = self.my.query_data(sql01, db_name='bfty_credit')


        sql = f"SELECT credit_odds,odds_type FROM o_account_order_match  WHERE order_no='{order_no}'"
        sum = self.my.query_data(sql, db_name='bfty_credit')


        #取得注单的赔率，欧盘保持原始赔率，香港盘原始赔率+1,顺便取得赔率类型
        credit_odds_list=[]
        yyds_ky=""
        mix_num=sum01[0][0]
        bet_type=sum01[0][1]
        login_account=sum01[0][2]
        for i in range(0,len(sum)):
            if sum[i][-1]==1:
                credit_odds_list.append(sum[i][0])
            else:
                if bet_type==1:
                    sum_odds = (sum[i][0])
                else:
                    sum_odds=(sum[i][0])+1
                credit_odds_list.append(sum_odds)
        # print(f"查询注单的盘赔率为：{credit_odds_list}")

        yyds_ky=self.Calculate_odds(credit_odds_list=credit_odds_list,bet_type=bet_type,AB_list=AB_list,dict=dict,order_no=order_no,login_account=login_account)

        return yyds_ky

    def total_odds(self, order_no,number):
        """
        @根据注单类型查询其赔率类型
        @根据赔率类型进行判断返回：欧盘、香港盘
        """

        sql = f"SELECT odds_type FROM o_account_order_match  WHERE order_no='{order_no}'"
        sum = self.my.query_data(sql, db_name='bfty_credit')

        # 取得注单的赔率，欧盘保持原始赔率，香港盘原始赔率+1,顺便取得赔率类型
        total_odds_list = []
        for i in range(0, len(sum)):
            total_odds_list.append(sum[i][0])
        # print(total_odds_list)
        # 取得赔率的赔率类型：
        if 1 in total_odds_list:
            if number==' ':
                type_odds = '1'
            else:
                type_odds = '欧赔'
        else:
            if number==' ':
                type_odds ='2'
            else:
                type_odds = '港赔'
        print(f"查询注单{order_no}的赔率类型为：{type_odds}")

        return type_odds

    def Calculate_odds(self, credit_odds_list,bet_type,AB_list,dict,order_no,login_account):
        """
        @根据注单类型判断其类型，1为单注，2为串关，3为复式串关
        @根据其类型赔率进行计算
        """
        odd=""
        bet_type_dict={'单注':[1,1_1_0],'串关':[2,2_1_0],
                       '复式串关':[3,{"3串4":[3_1_0,2_3_0]},{"4串11":[4_1_0,3_4_0,2_6_0]},{"5串26":[5_1_0,4_5_0,3_10_0,2_10_0]},{"6串57":[6_1_0,5_6_0,4_15_0,3_20_0,2_15_0]}]}
        if bet_type==1:
            odd=self.ce.single_bet(credit_odds_list=credit_odds_list,order_no=order_no,login_account=login_account)
        elif bet_type==2:
            odd=self.ce.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no,login_account=login_account)
        else:
            odd=self.ce.Duplex_bet(credit_odds_list=credit_odds_list,AB_list=AB_list, dict=dict,order_no=order_no,login_account=login_account)
        return odd



























#佣金计算
class water_ammount(BetController):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, *args):
        """
        模拟ctrl给我司推送数据
        """
        self.session = requests.session()
        self.dbq = DbQuery(mongo_info)
        self.cf = CommonFunc()
        self.mysql = MysqlCommonQuery(mysql_info)
        self.my = MysqlFunc(mysql_info)



    #注单是否能返水，预处理判断
    def market_id(self,order_no,agint_id):
        """
        @此函数用于对佣金比例进行对比：
        num_0=0，佣金全部赋值为0，
        num_0=1，佣金为真实计算佣金
        """
        # order_no = "XFDr4e3FSzD5"
        #可进行佣金结算的盘口ID
        market_id_dict = {'sr:sport:1': {1: ['16', '66', '18', '68', '104', '19', '20', '69', '70', '26', '37', '79', '547', '165', '176', '166','177', '172', '183', '139', '152', '116', '117', '127', '120'],3: ['16', '66', '18', '68', '104', '19', '20', '69', '70', '26', '74', '27', '28', '37', '79', '36','547', '165', '176', '166', '177', '172', '183', '139', '152', '116', '117', '127', '58', '59','120']},
                          'sr:sport:2': {1: ['223', '225', '227', '228', '66', '68', '303', '236', '756', '757'],3: ['223', '225', '227', '228', '229', '66', '68', '69', '70', '74', '303','236', '756', '757', '304']},
                          'sr:sport:3': {1: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '246', '247','248', '256', '258', '16', '18', '26', '410', '460', '446', '314'],3: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '245', '246','247', '248', '256', '258', '16', '18', '26', '410', '460', '446']},
                          'sr:sport:4': {1: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '246', '247','248', '256', '258', '16', '18', '26', '410', '460', '446', '314'],3: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '245', '246','247', '248', '256', '258', '16', '18', '26', '410', '460', '446']},
                          'sr:sport:5': {1: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '246', '247','248', '256', '258', '16', '18', '26', '410', '460', '446', '314'],3: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '245', '246','247', '248', '256', '258', '16', '18', '26', '410', '460', '446']},
                          'sr:sport:20': {1: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '246', '247','248', '256', '258', '16', '18', '26', '410', '460', '446', '314'],3: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '245', '246','247', '248', '256', '258', '16', '18', '26', '410', '460', '446']},
                          'sr:sport:23': {1: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '246', '247','248', '256', '258', '16', '18', '26', '410', '460', '446', '314'],3: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '245', '246','247', '248', '256', '258', '16', '18', '26', '410', '460', '446']},
                          'sr:sport:31': {1: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '246', '247','248', '256', '258', '16', '18', '26', '410', '460', '446', '314'],3: ['188', '187', '314', '189', '190', '191', '203', '204', '237', '238', '245', '246','247', '248', '256', '258', '16', '18', '26', '410', '460', '446']}}
        # 查询订单类型和可计算佣金的比赛类型：
        sql02 = f"SELECT c.bet_type,c.sport_id,b.is_live,b.market_id FROM o_account_order as c LEFT JOIN o_account_order_match as b ON b.order_no=c.order_no WHERE c.order_no='{order_no}'"
        sum02 = self.my.query_data(sql02, db_name='bfty_credit')

        water_account=""
        # 判断查询出的数据，是否能进行佣金结算
        if sum02[0][0]==1:
            if sum02[0][3] in market_id_dict[(sum02[0][1])][(sum02[0][2])]:
                num_0 = 1
                water_account=self.water(order_no,num_0)
            else:
                num_0 = 0
                water_account = self.water(order_no,num_0)
                print(f"\033[32m此订单号{order_no}为单注，不在佣金盘口计算之类，无法进行佣金计算,默认为0\033[0m")
        else:
            num_0 = 0
            water_account = self.water(order_no,num_0)
            print(f"\033[34m此订单号{order_no}为串关或负数串关,此两类订单类型，默认佣金为0，不用计算\033[0m")

        return water_account


    # 会员、代理返水佣金计算
    def water(self,order_no,num_0):
        yy_list = ["efficient_amount", "company_retreat_proportion", "level0_retreat_proportion",
                   "level1_retreat_proportion", "level2_retreat_proportion", "level3_retreat_proportion",
                   "company_actual_percentage", "level0_actual_percentage", "level1_actual_percentage",
                   "level2_actual_percentage", "level3_actual_percentage", ]
        yy_dict = {'efficient_amount': [], 'company_retreat_proportion': [], 'level0_retreat_proportion': [],
                   'level1_retreat_proportion': [], 'level2_retreat_proportion': [], 'level3_retreat_proportion': [],
                   'company_actual_percentage': [], 'level0_actual_percentage': [], 'level1_actual_percentage': [],
                   'level2_actual_percentage': [], 'level3_actual_percentage': []}

        yyts="efficient_amount,company_retreat_proportion,level0_retreat_proportion,level1_retreat_proportion,level2_retreat_proportion,level3_retreat_proportion,"\
             "company_actual_percentage,level0_actual_percentage,level1_actual_percentage,level2_actual_percentage,level3_actual_percentage"

        yybs="backwater_amount,level3_backwater_amount,level2_backwater_amount,level1_backwater_amount,level0_backwater_amount,company_backwater_amount"

        water_list = []
        sum_list=[]
        #判断是否进行佣金计算的字段：0不计算赋值为0、1计算返回计算值
        if num_0==1:
            #查询会员、公司~登3的佣金
            sql=f"SELECT {yybs} FROM o_account_order WHERE order_no='{order_no}'"
            sum=self.my.query_data(sql, db_name='bfty_credit')

            ##循环SQL返回数据，并写入对应的列表里
            for i in range(0, len(sum[0])):
                sum_list.append(float(sum[0][i]))


            #查询有效金额、公司~登3的佣金比例、占成比例
            sql01 = f"SELECT {yyts} FROM o_account_order WHERE order_no='{order_no}'"
            sum01 = self.my.query_data(sql01, db_name='bfty_credit')

            #循环SQL返回数据，并写入对应的字典里
            for i in range(0, len(sum01[0])):
                yy_dict[yy_list[i]] = (sum01[0][i])
            # print(yy_dict)

            #计算会员、登3~公司的佣金，并写入列表
            # 计算会员、登3~公司的佣金，并写入列表
            # 会员佣金
            member = (yy_dict['efficient_amount'] * yy_dict['level3_retreat_proportion'])
            member = self.water_intercept(number=member)
            water_list.append(member)
            # 登3佣金
            d3 = yy_dict['efficient_amount'] * (yy_dict['level2_retreat_proportion']) * (1 - (yy_dict['level3_actual_percentage']))
            d3 = float(d3) - member
            d3 = self.water_intercept(number=d3)
            water_list.append(d3)
            # 登2佣金
            d2 = yy_dict['efficient_amount'] * (yy_dict['level1_retreat_proportion']) * (1 - (yy_dict['level2_actual_percentage'] + yy_dict['level3_actual_percentage']))
            d2 = float(d2) - (d3 + member)
            d2 = self.water_intercept(number=d2)
            water_list.append(d2)
            # 登1佣金
            d1 = yy_dict['efficient_amount'] * (yy_dict['level0_retreat_proportion']) * (1 - (yy_dict['level1_actual_percentage'] + yy_dict['level2_actual_percentage'] + yy_dict['level3_actual_percentage']))
            d1 = float(d1) - (d2 + d3 + member)
            d1 = self.water_intercept(number=d1)
            water_list.append(d1)
            # 登0佣金
            d0 = yy_dict['efficient_amount'] * (yy_dict['company_retreat_proportion']) * (1 - (yy_dict['level0_actual_percentage'] + yy_dict['level1_actual_percentage'] + yy_dict['level2_actual_percentage'] + yy_dict['level3_actual_percentage']))
            d0 = float(d0) - (d1 + d2 + d3 + member)
            d0 = self.water_intercept(number=d0)
            water_list.append(d0)
            # 公司佣金
            d = -(member + d3 + d2 + d1 + d0)
            d = self.water_intercept(number=d)
            water_list.append(d)
            # 所有佣金相加是否等于0
            d_z = member + d3 + d2 + d1 + d0 + d

            print(f"---------------------------------------------------------------------------------------------\n"
                  f"我的佣金计算：会员的佣金：{water_list[0]},d3的佣金：{water_list[1]},d2的佣金：{water_list[2]},d1的佣金：{water_list[3]},d0的佣金：{water_list[4]},公司的佣金：{water_list[5]}")
            print(f"SQL佣金计算:会员的佣金：{sum_list[0]},d3的佣金：{sum_list[1]},d2的佣金：{sum_list[2]},d1的佣金：{sum_list[3]},d0的佣金：{sum_list[4]},公司的佣金：{sum_list[5]}"
                  f"\n---------------------------------------------------------------------------------------------")

            #循环取到的SQL数据的所有佣金值，和自己计算的佣金制，验证对应佣金是否相等
            for i in range(0,len(water_list)):
                if water_list[i]==sum_list[i]:
                    pass
                else:
                    print(f"我的佣金计算和SQL佣金计算数据对比错误,{water_list[i]}/{sum_list[i]}")
        else:
            for number in range(0,5):
                water_list.append(0)
        return water_list

    #根据佣金金额，进行正则表达式截取、保留两位小数
    def water_intercept(self,number):
        # 判断number，并对佣金值做截取，然后返回
        # print(re.findall(r"\d{1,}?\.\d{2}", str(number)))
        if number==0:
            lember=0
        elif re.findall(r"\d{1,}?\.\d{2}", str(number))==[]:
            lember=number
        elif number > 0:
            lember =float(str(re.findall(r"\d{1,}?\.\d{2}",str(number))[0]))
        else:
            lember =-float(str(re.findall(r"\d{1,}?\.\d{2}",str(number))[0]))

        #若lember=0.0，直接返回为0
        if lember==0.0:
            lember=0
        else:
            lember=lember
        return lember



    # 总佣金结算
    def total_commission(self,agent_id,member_id,sportId,marketId,tournamentId,matchId,login_account,begin,end,Duplex,ZD,excel_num):
        '''
        @报表规则：
        1、总佣金是查询登陆者的下级所产生的总和（涉及总台~登3），会员的总佣金取此账号，所订单会员佣金的总和
        2、公司是查询登录者的公司输赢（包括跳转任意下级代理），会员的公司输赢取此账号，所订单(公司输赢+公司佣金)的总和
        '''

        # 判断agent_id为代理ID，还是为代理账号
        z_m_num01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        vv_id = []
        qq_id = []
        for j in list(agent_id):
            if j in z_m_num01:
                pass
            else:
                vv_id.append(0)
                # print("这是一个代理账号")
        # 判断member_id为会员ID，还是为会员账号
        for j in list(member_id):
            if j in z_m_num01:
                pass
            else:
                qq_id.append(0)
                # print("这是一个代理账号")
        # agent_id传递：
        if vv_id == []:
            pass
        else:
            sql00 = f"SELECT id as '代理ID' FROM m_account as c WHERE account='{agent_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            agent_id =sum00[0][0]


        # member_id传递：
        if qq_id == []:
            pass
        else:
            sql00 = f"SELECT id as '会员ID' FROM u_user WHERE login_account='{member_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            member_id = sum00[0][0]

        # 查询登录代理的代理等级,num是查询者ID，num_new是求和条件，错位取
        if ZD=='':
            if vv_id == [] and agent_id!='':
                sql = f"SELECT role_id FROM m_account WHERE id='{agent_id}'"
                sum = self.my.query_data(sql, db_name='bfty_credit')
                num = int(sum[0][0])
                num_new = num
            else:
                sql = f"SELECT role_id FROM m_account WHERE login_account='{login_account}'"
                sum = self.my.query_data(sql, db_name='bfty_credit')
                num = int(sum[0][0])
                num_new=num+1
        else:
            if agent_id=='':
                sql = f"SELECT role_id FROM m_account WHERE login_account='{login_account}'"
                sum = self.my.query_data(sql, db_name='bfty_credit')
                num = int(sum[0][0])
                num_new = num + 1
            else:
                num=0
                num_new=0

        #SQL参数列表
        bet_type_list = ['=', '!=']
        proxy_id_list = ['c.proxy0_id', 'c.proxy1_id', 'c.proxy2_id', 'c.proxy3_id','c.user_id','c.sport_id','d.market_id','d.tournament_id','d.match_id']
        water_SQL_list = [
                        'SUM(c.efficient_amount*c.company_retreat_proportion)',
                        'SUM(c.efficient_amount*c.level0_retreat_proportion)',
                        'SUM(c.efficient_amount*c.level1_retreat_proportion)',
                        'SUM(c.efficient_amount*c.level2_retreat_proportion)',
                        'SUM(c.efficient_amount*c.level3_retreat_proportion)']

        total_tuple=(agent_id,member_id,sportId,marketId,tournamentId,matchId)
        xxx_list=['agent_id','member_id','sportId','marketId','tournamentId','matchId']
        total_list=[]
        for jj in  total_tuple:
            if jj=='' or jj=="":
                pass
            else:
                total_list.append(xxx_list[total_tuple.index(jj)])

        #判断以什么时间计算的报表
        if excel_num==1:
            time='c.create_time'
            time_value='投注时间'
        elif excel_num==2:
            time = 'd.match_time'
            time_value = '赛事时间'
        else:
            time='c.award_time'
            time_value = '结算时间'

        #判断代理佣金比等级
        #判断到相应的ID时，进行数据处理
        sum02=""
        if len(total_list)==1:
            if total_list[0]=='agent_id':
                # # 查询ID的代理等级：
                # if ZD=='454':
                #     sql01 = f"SELECT role_id FROM m_account WHERE id='{agent_id}'"
                #     sum01 = self.my.query_data(sql01, db_name='bfty_credit')
                #     num = int(sum01[0][0])
                #     num_new=num
                # 根据查询等级，进行参数替换
                # print(water_SQL_list[num_new],proxy_id_list[num])
                sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金' FROM o_account_order as c WHERE {proxy_id_list[num]}='{agent_id}' AND c.award_time>='{begin}' AND c.award_time<='{end}' AND c.status=2"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                sum02 = float(sum02[0][0])
                print(sum02)
                sum02 = self.water_intercept(number=sum02)
                print(f"\033[34m{time_value}-登{num}查询-登{num_new}-{agent_id}的总佣金为{sum02}\033[0m")
            elif total_list[0]=='member_id':
                # 根据会员ID，进行参数替换：
                num=4
                num_new=4
                if Duplex=='':
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金',any_value(c.login_account) as '登入账号' FROM o_account_order as c WHERE {proxy_id_list[num]}='{member_id}' AND c.award_time>='{begin}' AND c.award_time<='{end}' AND c.status=2"
                else:
                    bet_type = bet_type_list[1]
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金',any_value(c.login_account) as '登入账号' FROM o_account_order as c LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE {proxy_id_list[num]}='{member_id}' AND {time}>='{begin}' AND {time}<='{end}' AND c.bet_type{bet_type}1"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                username = (sum02[0][1])
                sum02 = float(sum02[0][0])
                print(sum02)
                sum02 = self.water_intercept(number=sum02)
                print(f"\033[34m{time_value}-登{num-1}查询-会员{username}-{member_id}的总佣金为{sum02}\033[0m")
            elif total_list[0]=='sportId':
                # 根据球类ID，进行参数替换：
                if sportId=='串关':
                    sum02=0
                else:
                    num01 = 5
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE {proxy_id_list[num01]}='{sportId}' AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' AND c.status=2"
                    sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                    username = (sum02[0][1])
                    sum02 = float(sum02[0][0])
                    sum02 = self.water_intercept(number=sum02)
                    # print(sql02)
                    print(f"\033[34m{time_value}-登{num}查询-{username}的-{sportId}的总佣金为{sum02}\033[0m")
            elif total_list[0] == 'tournamentId':
                # 根据球类ID和联赛ID，进行参数替换：
                num01 = 7
                if tournamentId=='串关':
                    bet_type = bet_type_list[1]
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金','串关',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE  {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' AND c.bet_type{bet_type}1"
                else:
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金',any_value(tournament_name),CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN o_account_order_match as d ON d.order_no=c.order_no WHERE {proxy_id_list[num01]}='{tournamentId}' AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' AND c.status=2"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                username =sum02[0][2]
                tournamentId = sum02[0][1]
                sum02 =float(sum02[0][0])
                sum02 = self.water_intercept(number=sum02)
                print(f"\033[34m{time_value}-登{num}查询-{username}-{tournamentId}的总佣金为{sum02}\033[0m")
            elif total_list[0] == 'matchId':
                # 根据球类ID和赛事ID，进行参数替换：
                num01 = 8
                if matchId == '串关':
                    bet_type = bet_type_list[1]
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金','串关',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c LEFT JOIN v_order_match as d ON c.order_no=d.order_no  WHERE  {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' AND c.bet_type{bet_type}1"
                else:
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金',any_value({proxy_id_list[num01]}),any_value({proxy_id_list[num01]}),CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN o_account_order_match as d ON d.order_no=c.order_no WHERE {proxy_id_list[num01]}='{matchId}' AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' AND c.status=2"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                matchId = (sum02[0][1])
                username = (sum02[0][2])
                sum02 = float(sum02[0][0])
                sum02 = self.water_intercept(number=sum02)
                print(f"\033[34m{time_value}-登{num}查询-{username}-{matchId}的总佣金为{sum02}\033[0m")
        elif len(total_list)==2 or len(total_list)==3:
            if total_list[1] == 'marketId':
                # 根据球类ID和盘口ID，进行参数替换：
                num01 = 6
                if marketId=='串关':
                    bet_type = bet_type_list[1]
                    bet_type=f"AND c.bet_type{bet_type}1"
                    sql02 = f"SELECT {water_SQL_list[num+1]} as '总佣金','串关',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' {bet_type} AND c.status=2"
                else:
                    bet_type = bet_type_list[0]
                    if matchId == '':
                        bet_type=f"AND c.bet_type{bet_type}1"
                    else:
                        bet_type = f"AND c.bet_type{bet_type}1 AND d.match_id='{matchId}'"
                    sql02 = f"SELECT {water_SQL_list[num_new]} as '总佣金',any_value(market_name),CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN o_account_order_match as d ON d.order_no=c.order_no  WHERE {proxy_id_list[num01]}='{marketId}' and {proxy_id_list[5]}='{sportId}' AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND c.status=2 AND {time}<='{end}' {bet_type}"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                username = (sum02[0][2])
                marketId= (sum02[0][1])
                sum02=float(sum02[0][0])
                # print(sum02)
                sum02 = self.water_intercept(number=sum02)
                print(f"\033[34m{time_value}-登{num}查询-{username}-{marketId}的总佣金为{sum02}\033[0m")
        print(sql02)
        return sum02

    # 公司输赢计算
    def Company_winlose(self,agent_id,member_id,sportId,marketId,tournamentId,matchId,login_account,begin,end,Duplex,excel_num):
        '''
         @报表规则：
         1、总佣金是查询登陆者的下级所产生的总和（涉及总台~登3），会员的总佣金取此账号，所订单会员佣金的总和
         2、公司是查询登录者的公司输赢（包括跳转任意下级代理），会员的公司输赢取此账号，所订单(公司输赢+公司佣金)的总和
        '''

        #判断agent_id为代理ID，还是为代理账号
        z_m_num01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        vv_id = []
        qq_id=[]
        for j in list(agent_id):
            if j in z_m_num01:
                pass
            else:
                vv_id.append(0)
                # print("这是一个代理账号")
        # 判断member_id为会员ID，还是为会员账号
        for j in list(member_id):
            if j in z_m_num01:
                pass
            else:
                qq_id.append(0)
                # print("这是一个代理账号")
        #agent_id传递：
        if vv_id==[]:
            pass
        else:
            sql00 = f"SELECT id as '代理ID' FROM o_account_order as c WHERE account='{agent_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            agent_id = sum00[0][0]


        #member_id传递：
        if qq_id==[]:
            pass
        else:
            sql00 = f"SELECT id as '会员ID' FROM u_user as c WHERE account='{member_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            member_id = sum00[0][0]

        # SQL参数列表
        bet_type_list=['=','!=']
        proxy_id_list = ['c.proxy0_id', 'c.proxy1_id', 'c.proxy2_id', 'c.proxy3_id','c.user_id','c.sport_id','d.market_id','d.tournament_id','d.match_id']
        total_list=['SUM(c.company_win_or_lose)','SUM(c.level0_win_or_lose+c.company_win_or_lose)','SUM(c.level0_win_or_lose+c.company_win_or_lose+c.level1_win_or_lose)','SUM(c.level0_win_or_lose+c.company_win_or_lose+c.level1_win_or_lose+c.level2_win_or_lose)','SUM(c.company_win_or_lose)']

        #查询登录代理的代理等级
        sql = f"SELECT role_id FROM m_account WHERE login_account='{login_account}'"
        sum = self.my.query_data(sql, db_name='bfty_credit')
        num = int(sum[0][0])

        total_tuple = (agent_id, member_id, sportId, marketId, tournamentId, matchId)
        xxx_list = ['agent_id', 'member_id', 'sportId', 'marketId', 'tournamentId', 'matchId']
        total_list01 = []
        for jj in total_tuple:
            if jj == '' or jj == "":
                pass
            else:
                total_list01.append(xxx_list[total_tuple.index(jj)])

        # 判断以什么时间计算的报表
        if excel_num == 1:
            time = 'c.create_time'
            time_value='投注时间'
        elif excel_num == 2:
            time = 'd.match_time'
            time_value = '赛事时间'
        else:
            time = 'c.award_time'
            time_value = '结算时间'

        # 判断到相应的ID时，进行数据处理
        sum02 = ""
        if len(total_list01) == 1:
            if total_list01[0] == 'agent_id':
                # 查询传参agent_id的代理等级
                sql01 = f"SELECT role_id FROM m_account WHERE id='{agent_id}'"
                sum01 = self.my.query_data(sql01, db_name='bfty_credit')
                num01 = int(sum01[0][0])

                # 根据登录代理的代理等级，返回查询公司输赢
                sql02 = f"SELECT {total_list[num]} as '公司共计' FROM o_account_order as c WHERE {proxy_id_list[num01]}='{agent_id}' and c.STATUS=2 AND c.award_time IS NOT NULL AND c.award_time>='{begin}' AND c.award_time<='{end}'"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                sum02 = float(sum02[0][0])
                print(f"\033[32m{time_value}-登录账号:(登{num})-查询登{num01}-{agent_id}的总公司输赢为{sum02}\033[0m")
            elif total_list01[0] == 'member_id':
                # 根据会员ID，进行参数替换：
                # 根据会员member_id，返回查询公司输赢：
                num01 = 4
                if Duplex=='':
                    sql02 = f"SELECT {total_list[num]} as '公司共计',any_value(c.login_account) as '登入账号' FROM o_account_order as c WHERE {proxy_id_list[num01]}='{member_id}' AND c.award_time>='{begin}' AND c.award_time<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL"
                else:
                    bet_type=bet_type_list[1]
                    sql02 = f"SELECT {total_list[num]} as '公司共计',any_value(c.login_account) as '登入账号' FROM o_account_order as c LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE {proxy_id_list[num01]}='{member_id}' AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL AND c.bet_type{bet_type}1"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                username = (sum02[0][1])
                sum02 = float(sum02[0][0])
                print(f"\033[32m{time_value}-登{num}查询会员{username}-{member_id}的总公司输赢为{sum02}\033[0m")
            elif total_list01[0] == 'sportId':
                # 根据球类ID，进行参数替换：
                num01 = 5
                sql02 = f"SELECT {total_list[num]} as '公司共计',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE {proxy_id_list[num01]}='{sportId}' AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                username = (sum02[0][1])
                sum02 = float(sum02[0][0])
                print(f"\033[32m{time_value}-登{num}查询{username}的-{sportId}的总公司输赢为{sum02}\033[0m")
            elif total_list01[0] == 'tournamentId':
                # 根据球类ID和联赛ID，进行参数替换：
                num01 = 7
                if tournamentId=='串关':
                    bet_type=bet_type_list[1]
                    sql02 = f"SELECT {total_list[num]} as '公司共计','串关',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL AND c.bet_type{bet_type}1"
                else:
                    bet_type=bet_type_list[0]
                    sql02 = f"SELECT {total_list[num]} as '公司共计',any_value(tournament_name),CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN o_account_order_match as d ON d.order_no=c.order_no WHERE {proxy_id_list[num01]}='{tournamentId}' AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL AND c.bet_type{bet_type}1"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                username =sum02[0][2]
                tournamentId = sum02[0][1]
                sum02 =float(sum02[0][0])
                print(f"\033[32m{time_value}-登{num}查询{username}-{tournamentId}的总公司输赢为{sum02}\033[0m")
            elif total_list01[0] == 'matchId':
                # 根据球类ID和赛事ID，进行参数替换：
                num01 = 8
                if matchId == '串关':
                    bet_type=bet_type_list[1]
                    sql02 = f"SELECT {total_list[num]} as '公司共计','串关',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE  {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL AND c.bet_type{bet_type}1"
                else:
                    bet_type = bet_type_list[0]
                    sql02 = f"SELECT {total_list[num]} as '公司共计',any_value({proxy_id_list[num01]}),CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN o_account_order_match as d ON d.order_no=c.order_no WHERE {proxy_id_list[num01]}='{matchId}' AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL AND c.bet_type{bet_type}1"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                matchId = (sum02[0][1])
                username = (sum02[0][2])
                sum02 = float(sum02[0][0])
                print(f"\033[32m{time_value}-登{num}查询{username}-{matchId}的总公司输赢为{sum02}\033[0m")
        elif len(total_list01)==2 or len(total_list01)==3:
            if total_list01[1] == 'marketId':
                # 根据球类ID和盘口ID，进行参数替换：
                num01 = 6
                if marketId=='串关':
                    bet_type=bet_type_list[1]
                    bet_type=f"AND c.bet_type{bet_type}1"
                    sql02 = f"SELECT {total_list[num]} as '公司共计','串关',CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN v_order_match as d ON c.order_no=d.order_no WHERE {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL AND c.sport_id='{sportId}' {bet_type} GROUP BY c.sport_id"
                else:
                    bet_type = bet_type_list[0]
                    if matchId == '':
                        bet_type=f"AND c.bet_type{bet_type}1"
                    else:
                        bet_type = f"AND c.bet_type{bet_type}1 AND d.match_id='{matchId}'"
                    sql02 = f"SELECT {total_list[num]} as '公司共计',any_value(market_name),CASE any_value(c.sport_id) WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类' FROM o_account_order as c  LEFT JOIN o_account_order_match as d ON d.order_no=c.order_no  WHERE {proxy_id_list[num01]}='{marketId}'  AND {proxy_id_list[num]}=(SELECT id FROM m_account WHERE login_account='{login_account}') AND {time}>='{begin}' AND {time}<='{end}' and c.STATUS=2 AND c.award_time IS NOT NULL {bet_type} AND c.sport_id='{sportId}'"
                sum02 = self.my.query_data(sql02, db_name='bfty_credit')
                username = (sum02[0][2])
                marketId = (sum02[0][1])
                sum02=float(sum02[0][0])
                print(f"\033[32m{time_value}-登{num}查询{username}-{marketId}的总公司输赢为{sum02}\033[0m")
        print(sql02)
        return sum02

    #查询首页详细资料
    def Home_Balance_Details(self,agent_id):
        """
        @查询登0~登3的首页详细资料
        @根据登入账号的传参去做查询
        """
        # 判断agent_id为代理ID，还是为代理账号
        z_m_num01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        vv_id = []
        qq_id = []
        for j in list(agent_id):
            if j in z_m_num01:
                pass
            else:
                vv_id.append(0)
                # print("这是一个代理账号")
        # agent_id传递：
        if vv_id == []:
            sql00 = f"SELECT role_id FROM m_account as c WHERE id='{agent_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            agent_id=agent_id
            role_id=int(sum00[0][0])
        else:
            sql00 = f"SELECT id  FROM m_account as c WHERE login_account='{agent_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            agent_id = sum00[0][0]

            sql01 = f"SELECT role_id FROM m_account as c WHERE id='{agent_id}'"
            sum01 = self.my.query_data(sql01, db_name='bfty_credit')
            role_id=int(sum01[0][0])

        Yesterday_cash_balance=['c.company_win_or_lose+c.level0_win_or_lose','c.company_win_or_lose+c.level0_win_or_lose+c.level1_win_or_lose',
                                'c.company_win_or_lose+c.level0_win_or_lose+c.level1_win_or_lose+c.level2_win_or_lose','c.company_win_or_lose+c.level0_win_or_lose+c.level1_win_or_lose+c.level2_win_or_lose+c.level3_win_or_lose']
        Yesterday_balance=['c.company_win_or_lose','c.company_win_or_lose+c.level0_win_or_lose','c.company_win_or_lose+c.level0_win_or_lose+c.level1_win_or_lose','c.company_win_or_lose+c.level0_win_or_lose+c.level1_win_or_lose+c.level2_win_or_lose']
        Outstanding_transaction_amount=['c.level0_actual_percentage','c.level1_actual_percentage','c.level2_actual_percentage','c.level3_actual_percentage']

        #根据role_id判断代理等级,计算返回登0~登3的首页详细资料:
        sql00 = f"SELECT SUM(IF(any_value(c.STATUS) IN(1,2) AND c.award_time is null,c.bet_amount,0))'未完成交易总数',SUM(IF(any_value(c.STATUS=2) AND any_value(b.payment_status_for_sub)=0 AND c.award_time is NOT null AND DATE_FORMAT(c.award_time,'%Y-%m-%d')<DATE_FORMAT(CONVERT_TZ(now(),'+00:00','-04:00'),'%Y-%m-%d'),({Yesterday_cash_balance[role_id]}),0))'昨日现金余额',-SUM(IF(any_value(c.STATUS=2) AND any_value(b.payment_status)=0 AND c.award_time is NOT null AND DATE_FORMAT(c.award_time,'%Y-%m-%d')<DATE_FORMAT(CONVERT_TZ(now(),'+00:00','-04:00'),'%Y-%m-%d'),({Yesterday_balance[role_id]}),0))'昨日余额',SUM(IF(any_value(c.STATUS=2) AND c.award_time is NOT null AND DATE(c.award_time)=DATE_FORMAT(DATE_SUB(CONVERT_TZ(now(),'+00:00','-04:00'),INTERVAL 1 DAY),'%Y-%m-%d'),c.level0_win_or_lose,0))'昨日输赢',SUM((IF(any_value(c.STATUS) IN(1,2) AND c.award_time is null,c.bet_amount*{Outstanding_transaction_amount[role_id]},0)))'未完成交易金额',SUM(IF(any_value(c.STATUS=2) AND any_value(b.payment_status_for_sub)=0 AND c.award_time is NOT null,({Yesterday_cash_balance[role_id]}),0))'现金余额',-SUM(IF(any_value(c.STATUS=2) AND any_value(b.payment_status)=0 AND c.award_time is NOT null,({Yesterday_balance[role_id]}),0))as'余额',SUM(IF(any_value(c.STATUS=2) AND c.award_time is NOT null AND DATE(c.award_time)=DATE_FORMAT(CONVERT_TZ(now(),'+00:00','-04:00'),'%Y-%m-%d'),c.level0_win_or_lose,0))'今日输赢' FROM o_account_order as c LEFT JOIN m_account as a  ON c.proxy{role_id}_id=a.id LEFT JOIN m_account_unsettlement_amount_record as b ON  (b.account_id=a.id AND b.order_no=c.order_no) LEFT JOIN m_account_credits as d ON d.account_id=a.id WHERE a.id='{agent_id}' GROUP BY a.id"
        # print(sql00)
        sum00 = self.my.query_data(sql00, db_name='bfty_credit')
        sum00=sum00[0]
        yy_list_01=[]
        yy_list=[]
        for yy in sum00:
            yy=float(yy)
            yy_list_01.append(yy)
        yy_list.append(yy_list_01)
        print(sql00)
        print(f"\033[34m登{role_id}-{agent_id}的首页详细资料是：{yy_list}\033[0m")
        return yy_list

    # 查询首页统计
    def Home_Statistics(self,agent_id):
        """
                @查询登0~登3的首页详细资料
                @根据登入账号的传参去做查询
                """
        # 判断agent_id为代理ID，还是为代理账号
        z_m_num01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        vv_id = []
        qq_id = []
        for j in list(agent_id):
            if j in z_m_num01:
                pass
            else:
                vv_id.append(0)
                # print("这是一个代理账号")
        # agent_id传递：
        if vv_id == []:
            sql00 = f"SELECT role_id FROM m_account as c WHERE id='{agent_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            agent_id = agent_id
            role_id = int(sum00[0][0])
        else:
            sql00 = f"SELECT id  FROM m_account as c WHERE login_account='{agent_id}'"
            sum00 = self.my.query_data(sql00, db_name='bfty_credit')
            agent_id = sum00[0][0]

            sql01 = f"SELECT role_id FROM m_account as c WHERE id='{agent_id}'"
            sum01 = self.my.query_data(sql01, db_name='bfty_credit')
            role_id = int(sum01[0][0])

        role_list=[0,1,2,3]
        total_num=[]
        assemble_sum=''
        parent_id=''
        sum00=()
        #根据role_id去判断代理等级，计算额度和户数
        # 统计当前登录代理的额度
        sql00 = f"SELECT d.credits FROM m_account as a LEFT JOIN m_account_credits as d ON d.account_id=a.id WHERE d.account_id='{agent_id}'"
        sum00 = self.my.query_data(sql00, db_name='bfty_credit')
        sum00 = sum00[0]
        print(sql00)
        if role_id==0:
            assemble_sum=f"SUM(IF(any_value(d.account_id) in (SELECT id FROM m_account WHERE top_parent_id='{agent_id}' AND role_id=1),any_value(d.credits),0))'登1代理',SUM(IF(any_value(d.account_id) in (SELECT id FROM m_account WHERE top_parent_id='{agent_id}' AND role_id=3),any_value(d.credits),0))'登3代理',SUM(IF(any_value(d.account_id) in (SELECT id FROM m_account WHERE top_parent_id='{agent_id}' AND role_id=2),any_value(d.credits),0))'登2代理',"
            parent_id="top_parent_id"
        elif role_id==1:
            assemble_sum=f"SUM(IF(any_value(d.account_id) in (SELECT id FROM m_account WHERE parent_id in (SELECT id FROM m_account WHERE parent_id='{agent_id}') AND role_id=3),any_value(d.credits),0))'登3代理',SUM(IF(any_value(d.account_id) in (SELECT id FROM m_account WHERE parent_id='{agent_id}' AND role_id=2),any_value(d.credits),0))'登2代理',"
            parent_id = "parent_id"
        elif role_id==2:
            assemble_sum=f"SUM(IF(any_value(d.account_id) in (SELECT id FROM m_account WHERE parent_id='{agent_id}' AND role_id=3),any_value(d.credits),0))'登3代理',"
            parent_id = "parent_id"
        else:
            assemble_sum=assemble_sum
            parent_id = "parent_id"
        sql01 = f"SELECT {assemble_sum}SUM(IF(c.user_id IN(SELECT id FROM u_user WHERE proxy{role_id}_id='{agent_id}') ,c.credits_amount,0))'会员'FROM m_account as a LEFT JOIN m_account_credits as d ON d.account_id=a.id LEFT JOIN u_user as b ON b.proxy{role_id}_id=a.id LEFT JOIN u_user_balance as c ON (c.user_id=b.id)"
        print(sql01)
        sum01 = self.my.query_data(sql01, db_name='bfty_credit')
        sum01 = sum01[0]
        if role_id==2:
            credits_total = []
            credits_total.append(sum01[0])
            credits_total.append(sum00[0])
            credits_total.append(sum01[1])
        elif role_id==3 or role_id==1:
            credits_total=sum00+sum01
        else:
            credits_total = sum01+sum00
        #统计登1~登3的户数
        #登1~登3循环
        for i in range(role_list[role_id]+1,len(role_list)):
            sql02 = f"SELECT IF (account_status=2,COUNT(2),0) '停用',IF (account_status=0,COUNT(0),0) '启用',IF (account_status=3,COUNT(3),0) '禁止登入',IF (account_status=1,COUNT(1),0) '只能看账' FROM m_account WHERE id IN (SELECT id FROM m_account WHERE {parent_id}='{agent_id}' AND role_id={i}) GROUP BY account_status"
            sum02 = self.my.query_data(sql02, db_name='bfty_credit')
            # sum02 = sum00[0]
            print(sql02)
            agent_proxy_list=[]
            for j in range(0,4):
                num_list=[]
                for kk in sum02:
                    num_list.append(kk[j])
                agent_proxy_list.append(sum(num_list))
            total_num.append(agent_proxy_list)
        #统计会员的户数
        sql02 = f"SELECT IF (current_status=3,COUNT(3),0) '停用',IF (current_status=0,COUNT(0),0) '启用',IF (current_status=2,COUNT(2),0) '禁止登入',IF (current_status=1,COUNT(1),0) '只能看账' FROM u_user WHERE proxy{role_id}_id='{agent_id}' GROUP BY current_status"
        sum02 = self.my.query_data(sql02, db_name='bfty_credit')
        print(sql02)
        member_proxy_list=[]
        for j in range(0,4):
            num_list=[]
            for kk in sum02:
                num_list.append(kk[j])
            member_proxy_list.append(sum(num_list))
        total_num.append(member_proxy_list)
        print(f"登{role_id}户数{total_num}")
        print(f"登{role_id}额度{credits_total}")












if __name__ == "__main__":
    #120环境
    # mongo_inf = ['app', '123456', '192.168.10.120', '27017']
    # mysql_inf = ['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']
    #MDE环境
    mongo_inf = ['sport_test', 'BB#gCmqf3gTO5777', '35.194.233.30', '27017']
    mysql_inf = ['35.194.233.30', 'root', 'BB#gCmqf3gTO5b*', '3306']

    AB_list = ["A", "B", "C", "D", "E", "F", ]
    dict = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}
    account_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    NEW_account=[]
    z_m_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    # mf = MongoFunc(mongo_inf)
    # bc = BetController(mysql_inf, mongo_inf,AB_list,dict)

    yy_list = ["efficient_amount","company_retreat_proportion", "level0_retreat_proportion", "level1_retreat_proportion", "level2_retreat_proportion", "level3_retreat_proportion",
               "company_actual_percentage", "level0_actual_percentage", "level1_actual_percentage", "level2_actual_percentage", "level3_actual_percentage", ]
    yy_dict = {'efficient_amount': [], 'company_retreat_proportion': [], 'level0_retreat_proportion': [], 'level1_retreat_proportion': [], 'level2_retreat_proportion': [], 'level3_retreat_proportion': [],
               'company_actual_percentage': [], 'level0_actual_percentage': [], 'level1_actual_percentage': [], 'level2_actual_percentage': [], 'level3_actual_percentage': []}

    bc=SQL_report_ods(mysql_inf, mongo_inf, AB_list,dict)
    tt = water_ammount(mysql_inf, mongo_inf)
    # 代理相关:
    # account=''
    # for i in z_m_list:
    #     for j in account_list:
    #         account=i+str(j)
    #     ppds = tt.DL_D0(account=account,login_account='')
    # print(NEW_account)
    # loginAccount_list = ['test00', 'test01', 'test02', 'test03']
    # for login_account in loginAccount_list:
    #     ppds = tt.DL_D0(account='', login_account=login_account)







    # yyds=bc.Type_odd()
    # yydt=bc.order_no(bet_type=0, status=1, AB_list=AB_list,dict=dict,proxy3_id=1531517760300163074)

    # yybt=bc.credit_odds(order_no="XFBa6SNxq5xS",bet_type="",AB_list=AB_list,dict=dict)
    # print(yybt)

    # yyds=bc.water()
    #佣金计算：
    # order_no_list=['XFMvkaAa2EyQ', 'XH4ss4C8CJrA', 'XH4svST7h8L2', 'XH4tqsrmgi4u', 'XH4tRJjpTbw4', 'XH4tSR96m5dQ', 'XH4tVrSP4AfW', 'XH4u4xZyAimC', 'XH4uaSmddnM3', 'XH4uhKSs4EG5', 'XH4unwkeUDy4', 'XH4uDywxHmRv', 'XH4uZjmuZh7p', 'XH4v2VDFg9eb', 'XH4v8HX6evZx', 'XH4vdh7MXkgA', 'XH4veP3HQaBY', 'XH4vjsHg5K4S', 'XH4vmG2AR4vB', 'XH4vq98PBVgg', 'XH4vygGCgd6b', 'XH4vCZGr2NT9', 'XH4vGtjuxzu8', 'XH4vPj6YQNFy', 'XH4vS8mLWXVS', 'XH4vZWTcx3gC', 'XH4w4aWhGz36', 'XH4wf2et6e54', 'XH4wssFn5Zxa', 'XH4wGvtBj9en']
    # for order_no in order_no_list:
    #     tt.water(order_no=order_no, num_0=1)
    #总赔率计算
    # order_no_list=['XH4ud8cbEa8M','XH4tL4REXVDW','XH4ud8cbEa8M','XHwDVJrkf2Ae']
    # for order_no in order_no_list:
    #     bc.total_odds(order_no=order_no, number='252')








    #总佣金和公司输赢计算、首页详细资料调试：
    login_account =['sh','d10','d2','d3']
    begin="2022-07-10 00:00:00"
    end="2022-07-16 23:59:59"
    agent_id_list=['1531516017847869442','1531517033355976705','1531517351158390786','1531517760300163074']
    member_id_list=['fceshi04','fceshi056','fceshi0126','fceshi0190','fceshi0223','fceshi0280','fceshi0315','fceshi0362','fceshi0418','fceshi0444','fceshi0480','fceshi0551','fceshi0572','fceshi0623','fceshi0661','fceshi0735']
    yyds=tt.total_commission(agent_id='',member_id='',sportId='sr:sport:1',marketId='37',tournamentId='',matchId='sr:match:34506443',login_account=login_account[0],begin=begin,end=end,Duplex='',ZD='',excel_num=1)

    # for i in agent_id_list:
    # yyts=tt.Home_Balance_Details(agent_id=login_account[0])
    #     yyds=tt.total_commission(agent_id=i,member_id='',sportId='',marketId='',tournamentId='',matchId='',login_account=login_account[0],begin=begin,end=end,Duplex='',ZD='',excel_num=3)
    # yyrs=tt.Home_Statistics(agent_id=agent_id_list[3])

    # for member_id in member_id_list:
    #     yy_num = tt.total_commission(agent_id='', member_id=member_id, sportId='', marketId='',tournamentId='', matchId='', login_account=login_account, begin=begin, end=end, Duplex='')

    # for agent_id in range(len(agent_id_list)+len(member_id_list)):
    #     if agent_id<=len(agent_id_list)-1:
    #         yyds=tt.total_commission(agent_id=agent_id_list[agent_id],member_id='',sportId='',marketId='',tournamentId='',matchId='',login_account=login_account)
    #         yyqt=tt.Company_winlose(agent_id=agent_id_list[agent_id],member_id='',login_account=login_account)
    #     else:
    #         yyds=tt.total_commission(agent_id='', member_id=member_id_list[agent_id-(len(agent_id_list))])
    #         yyqt=tt.Company_winlose(agent_id='', member_id=member_id_list[agent_id-(len(agent_id_list))],login_account=login_account)
    # yyds = tt.total_commission(agent_id='', member_id='', sportId='sr:sport:1', marketId='1', tournamentId='',matchId='sr:match:32013725', login_account=login_account,begin="2022-06-17 00:00:00",end="2022-06-23 23:59:59")


    # begin="2022-06-17 00:00:00"
    # end="2022-06-23 23:59:59"
    # marketId='串关'
    # for agent_id in agent_id_list:
    #     yybt = tt.total_commission(agent_id='', member_id='', sportId='', marketId='',tournamentId='', matchId='sr:match:33725427', login_account=login_account,begin=begin,end=end,Duplex='')
    #     yyds=tt.Company_winlose(agent_id=agent_id, member_id='', sportId='', marketId='', tournamentId='',matchId='', login_account=login_account,begin=begin,end=end,Duplex='')




