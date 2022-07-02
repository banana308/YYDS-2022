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

import time
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import requests
import json
import base64
import random
import datetime
from concurrent.futures import ThreadPoolExecutor
import openpyxl

from Computational_N_N import SQL_report_ods,betting_odds,water_ammount
from Get_excel_path import owner_backer_path





class report_data(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, *args):
        """
        模拟ctrl给我司推送数据
        """
        self.session = requests.session()
        self.tt=BetController(mysql_info, mongo_info)

    # rsa加密账号、密码
    def rsa_encrypt(self,data):
        '''
        rsa加密（encrypt）
        :param data:
        :return:
        '''
        msg = data.encode('utf-8')
        pub_key = "-----BEGIN PUBLIC KEY-----\nMFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAL1XuLmIZttk13hmAGVuXiKSfQggfVck" \
                  "p+iNr9jBIxkmBBfmygJ9D5A7lhUbhBEY1SqyGNIHI1DsNLfxfRvW2EcCAwEAAQ==\n-----END PUBLIC KEY-----"
        rsa_key = RSA.importKey(pub_key)
        cipher = Cipher_pkcs1_v1_5.new(rsa_key)
        cipher_text = base64.b64encode(cipher.encrypt(msg)).decode('utf-8')
        # print(cipher_text)
        return cipher_text


    def reading_Excel(self,excel,save_excel,begin,end,URL):
        """
        @获循环所有表，取Excel的数据，并把数据写入list中
        """
        # 获取 工作簿对象
        workbook = openpyxl.load_workbook(excel[0])
        print("读取表格成功")
        # shenames = workbook.get_sheet_names()
        shenames = workbook.sheetnames
        print("整个表格所有表名:", shenames)  # ['各省市', '测试表']

        #统计用例通过的数量
        execute=0
        #统计用例不通过的数量
        Failed=0
        # 获取用例执行前的时间
        time01 = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')

        #循环Excel所有表
        for gg in range(0,1):
            gg = shenames[gg]
        # for gg in shenames:
            # 获取该表相应的行数和列数
            worksheet= workbook[shenames[shenames.index(gg)]]
            rows=0
            for yy in range(1,1000):
                if worksheet.cell(yy, 1).value!=None:
                    rows=rows+1
                else:
                    break
            # rows = worksheet.max_row
            columns = worksheet.max_column
            print(f"所在\033[32m（{gg}）\033[0m组成有： {rows}行  {columns}列")

            #判断表中第二行数据，是否为空，为空跳过，循环其他表
            content_A2 = worksheet.cell(2, 1).value
            if content_A2!=None:
                # 循环行数
                # for i in range(5, 6):
                for i in range(2, rows+1):
                    excel_report = []
                    # 循环列数
                    for j in range(2, int(columns)-2):
                        report=worksheet.cell(i,j).value
                        #获取到的数据写入列表
                        excel_report.append(report)
                    #调用登录接口，获取token，访问接口，获取数据
                    # print(excel_report)
                    # exit()
                    self.login(URL=URL, begin=begin, end=end, excel_report=excel_report)

                    '''
                    #调试SQL数据
                    # print(excel_report)
                    # sport_report_list={'account': 'd0d1d2d38y/fceshi0224', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网', 'betResult': '输', 'betTime': '2022-06-24 08:57:04', 'betType': '单注', 'level0Commission': 0.0, 'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3CommissionRatio': 0.0, 'level3Percentage': 0.2, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'memberCommission': 0.0, 'memberCommissionRatio': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号iy', 'odds': 1.69, 'oddsType': '1', 'options': [{'awayTeamName': '芹苴', 'betScore': None, 'homeTeamName': 'QNK广南足球俱乐部', 'marketName': '独赢', 'matchTime': '2022-06-25 06:00:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1', 'orderNo': 'XH4ydmPbRncK', 'outcomeName': 'QNK广南足球俱乐部', 'specifier': '', 'tournamentName': '越南职业足球乙级联赛'}], 'orderNo': 'XH4ydmPbRncK', 'settlementTime': '2022-06-25 08:01:45', 'sportId': 'sr:sport:1', 'sportType': '足球', 'validAmount': 10.0, 'winOrLose': -10.0}
                    # sport_report_dict=['account', 'betAmount', 'betIp', 'betIpAddress', 'betResult', 'betTime', 'betType', 'level0Commission', 'level0CommissionRatio', 'level0Percentage', 'level0Total', 'level0WinOrLose', 'level1Commission', 'level1CommissionRatio', 'level1Percentage', 'level1Total', 'level1WinOrLose', 'level2Commission', 'level2CommissionRatio', 'level2Percentage', 'level2Total', 'level2WinOrLose', 'level3Commission', 'level3CommissionRatio', 'level3Percentage', 'level3Total', 'level3WinOrLose', 'memberCommission', 'memberCommissionRatio', 'memberTotal', 'memberWinOrLose', 'name', 'odds', 'oddsType', 'options', 'orderNo', 'settlementTime', 'sportId', 'sportType', 'validAmount', 'winOrLose']
                    # self.tt.sport_report_sql(begin=begin, end=end, excel_report=excel_report, sport_report_dict=sport_report_list, sport_report_list=sport_report_dict)
                    '''

                    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    #判断用例是否通过
                    if sport_error==[]:
                        execute=execute+1
                        worksheet.cell(i,12,("测试通过"+"\n"+now))
                        worksheet.cell(i,13, "")
                        worksheet.cell(i,14, "")
                        worksheet.cell(i,15, "")
                        # worksheet.cell(i, int(columns)-1, str(Prepare_enough_list))
                    else:
                        Failed=Failed+1
                        worksheet.cell(i,12, ("测试不通过"+"\n"+now))
                        worksheet.cell(i,13, str(sport_error))
                        worksheet.cell(i,14, str(sport_all_error))
                        worksheet.cell(i,15, str(Prepare_enough_list))
                    workbook.save(filename=save_excel[0])
            else:
                continue
        time02=datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
        date_time=time02-time01
        print(f"\033[32m\n\n执行通过用例共计{execute}条,\033[0m未通过用例共计\033[31m{Failed}条\033[0m,共计消耗时间{date_time}")
        workbook.close()

    def login(self,URL, begin, end,excel_report):
        """
        @第一次获取token，并保持token连接中，便于后面其他接口访问
        """
        global token

        if toten=='':
            # 登0~登3登录获取token
            count = 0
            if count==0:
                url = str(URL) + "/system/accountLogin"
                headers = {
                    'Content-Type': 'application/json;charset=UTF-8'
                }
                data = {"userName": self.rsa_encrypt(data=Dl_list[pkk]),
                        "password": self.rsa_encrypt(data="Bfty123456"),
                        "securityCode": "Bf123456",
                        "loginDiv": 555666}
                session = requests.session()
                response = session.post(url=url, headers=headers, json=data)
                # 返回结果json转化
                results = json.loads(response.text)
                if results['code'] == 0:
                    pass
                    # print("登录成功"+"\n")
                else:
                    print(results)

                token = results['data']['token']
                id = results['data']['id']



                # 过渡调用函数：
                url01 = str(URL) + "/system/userDetailByToken?"
                headers01 = {
                    'Content-Type': 'application/json;charset=UTF-8',
                    'LoginDiv': '555666',
                    'Account_Login_Identify': token
                }
                data01 = {
                    "token": token,
                    "accountId": id
                }
                session = requests.session()
                response01 = session.get(url=url01, headers=headers01, params=data01)
                # 返回结果json转化
                results01=json.loads(response01.text)
                # print(results01)
                count=count+1
            else:
                pass
        else:
            token=toten

        if excel_report[3]==1:
            self.sport_report01(URL=URL, token=token, excel_report=excel_report, begin=begin, end=end)
        elif  excel_report[3]==2:
            self.sport_report02(URL=URL, token=token, excel_report=excel_report, begin=begin, end=end)
        else:
            self.sport_report03(URL=URL, token=token, excel_report=excel_report, begin=begin, end=end)



    def sport_report01(self,URL, token, excel_report, begin, end):
        global sportId_list

        sport_report_dict = []
        sport_report_list = []

        url = str(URL)+(excel_report[1])
        headers=eval(excel_report[4])
        if excel_report[0] in sport_report02_list:
            data = eval(excel_report[5])
        else:
            data = eval(excel_report[5])[0]
        session = requests.session()
        # print(headers)
        # print(data)

        method_list=["post"]
        if excel_report[7]==method_list[0]:
            response = session.post(url=url, headers=headers, json=data)
        else:
            response = session.get(url=url, headers=headers, params=data)
        results = json.loads(response.text)

        if excel_report[0] in module_list:
            yyds = results['data']
        else:
            yyds = results['data']['data']
        sportId_list = []

        if yyds==[]:
            pass
        else:
            str_sum=excel_report[2]

            for i in range(0,len(yyds)):
                if excel_report[2] != None:
                    ppxt_lsit = str_sum.split(",")
                    for j in ppxt_lsit:
                        # print(j)
                        del yyds[i][j]
                sport_report_list.append(yyds[i])

            for key,value in yyds[0].items():
                sport_report_dict.append(key)
            # print(sport_report_dict)

        time_list=[" 00:00:00"," 23:59:59"]
        print(sport_report_list[1])
        self.tt.sport_report_sql(begin=begin+time_list[0], end=end+time_list[1],excel_report=excel_report,sport_report_dict=sport_report_dict,sport_report_list=sport_report_list)
        return sport_report_dict


    def sport_report02(self,URL, token, excel_report, begin, end):
        global sportId_list,sportId_yyds_lsit

        sportId_list = []
        marketID_list=[]
        sport_report_list=[]
        sport_report_dict = []
        sportId_yyds_lsit = []
        yyds=''
        index=''
        for url in eval(excel_report[1]):
            headers = eval(excel_report[4])
            if eval(excel_report[1]).index(url) == 0:
                url = str(URL) + url
                data = eval(excel_report[5])[0]
                session = requests.session()
                method_list = ["post"]

                if excel_report[7] == method_list[0]:
                    response = session.post(url=url, headers=headers, json=data)
                else:
                    response = session.get(url=url, headers=headers, params=data)
                results = json.loads(response.text)

                if excel_report[0] in module_list:
                    yyds = results['data']
                else:
                    yyds = results['data']['data']

                if yyds == []:
                    pass
                else:
                    for i in yyds:
                        if i[excel_report[6]]=='串关':
                            pass
                        else:
                            sportId_list.append(i[excel_report[6]])
            else:
                if yyds == []:
                    break
                else:
                    if len(eval(excel_report[1]))>2:
                        index=2
                        if eval(excel_report[1]).index(url)==1:
                            url = str(URL) + url
                            market_id_list = []
                            if excel_report[0]=="报表-球类报表-订单查询（根据其盘口查询订单）":
                                for sportId in sportId_list:
                                    data = eval(excel_report[5])[1]
                                    data[excel_report[6]] = sportId
                                    session = requests.session()
                                    method_list = ["post"]

                                    if excel_report[7] == method_list[0]:
                                        response = session.post(url=url, headers=headers, json=data)
                                    else:
                                        response = session.get(url=url, headers=headers, params=data)
                                    results = json.loads(response.text)
                                    yyds = results['data']['data']

                                    if yyds == []:
                                        pass
                                    else:
                                        for i in yyds:
                                            if i['marketId'] == '串关':
                                                pass
                                            else:
                                                market_id_list.append(i['marketId'])
                                    marketID_list.append(market_id_list)
                        else:
                            url = str(URL) + url
                            for sportId in sportId_list:
                                for marketID in marketID_list[sportId_list.index(sportId)]:
                                    data = eval(excel_report[5])[2]
                                    data[excel_report[6]] = sportId
                                    data['marketId'] = marketID
                                    session = requests.session()
                                    method_list = ["post"]

                                    if excel_report[7] == method_list[0]:
                                        response = session.post(url=url, headers=headers, json=data)
                                    else:
                                        response = session.get(url=url, headers=headers, params=data)
                                    results = json.loads(response.text)
                                    yyds = results['data']['data']['data']
                                    sportId_yyds_lsit.append(yyds)
                    else:
                        url = str(URL) + url
                        for sportId in sportId_list:
                            data = eval(excel_report[5])[1]
                            if excel_report[0]in ("未完成交易-登0-登3-会员-查看订单详情-子查询","盈亏详情-登0-登3-会员-查看订单详情-子查询"):
                                data['parentId']=sportId
                            else:
                                data[excel_report[6]] = sportId
                            session = requests.session()
                            method_list = ["post"]

                            if excel_report[7] == method_list[0]:
                                response = session.post(url=url, headers=headers, json=data)
                            else:
                                response = session.get(url=url, headers=headers, params=data)
                            results = json.loads(response.text)

                            if excel_report[0] in module_list:
                                if excel_report[0] in ("未完成交易-登0-登3-会员-查看订单详情-子查询","盈亏详情-登0-登3-会员-查看订单详情-子查询"):
                                    if results['data']['data'] == []:
                                        pass
                                    else:
                                        # print(results)
                                        #data字典里的数据
                                        yyds = results['data']['data']
                                        if excel_report[0]=="未完成交易-登0-登3-会员-查看订单详情-子查询":
                                            Total_Amount = results['data']['totalData']['betAmount']
                                            for ppds in range(0,len(yyds)):
                                                data =yyds[ppds]['bettingTime']
                                                data = data.replace("T", " ")
                                                data = data.replace(".000Z", "")
                                                yyds[ppds]['bettingTime']=data
                                                yyds[ppds]['Total_Amount']=Total_Amount
                                        elif excel_report[0]=="盈亏详情-登0-登3-会员-查看订单详情-子查询":
                                            # 双字典totalData的数据
                                            totalData = ['level0Commission', 'level0Total', 'level0WinOrLose','level1Commission', 'level1Total', 'level1WinOrLose','level2Commission', 'level2Total', 'level2WinOrLose','level3Commission', 'level3Total', 'level3WinOrLose', 'memberCommission', 'memberTotal', 'memberWinOrLose', 'validAmount','winOrLose']
                                            totalData_dict = {}
                                            # print(results['data']['totalData'])
                                            #把第二字典需要对比的数据取出来，放进第一个data里面，方便对比
                                            for ppds in range(0, len(yyds)):
                                                for total in totalData:
                                                    ppt = " total_" + total
                                                    yyds[ppds][ppt]= results['data']['totalData'][total]
                                            # print(yyds[0])
                                else:
                                    yyds = results['data']
                            else:
                                yyds = results['data']['data']
                            sportId_yyds_lsit.append(yyds)
                            # print(sportId_yyds_lsit)
                        # print(sportId_yyds_lsit)

        report02_list = []
        print(sportId_yyds_lsit[0:2])
        for gg in range(0, len(sportId_yyds_lsit)):
            for yy in range(0, len(sportId_yyds_lsit[gg])):
                report02_list.append(sportId_yyds_lsit[gg][yy])
        # print(report02_list)

        str_sum = excel_report[2]
        for i in range(0, len(report02_list)):
            if excel_report[0] in ("未完成交易-登0-登3-会员-查看订单详情-子查询","盈亏详情-登0-登3-会员-查看订单详情-子查询"):
                for options in report02_list[i]['options']:
                    del options['matchTime']
            if excel_report[2] != None:
                ppxt_lsit = str_sum.split(",")
                # print(ppxt_lsit)
                for j in ppxt_lsit:
                    # print(sportId_yyds_lsit[i])
                    del report02_list[i][j]
            sport_report_list.append(report02_list[i])

        for key, value in sportId_yyds_lsit[0][0].items():
            sport_report_dict.append(key)
        # print(sport_report_dict)

        time_list = [" 00:00:00", " 23:59:59"]
        print(sport_report_list[1])
        self.tt.sport_report_sql(begin=begin + time_list[0], end=end + time_list[1], excel_report=excel_report,sport_report_dict=sport_report_dict, sport_report_list=sport_report_list)
        return sportId_list

    def sport_report03(self, URL, token, excel_report, begin, end):
        global sportId_list, sportId_yyds_lsit

        sportId_list = []
        sportId_yyds_lsit=[]
        yyds = ''
        for yytt in range(0,int(excel_report[3])):
            headers = eval(excel_report[4])
            if yytt==0:
                url = str(URL) + excel_report[1]
                data = eval(excel_report[5])[0]
                session = requests.session()
                method_list = ["post"]

                if excel_report[7] == method_list[0]:
                    response = session.post(url=url, headers=headers, json=data)
                else:
                    response = session.get(url=url, headers=headers, params=data)
                results = json.loads(response.text)

                if excel_report[0] in module_list:
                    yyds = results['data']
                else:
                    yyds = results['data']['data']

                sportId_yyds_lsit.append(yyds)

                if yyds == []:
                    pass
                else:
                    for i in yyds:
                        if i[excel_report[6]] == '串关':
                            pass
                        elif excel_report[0] in interface_list:
                            sportId_list.append(i[excel_report[6]])
                            sportId_list.append(i['accountId'])
                            roid_list.append(i['levelId'])
                        else:
                            sportId_list.append(i[excel_report[6]])
            else:
                if yyds == []:
                    break
                else:
                    url = str(URL) + excel_report[1]
                    #特殊处理（未完成交易-登0-主查询接口的bady传参）
                    if excel_report[0] in interface_list:
                        data = eval(excel_report[5])[0]
                        # print(excel_report[6],sportId_list[yytt])
                        data[excel_report[6]]=sportId_list[yytt]
                    else:
                        data = eval(excel_report[5])[0]
                    session = requests.session()
                    method_list = ["post"]

                    if excel_report[7] == method_list[0]:
                        response = session.post(url=url, headers=headers, json=data)
                    else:
                        response = session.get(url=url, headers=headers, params=data)
                    results = json.loads(response.text)

                    if excel_report[0] in module_list:
                        yyds = results['data']
                    else:
                        yyds = results['data']['data']
                    sportId_yyds_lsit.append(yyds)

                    for i in yyds:
                        if i[excel_report[6]] == '串关':
                            pass
                        elif excel_report[0] in interface_list:
                            sportId_list.append(i['accountId'])
                            roid_list.append(i['levelId'])
                            # print(sportId_list, roid_list)
                        else:
                            sportId_list.append(i[excel_report[6]])

        if yyds == []:
            pass
        else:
            report03_list = []
            for gg in range(0, len(sportId_yyds_lsit)):
                for yy in range(0, len(sportId_yyds_lsit[gg])):
                    report03_list.append(sportId_yyds_lsit[gg][yy])
            # print(report02_list)

            sport_report_list = []
            str_sum = excel_report[2]
            for i in range(0, len(report03_list)):
                if excel_report[2] != None:
                    ppxt_lsit = str_sum.split(",")
                    # print(ppxt_lsit)
                    for j in ppxt_lsit:
                        # print(sportId_yyds_lsit[i])
                        del report03_list[i][j]
                sport_report_list.append(report03_list[i])

            sport_report_dict = []
            for key, value in sportId_yyds_lsit[0][0].items():
                sport_report_dict.append(key)
            # print(sport_report_dict)

            print(sport_report_list[1])
            time_list = [" 00:00:00", " 23:59:59"]
            self.tt.sport_report_sql(begin=begin + time_list[0], end=end + time_list[1], excel_report=excel_report,sport_report_dict=sport_report_dict, sport_report_list=sport_report_list)
            return sportId_list


