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


    def single_bet(self, credit_odds_list,order_no):
        odds = credit_odds_list
        win_amount = (int(odds[0]) * (bet_amount)) - bet_amount
        backwater_amount = level3_retreat_proportion * bet_amount
        rebate_amount = win_amount + backwater_amount + bet_amount

        a=credit_odds_list[0]
        single_bet_odds=str(re.findall(r"\d{1,}?\.\d{2}",str(a))[0])
        print(f"\033[33m注单：{order_no}，单注的总赔率：{single_bet_odds}\033[0m")
        return rebate_amount

    def stray_bet(self, credit_odds_list,order_no):

        # 计算赔率
        odds = 1
        for j in credit_odds_list:
            odds = odds*j
        odds=float(str(re.findall(r"\d{1,}?\.\d{2}",str(odds))[0]))
        print(f"\033[35m注单：{order_no}，串关{len(credit_odds_list)}串1的总赔率为：{odds}\033[0m")

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
        odds_2_3 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_2_3))[0]))
        print(f"\033[32m注单：{order_no}复式串关2串1*3的总赔率为：{odds_2_3}\033[0m")

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
        odds_3_4 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_3_4))[0]))
        print(f"\033[32m注单：{order_no}复式串关3串1*4的总赔率为：{odds_3_4}\033[0m")

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
        odds_2_6 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_2_6))[0]))
        print(f"\033[32m注单：{order_no}复式串关2串1*6的总赔率为：{odds_2_6}\033[0m")

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
        odds_4_5 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_4_5))[0]))
        print(f"\033[32m注单：{order_no}复式串关4串1*5的总赔率为：{odds_4_5}\033[0m")

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
        odds_3_10 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_3_10))[0]))
        print(f"\033[32m注单：{order_no}复式串关3串1*10的总赔率为：{odds_3_10}\033[0m")

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
        odds_2_10 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_2_10))[0]))
        print(f"\033[32m注单：{order_no}复式串关2串1*10的总赔率为：{odds_2_10}\033[0m")

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
        odds_5_6 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_5_6))[0]))
        print(f"\033[32m注单：{order_no}复式串关5串1*6的总赔率为：{odds_5_6}\033[0m")

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
        odds_4_15 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_4_15))[0]))
        print(f"\033[32m注单：{order_no}复式串关4串1*15的总赔率为：{odds_4_15}\033[0m")

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
        odds_3_20 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_3_20))[0]))
        print(f"\033[32m注单：{order_no}复式串关3串1*20的总赔率为：{odds_3_20}\033[0m")

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

        CD = dict['D'] * dict['C']
        AB = dict['A'] * dict['B']
        BC = dict['B'] * dict['C']
        AC = dict['A'] * dict['C']
        odds_2_15 = AB + BC + AC + CD + BD + AD + AE + BE + CE + DE
        odds_2_15 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_2_15))[0]))
        print(f"\033[32m注单：{order_no}复式串关2串1*15的总赔率为：{odds_2_15}\033[0m")

        return odds_2_15

    def Duplex_bet(self, credit_odds_list,AB_list,dict,order_no):
        yyds = {'复式串关': [3, {"3串4": [3_1_0, 2_3_0,3_4_1]}, {"4串11": [4_1_0, 3_4_0, 2_6_0,4_11_1]},{"5串26": [5_1_0, 4_5_0, 3_10_0, 2_10_0,5_26_1]}, {"6串57": [6_1_0, 5_6_0, 4_15_0, 3_20_0, 2_15_0,6_57_1]}]}

        # print(mix_num)
        # 3串4赔率结算：
        if mix_num=='2_3_0':
            odds_2_3=self.Duplex_2_3(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num==str('3_4_1'):
            sum01 = self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no)
            sum02=self.Duplex_2_3(credit_odds_list=credit_odds_list,  AB_list=AB_list, dict=dict,order_no=order_no)
            odds_3_4=sum01+sum02
            print(f"\033[34m注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]}的总赔率为：{odds_3_4}\n\033[0m")

        # 4串11赔率结算：
        if mix_num == str('3_4_0'):
            odds_3_4=self.Duplex_3_4(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num == str('2_6_0'):
            odds_2_6=self.Duplex_2_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num == str('4_11_1'):
            sum01 = self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no)
            sum02 = self.Duplex_3_4(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum03 = self.Duplex_2_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            odds_4_11 = sum01 + sum02+sum03
            odds_4_11 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_4_11))[0]))
            print(f"\033[34m注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]+list(mix_num)[3]}的总赔率为：{odds_4_11}\n\033[0m")

        # 5串26赔率结算：
        if mix_num == str('4_5_0'):
            odds_4_5 = self.Duplex_4_5(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num == str('3_10_0'):
            odds_3_10 = self.Duplex_3_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num == str('2_10_0'):
            odds_2_10 = self.Duplex_2_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num == str('5_26_1'):
            sum01 = self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no)
            sum02 = self.Duplex_4_5(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum03 = self.Duplex_3_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum04= self.Duplex_2_10(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            odds_5_26 = sum01 + sum02+sum03+sum04
            odds_5_26 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_5_26))[0]))
            print(f"\033[34m注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]+list(mix_num)[3]}的总赔率为：{odds_5_26}\n\033[0m")

        # 6串57赔率结算：
        if mix_num == str('5_6_0'):
            odds_5_6 = self.Duplex_5_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num == str('4_15_0'):
            odds_4_15 = self.Duplex_4_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
        if mix_num == str('3_20_0'):
            odds_3_20 = self.Duplex_3_20(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
        if mix_num == str('2_15_0'):
            odds_2_15 = self.Duplex_2_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict, order_no=order_no)
        if mix_num == str('6_57_1'):
            sum01 = self.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no)
            sum02 = self.Duplex_5_6(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum03 = self.Duplex_4_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum04 = self.Duplex_3_20(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            sum05 = self.Duplex_2_15(credit_odds_list=credit_odds_list, AB_list=AB_list, dict=dict,order_no=order_no)
            odds_6_57 = sum01 + sum02+sum03+sum04+sum05
            odds_6_57 = float(str(re.findall(r"\d{1,}?\.\d{2}", str(odds_6_57))[0]))
            print(f"\033[34m注单：{order_no}复式串关{list(mix_num)[0]}串{list(mix_num)[2]+list(mix_num)[3]}的总赔率为：{odds_6_57}\n\033[0m")





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


    def bet_type(self,order_no,AB_list,dict,proxy3_id,status):
        global bet_amount,level3_retreat_proportion,mix_num
        """
        @判断注单的类型：bet_type:1(单注)，bet_type:2(串关)，bet_type:3(复式串关)
        @根据类型调用相应的函数进行结算
        """
        sql =f"SELECT bet_type,mix_num,bet_amount,level3_retreat_proportion FROM o_account_order WHERE STATUS='{status}' AND order_no='{order_no}'AND proxy3_id='{proxy3_id}'"
        sum = self.my.query_data(sql, db_name='bfty_credit')
        # print(sum)

        bet_type=sum[0][0]
        mix_num=sum[0][1]
        bet_amount = sum[0][2]
        level3_retreat_proportion=sum[0][3]

        self.credit_odds(order_no=order_no,bet_type=bet_type,AB_list=AB_list,dict=dict)

        return bet_type

    def credit_odds(self,order_no,bet_type,AB_list,dict):
        """
        @根据注单类型查询其赔率
        @根据赔率进行计算
        """
        sql = f"SELECT credit_odds FROM o_account_order_match  WHERE order_no='{order_no}'"
        sum = self.my.query_data(sql, db_name='bfty_credit')

        credit_odds_list=[]
        for i in range(0,len(sum)):
            credit_odds_list.append(sum[i][0])
        # print(credit_odds_list)

        self.Calculate_odds(credit_odds_list=credit_odds_list,bet_type=bet_type,AB_list=AB_list,dict=dict,order_no=order_no)

        return credit_odds_list

    def Calculate_odds(self, credit_odds_list,bet_type,AB_list,dict,order_no):
        """
        @根据注单类型判断其类型，1为单注，2为串关，3为复式串关
        @根据其类型赔率进行计算
        """
        bet_type_dict={'单注':[1,1_1_0],'串关':[2,2_1_0],
                       '复式串关':[3,{"3串4":[3_1_0,2_3_0]},{"4串11":[4_1_0,3_4_0,2_6_0]},{"5串26":[5_1_0,4_5_0,3_10_0,2_10_0]},{"6串57":[6_1_0,5_6_0,4_15_0,3_20_0,2_15_0]}]}
        if bet_type==1:
            self.ce.single_bet(credit_odds_list=credit_odds_list,order_no=order_no)
        if bet_type==2:
            self.ce.stray_bet(credit_odds_list=credit_odds_list,order_no=order_no)
        else:
            self.ce.Duplex_bet(credit_odds_list=credit_odds_list,AB_list=AB_list, dict=dict,order_no=order_no)



if __name__ == "__main__":
    #120环境
    # mongo_inf = ['app', '123456', '192.168.10.120', '27017']
    # mysql_inf = ['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']
    #MDE环境
    mongo_inf = ['sport_test', 'BB#gCmqf3gTO5777', '35.194.233.30', '27017']
    mysql_inf = ['35.194.233.30', 'root', 'BB#gCmqf3gTO5b*', '3306']

    AB_list = ["A", "B", "C", "D", "E", "F", ]
    dict = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}
    # mf = MongoFunc(mongo_inf)
    bc = BetController(mysql_inf, mongo_inf,AB_list,dict)

    # yyds=bc.Type_odd()
    # yyds=bc.bet_type(order_no="XEP93LkShTT3",AB_list=AB_list,dict=dict)
    yydt=bc.order_no(bet_type=0, status=2, AB_list=AB_list,dict=dict,proxy3_id=1531517760300163074)