class BetController(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self, mysql_info, mongo_info, *args):
        """
        模拟ctrl给我司推送数据
        """
        self.session = requests.session()
        self.dbq = DbQuery(mongo_info)
        # self.ctrl_docs = CtrlIoDocs(mysql_info, mongo_info)
        self.cf = CommonFunc()
        self.mysql = MysqlCommonQuery(mysql_info)
        self.my = MysqlFunc(mysql_info)
        self.sr=SQL_report_ods(mysql_info, mongo_info,AB_list,dict)
        self.b0=betting_odds(mysql_info, mongo_info,AB_list,dict)
        self.wt=water_ammount(mysql_info, mongo_info)

    def report_list_Compared01(self,sport_list,sql_list,Compared,excel_report):
        if sport_list!= [] and sql_list!= []:
            yyds_list = []
            for key, value in sport_list[0].items():
                yyds_list.append(key)
            for i in range(0, len(sport_list)):
                for j in range(0, len(sql_list)):
                    print(sport_list[i][Compared],sql_list[j][Compared])
                    if sport_list[i][Compared] == sql_list[j][Compared]:
                        if sport_list[i] == sql_list[j]:
                            correct_list.append(sql_list[j])
                            # print(correct_list[-1])
                            print(sport_list[i][Compared],"数据对比正确：" + str(sport_list[i]) + "/" + str(sql_list[j]))
                            break
                        else:
                            for report in range(0, len(sql_list[j])):
                                if sport_list[i][yyds_list[report]] == sql_list[j][yyds_list[report]]:
                                    # pass
                                    print(sport_list[i][Compared], str(yyds_list[report]),"数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                else:
                                    sport_all_error.append(str(sport_list[i][Compared]) + "/" + str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str({sport_list[i][Compared]}) + "/" + (str({sql_list[j][Compared]})))
                                    print("\033[31m" + sport_list[i][Compared], str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]) + "\033[0m",type(sport_list[i][yyds_list[report]]),type(sql_list[j][yyds_list[report]]))
        else:
            if sport_list== []:
                sport_all_error.append("接口数据为空")
            if sql_list== []:
                sport_all_error.append("SQL数据为空")

    def report_list_Compared02(self, sport_list,sql_list, Compared,excel_report):
        # print(sport_list)
        # print(sql_list)
        # print(Compared)
        # print(excel_report)
        if sport_list!=[] and sql_list!=[] :
            yyds_list = []
            for key, value in sport_list[0].items():
                yyds_list.append(key)
            for i in range(0, len(sport_list)):
                for j in range(0, len(sql_list)):
                    ppxt_lsit =Compared.split(",")
                    if sport_list[i][ppxt_lsit[0]] == sql_list[j][ppxt_lsit[0]]:
                        if sport_list[i][ppxt_lsit[1]] == sql_list[j][ppxt_lsit[1]]:
                            if sport_list[i] == sql_list[j]:
                                correct_list.append(sql_list[j])
                                print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]),"数据对比正确：" + str(sport_list[i]) + "/" + str(sql_list[j]))
                                break
                            else:
                                print(sport_list[i],"\n",sql_list[j])
                                for report in range(0, len(sql_list[j])):
                                    if sport_list[i][yyds_list[report]] == sql_list[j][yyds_list[report]]:
                                        # pass
                                        print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]), str(yyds_list[report]),"数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                    else:
                                        if i<len(sportId_list):
                                            yyth = sportId_list[i]
                                        else:
                                            yyth="参数已用完"
                                        if excel_report[3] == 1:
                                            sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])) + "/" + str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" +  str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                            print("\033[31m" + str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str( sql_list[j][yyds_list[report]]) + "\033[0m",type(sport_list[i][yyds_list[report]]),type(sql_list[j][yyds_list[report]]))
                                            if yyds_list[report] == 'options':
                                                self.options_report(A=sport_list[i][ppxt_lsit[0]],B=sport_list[i][ppxt_lsit[1]],C=yyds_list[report],D=sport_list[i][yyds_list[report]],E=sql_list[j][yyds_list[report]])
                                        else:
                                            sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])) + "/" +yyth + "/"+str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" +  str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                            print("\033[31m" + str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]+"-"+yyth), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str( sql_list[j][yyds_list[report]]) +"\033[0m",type(sport_list[i][yyds_list[report]]),type(sql_list[j][yyds_list[report]]))
                                            if yyds_list[report]=='options':
                                                self.options_report(A=sport_list[i][ppxt_lsit[0]],B=sport_list[i][ppxt_lsit[1]], C=yyds_list[report],D=sport_list[i][yyds_list[report]], E=sql_list[j][yyds_list[report]])
                    #     else:
                    #         print(f"数据对比错误：{sport_list[i][ppxt_lsit[1]]}/{sql_list[j][ppxt_lsit[1]]}，{type(sport_list[i][ppxt_lsit[1]])}/{type(sport_list[i][ppxt_lsit[1]])}")
                    # else:
                    #     print(f"数据对比错误：{sport_list[i][ppxt_lsit[0]]}/{sql_list[j][ppxt_lsit[0]]}，{type(sport_list[i][ppxt_lsit[0]])}/{type(sport_list[i][ppxt_lsit[0]])}")
        else:
            if sport_list== []:
                sport_all_error.append("接口数据为空")
            if sql_list== []:
                sport_all_error.append("SQL数据为空")

    def report_list_Compared03(self, sport_list,sql_list, Compared,excel_report):
        if sport_list!= [] and sql_list!= []:
            yyds_list = []
            for key, value in sport_list[0].items():
                yyds_list.append(key)
            for i in range(0, len(sql_list)):
                for j in range(0, len(sql_list)):
                    str_sum = Compared
                    ppxt_lsit = str_sum.split(",")
                    # print(ppxt_lsit)
                    if sport_list[i][ppxt_lsit[0]] == sql_list[j][ppxt_lsit[0]]:
                        if sport_list[i][ppxt_lsit[1]] == sql_list[j][ppxt_lsit[1]]:
                            if sport_list[i][ppxt_lsit[2]] == sql_list[j][ppxt_lsit[2]]:
                                if sport_list[i] == sql_list[j]:
                                    correct_list.append(sql_list[j])
                                    print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])+"-"+str(sport_list[i][ppxt_lsit[2]]),"数据对比正确：" + str(sport_list[i]) + "/" + str(sql_list[j]))
                                    break
                                else:
                                    for report in range(0, len(sql_list[j])):
                                        if sport_list[i][yyds_list[report]] == sql_list[j][yyds_list[report]]:
                                            # pass
                                            print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])+"-"+str(sport_list[i][ppxt_lsit[2]]), str(yyds_list[report]),"数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                        else:
                                            if i < len(sportId_list):
                                                yyth = sportId_list[i]
                                            else:
                                                yyth = "参数已用完"
                                            if excel_report[3] == 1:
                                                sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])) +"-"+str(sport_list[i][ppxt_lsit[2]])+ "/" + str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" +  str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                                print("\033[31m" + str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]+"-"+str(sport_list[i][ppxt_lsit[2]]), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str( sql_list[j][yyds_list[report]]) +"\033[0m"),type(sport_list[i][yyds_list[report]]),type(sql_list[j][yyds_list[report]]))
                                            else:
                                                sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]]) + "-" + str(sport_list[i][ppxt_lsit[1]])) + "-" + str(sport_list[i][ppxt_lsit[2]]) + "/" +yyth + "/" +str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                                print("\033[31m" + str(sport_list[i][ppxt_lsit[0]]) + "-" + str(sport_list[i][ppxt_lsit[1]] + "-" + str(sport_list[i][ppxt_lsit[2]]+"-"+yyth), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]) +"\033[0m"),type(sport_list[i][yyds_list[report]]),type(sql_list[j][yyds_list[report]]))
        else:
            if sport_list == []:
                sport_all_error.append("接口数据为空")
            if sql_list== []:
                sport_all_error.append("SQL数据为空")

    def options_report(self,A, B, C,D,E):
        options_yyds=0
        print(f"\033[32m{A}-{B},{C}：数据对比开始---------------------------------------------------------------------------\033[0m")
        aa_list = []
        print(D[0])
        print(E[0])
        for key, value in D[0].items():
            aa_list.append(key)
        if D==E:
            print("数据对比正确")
        else:
            for ykk in range(0, len(D)):
                for i in aa_list:
                    if D[ykk][i] == E[ykk][i]:
                        print(f"{A}-{B},{C}数据对比正确：{D[ykk][i]}/{E[ykk][i]}")
                    else:
                        print(f"\033[31m{A}-{B},{C}数据对比错误：{D[ykk][i]}/{E[ykk][i]}\033[0m{type(D[ykk][i])}/{type(E[ykk][i])}-")
                        options_yyds = 1
        print(f"\033[32m{A}-{B},{C}：数据对比结束----------------------------------------------------------------------------------------------\033[0m")
        return options_yyds


    def if_error(self, A,B):
        key01=[]
        key02 = []
        error=''
        number_num = random.randint(0, len(A))
        if number_num>len(B):
            number_num=':'
        else:
            if len(A[number_num])==len(B[number_num]):
                # if A['options']
                for key,value in A[0].items():
                    key01.append(key)
                if 'options' in key01:
                    if len(A['options'].keys)==len(B['options'].keys):
                        yytr=self.options_report(A=A[key01[0]], B=A[key01[-1]], C='options',D=A['options'],E=B['options'])
                        if yytr==0:
                            if A==B:
                                print(f"\33[31m数据预校验通过\33[0m")
                                A=correct_list
                            else:
                                print("\33[31m数据预校验不通过\33[0m")
                                error = '错误'
                    else:
                        print(f"A与B，key值不一致{len(A['options'].keys)}/{len(B['options'].keys)}")
                        for key, value in B[0]['options'].items():
                            key02.append(key)
                        for key_value in key02:
                            if key_value in key01:
                                del key01[key01.index(key_value)]
                            else:
                                pass
                        print(f"\33[31mA与B，options字典数量不相等,他们相差{key01}\33[0m")
                else:
                    if A==B:
                        print(f"\33[31m数据预校验通过\33[0m")
                        A=correct_list
                    else:
                        print(f"\33[32m数据预校验不通过\33[0m")
                        error='错误'
            else:
                print(f"\33[32m接口数据与SQL数据字段比对错误,A:{len(A[number_num])}/B:{len(A[number_num])}\33[0m")
                error = '错误'
        return error




    def null_data_processing(self,sort_num,mix_number,excel_report):
        print(f"\33[33m正在检验{excel_report[0]}-{excel_report[1]}数据是否返回为空\33[0m")

        report_null=''
        if sort_num==() or sort_num==None or sort_num[0][0]==() or sort_num[0][0]==None:
            report_null = []
        else:
            pass
        return report_null

    def null_report(self,sport_report_list,sql_report_list,excel_report):
        global Prepare_enough_list,Prepare_enough_list,sport_error
        Prepare_enough_list=[]
        sport_error=[]
        if sport_report_list==[]:
            sql_report_list=[]
        else:
            pass

        if sport_report_list==sql_report_list:
            print(f"\033[32m代理{sport_report_list}-{sql_report_list}数据一致,都是空列表\033[0m")
            Prepare_enough_list.append(f"\033[32m代理{sport_report_list}-{sql_report_list}数据一致,都是空列表\033[0m")
        else:
            print(f"\033[31m代理{excel_report[0]}-{excel_report[1]}，数据错误，需要比对\033[0m")
            Prepare_enough_list.append(f"\033[31m代理{sport_report_list}-{sql_report_list}，数据错误，需要比对\033[0m")
            sport_error.append(sport_report_list)
            sport_error.append(sql_report_list)

    def if_f(self,BBQ,all,num,all_order_no,begin,end):
        if BBQ[0] == "f":
            sql=eval(BBQ)
        else:
            sql=BBQ
        return sql

    def order_no_new(self,yyds_list):
        orderNo_list = []
        count_i = 0
        count_j = 1
        count = 0
        for i in range(0, len(yyds_list)):
            print("i循环:", i, count_i)
            orderNo_tuple = ()
            if i == count_i:
                # new_list.append(yyds_list[i])
                for j in range(count_j, len(yyds_list)):
                    print("j循环:", j, count_j)
                    if j == count_j:
                        # print(yyds_list[i][8],yyds_list[j][8])
                        if yyds_list[i][8] == yyds_list[j][8]:
                            orderNo_tuple = yyds_list[i] + yyds_list[j]
                            print(yyds_list[i][8], yyds_list[j][8])
                            count_j = count_j + 1
                            count_i = count_i + 1
                            if j == len(yyds_list) - 1:
                                orderNo_list.append(orderNo_tuple)
                                print(f"第{count}次,{count_i},{count_j}")
                            else:
                                for k in range(count_j, len(yyds_list)):
                                    print(yyds_list[i][8], yyds_list[k][8])
                                    if yyds_list[i][8] == yyds_list[k][8]:
                                        if k == len(yyds_list) - 1:
                                            count = count + 1
                                            count_j = count_j + 1
                                            count_i = count_i + 1
                                            orderNo_list.append(orderNo_tuple)
                                            print(f"第{count}次,{count_i},{count_j}")
                                        else:
                                            orderNo_tuple = orderNo_tuple + yyds_list[k]
                                            count_j = count_j + 1
                                            count_i = count_i + 1
                                    else:
                                        orderNo_list.append(orderNo_tuple)
                                        count_j = count_j + 1
                                        count_i = count_i + 1
                                        count = count + 1
                                        print(f"第{count}次,{count_i},{count_j}")
                                        break
                        else:
                            count_i = count_i + 1
                            count_j = count_j + 1
                            count = count + 1
                            break
                    else:
                        break
            else:
                continue
        return orderNo_list




    def sport_report_sql(self,begin,end,excel_report,sport_report_dict,sport_report_list):
        global options_list,sportId_sql_list
        print(f"\33[34m正在执行{excel_report[0]}-{excel_report[1]}\33[0m")

        num_list = []
        sort_num_list = []
        mix_number=[]
        options_list = []
        sportId_sql_list = []
        sport_num_sql_list=[]
        sql_yyds =[]
        marketID_sql_list = []
        marketID_sql_dict={}


        sum_yyds = excel_report[8]
        yyds = sum_yyds.split("@")
        report_null=''
        all=''
        num=''
        sql_count=0
        all_order_no=''
        if yyds[0]=='':
            del yyds[0]
        if excel_report[3] == 1:
            if len(yyds) == 1:
                sql=self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                sort_num = self.my.query_data(sql, db_name='bfty_credit')
                mix_number.append("1-1")
                report_null=self.null_data_processing(sort_num=sort_num,mix_number=mix_number,excel_report=excel_report)
                if report_null==[]:
                    self.null_report(sport_report_list=sport_report_list,sql_report_list=report_null,excel_report=excel_report)
                else:
                    pass
            else:
                sql01 =self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                sql02 =self.if_f(BBQ=yyds[1],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                sort_num_list.append(sort_num01)
                sort_num_list.append(sort_num02)
                print(sql01,sql02)
                print(sort_num01,sort_num02)

                num_list.append(sort_num_list)
                sort_num = num_list
                print(sort_num)
                mix_number.append("2-2")
                report_null = self.null_data_processing(sort_num=sort_num,mix_number=mix_number,excel_report=excel_report)
                if report_null == []:
                    self.null_report(sport_report_list=sport_report_list, sql_report_list=report_null,excel_report=excel_report)
                else:
                    pass
        elif excel_report[3] == 2:
            sql011=self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
            sort_num = self.my.query_data(sql011, db_name='bfty_credit')
            del yyds[0]
            report_null = self.null_data_processing(sort_num=sort_num, mix_number=mix_number, excel_report=excel_report)
            if report_null == []:
                self.null_report(sport_report_list=sport_report_list, sql_report_list=report_null,excel_report=excel_report)
            else:
                for sportId in sort_num:
                    sportId_sql_list.append(sportId[0])
                for all in sportId_sql_list:
                    sort_num_list = []
                    if len(yyds) == 1:
                        sql=self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                        sort_num = self.my.query_data(sql, db_name='bfty_credit')
                        num_list.append(sort_num)
                        if num_list[0] ==():
                            del num_list[0]
                        sort_num = num_list
                        mix_number.append("2-1")
                        sql_count = sql_count + 1
                        print(len(sport_report_list), sql_count)
                    elif len(yyds) == 2:
                        sql01 = self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                        sql02 = self.if_f(BBQ=yyds[1],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                        sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                        sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                        sort_num_list.append(sort_num01)
                        sort_num_list.append(sort_num02)
                        num_list.append(sort_num_list)
                        sort_num = num_list
                        mix_number.append("2-2")
                        sql_count = sql_count + 1
                        print(len(sport_report_list), sql_count)
                    else:
                        if excel_report[0] in ("未完成交易-登0-登3-会员-查看订单详情-子查询","盈亏详情-登0-登3-会员-查看订单详情-子查询"):
                            order_list=[]
                            sql01=self.if_f(BBQ=yyds[1],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                            sql=self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                            sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                            sort_num=self.my.query_data(sql, db_name='bfty_credit')
                            for i in sort_num01:
                                order_list.append(i[0])
                            # print(order_list)
                            for all_order_no in order_list:
                                yyrt_list = []
                                sql02 = self.if_f(BBQ=yyds[2],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                                sql03 = self.if_f(BBQ=yyds[3],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                                sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                                sort_num03 = self.my.query_data(sql03, db_name='bfty_credit')
                                #拼接元祖参数
                                # print(sort_num)
                                # print(sort_num01)
                                # print(sort_num02)
                                # print(sort_num03)
                                # print("拼接打印sort_num[0]：", sort_num[0])
                                yyrt_list.append(sort_num02[0])
                                ggg = yyrt_list[0] + sort_num[0]
                                yyrt_list[0]=ggg

                                #单独获取options列表的数据，然后组装回去
                                aa_list = []
                                jkk_list = []
                                for key, value in sport_report_list[0]['options'][0].items():
                                    aa_list.append(key)
                                # print(sort_num03)
                                for jkk in sort_num03:
                                    jkk_dict = {}
                                    for jkk_2 in range(0, len(jkk)):
                                        if str(type(jkk[jkk_2])) in type_list:
                                            if jkk[jkk_2]==None:
                                                new_jkk=None
                                            else:
                                                new_jkk=str(jkk[jkk_2])
                                        else:
                                            new_jkk = float(jkk[jkk_2])
                                        jkk_dict[aa_list[jkk_2]]=new_jkk
                                    jkk_list.append(jkk_dict)
                                options_list.append(jkk_list)
                                num_list.append(yyrt_list)
                                sql_count = sql_count + 1
                                print(len(sport_report_list), sql_count)
                            mix_number.append("2-1")
                            sort_num = num_list
                        elif excel_report[0] in ("报表-球类报表-订单查询（根据其盘口查询订单）"):
                            marketID_sql_new_list=[]
                            # sql = self.if_f(BBQ=yyds[0], all=all, num=num, all_order_no=all_order_no, begin=begin,end=end)
                            # sort_num = self.my.query_data(sql, db_name='bfty_credit')
                            # for marketID in sort_num:
                            #     marketID_sql_new_list.append(marketID[0])
                            # marketID_sql_dict[all]=marketID_sql_new_list
                            #
                            # for all_order_no in marketID_sql_dict[all]:
                            #     print(all,all_order_no)
                            #     order_list=[]
                            #     order_list_Duplex=[]
                            yyrt_list=[]
                            #获取球类的单注盘口的会员数据
                            sql01 = self.if_f(BBQ=yyds[0], all=all, num=num, all_order_no=all_order_no,begin=begin, end=end)
                            sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                            #获取球类的串关的会员数据
                            sql02 = self.if_f(BBQ=yyds[1], all=all, num=num, all_order_no=all_order_no,begin=begin, end=end)
                            sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')

                            #for循环单注和串关的会员数据
                            for member in (sort_num01,sort_num02):
                                for num in range(0,len(member)):
                                    tuple_new=()
                                    tuple_new=member[num]
                                    num_list.append(tuple_new)

                            # 遍历options里的键值对，方便写入组装数据
                            aa_list = []
                            for key, value in sport_report_list[0]['options'][0].items():
                                aa_list.append(key)
                            print(aa_list)
                            # 获取单注赛事选项
                            sql03 = self.if_f(BBQ=yyds[2], all=all, num=num, all_order_no=all_order_no, begin=begin,end=end)
                            sort_num03 = self.my.query_data(sql03, db_name='bfty_credit')
                            # 单独获取options列表的数据，然后组装回去
                            jkk_list = []
                            jkk_dict = {}
                            for single in sort_num03:
                                for jkk in range(0, len(single[0])):
                                    print()
                                    if str(type(single[0][jkk])) in type_list:
                                        if single[0][jkk] == None:
                                            new_jkk = None
                                        else:
                                            new_jkk = str(single[0][jkk])
                                    else:
                                        new_jkk = float(single[0][jkk])
                                    print(new_jkk)
                                    print(aa_list[jkk])
                                    print(jkk)
                                    jkk_dict[aa_list[jkk]] = new_jkk
                                jkk_list.append(jkk_dict)
                                options_list.append(jkk_list)

                            #获取串关options的数据
                            sql04 = self.if_f(BBQ=yyds[3], all=all, num=num, all_order_no=all_order_no, begin=begin,end=end)
                            sort_num04 = self.my.query_data(sql04, db_name='bfty_credit')
                            Duplex=self.order_no_new(yyds_list=sort_num04)
                            # 单独获取options列表的数据，然后组装回去
                            jkk_list = []
                            for Duplex_report in Duplex:
                                for jkk in range(0,len(Duplex_report)):
                                    jkk_dict = {}
                                    for jkk_2 in range(0, len(Duplex[jkk])):
                                        if str(type(Duplex[jkk][jkk_2])) in type_list:
                                            if Duplex[jkk][jkk_2]== None:
                                                new_jkk = None
                                            else:
                                                new_jkk = str(Duplex[jkk][jkk_2])
                                        else:
                                            new_jkk = float(Duplex[jkk][jkk_2])
                                        jkk_dict[aa_list[jkk_2]] = new_jkk
                                    jkk_list.append(jkk_dict)
                                options_list.append(jkk_list)
                            mix_number.append("2-1")
                            sort_num = num_list
                            print(sort_num[0],sort_num[-1])
                            print(options_list[0],options_list[-1])
                            exit()

        else:
            sql011=self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
            sort_num = self.my.query_data(sql011, db_name='bfty_credit')
            report_null = self.null_data_processing(sort_num=sort_num, mix_number=mix_number, excel_report=excel_report)
            if report_null == []:
                self.null_report(sport_report_list=sport_report_list, sql_report_list=report_null,excel_report=excel_report)
            else:
                for all in sort_num[0]:
                    sql012 = self.if_f(BBQ=yyds[1],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                    sort_num = self.my.query_data(sql012, db_name='bfty_credit')
                    sql_yyds.append(sort_num)
                del yyds[0:2]
                for sportId in sql_yyds:
                    sportId_sql_list.append(sportId[0][0])
                    sport_num_sql_list.append(sportId[0][1])
                for all in sportId_sql_list:
                    sort_num_list = []
                    if len(yyds) == 1:
                        if excel_report[0] in interface_list:
                            sort_num = ''
                            num=int(sport_num_sql_list[sportId_sql_list.index(all)])
                            if num==0:
                                continue
                            else:
                                sql = self.if_f(BBQ=eval(yyds[0]),all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                                sort_num = self.my.query_data(sql, db_name='bfty_credit')
                                num_list.append(sort_num)
                                # if num==0:
                                #     num_list.clear()
                                mix_number.append("2-1")
                                sql_count = sql_count + 1
                                print(len(sport_report_list), sql_count)
                    else:
                        sql01 = self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                        sql02 = self.if_f(BBQ=yyds[1],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                        sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                        sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                        sort_num_list.append(sort_num01)
                        sort_num_list.append(sort_num02)
                        num_list.append(sort_num_list)
                        mix_number.append("2-2")
                        sql_count = sql_count + 1
                        print(len(sport_report_list), sql_count)
                sort_num = num_list
                print(sort_num)


        sport_sql_list = sport_report_dict
        sql_sport_list = []
        # print(sort_num[0:2])
        # print(options_list)
        # print(f"SQL数据：{sort_num}\n接口数据：{sport_report_list}\n-----------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------")
        if report_null==[]:
            pass
        else:
            self.Compared_report(sort_num=sort_num,sport_list=sport_report_list,sql_name_list=sport_sql_list,sql_list=sql_sport_list,Compared=excel_report[9],report_name=excel_report[0]+"  "+excel_report[1],excel_report=excel_report,mix=mix_number,begin=begin,end=end)

    def Compared_report(self, sort_num, sport_list, sql_name_list, sql_list, Compared, report_name, excel_report,mix,begin,end):
        global sport_error,sport_all_error,yyds01,correct_list,Prepare_enough_list
        correct_list=[]
        Prepare_enough_list=[]
        sport_error = []
        sport_all_error = []
        str_num=Compared
        yyds01=str_num.split(",")
        if mix==[]:
            pass
        else:
            print(mix[0])
        if mix[0]==str('1-1'):
            print(sort_num[0])
            # print(sort_num)
            # print(sort_num[0])
            for i in range(0, len(sort_num)):
                sql_dict = {}
                for j in range(0, len(sort_num[i])):
                    if str(type(sort_num[i][j])) in type_list:
                        if sort_num[i][j]=="odds":
                            yy_num =self.sr.credit_odds(order_no=sort_num[i][j+1],bet_type="",AB_list=AB_list,dict=dict)
                        elif sql_name_list[j]=="oddType":
                            yy_num = self.sr.total_odds(order_no=sort_num[i][j+1],number='')
                        elif sql_name_list[j] in int_list:
                            if sql_name_list[j]=="levelId":
                                yy_num = int(sort_num[i][j])+1
                            else:
                                yy_num = int(sort_num[i][j])
                        elif sort_num[i][j] == "公司总计":
                            if excel_report[0] in options_report_list:
                                yy_num = self.wt.Company_winlose(agent_id='',member_id=sort_num[i][1],sportId='',marketId='',tournamentId='',matchId='',login_account=Dl_list[pkk],begin=begin,end=end,Duplex='')
                            elif  excel_report[0] in one_report_list:
                                if excel_report[0]=="报表-球类报表-主查询":
                                    yy_num = self.wt.Company_winlose(agent_id='',member_id='',sportId=sort_num[i][-2],marketId='',tournamentId='',matchId='',login_account=Dl_list[pkk],begin=begin,end=end,Duplex='')
                                elif excel_report[0] == "报表-混合串关-主查询":
                                    yy_num = self.wt.Company_winlose(agent_id='', member_id=sort_num[i][-1], sportId='',marketId='', tournamentId='', matchId='',login_account=Dl_list[pkk], begin=begin, end=end,Duplex=1)
                        elif sort_num[i][j] == "总佣金":
                            if excel_report[0] in options_report_list:
                                yy_num = self.wt.total_commission(agent_id='', member_id=sort_num[i][1],sportId='',marketId='',tournamentId='',matchId='',login_account=Dl_list[pkk],begin=begin,end=end,Duplex='')
                            elif  excel_report[0] in one_report_list:
                                if excel_report[0]=="报表-球类报表-主查询":
                                    yy_num = self.wt.total_commission(agent_id='',member_id='',sportId=sort_num[i][-2],marketId='',tournamentId='',matchId='',login_account=Dl_list[pkk],begin=begin,end=end,Duplex='')
                                elif excel_report[0] == "报表-混合串关-主查询":
                                    yy_num = self.wt.total_commission(agent_id='', member_id=sort_num[i][-1],sportId='', marketId='', tournamentId='',matchId='', login_account=Dl_list[pkk],begin=begin, end=end,Duplex=1)
                        else:
                            yy_num=str(sort_num[i][j])
                    else:
                        yy_num = float(sort_num[i][j])
                    sql_dict[sql_name_list[j]] =yy_num
                sql_list.append(sql_dict)
            print("sport_list组装数据对比：", sport_list[1])
            print("sql_list组装数据对比：", sql_list[1])
        if mix[0]==str('2-1'):
            print(sort_num[0][0])
            # print(sort_num)
            # print(sort_num[0])
            # print(sort_num[0][0])
            count = 0
            for i in range(0, len(sort_num)):
                for j in range(0,len(sort_num[i])):
                    sql_dict = {}
                    for g in range(0,len(sort_num[i][j])):
                        if str(type(sort_num[i][j][g]))in type_list:
                            if sql_name_list[g] in int_list:
                                if excel_report[0] in ('盈亏详情-登0-登3-会员-查看订单详情-子查询','报表-球类报表-订单查询（根据其盘口查询订单）'):
                                    yy_num = str(sort_num[i][j][g])
                                else:
                                    yy_num = int(sort_num[i][j][g])
                            elif sort_num[i][j][g] == "options":
                                yy_num = options_list[i]
                            elif sort_num[i][j][g] == "公司总计":
                                if excel_report[0] in interface_list:
                                    yy_num = self.wt.Company_winlose(agent_id=sort_num[i][j][1], member_id='', sportId='',marketId='', tournamentId='', matchId='',login_account=Dl_list[pkk], begin=begin, end=end,Duplex='')
                                elif excel_report[0] in two_report_list:
                                    if excel_report[0]=='报表-球类报表-子查询（根据其球类查询盘口）':
                                        yy_num = self.wt.Company_winlose(agent_id='', member_id='', sportId=sort_num[i][j][-3],marketId=sort_num[i][j][-8], tournamentId='',matchId='',login_account=Dl_list[pkk], begin=begin, end=end,Duplex='')
                                    else:
                                        yy_num = self.wt.Company_winlose(agent_id='', member_id='', sportId=sort_num[i][j][-3],marketId=sort_num[i][j][-8], tournamentId='',matchId=str(sportId_sql_list[i]),login_account=Dl_list[pkk], begin=begin, end=end,Duplex='')
                            elif sort_num[i][j][g] == "总佣金":
                                if excel_report[0] in interface_list:
                                    yy_num = self.wt.total_commission(agent_id=sort_num[i][j][1],member_id='', sportId='',marketId='', tournamentId='', matchId='',login_account=Dl_list[pkk], begin=begin, end=end,Duplex='')
                                elif excel_report[0] in two_report_list:
                                    if excel_report[0]=="报表-球类报表-子查询（根据其球类查询盘口）":
                                        yy_num = self.wt.total_commission(agent_id='', member_id='',sportId=sort_num[i][j][-3], marketId=sort_num[i][j][-8],tournamentId='', matchId='',login_account=Dl_list[pkk], begin=begin, end=end,Duplex='')
                                    else:
                                        yy_num = self.wt.total_commission(agent_id='', member_id='',sportId=sort_num[i][j][-3], marketId=sort_num[i][j][-8],tournamentId='', matchId=str(sportId_sql_list[i]),login_account=Dl_list[pkk], begin=begin,end=end,Duplex='')
                            elif type(sort_num[i][j][g])==type(None):
                                yy_num = sort_num[i][j][g]
                            else:
                                yy_num = str(sort_num[i][j][g])
                        else:
                            yy_num = float(sort_num[i][j][g])
                        sql_dict[sql_name_list[g]]=yy_num
                    sql_list.append(sql_dict)
            print("sport_list组装数据对比：", sport_list[1])
            print("sql_list组装数据对比：", sql_list[1])
        if mix[0]==str('2-2'):
            print(sort_num[0][0][0])
            # print(sort_num)
            # print(sort_num[0])
            # print(sort_num[0][0])
            # print(sort_num[0][0][0])
            for i in range(0, len(sort_num)):
                for j in range(0, len(sort_num[i])):
                    for l in range(0, len(sort_num[i][j])):
                        sql_dict = {}
                        for g in range(0,len(sort_num[i][j][l])):
                            if str(type(sort_num[i][j][l][g])) in type_list:
                                if sql_name_list[g] in int_list:
                                    yy_num = int(sort_num[i][j][l][g])
                                elif sort_num[i][j][l][g] == "公司总计":
                                    if excel_report[0] in two_report_list:
                                        yy_num = self.wt.Company_winlose(agent_id='', member_id='',sportId=sort_num[i][j][l][-3], marketId=sort_num[i][j][l][-8],tournamentId='', matchId='',login_account=Dl_list[pkk], begin=begin,end=end,Duplex='')
                                    elif excel_report[0] == "报表-联赛报表-主查询":
                                        yy_num = self.wt.Company_winlose(agent_id='', member_id='', sportId='',marketId='', tournamentId=sort_num[i][j][l][-2],matchId='', login_account=Dl_list[pkk],begin=begin, end=end,Duplex='')
                                    elif excel_report[0] == "报表-赛事盈亏-主查询":
                                        yy_num = self.wt.Company_winlose(agent_id='', member_id='', sportId='',marketId='', tournamentId='',matchId=str(sort_num[i][j][l][-6]),login_account=Dl_list[pkk], begin=begin,end=end,Duplex='')
                                elif sort_num[i][j][l][g] == "总佣金":
                                    if excel_report[0] in two_report_list:
                                        yy_num = self.wt.total_commission(agent_id='', member_id='',sportId=sort_num[i][j][l][-3], marketId=sort_num[i][j][l][-8],tournamentId='', matchId='',login_account=Dl_list[pkk], begin=begin,end=end,Duplex='')
                                    elif excel_report[0] == "报表-联赛报表-主查询":
                                        yy_num = self.wt.total_commission(agent_id='', member_id='', sportId='',marketId='', tournamentId=sort_num[i][j][l][-2],matchId='', login_account=Dl_list[pkk],begin=begin, end=end,Duplex='')
                                    elif excel_report[0] == "报表-赛事盈亏-主查询":
                                        yy_num = self.wt.total_commission(agent_id='', member_id='', sportId='',marketId='', tournamentId='',matchId=str(sort_num[i][j][l][-6]),login_account=Dl_list[pkk], begin=begin,end=end,Duplex='')
                                elif type(sort_num[i][j][l][g]) == type(None):
                                    yy_num = sort_num[i][j][l][g]
                                else:
                                    yy_num = str(sort_num[i][j][l][g])
                            else:
                                yy_num = float(sort_num[i][j][l][g])
                            sql_dict[sql_name_list[g]] = yy_num
                        sql_list.append(sql_dict)
            print("sport_list组装数据对比：",sport_list[1])
            print("sql_list组装数据对比：",sql_list[1])


        yyts=self.if_error(A=sport_list, B=sql_list)
        if yyts=='':
            if len(yyds01)==1:
                self.report_list_Compared01(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)
            elif len(yyds01)==2:
                self.report_list_Compared02(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)
            else:
                self.report_list_Compared03(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)
        else:
            pass

        if len(sport_list) == len(correct_list):
            print(f"\033[32m代理{Dl_list[pkk]}的{report_name}，接口数据比对全部正确：{len(sport_list)}-{len(correct_list)}\033[0m")
            Prepare_enough_list.append(f"\033[32m代理{Dl_list[pkk]}的{report_name}，接口数据比对全部正确\033[0m")
        else:
            print(f"\033[31m代理{Dl_list[pkk]}的{report_name}，数据错误，需要比对,{len(sport_list)},{len(correct_list)}\033[0m")
            Prepare_enough_list.append(f"\033[31m代理{Dl_list[pkk]}的{report_name}，数据错误，需要比对,{len(sport_list)},{len(correct_list)}\033[0m")
            for ff in range(0,len(correct_list)):
                if correct_list[ff] in sql_list:
                    del sql_list[sql_list.index(correct_list[ff])]
            # print(sql_list)
            sport_error.append(sport_list)
            sport_error.append(sql_list)
            # print(f"\033[34m部分数据：{sport_error}\033[0m")
            # print(f"\033[34m全部数据：{sport_all_error}\033[0m")









    # def Duplex_report_sql(self, begin, end):
    #     sql = f"SELECT c.sport_id,CASE c.sport_id WHEN 'sr:sport:1' THEN '足球' WHEN 'sr:sport:20' THEN '乒乓球' WHEN 'sr:sport:5' THEN '网球' WHEN 'sr:sport:3' THEN '棒球' WHEN 'sr:sport:2' THEN '篮球' WHEN 'sr:sport:31' THEN '羽毛球' WHEN 'sr:sport:4' THEN '冰球' WHEN 'sr:sport:23' THEN '排球' END AS '球类',SUM(c.bet_amount) '总投注额',SUM(c.efficient_amount) '总有效金额',CASE WHEN any_value (c.proxy0_id=1531516017847869442) THEN SUM(c.backwater_amount+c.level3_backwater_amount+c.level2_backwater_amount+c.level1_backwater_amount+c.level0_backwater_amount) END AS '总佣金',SUM(c.handicap_win_or_lose) '会员输/赢',SUM(c.backwater_amount) '会员佣金',(SUM(c.handicap_win_or_lose)+SUM(c.backwater_amount)) '会员总计',(SUM(c.level3_win_or_lose)-SUM(c.level3_backwater_amount)) '三级代理输/赢',SUM(c.level3_backwater_amount) '三级代理佣金',SUM(c.level3_win_or_lose) '三级代理总计',(SUM(c.level2_win_or_lose)-SUM(c.level2_backwater_amount)) '二级代理输/赢',SUM(c.level2_backwater_amount) '二级代理佣金',SUM(c.level2_win_or_lose) '二级代理总计',(SUM(c.level1_win_or_lose)-SUM(c.level1_backwater_amount)) '一级代理输/赢',SUM(c.level1_backwater_amount) '一级代理佣金',SUM(c.level1_win_or_lose) '一级代理总计',(SUM(c.level0_win_or_lose)-SUM(c.level0_backwater_amount)) '总代输/赢',SUM(c.level0_backwater_amount) '总代佣金',SUM(c.level0_win_or_lose) '总代总计',(SUM(c.company_win_or_lose)-SUM(c.company_backwater_amount)) '公司输/赢',SUM(c.company_backwater_amount) '公司代理佣金',SUM(c.company_win_or_lose) '公司代理总计' FROM o_account_order AS c LEFT JOIN m_account AS e ON e.id=c.proxy0_id WHERE c.STATUS=2 AND c.award_time IS NOT NULL AND c.settlement_time>='{begin}' AND c.settlement_time<='{end}' AND c.proxy0_id=(SELECT id FROM m_account WHERE login_account='d0')GROUP BY c.sport_id"  # print(sql)
    #     sort_num = self.my.query_data(sql, db_name='bfty_credit')
    #     Duplex_sql_list=['account','betAmount',
    #                     'betIp','betTime','currency',
    #                     'ipAddress','level0ActualPercentage','level0RetreatProportion',
    #                     'level1ActualPercentage','level1RetreatProportion','level2ActualPercentage',
    #                     'level2RetreatProportion','level3ActualPercentage','level3RetreatProportion',
    #                     'loginAccount','mix','mixType',
    #                     'name','oddType','odds',
    #                     'orderNo','orderStatus','sportName']
    #     sql_Duplex_list = []
        # self.Compared_report(sort_num=sort_num, sport_list=Duplex_sql_list, sql_name_list=sport_sql_list,sql_list=sql_Duplex_list, Compared='account', report_name="总投注串关全部查询")








if __name__ == "__main__":
    # MDE环境
    URL = "https://mdesearch.betf.best"

    #120环境
    # mongo_inf = ['app', '123456', '192.168.10.120', '27017']
    # mysql_inf = ['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']
    #MDE环境
    mongo_inf = ['sport_test', 'BB#gCmqf3gTO5777', '35.194.233.30', '27017']
    mysql_inf = ['35.194.233.30', 'root', 'BB#gCmqf3gTO5b*', '3306']

    AB_list = ["A", "B", "C", "D", "E", "F", ]
    dict = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}


    # mf = MongoFunc(mongo_inf)
    bc =BetController(mysql_inf, mongo_inf)
    cc=report_data(mysql_inf, mongo_inf)

    for pkk in range(0,1):
        #参数化接口数据列表
        # sport_report_list = []
        # 参数化代理账号数据列表
        Dl_list=["d0","d10","d2","d3"]
        # 参数化EXCEL路径列表
        excel = [r"C:\\test\\d0_comparison_report.xlsx", 0]
        save_excel = ["C:\\test\\d0_comparison_report.xlsx"]
        # 参数化接口返回数据，字典取值判断list，在list中，取results['data'],不在列表中，取results['data']['data']
        module_list = ["总投注-混合串关-主查询","总投注-混合串关-子查询(查询其注单号，包含的比赛)",
                       "未完成交易-登0-主查询","未完成交易-登0-登3-会员-子查询","未完成交易-登0-登3-会员-查看订单详情-子查询",
                       "盈亏详情-登0-主查询","盈亏详情-登0-登3-会员-子查询","盈亏详情-登0-登3-会员-查看订单详情-子查询"]
        roid_list=[]
        proxy_id_list=['0','1','2','3']
        int_list=['levelId','numberOfBets',"betType"]
        type_list=["<class 'str'>", "<class 'datetime.datetime'>", "<class 'NoneType'>", "<class 'int'>"]
        sport_report02_list=[]
        interface_list = ["未完成交易-登0-主查询", "盈亏详情-登0-主查询"]
        options_report_list=['未完成交易-登0-登3-会员-查看订单详情-子查询','盈亏详情-登0-登3-会员-查看订单详情-子查询','盈亏详情-登0-登3-会员-子查询']

        one_report_list=['报表-球类报表-主查询','报表-联赛报表-主查询','报表-赛事盈亏-主查询','报表-混合串关-主查询']
        two_report_list=['报表-球类报表-子查询（根据其球类查询盘口）','报表-赛事盈亏-子查询（根据其赛事查询其盘口）']


        # yyds=cc.login(URL=URL,begin="2022-06-04",end="2022-06-10")
        # ppds=bc.
        # (begin="2022-06-04 00:00:00",end="2022-06-10 23:59:59")

        # time_new_list=[]
        # for i in range(0,100):
        #     time.sleep(600)
        #     time01 = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
        #     time_new_list.append(time01)
        #     #调用本地Exce读取数据
        #     ccds=cc.reading_Excel(excel=excel, save_excel=save_excel,begin="2022-06-15",end="2022-06-21", URL=URL)
        # print(time_new_list)

        # 调用本地Exce读取数据
        # toten='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE1MzE1MTYwMTc4NDc4Njk0NDIiLCJleHAiOjE2NTY3NzMxMzMsInVzZXJuYW1lIjoiZDAifQ.L9lyGj3R8UafesdblbplhHrw5OxXyrmDmBvx_PXHEX4'
        # # toten=''
        # ccds=cc.reading_Excel(excel=excel, save_excel=save_excel,begin="2022-06-22",end="2022-06-28", URL=URL)




        #调试SQL数据:
        excel_report=['报表-球类报表-订单查询（根据其盘口查询订单）', '"/winOrLost/sport","/winOrLost/market","/winOrLost/order/details"', 'companyCommission,companyCommissionRatio,companyPercentage,companyTotal,companyWinOrLose,mixNum', 2, "{\n        'Content-Type': 'application/json;charset=UTF-8',\n        'LoginDiv': '555666',\n        'Account_Login_Identify': token\n    }", '[{"matchId":"", "sportId":"","queryDateType":3, "begin":begin,"end":end,"searchAccount":"", "page":1,"limit":50},{"sportId":"sr:sport:1","queryDateType":3,"begin":begin,"end":end},{"begin":begin,"end":end,"dateType":3,"page":1,"limit":500,"sportId":"sr:sport:1","marketId":"1","account":"","queryDateType":3,"tournamentId":""}]', 'sportId', 'post', '@f"SELECT c.sport_id FROM o_account_order AS c LEFT JOIN m_account AS e ON e.id=c.proxy0_id WHERE c.STATUS=2 AND c.award_time IS NOT NULL AND c.award_time>=\'{begin}\' AND c.award_time<=\'{end}\' AND c.proxy0_id=(SELECT id FROM m_account WHERE login_account=\'d0\') GROUP BY c.sport_id"\n@f"SELECT CONCAT(c.user_name,\'/\',c.login_account) AS \'账号/登入账号\',any_value (c.bet_amount) \'投注额\',any_value (c.bet_ip),any_value (c.ip_address),(CASE any_value (c.settlement_result) WHEN \'1\' THEN \'赢\' WHEN \'2\' THEN \'输\' WHEN \'5\' THEN \'平局走水\' WHEN \'6\' THEN \'注单取消\' END) AS \'注单状态\',any_value (c.create_time),CASE any_value(c.bet_type) WHEN \'1\' THEN \'单注\' WHEN \'2\' THEN \'串关\' WHEN \'3\' THEN \'复式串关\' END \'注单状态\',any_value (c.level0_backwater_amount) \'总代佣金\',c.company_retreat_proportion \'总代佣金比例\',c.level0_actual_percentage \'总代占成数\',any_value (c.level0_win_or_lose) \'总代总计\',(any_value (c.level0_win_or_lose)-any_value (c.level0_backwater_amount)) \'总代输/赢\',any_value (c.level1_backwater_amount) \'一级代理佣金\',c.level0_retreat_proportion \'一级代理佣金比例\',c.level1_actual_percentage \'一级代理占成数\',any_value (c.level1_win_or_lose) \'一级代理总计\',(any_value (c.level1_win_or_lose)-any_value (c.level1_backwater_amount)) \'一级代理输/赢\',any_value (c.level2_backwater_amount) \'二级代理佣金\',c.level1_retreat_proportion \'二级代理佣金比例\',c.level2_actual_percentage \'二级代理占成数\',any_value (c.level2_win_or_lose) \'二级代理总计\',(any_value (c.level2_win_or_lose)-any_value (c.level2_backwater_amount)) \'二级代理输/赢\',any_value (c.level3_backwater_amount) \'三级代理佣金\',c.level2_retreat_proportion \'三级代理佣金比例\',c.level3_actual_percentage \'三级代理占成数\',any_value (c.level3_win_or_lose) \'三级代理总计\',(any_value (c.level3_win_or_lose)-any_value (c.level3_backwater_amount)) \'三级代理输/赢\',any_value (c.backwater_amount) \'会员佣金\',c.level3_retreat_proportion \'会员佣金比例\',(any_value (c.handicap_win_or_lose)+any_value (c.backwater_amount)) \'会员总计\',any_value (c.handicap_win_or_lose) \'会员输/赢\',any_value (b.NAME) \'名称\',any_value (a.credit_odds) \'赔率\',any_value (a.odds_type) \'赔率类型\',\'options\' AS \'比赛\',c.order_no,c.award_time,c.sport_id,CASE c.sport_id WHEN \'sr:sport:1\' THEN \'足球\' WHEN \'sr:sport:20\' THEN \'乒乓球\' WHEN \'sr:sport:5\' THEN \'网球\' WHEN \'sr:sport:3\' THEN \'棒球\' WHEN \'sr:sport:2\' THEN \'篮球\' WHEN \'sr:sport:31\' THEN \'羽毛球\' WHEN \'sr:sport:4\' THEN \'冰球\' WHEN \'sr:sport:23\' THEN \'排球\' END AS \'球类\',c.efficient_amount,any_value (c.handicap_win_or_lose) \'会员输/赢\' FROM o_account_order AS c LEFT JOIN u_user AS b ON b.id=c.user_id LEFT JOIN o_account_order_match AS a ON a.order_no=c.order_no WHERE c.STATUS=2 AND c.award_time IS NOT NULL  AND c.award_time>=\'{begin}\' AND c.award_time<=\'{end}\' AND c.bet_type=1 AND c.proxy0_id=(SELECT id FROM m_account WHERE login_account=\'d0\') AND c.sport_id=\'{all}\' GROUP BY c.user_name,c.login_account,c.user_id,c.currency,sport_id,c.order_no,c.sport_id,c.company_retreat_proportion,c.level0_actual_percentage,c.level1_actual_percentage,c.level2_actual_percentage,c.level3_actual_percentage,c.level0_retreat_proportion,c.level1_retreat_proportion,c.level2_retreat_proportion,c.level3_retreat_proportion,c.award_time,c.efficient_amount,c.create_time"\n@f"SELECT CONCAT(c.user_name,\'/\',c.login_account) AS \'账号/登入账号\',any_value (c.bet_amount) \'投注额\',any_value (c.bet_ip),any_value (c.ip_address),(CASE any_value (c.settlement_result) WHEN \'1\' THEN \'赢\' WHEN \'2\' THEN \'输\' WHEN \'5\' THEN \'平局走水\' WHEN \'6\' THEN \'注单取消\' END) AS \'注单状态\',any_value (c.create_time),CASE any_value(c.bet_type) WHEN \'1\' THEN \'单注\' WHEN \'2\' THEN \'串关\' WHEN \'3\' THEN \'复式串关\' END \'注单状态\',any_value (c.level0_backwater_amount) \'总代佣金\',c.company_retreat_proportion \'总代佣金比例\',c.level0_actual_percentage \'总代占成数\',any_value (c.level0_win_or_lose) \'总代总计\',(any_value (c.level0_win_or_lose)-any_value (c.level0_backwater_amount)) \'总代输/赢\',any_value (c.level1_backwater_amount) \'一级代理佣金\',c.level0_retreat_proportion \'一级代理佣金比例\',c.level1_actual_percentage \'一级代理占成数\',any_value (c.level1_win_or_lose) \'一级代理总计\',(any_value (c.level1_win_or_lose)-any_value (c.level1_backwater_amount)) \'一级代理输/赢\',any_value (c.level2_backwater_amount) \'二级代理佣金\',c.level1_retreat_proportion \'二级代理佣金比例\',c.level2_actual_percentage \'二级代理占成数\',any_value (c.level2_win_or_lose) \'二级代理总计\',(any_value (c.level2_win_or_lose)-any_value (c.level2_backwater_amount)) \'二级代理输/赢\',any_value (c.level3_backwater_amount) \'三级代理佣金\',c.level2_retreat_proportion \'三级代理佣金比例\',c.level3_actual_percentage \'三级代理占成数\',any_value (c.level3_win_or_lose) \'三级代理总计\',(any_value (c.level3_win_or_lose)-any_value (c.level3_backwater_amount)) \'三级代理输/赢\',any_value (c.backwater_amount) \'会员佣金\',c.level3_retreat_proportion \'会员佣金比例\',(any_value (c.handicap_win_or_lose)+any_value (c.backwater_amount)) \'会员总计\',any_value (c.handicap_win_or_lose) \'会员输/赢\',any_value (b.NAME) \'名称\',any_value (a.credit_odds) \'赔率\',any_value (a.odds_type) \'赔率类型\',\'options\' AS \'比赛\',c.order_no,c.award_time,c.sport_id,CASE c.sport_id WHEN \'sr:sport:1\' THEN \'足球\' WHEN \'sr:sport:20\' THEN \'乒乓球\' WHEN \'sr:sport:5\' THEN \'网球\' WHEN \'sr:sport:3\' THEN \'棒球\' WHEN \'sr:sport:2\' THEN \'篮球\' WHEN \'sr:sport:31\' THEN \'羽毛球\' WHEN \'sr:sport:4\' THEN \'冰球\' WHEN \'sr:sport:23\' THEN \'排球\' END AS \'球类\',c.efficient_amount,any_value (c.handicap_win_or_lose) \'会员输/赢\' FROM o_account_order AS c LEFT JOIN u_user AS b ON b.id=c.user_id LEFT JOIN o_account_order_match AS a ON a.order_no=c.order_no WHERE c.STATUS=2 AND c.award_time IS NOT NULL  AND c.award_time>=\'{begin}\' AND c.award_time<=\'{end}\' AND c.bet_type!=1 AND c.proxy0_id=(SELECT id FROM m_account WHERE login_account=\'d0\') AND c.sport_id=\'{all}\' GROUP BY c.user_name,c.login_account,c.user_id,c.currency,sport_id,c.order_no,c.sport_id,c.company_retreat_proportion,c.level0_actual_percentage,c.level1_actual_percentage,c.level2_actual_percentage,c.level3_actual_percentage,c.level0_retreat_proportion,c.level1_retreat_proportion,c.level2_retreat_proportion,c.level3_retreat_proportion,c.award_time,c.efficient_amount,c.create_time"\n@f"SELECT away_team_name,bet_score,home_team_name,market_name,match_time,CASE is_live WHEN \'1\' THEN \'滚球盘\' WHEN \'3\' THEN \'早盘\' END \'盘口类型\',credit_odds,odds_type AS \'赔率类型\',order_no,outcome_name,specifier,tournament_name FROM o_account_order_match WHERE order_no in (SELECT c.order_no FROM o_account_order AS c LEFT JOIN u_user AS b ON b.id=c.user_id LEFT JOIN o_account_order_match AS a ON a.order_no=c.order_no WHERE c.STATUS=2 AND c.award_time IS NOT NULL  AND c.award_time>=\'{begin}\' AND c.award_time<=\'{end}\' AND c.bet_type=1 AND c.proxy0_id=(SELECT id FROM m_account WHERE login_account=\'d0\') AND c.sport_id=\'{all}\' GROUP BY c.order_no)"\n@f"SELECT away_team_name,bet_score,home_team_name,market_name,match_time,CASE is_live WHEN \'1\' THEN \'滚球盘\' WHEN \'3\' THEN \'早盘\' END \'盘口类型\',credit_odds,odds_type AS \'赔率类型\',order_no,outcome_name,specifier,tournament_name FROM o_account_order_match WHERE order_no in (SELECT c.order_no FROM o_account_order AS c LEFT JOIN u_user AS b ON b.id=c.user_id LEFT JOIN o_account_order_match AS a ON a.order_no=c.order_no WHERE c.STATUS=2 AND c.award_time IS NOT NULL  AND c.award_time>=\'{begin}\' AND c.award_time<=\'{end}\' AND c.bet_type!=1 AND c.proxy0_id=(SELECT id FROM m_account WHERE login_account=\'d0\') AND c.sport_id=\'{all}\' GROUP BY c.order_no) GROUP BY order_no,away_team_name,bet_score,home_team_name,market_name,match_time,is_live,credit_odds,odds_type,outcome_name,specifier,tournament_name"', 'account,orderNo', '测试不通过\n2022-06-30 18:41:39']
        sport_report_list = [{'account': 'd0d1d2d38y/fceshi0224', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网', 'betMix': '', 'betResult': '输', 'betTime': '2022-06-24 08:57:04', 'betType': '单注', 'level0Commission': 0.0, 'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3CommissionRatio': 0.0, 'level3Percentage': 0.2, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'memberCommission': 0.0, 'memberCommissionRatio': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号iy', 'odds': 1.69, 'oddsType': '1', 'options': [{'awayTeamName': '芹苴', 'betScore': None, 'homeTeamName': 'QNK广南足球俱乐部', 'marketName': '独赢', 'matchTime': '2022-06-25 06:00:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1', 'orderNo': 'XH4ydmPbRncK', 'outcomeName': 'QNK广南足球俱乐部', 'specifier': '', 'tournamentName': '越南职业足球乙级联赛'}], 'orderNo': 'XH4ydmPbRncK', 'settlementTime': '2022-06-25 08:01:45', 'sportId': 'sr:sport:1', 'sportType': '足球', 'validAmount': 10.0, 'winOrLose': -10.0}]
        sport_report_dict = ['调试SQL类容']
        yyds=bc.sport_report_sql(begin="2022-06-22 00:00:00",end="2022-06-28 23:59:59", excel_report=excel_report, sport_report_dict=sport_report_dict,sport_report_list=sport_report_list)







