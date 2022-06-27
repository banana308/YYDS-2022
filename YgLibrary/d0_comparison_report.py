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
                for i in range(2, 4):
                # for i in range(2, rows+1):
                    excel_report = []
                    # 循环列数
                    for j in range(2, int(columns)-2):
                        report=worksheet.cell(i,j).value
                        #获取到的数据写入列表
                        excel_report.append(report)
                    #调用登录接口，获取token，访问接口，获取数据
                    self.login(URL=URL, begin=begin, end=end, excel_report=excel_report)
                    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    #判断用例是否通过
                    if sport_error==[]:
                        execute=execute+1
                        worksheet.cell(i,int(columns)-4,("测试通过"+"\n"+now))
                        worksheet.cell(i, int(columns) - 3, "")
                        worksheet.cell(i, int(columns)-2, "")
                        worksheet.cell(i, int(columns-1), str(Prepare_enough_list))
                    else:
                        Failed=Failed+1
                        worksheet.cell(i, int(columns)-4, ("测试不通过"+"\n"+now))
                        worksheet.cell(i, int(columns)-3, str(sport_error))
                        worksheet.cell(i, int(columns)-2, str(sport_all_error))
                        worksheet.cell(i,int(columns)-1, str(Prepare_enough_list))
            else:
                continue
        time02=datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
        date_time=time02-time01
        print(f"\033[32m\n\n执行通过用例共计{execute}条,\033[0m未通过用例共计\033[31m{Failed}条\033[0m,共计消耗时间{date_time}")
        workbook.save(filename=save_excel[0])
        workbook.close()

    def login(self,URL, begin, end,excel_report):
        """
        @第一次获取token，并保持token连接中，便于后面其他接口访问
        """
        global token
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
        sport_report_list=[]
        sport_report_dict = []
        sportId_yyds_lsit = []
        yyds=''
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
            for i in range(0, len(sql_list)):
                for j in range(0, len(sql_list)):
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
            for i in range(0, len(sql_list)):
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
                                            if excel_report[0] in options_report_list:
                                                if yyds_list[report] == 'options':
                                                    self.options_report(A=sport_list[i][ppxt_lsit[0]],B=sport_list[i][ppxt_lsit[1]],C=yyds_list[report],D=sport_list[i][yyds_list[report]],E=sql_list[j][yyds_list[report]])
                                        else:
                                            sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])) + "/" +yyth + "/"+str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" +  str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                            print("\033[31m" + str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]+"-"+yyth), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str( sql_list[j][yyds_list[report]]) +"\033[0m",type(sport_list[i][yyds_list[report]]),type(sql_list[j][yyds_list[report]]))
                                            if excel_report[0] in options_report_list:
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
        print(f"\033[32m{A}-{B},{C}：数据对比开始---------------------------------------------------------------------------\033[0m")
        aa_list = []
        print(type(D))
        print(type(D[0]))
        print(D[0])
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
                        print(
                            f"\033[31m{A}-{B},{C}数据对比错误：{D[ykk][i]}/{E[ykk][i]}\033[0m{type(D[ykk][i])}/{type(E[ykk][i])}-")
        print(f"\033[32m{A}-{B},{C}：数据对比结束----------------------------------------------------------------------------------------------\033[0m")

    def null_data_processing(self,sort_num,mix_number,excel_report):
        print(f"正在检验{excel_report[0]}-{excel_report[1]}数据是否返回为空")
        print(sort_num)

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

    def sport_report_sql(self,begin,end,excel_report,sport_report_dict,sport_report_list):
        global options_list,sportId_sql_list
        print(f"正在执行{excel_report[0]}-{excel_report[1]}")

        num_list = []
        sort_num_list = []
        mix_number=[]
        options_list = []
        sportId_sql_list = []
        sport_num_sql_list=[]
        sql_yyds =[]
        sum_yyds = excel_report[8]
        yyds = sum_yyds.split("@")
        report_null=''
        all=''
        num=''
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
                    else:
                        if excel_report[0]in ("未完成交易-登0-登3-会员-查看订单详情-子查询","盈亏详情-登0-登3-会员-查看订单详情-子查询"):
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
                                ggg=yyrt_list[0]+sort_num[0]
                                # print(ggg)
                                yyrt_list[0]=ggg
                                # print(yyrt_list)
                                # print("拼接打印yyrt_list：",yyrt_list)

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
                                # print(jkk_list)
                                # print(options_list)
                                num_list.append(yyrt_list)
                                # print(num_list)
                                mix_number.append("2-1")
                                sort_num = num_list
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
                            sql = self.if_f(BBQ=eval(yyds[0]),all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                            sort_num = self.my.query_data(sql, db_name='bfty_credit')
                            num_list.append(sort_num)
                            # if num==0:
                            #     num_list.clear()
                            mix_number.append("2-1")
                    else:
                        sql01 = self.if_f(BBQ=yyds[0],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                        sql02 = self.if_f(BBQ=yyds[1],all=all,num=num,all_order_no=all_order_no,begin=begin,end=end)
                        sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                        sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                        sort_num_list.append(sort_num01)
                        sort_num_list.append(sort_num02)
                        num_list.append(sort_num_list)
                        mix_number.append("2-2")
                sort_num = num_list
                print(sort_num)


        sport_sql_list = sport_report_dict
        sql_sport_list = []
        # print(sort_num)
        # print(f"SQL数据：{sort_num}\n接口数据：{sport_report_list}\n-----------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------")
        if report_null==[]:
            pass
        else:
            self.Compared_report(sort_num=sort_num,sport_list=sport_report_list,sql_name_list=sport_sql_list,sql_list=sql_sport_list,Compared=excel_report[9],report_name=excel_report[0]+"  "+excel_report[1],excel_report=excel_report,mix=mix_number,begin=begin,end=end)

    def Compared_report(self, sort_num, sport_list, sql_name_list, sql_list, Compared, report_name, excel_report,mix,begin,end):
        global sport_error,sport_all_error,yyds01,correct_list,Prepare_enough_list
        print(sport_list)
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
        print(sql_name_list)
        print(sort_num[0])
        if mix[0]==str('1-1'):
            print(len(sql_name_list), len(sort_num[0]))
            # print(sort_num)
            # print(sort_num[0])
            for i in range(0, len(sort_num)):
                sql_dict = {}
                for j in range(0, len(sort_num[i])):
                    if str(type(sort_num[i][j])) in type_list:
                        if sort_num[i][j]=="odds":
                            yy_num =self.sr.credit_odds(order_no=sort_num[i][j+1],bet_type="",AB_list=AB_list,dict=dict)
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
            print(sport_list[1])
            print(sql_list[1])
        if mix[0]==str('2-1'):
            print(len(sql_name_list), len(sort_num[0][0]))
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
                                if excel_report[0]=="盈亏详情-登0-登3-会员-查看订单详情-子查询":
                                    yy_num = str(sort_num[i][j][g])
                                else:
                                    yy_num = int(sort_num[i][j][g])
                            elif sort_num[i][j][g] == "options":
                                yy_num = options_list[i]
                            elif sort_num[i][j][g] == "公司总计":
                                if excel_report[0] in interface_list:
                                    yy_num = self.wt.Company_winlose(agent_id=sort_num[i][j][1], member_id='', sportId='',marketId='', tournamentId='', matchId='',login_account=Dl_list[pkk], begin=begin, end=end,Duplex='')
                                elif excel_report[0] in two_report_list:
                                    if excel_report[0]=="报表-球类报表-子查询（根据其球类查询盘口）":
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
            print(sport_list[1])
            print(sql_list[1])
            print(len(sport_list[1]),len(sql_list[1]))
        if mix[0]==str('2-2'):
            print(len(sql_name_list), len(sort_num[0][0][0]))
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
            print(sport_list[1])
            print(sql_list[1])
        if len(yyds01)==1:
            self.report_list_Compared01(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)
        elif len(yyds01)==2:
            self.report_list_Compared02(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)
        else:
            self.report_list_Compared03(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)

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
    bc = BetController(mysql_inf, mongo_inf)
    cc=report_data(mysql_inf, mongo_inf)

    for pkk in range(0,1):
        #参数化接口数据列表
        sport_report_list = []
        # 参数化代理账号数据列表
        Dl_list=["d0","d10","d2","d3"]
        # 参数化EXCEL路径列表
        excel = [r"C:\test\d0_comparison_report.xlsx",0]
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
        ccds=cc.reading_Excel(excel=excel, save_excel=save_excel,begin="2022-06-15",end="2022-06-21", URL=URL)


        # sport_list=[{'account': 'd0d1d2d30c/fceshi02', 'accountId': '1531519197046415362', 'companyTotal': -54.87, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -54.85, 'level0WinOrLose': -54.85, 'level1Commission': 0.0, 'level1Total': -54.85, 'level1WinOrLose': -54.85, 'level2Commission': 0.0, 'level2Total': -54.85, 'level2WinOrLose': -54.85, 'level3Commission': 0.0, 'level3Total': -54.85, 'level3WinOrLose': -54.85, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 274.27, 'memberWinOrLose': 274.27, 'name': '杜鑫test账号ac', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 190.0, 'totalCommission': 0.0, 'totalEfficientAmount': 190.0}, {'account': 'd0d1d2d30m/fceshi012', 'accountId': '1531519243502526466', 'companyTotal': -108.24, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -108.2, 'level0WinOrLose': -108.2, 'level1Commission': 0.0, 'level1Total': -108.2, 'level1WinOrLose': -108.2, 'level2Commission': 0.0, 'level2Total': -108.2, 'level2WinOrLose': -108.2, 'level3Commission': 0.0, 'level3Total': -108.2, 'level3WinOrLose': -108.2, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 541.04, 'memberWinOrLose': 541.04, 'name': '杜鑫test账号am', 'numberOfBets': 4, 'parentId': '1531517760300163074', 'totalBet': 320.0, 'totalCommission': 0.0, 'totalEfficientAmount': 320.0}, {'account': 'd0d1d2d30o/fceshi014', 'accountId': '1531519253065539586', 'companyTotal': 8.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 8.0, 'level0WinOrLose': 8.0, 'level1Commission': 0.0, 'level1Total': 8.0, 'level1WinOrLose': 8.0, 'level2Commission': 0.0, 'level2Total': 8.0, 'level2WinOrLose': 8.0, 'level3Commission': 0.0, 'level3Total': 8.0, 'level3WinOrLose': 8.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -40.0, 'memberWinOrLose': -40.0, 'name': '杜鑫test账号ao', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 40.0, 'totalCommission': 0.0, 'totalEfficientAmount': 40.0}, {'account': 'd0d1d2d30p/fceshi015', 'accountId': '1531519257226289154', 'companyTotal': -18.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -18.0, 'level0WinOrLose': -18.0, 'level1Commission': 0.0, 'level1Total': -18.0, 'level1WinOrLose': -18.0, 'level2Commission': 0.0, 'level2Total': -18.0, 'level2WinOrLose': -18.0, 'level3Commission': 0.0, 'level3Total': -18.0, 'level3WinOrLose': -18.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 90.0, 'memberWinOrLose': 90.0, 'name': '杜鑫test账号ap', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 70.0, 'totalCommission': 0.0, 'totalEfficientAmount': 30.0}, {'account': 'd0d1d2d30r/fceshi017', 'accountId': '1531519265463902210', 'companyTotal': 7.36, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 7.36, 'level0WinOrLose': 7.36, 'level1Commission': 0.0, 'level1Total': 7.36, 'level1WinOrLose': 7.36, 'level2Commission': 0.0, 'level2Total': 7.36, 'level2WinOrLose': 7.36, 'level3Commission': 0.0, 'level3Total': 7.36, 'level3WinOrLose': 7.36, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -36.8, 'memberWinOrLose': -36.8, 'name': '杜鑫test账号ar', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 50.0, 'totalCommission': 0.0, 'totalEfficientAmount': 36.8}, {'account': 'd0d1d2d30s/fceshi018', 'accountId': '1531519269557542914', 'companyTotal': 29.3, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 29.3, 'level0WinOrLose': 29.3, 'level1Commission': 0.0, 'level1Total': 29.3, 'level1WinOrLose': 29.3, 'level2Commission': 0.0, 'level2Total': 29.3, 'level2WinOrLose': 29.3, 'level3Commission': 0.0, 'level3Total': 29.3, 'level3WinOrLose': 29.3, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -146.5, 'memberWinOrLose': -146.5, 'name': '杜鑫test账号as', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 260.0, 'totalCommission': 0.0, 'totalEfficientAmount': 146.5}, {'account': 'd0d1d2d31a/fceshi026', 'accountId': '1531519302432497666', 'companyTotal': -152.15, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -152.14, 'level0WinOrLose': -152.14, 'level1Commission': 0.0, 'level1Total': -152.14, 'level1WinOrLose': -152.14, 'level2Commission': 0.0, 'level2Total': -152.14, 'level2WinOrLose': -152.14, 'level3Commission': 0.0, 'level3Total': -152.14, 'level3WinOrLose': -152.14, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 760.71, 'memberWinOrLose': 760.71, 'name': '杜鑫test账号ba', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 160.0, 'totalCommission': 0.0, 'totalEfficientAmount': 160.0}, {'account': 'd0d1d2d31c/fceshi028', 'accountId': '1531519310657527809', 'companyTotal': 30.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 30.0, 'level0WinOrLose': 30.0, 'level1Commission': 0.0, 'level1Total': 30.0, 'level1WinOrLose': 30.0, 'level2Commission': 0.0, 'level2Total': 30.0, 'level2WinOrLose': 30.0, 'level3Commission': 0.0, 'level3Total': 30.0, 'level3WinOrLose': 30.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -150.0, 'memberWinOrLose': -150.0, 'name': '杜鑫test账号bc', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 150.0, 'totalCommission': 0.0, 'totalEfficientAmount': 150.0}, {'account': 'd0d1d2d31f/fceshi031', 'accountId': '1531519323030724609', 'companyTotal': 4.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 4.0, 'level0WinOrLose': 4.0, 'level1Commission': 0.0, 'level1Total': 4.0, 'level1WinOrLose': 4.0, 'level2Commission': 0.0, 'level2Total': 4.0, 'level2WinOrLose': 4.0, 'level3Commission': 0.0, 'level3Total': 4.0, 'level3WinOrLose': 4.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -20.0, 'memberWinOrLose': -20.0, 'name': '杜鑫test账号bf', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 20.0, 'totalCommission': 0.0, 'totalEfficientAmount': 20.0}, {'account': 'd0d1d2d31o/fceshi040', 'accountId': '1531519360410361857', 'companyTotal': 12.72, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 12.74, 'level0WinOrLose': 12.74, 'level1Commission': 0.0, 'level1Total': 12.74, 'level1WinOrLose': 12.74, 'level2Commission': 0.0, 'level2Total': 12.74, 'level2WinOrLose': 12.74, 'level3Commission': 0.0, 'level3Total': 12.74, 'level3WinOrLose': 12.74, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -63.68, 'memberWinOrLose': -63.68, 'name': '杜鑫test账号bo', 'numberOfBets': 3, 'parentId': '1531517760300163074', 'totalBet': 290.0, 'totalCommission': 0.0, 'totalEfficientAmount': 146.32}, {'account': 'd0d1d2d31p/fceshi041', 'accountId': '1531519364529168386', 'companyTotal': -146.94, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -146.92, 'level0WinOrLose': -146.92, 'level1Commission': 0.0, 'level1Total': -146.92, 'level1WinOrLose': -146.92, 'level2Commission': 0.0, 'level2Total': -146.92, 'level2WinOrLose': -146.92, 'level3Commission': 0.0, 'level3Total': -146.92, 'level3WinOrLose': -146.92, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 734.62, 'memberWinOrLose': 734.62, 'name': '杜鑫test账号bp', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 60.0, 'totalCommission': 0.0, 'totalEfficientAmount': 60.0}, {'account': 'd0d1d2d31r/fceshi043', 'accountId': '1531519378554920961', 'companyTotal': 1.92, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 1.93, 'level0WinOrLose': 1.93, 'level1Commission': 0.0, 'level1Total': 1.93, 'level1WinOrLose': 1.93, 'level2Commission': 0.0, 'level2Total': 1.93, 'level2WinOrLose': 1.93, 'level3Commission': 0.0, 'level3Total': 1.93, 'level3WinOrLose': 1.93, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -9.64, 'memberWinOrLose': -9.64, 'name': '杜鑫test账号br', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 120.0, 'totalCommission': 0.0, 'totalEfficientAmount': 50.36}, {'account': 'd0d1d2d32a/fceshi044', 'accountId': '1531519635850305537', 'companyTotal': -550.86, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -550.88, 'level0WinOrLose': -550.88, 'level1Commission': 0.0, 'level1Total': -550.88, 'level1WinOrLose': -550.88, 'level2Commission': 0.0, 'level2Total': -550.88, 'level2WinOrLose': -550.88, 'level3Commission': 0.0, 'level3Total': -550.88, 'level3WinOrLose': -550.88, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 2754.38, 'memberWinOrLose': 2754.38, 'name': '杜鑫test账号ca', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 1140.0, 'totalCommission': 0.0, 'totalEfficientAmount': 1053.74}, {'account': 'd0d1d2d32i/fceshi052', 'accountId': '1531519668859478017', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号ci', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d32k/fceshi054', 'accountId': '1531519677063536642', 'companyTotal': 8.86, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 8.86, 'level0WinOrLose': 8.86, 'level1Commission': 0.0, 'level1Total': 8.86, 'level1WinOrLose': 8.86, 'level2Commission': 0.0, 'level2Total': 8.86, 'level2WinOrLose': 8.86, 'level3Commission': 0.0, 'level3Total': 8.86, 'level3WinOrLose': 8.86, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -44.3, 'memberWinOrLose': -44.3, 'name': '杜鑫test账号ck', 'numberOfBets': 3, 'parentId': '1531517760300163074', 'totalBet': 60.0, 'totalCommission': 0.0, 'totalEfficientAmount': 44.3}, {'account': 'd0d1d2d32m/fceshi056', 'accountId': '1531519685234040833', 'companyTotal': 34.7, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 34.7, 'level0WinOrLose': 34.7, 'level1Commission': 0.0, 'level1Total': 34.7, 'level1WinOrLose': 34.7, 'level2Commission': 0.0, 'level2Total': 34.7, 'level2WinOrLose': 34.7, 'level3Commission': 0.0, 'level3Total': 34.7, 'level3WinOrLose': 34.7, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -173.5, 'memberWinOrLose': -173.5, 'name': '杜鑫test账号cm', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 200.0, 'totalCommission': 0.0, 'totalEfficientAmount': 173.5}, {'account': 'd0d1d2d32p/fceshi059', 'accountId': '1531519697598849026', 'companyTotal': -136.61, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -136.57, 'level0WinOrLose': -136.57, 'level1Commission': 0.0, 'level1Total': -136.57, 'level1WinOrLose': -136.57, 'level2Commission': 0.0, 'level2Total': -136.57, 'level2WinOrLose': -136.57, 'level3Commission': 0.0, 'level3Total': -136.57, 'level3WinOrLose': -136.57, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 682.89, 'memberWinOrLose': 682.89, 'name': '杜鑫test账号cp', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 160.0, 'totalCommission': 0.0, 'totalEfficientAmount': 160.0}, {'account': 'd0d1d2d32t/fceshi063', 'accountId': '1531519714225070082', 'companyTotal': 17.88, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 17.88, 'level0WinOrLose': 17.88, 'level1Commission': 0.0, 'level1Total': 17.88, 'level1WinOrLose': 17.88, 'level2Commission': 0.0, 'level2Total': 17.88, 'level2WinOrLose': 17.88, 'level3Commission': 0.0, 'level3Total': 17.88, 'level3WinOrLose': 17.88, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -89.4, 'memberWinOrLose': -89.4, 'name': '杜鑫test账号ct', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 89.4}, {'account': 'd0d1d2d35e/fceshi0126', 'accountId': '1531520000230465537', 'companyTotal': -1.39, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -1.38, 'level0WinOrLose': -1.38, 'level1Commission': 0.0, 'level1Total': -1.38, 'level1WinOrLose': -1.38, 'level2Commission': 0.0, 'level2Total': -1.38, 'level2WinOrLose': -1.38, 'level3Commission': 0.01, 'level3Total': -1.37, 'level3WinOrLose': -1.38, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 6.9, 'memberWinOrLose': 6.9, 'name': '杜鑫test账号fe', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 6.9}, {'account': 'd0d1d2d36x/fceshi0171', 'accountId': '1531520192103096322', 'companyTotal': -19.9, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -19.9, 'level0WinOrLose': -19.9, 'level1Commission': 0.0, 'level1Total': -19.9, 'level1WinOrLose': -19.9, 'level2Commission': 0.0, 'level2Total': -19.9, 'level2WinOrLose': -19.9, 'level3Commission': 0.0, 'level3Total': -19.9, 'level3WinOrLose': -19.9, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 99.5, 'memberWinOrLose': 99.5, 'name': '杜鑫test账号gx', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3ax/fceshi0275', 'accountId': '1531520731645779969', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.01, 'level3Total': 2.01, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号ax', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3bd/fceshi0281', 'accountId': '1531520756333453313', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号bd', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3bq/fceshi0294', 'accountId': '1531520809617891329', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.01, 'level3Total': 2.01, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号bq', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3gq/fceshi0424', 'accountId': '1531521359801524225', 'companyTotal': -2.77, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -2.76, 'level0WinOrLose': -2.76, 'level1Commission': 0.0, 'level1Total': -2.76, 'level1WinOrLose': -2.76, 'level2Commission': 0.0, 'level2Total': -2.76, 'level2WinOrLose': -2.76, 'level3Commission': 0.01, 'level3Total': -2.75, 'level3WinOrLose': -2.76, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 13.8, 'memberWinOrLose': 13.8, 'name': '杜鑫test账号gq', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3gv/fceshi0429', 'accountId': '1531521380181647362', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.01, 'level3Total': 2.01, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号gv', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3ig/fceshi0466', 'accountId': '1531521538898305025', 'companyTotal': -1.65, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -1.64, 'level0WinOrLose': -1.64, 'level1Commission': 0.0, 'level1Total': -1.64, 'level1WinOrLose': -1.64, 'level2Commission': 0.0, 'level2Total': -1.64, 'level2WinOrLose': -1.64, 'level3Commission': 0.01, 'level3Total': -1.63, 'level3WinOrLose': -1.64, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 8.2, 'memberWinOrLose': 8.2, 'name': '杜鑫test账号ig', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 8.2}, {'account': 'd0d1d2d3px/fceshi0665', 'accountId': '1531522376018468866', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号px', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3tt/fceshi0765', 'accountId': '1531522809348792321', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.01, 'memberTotal': -9.99, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号tt', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.01, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d30b/fceshi01', 'accountId': '1531519190650101761', 'companyTotal': -44.11, 'currency': 'CNY', 'level0Commission': -0.1, 'level0Total': -44.1, 'level0WinOrLose': -44.0, 'level1Commission': -0.1, 'level1Total': -44.1, 'level1WinOrLose': -44.0, 'level2Commission': -0.09, 'level2Total': -44.09, 'level2WinOrLose': -44.0, 'level3Commission': 0.14, 'level3Total': -43.86, 'level3WinOrLose': -44.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.26, 'memberTotal': 220.26, 'memberWinOrLose': 220.0, 'name': '杜鑫test账号ab', 'numberOfBets': 3, 'parentId': '1531517760300163074', 'totalBet': 1020.0, 'totalCommission': 0.26, 'totalEfficientAmount': 260.0}, {'account': 'd0d1d2d32d/fceshi047', 'accountId': '1531519648210919426', 'companyTotal': 15.25, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 15.23, 'level0WinOrLose': 15.23, 'level1Commission': 0.0, 'level1Total': 15.23, 'level1WinOrLose': 15.23, 'level2Commission': 0.0, 'level2Total': 15.23, 'level2WinOrLose': 15.23, 'level3Commission': 0.0, 'level3Total': 15.23, 'level3WinOrLose': 15.23, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -76.17, 'memberWinOrLose': -76.17, 'name': '杜鑫test账号cd', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 76.17}, {'account': 'd0d1d2d32l/fceshi055', 'accountId': '1531519681106845698', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号cl', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d30g/fceshi06', 'accountId': '1531519218764521474', 'companyTotal': 6.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 6.0, 'level0WinOrLose': 6.0, 'level1Commission': 0.0, 'level1Total': 6.0, 'level1WinOrLose': 6.0, 'level2Commission': 0.0, 'level2Total': 6.0, 'level2WinOrLose': 6.0, 'level3Commission': 0.0, 'level3Total': 6.0, 'level3WinOrLose': 6.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -30.0, 'memberWinOrLose': -30.0, 'name': '杜鑫test账号ag', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 30.0, 'totalCommission': 0.0, 'totalEfficientAmount': 30.0}, {'account': 'd0d1d2d31g/fceshi032', 'accountId': '1531519327241805825', 'companyTotal': -4.22, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -4.21, 'level0WinOrLose': -4.21, 'level1Commission': 0.0, 'level1Total': -4.21, 'level1WinOrLose': -4.21, 'level2Commission': 0.0, 'level2Total': -4.21, 'level2WinOrLose': -4.21, 'level3Commission': 0.0, 'level3Total': -4.21, 'level3WinOrLose': -4.21, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 21.06, 'memberWinOrLose': 21.06, 'name': '杜鑫test账号bg', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 40.0, 'totalCommission': 0.0, 'totalEfficientAmount': 21.06}, {'account': 'd0d1d2d31j/fceshi035', 'accountId': '1531519339581448193', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号bj', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d32x/fceshi067', 'accountId': '1531519730788376577', 'companyTotal': 31.16, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 31.16, 'level0WinOrLose': 31.16, 'level1Commission': 0.0, 'level1Total': 31.16, 'level1WinOrLose': 31.16, 'level2Commission': 0.0, 'level2Total': 31.16, 'level2WinOrLose': 31.16, 'level3Commission': 0.0, 'level3Total': 31.16, 'level3WinOrLose': 31.16, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -155.8, 'memberWinOrLose': -155.8, 'name': '杜鑫test账号cx', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 320.0, 'totalCommission': 0.0, 'totalEfficientAmount': 203.2}, {'account': 'd0d1d2d32z/fceshi069', 'accountId': '1531519738950492161', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号cz', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d33b/fceshi071', 'accountId': '1531519747196493826', 'companyTotal': 0.31, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 0.27, 'level0WinOrLose': 0.27, 'level1Commission': 0.0, 'level1Total': 0.27, 'level1WinOrLose': 0.27, 'level2Commission': 0.0, 'level2Total': 0.27, 'level2WinOrLose': 0.27, 'level3Commission': 0.0, 'level3Total': 0.27, 'level3WinOrLose': 0.27, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -1.39, 'memberWinOrLose': -1.39, 'name': '杜鑫test账号db', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 100.0, 'totalCommission': 0.0, 'totalEfficientAmount': 1.39}, {'account': 'd0d1d2d3kp/fceshi0527', 'accountId': '1531521794973147137', 'companyTotal': -4.6, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -4.6, 'level0WinOrLose': -4.6, 'level1Commission': 0.0, 'level1Total': -4.6, 'level1WinOrLose': -4.6, 'level2Commission': 0.0, 'level2Total': -4.6, 'level2WinOrLose': -4.6, 'level3Commission': 0.0, 'level3Total': -4.6, 'level3WinOrLose': -4.6, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 23.0, 'memberWinOrLose': 23.0, 'name': '杜鑫test账号kp', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3pd/fceshi0645', 'accountId': '1531522293508120578', 'companyTotal': 0.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 0.0, 'level0WinOrLose': 0.0, 'level1Commission': 0.0, 'level1Total': 0.0, 'level1WinOrLose': 0.0, 'level2Commission': 0.0, 'level2Total': 0.0, 'level2WinOrLose': 0.0, 'level3Commission': 0.0, 'level3Total': 0.0, 'level3WinOrLose': 0.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 0.0, 'memberWinOrLose': 0.0, 'name': '杜鑫test账号pd', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 0.0}, {'account': 'd0d1d2d30i/fceshi08', 'accountId': '1531519226964385794', 'companyTotal': 14.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 14.0, 'level0WinOrLose': 14.0, 'level1Commission': 0.0, 'level1Total': 14.0, 'level1WinOrLose': 14.0, 'level2Commission': 0.0, 'level2Total': 14.0, 'level2WinOrLose': 14.0, 'level3Commission': 0.0, 'level3Total': 14.0, 'level3WinOrLose': 14.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -70.0, 'memberWinOrLose': -70.0, 'name': '杜鑫test账号ai', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 70.0}, {'account': 'd0d1d2d30q/fceshi016', 'accountId': '1531519261340901378', 'companyTotal': 28.13, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 28.13, 'level0WinOrLose': 28.13, 'level1Commission': 0.0, 'level1Total': 28.13, 'level1WinOrLose': 28.13, 'level2Commission': 0.0, 'level2Total': 28.13, 'level2WinOrLose': 28.13, 'level3Commission': 0.0, 'level3Total': 28.13, 'level3WinOrLose': 28.13, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -140.65, 'memberWinOrLose': -140.65, 'name': '杜鑫test账号aq', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 150.0, 'totalCommission': 0.0, 'totalEfficientAmount': 140.65}, {'account': 'd0d1d2d31q/fceshi042', 'accountId': '1531519368656363522', 'companyTotal': 7.1, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 7.1, 'level0WinOrLose': 7.1, 'level1Commission': 0.0, 'level1Total': 7.1, 'level1WinOrLose': 7.1, 'level2Commission': 0.0, 'level2Total': 7.1, 'level2WinOrLose': 7.1, 'level3Commission': 0.0, 'level3Total': 7.1, 'level3WinOrLose': 7.1, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -35.5, 'memberWinOrLose': -35.5, 'name': '杜鑫test账号bq', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 70.0, 'totalCommission': 0.0, 'totalEfficientAmount': 44.5}, {'account': 'd0d1d2d32e/fceshi048', 'accountId': '1531519652338114562', 'companyTotal': 12.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 12.0, 'level0WinOrLose': 12.0, 'level1Commission': 0.0, 'level1Total': 12.0, 'level1WinOrLose': 12.0, 'level2Commission': 0.0, 'level2Total': 12.0, 'level2WinOrLose': 12.0, 'level3Commission': 0.0, 'level3Total': 12.0, 'level3WinOrLose': 12.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -60.0, 'memberWinOrLose': -60.0, 'name': '杜鑫test账号ce', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 60.0, 'totalCommission': 0.0, 'totalEfficientAmount': 60.0}, {'account': 'd0d1d2d32g/fceshi050', 'accountId': '1531519660558950401', 'companyTotal': 15.74, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 15.74, 'level0WinOrLose': 15.74, 'level1Commission': 0.0, 'level1Total': 15.74, 'level1WinOrLose': 15.74, 'level2Commission': 0.0, 'level2Total': 15.74, 'level2WinOrLose': 15.74, 'level3Commission': 0.0, 'level3Total': 15.74, 'level3WinOrLose': 15.74, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -78.7, 'memberWinOrLose': -78.7, 'name': '杜鑫test账号cg', 'numberOfBets': 2, 'parentId': '1531517760300163074', 'totalBet': 100.0, 'totalCommission': 0.0, 'totalEfficientAmount': 78.7}, {'account': 'd0d1d2d32v/fceshi065', 'accountId': '1531519722500431873', 'companyTotal': 20.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 20.0, 'level0WinOrLose': 20.0, 'level1Commission': 0.0, 'level1Total': 20.0, 'level1WinOrLose': 20.0, 'level2Commission': 0.0, 'level2Total': 20.0, 'level2WinOrLose': 20.0, 'level3Commission': 0.0, 'level3Total': 20.0, 'level3WinOrLose': 20.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -100.0, 'memberWinOrLose': -100.0, 'name': '杜鑫test账号cv', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 100.0}, {'account': 'd0d1d2d33a/fceshi070', 'accountId': '1531519743081881601', 'companyTotal': -2.26, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -2.26, 'level0WinOrLose': -2.26, 'level1Commission': 0.0, 'level1Total': -2.26, 'level1WinOrLose': -2.26, 'level2Commission': 0.0, 'level2Total': -2.26, 'level2WinOrLose': -2.26, 'level3Commission': 0.0, 'level3Total': -2.26, 'level3WinOrLose': -2.26, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 11.3, 'memberWinOrLose': 11.3, 'name': '杜鑫test账号da', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3qt/fceshi0687', 'accountId': '1531522468255408130', 'companyTotal': -4.2, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -4.2, 'level0WinOrLose': -4.2, 'level1Commission': 0.0, 'level1Total': -4.2, 'level1WinOrLose': -4.2, 'level2Commission': 0.0, 'level2Total': -4.2, 'level2WinOrLose': -4.2, 'level3Commission': 0.0, 'level3Total': -4.2, 'level3WinOrLose': -4.2, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 21.0, 'memberWinOrLose': 21.0, 'name': '杜鑫test账号qt', 'numberOfBets': 1, 'parentId': '1531517760300163074', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}]
        # sql_list=[{'account': 'd0d1d2d30b/fceshi01', 'accountId': '1531519190650101761', 'companyTotal': -44.11, 'currency': 'CNY', 'level0Commission': -0.1, 'level0Total': -44.1, 'level0WinOrLose': -44.0, 'level1Commission': -0.1, 'level1Total': -44.1, 'level1WinOrLose': -44.0, 'level2Commission': -0.09, 'level2Total': -44.09, 'level2WinOrLose': -44.0, 'level3Commission': 0.14, 'level3Total': -43.86, 'level3WinOrLose': -44.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.26, 'memberTotal': 220.26, 'memberWinOrLose': 220.0, 'name': '杜鑫test账号ab', 'numberOfBets': 3, 'parentId': '1531517351158390786', 'totalBet': 1020.0, 'totalCommission': 0.26, 'totalEfficientAmount': 260.0}, {'account': 'd0d1d2d30m/fceshi012', 'accountId': '1531519243502526466', 'companyTotal': -108.24, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -108.2, 'level0WinOrLose': -108.2, 'level1Commission': 0.0, 'level1Total': -108.2, 'level1WinOrLose': -108.2, 'level2Commission': 0.0, 'level2Total': -108.2, 'level2WinOrLose': -108.2, 'level3Commission': 0.0, 'level3Total': -108.2, 'level3WinOrLose': -108.2, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 541.04, 'memberWinOrLose': 541.04, 'name': '杜鑫test账号am', 'numberOfBets': 4, 'parentId': '1531517351158390786', 'totalBet': 320.0, 'totalCommission': 0.0, 'totalEfficientAmount': 320.0}, {'account': 'd0d1d2d35e/fceshi0126', 'accountId': '1531520000230465537', 'companyTotal': -1.39, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -1.38, 'level0WinOrLose': -1.38, 'level1Commission': 0.0, 'level1Total': -1.38, 'level1WinOrLose': -1.38, 'level2Commission': 0.0, 'level2Total': -1.38, 'level2WinOrLose': -1.38, 'level3Commission': 0.01, 'level3Total': -1.37, 'level3WinOrLose': -1.38, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 6.9, 'memberWinOrLose': 6.9, 'name': '杜鑫test账号fe', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 6.9}, {'account': 'd0d1d2d30o/fceshi014', 'accountId': '1531519253065539586', 'companyTotal': 8.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 8.0, 'level0WinOrLose': 8.0, 'level1Commission': 0.0, 'level1Total': 8.0, 'level1WinOrLose': 8.0, 'level2Commission': 0.0, 'level2Total': 8.0, 'level2WinOrLose': 8.0, 'level3Commission': 0.0, 'level3Total': 8.0, 'level3WinOrLose': 8.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -40.0, 'memberWinOrLose': -40.0, 'name': '杜鑫test账号ao', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 40.0, 'totalCommission': 0.0, 'totalEfficientAmount': 40.0}, {'account': 'd0d1d2d30p/fceshi015', 'accountId': '1531519257226289154', 'companyTotal': -18.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -18.0, 'level0WinOrLose': -18.0, 'level1Commission': 0.0, 'level1Total': -18.0, 'level1WinOrLose': -18.0, 'level2Commission': 0.0, 'level2Total': -18.0, 'level2WinOrLose': -18.0, 'level3Commission': 0.0, 'level3Total': -18.0, 'level3WinOrLose': -18.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 90.0, 'memberWinOrLose': 90.0, 'name': '杜鑫test账号ap', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 70.0, 'totalCommission': 0.0, 'totalEfficientAmount': 30.0}, {'account': 'd0d1d2d30q/fceshi016', 'accountId': '1531519261340901378', 'companyTotal': 28.13, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 28.13, 'level0WinOrLose': 28.13, 'level1Commission': 0.0, 'level1Total': 28.13, 'level1WinOrLose': 28.13, 'level2Commission': 0.0, 'level2Total': 28.13, 'level2WinOrLose': 28.13, 'level3Commission': 0.0, 'level3Total': 28.13, 'level3WinOrLose': 28.13, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -140.65, 'memberWinOrLose': -140.65, 'name': '杜鑫test账号aq', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 150.0, 'totalCommission': 0.0, 'totalEfficientAmount': 140.65}, {'account': 'd0d1d2d30r/fceshi017', 'accountId': '1531519265463902210', 'companyTotal': 7.36, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 7.36, 'level0WinOrLose': 7.36, 'level1Commission': 0.0, 'level1Total': 7.36, 'level1WinOrLose': 7.36, 'level2Commission': 0.0, 'level2Total': 7.36, 'level2WinOrLose': 7.36, 'level3Commission': 0.0, 'level3Total': 7.36, 'level3WinOrLose': 7.36, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -36.8, 'memberWinOrLose': -36.8, 'name': '杜鑫test账号ar', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 50.0, 'totalCommission': 0.0, 'totalEfficientAmount': 36.8}, {'account': 'd0d1d2d36x/fceshi0171', 'accountId': '1531520192103096322', 'companyTotal': -19.9, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -19.9, 'level0WinOrLose': -19.9, 'level1Commission': 0.0, 'level1Total': -19.9, 'level1WinOrLose': -19.9, 'level2Commission': 0.0, 'level2Total': -19.9, 'level2WinOrLose': -19.9, 'level3Commission': 0.0, 'level3Total': -19.9, 'level3WinOrLose': -19.9, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 99.5, 'memberWinOrLose': 99.5, 'name': '杜鑫test账号gx', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d30s/fceshi018', 'accountId': '1531519269557542914', 'companyTotal': 29.3, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 29.3, 'level0WinOrLose': 29.3, 'level1Commission': 0.0, 'level1Total': 29.3, 'level1WinOrLose': 29.3, 'level2Commission': 0.0, 'level2Total': 29.3, 'level2WinOrLose': 29.3, 'level3Commission': 0.0, 'level3Total': 29.3, 'level3WinOrLose': 29.3, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -146.5, 'memberWinOrLose': -146.5, 'name': '杜鑫test账号as', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 260.0, 'totalCommission': 0.0, 'totalEfficientAmount': 146.5}, {'account': 'd0d1d2d30c/fceshi02', 'accountId': '1531519197046415362', 'companyTotal': -54.87, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -54.85, 'level0WinOrLose': -54.85, 'level1Commission': 0.0, 'level1Total': -54.85, 'level1WinOrLose': -54.85, 'level2Commission': 0.0, 'level2Total': -54.85, 'level2WinOrLose': -54.85, 'level3Commission': 0.0, 'level3Total': -54.85, 'level3WinOrLose': -54.85, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 274.27, 'memberWinOrLose': 274.27, 'name': '杜鑫test账号ac', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 190.0, 'totalCommission': 0.0, 'totalEfficientAmount': 190.0}, {'account': 'd0d1d2d31a/fceshi026', 'accountId': '1531519302432497666', 'companyTotal': -152.15, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -152.14, 'level0WinOrLose': -152.14, 'level1Commission': 0.0, 'level1Total': -152.14, 'level1WinOrLose': -152.14, 'level2Commission': 0.0, 'level2Total': -152.14, 'level2WinOrLose': -152.14, 'level3Commission': 0.0, 'level3Total': -152.14, 'level3WinOrLose': -152.14, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 760.71, 'memberWinOrLose': 760.71, 'name': '杜鑫test账号ba', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 160.0, 'totalCommission': 0.0, 'totalEfficientAmount': 160.0}, {'account': 'd0d1d2d3ax/fceshi0275', 'accountId': '1531520731645779969', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.01, 'level3Total': 2.01, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号ax', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d31c/fceshi028', 'accountId': '1531519310657527809', 'companyTotal': 30.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 30.0, 'level0WinOrLose': 30.0, 'level1Commission': 0.0, 'level1Total': 30.0, 'level1WinOrLose': 30.0, 'level2Commission': 0.0, 'level2Total': 30.0, 'level2WinOrLose': 30.0, 'level3Commission': 0.0, 'level3Total': 30.0, 'level3WinOrLose': 30.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -150.0, 'memberWinOrLose': -150.0, 'name': '杜鑫test账号bc', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 150.0, 'totalCommission': 0.0, 'totalEfficientAmount': 150.0}, {'account': 'd0d1d2d3bd/fceshi0281', 'accountId': '1531520756333453313', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号bd', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3bq/fceshi0294', 'accountId': '1531520809617891329', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.01, 'level3Total': 2.01, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号bq', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d31f/fceshi031', 'accountId': '1531519323030724609', 'companyTotal': 4.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 4.0, 'level0WinOrLose': 4.0, 'level1Commission': 0.0, 'level1Total': 4.0, 'level1WinOrLose': 4.0, 'level2Commission': 0.0, 'level2Total': 4.0, 'level2WinOrLose': 4.0, 'level3Commission': 0.0, 'level3Total': 4.0, 'level3WinOrLose': 4.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -20.0, 'memberWinOrLose': -20.0, 'name': '杜鑫test账号bf', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 20.0, 'totalCommission': 0.0, 'totalEfficientAmount': 20.0}, {'account': 'd0d1d2d31g/fceshi032', 'accountId': '1531519327241805825', 'companyTotal': -4.22, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -4.21, 'level0WinOrLose': -4.21, 'level1Commission': 0.0, 'level1Total': -4.21, 'level1WinOrLose': -4.21, 'level2Commission': 0.0, 'level2Total': -4.21, 'level2WinOrLose': -4.21, 'level3Commission': 0.0, 'level3Total': -4.21, 'level3WinOrLose': -4.21, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 21.06, 'memberWinOrLose': 21.06, 'name': '杜鑫test账号bg', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 40.0, 'totalCommission': 0.0, 'totalEfficientAmount': 21.06}, {'account': 'd0d1d2d31j/fceshi035', 'accountId': '1531519339581448193', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号bj', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d31o/fceshi040', 'accountId': '1531519360410361857', 'companyTotal': 12.72, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 12.74, 'level0WinOrLose': 12.74, 'level1Commission': 0.0, 'level1Total': 12.74, 'level1WinOrLose': 12.74, 'level2Commission': 0.0, 'level2Total': 12.74, 'level2WinOrLose': 12.74, 'level3Commission': 0.0, 'level3Total': 12.74, 'level3WinOrLose': 12.74, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -63.68, 'memberWinOrLose': -63.68, 'name': '杜鑫test账号bo', 'numberOfBets': 3, 'parentId': '1531517351158390786', 'totalBet': 290.0, 'totalCommission': 0.0, 'totalEfficientAmount': 146.32}, {'account': 'd0d1d2d31p/fceshi041', 'accountId': '1531519364529168386', 'companyTotal': -146.94, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -146.92, 'level0WinOrLose': -146.92, 'level1Commission': 0.0, 'level1Total': -146.92, 'level1WinOrLose': -146.92, 'level2Commission': 0.0, 'level2Total': -146.92, 'level2WinOrLose': -146.92, 'level3Commission': 0.0, 'level3Total': -146.92, 'level3WinOrLose': -146.92, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 734.62, 'memberWinOrLose': 734.62, 'name': '杜鑫test账号bp', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 60.0, 'totalCommission': 0.0, 'totalEfficientAmount': 60.0}, {'account': 'd0d1d2d31q/fceshi042', 'accountId': '1531519368656363522', 'companyTotal': 7.1, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 7.1, 'level0WinOrLose': 7.1, 'level1Commission': 0.0, 'level1Total': 7.1, 'level1WinOrLose': 7.1, 'level2Commission': 0.0, 'level2Total': 7.1, 'level2WinOrLose': 7.1, 'level3Commission': 0.0, 'level3Total': 7.1, 'level3WinOrLose': 7.1, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -35.5, 'memberWinOrLose': -35.5, 'name': '杜鑫test账号bq', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 70.0, 'totalCommission': 0.0, 'totalEfficientAmount': 44.5}, {'account': 'd0d1d2d3gq/fceshi0424', 'accountId': '1531521359801524225', 'companyTotal': -2.77, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -2.76, 'level0WinOrLose': -2.76, 'level1Commission': 0.0, 'level1Total': -2.76, 'level1WinOrLose': -2.76, 'level2Commission': 0.0, 'level2Total': -2.76, 'level2WinOrLose': -2.76, 'level3Commission': 0.01, 'level3Total': -2.75, 'level3WinOrLose': -2.76, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 13.8, 'memberWinOrLose': 13.8, 'name': '杜鑫test账号gq', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3gv/fceshi0429', 'accountId': '1531521380181647362', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.01, 'level3Total': 2.01, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号gv', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d31r/fceshi043', 'accountId': '1531519378554920961', 'companyTotal': 1.92, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 1.93, 'level0WinOrLose': 1.93, 'level1Commission': 0.0, 'level1Total': 1.93, 'level1WinOrLose': 1.93, 'level2Commission': 0.0, 'level2Total': 1.93, 'level2WinOrLose': 1.93, 'level3Commission': 0.0, 'level3Total': 1.93, 'level3WinOrLose': 1.93, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -9.64, 'memberWinOrLose': -9.64, 'name': '杜鑫test账号br', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 120.0, 'totalCommission': 0.0, 'totalEfficientAmount': 50.36}, {'account': 'd0d1d2d32a/fceshi044', 'accountId': '1531519635850305537', 'companyTotal': -550.86, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -550.88, 'level0WinOrLose': -550.88, 'level1Commission': 0.0, 'level1Total': -550.88, 'level1WinOrLose': -550.88, 'level2Commission': 0.0, 'level2Total': -550.88, 'level2WinOrLose': -550.88, 'level3Commission': 0.0, 'level3Total': -550.88, 'level3WinOrLose': -550.88, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 2754.38, 'memberWinOrLose': 2754.38, 'name': '杜鑫test账号ca', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 1140.0, 'totalCommission': 0.0, 'totalEfficientAmount': 1053.74}, {'account': 'd0d1d2d3ig/fceshi0466', 'accountId': '1531521538898305025', 'companyTotal': -1.65, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -1.64, 'level0WinOrLose': -1.64, 'level1Commission': 0.0, 'level1Total': -1.64, 'level1WinOrLose': -1.64, 'level2Commission': 0.0, 'level2Total': -1.64, 'level2WinOrLose': -1.64, 'level3Commission': 0.01, 'level3Total': -1.63, 'level3WinOrLose': -1.64, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 8.2, 'memberWinOrLose': 8.2, 'name': '杜鑫test账号ig', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 8.2}, {'account': 'd0d1d2d32d/fceshi047', 'accountId': '1531519648210919426', 'companyTotal': 15.25, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 15.23, 'level0WinOrLose': 15.23, 'level1Commission': 0.0, 'level1Total': 15.23, 'level1WinOrLose': 15.23, 'level2Commission': 0.0, 'level2Total': 15.23, 'level2WinOrLose': 15.23, 'level3Commission': 0.0, 'level3Total': 15.23, 'level3WinOrLose': 15.23, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -76.17, 'memberWinOrLose': -76.17, 'name': '杜鑫test账号cd', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 76.17}, {'account': 'd0d1d2d32e/fceshi048', 'accountId': '1531519652338114562', 'companyTotal': 12.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 12.0, 'level0WinOrLose': 12.0, 'level1Commission': 0.0, 'level1Total': 12.0, 'level1WinOrLose': 12.0, 'level2Commission': 0.0, 'level2Total': 12.0, 'level2WinOrLose': 12.0, 'level3Commission': 0.0, 'level3Total': 12.0, 'level3WinOrLose': 12.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -60.0, 'memberWinOrLose': -60.0, 'name': '杜鑫test账号ce', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 60.0, 'totalCommission': 0.0, 'totalEfficientAmount': 60.0}, {'account': 'd0d1d2d32g/fceshi050', 'accountId': '1531519660558950401', 'companyTotal': 15.74, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 15.74, 'level0WinOrLose': 15.74, 'level1Commission': 0.0, 'level1Total': 15.74, 'level1WinOrLose': 15.74, 'level2Commission': 0.0, 'level2Total': 15.74, 'level2WinOrLose': 15.74, 'level3Commission': 0.0, 'level3Total': 15.74, 'level3WinOrLose': 15.74, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -78.7, 'memberWinOrLose': -78.7, 'name': '杜鑫test账号cg', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 100.0, 'totalCommission': 0.0, 'totalEfficientAmount': 78.7}, {'account': 'd0d1d2d32i/fceshi052', 'accountId': '1531519668859478017', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号ci', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d3kp/fceshi0527', 'accountId': '1531521794973147137', 'companyTotal': -4.6, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -4.6, 'level0WinOrLose': -4.6, 'level1Commission': 0.0, 'level1Total': -4.6, 'level1WinOrLose': -4.6, 'level2Commission': 0.0, 'level2Total': -4.6, 'level2WinOrLose': -4.6, 'level3Commission': 0.0, 'level3Total': -4.6, 'level3WinOrLose': -4.6, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 23.0, 'memberWinOrLose': 23.0, 'name': '杜鑫test账号kp', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d32k/fceshi054', 'accountId': '1531519677063536642', 'companyTotal': 8.86, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 8.86, 'level0WinOrLose': 8.86, 'level1Commission': 0.0, 'level1Total': 8.86, 'level1WinOrLose': 8.86, 'level2Commission': 0.0, 'level2Total': 8.86, 'level2WinOrLose': 8.86, 'level3Commission': 0.0, 'level3Total': 8.86, 'level3WinOrLose': 8.86, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -44.3, 'memberWinOrLose': -44.3, 'name': '杜鑫test账号ck', 'numberOfBets': 3, 'parentId': '1531517351158390786', 'totalBet': 60.0, 'totalCommission': 0.0, 'totalEfficientAmount': 44.3}, {'account': 'd0d1d2d32l/fceshi055', 'accountId': '1531519681106845698', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号cl', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d32m/fceshi056', 'accountId': '1531519685234040833', 'companyTotal': 34.7, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 34.7, 'level0WinOrLose': 34.7, 'level1Commission': 0.0, 'level1Total': 34.7, 'level1WinOrLose': 34.7, 'level2Commission': 0.0, 'level2Total': 34.7, 'level2WinOrLose': 34.7, 'level3Commission': 0.0, 'level3Total': 34.7, 'level3WinOrLose': 34.7, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -173.5, 'memberWinOrLose': -173.5, 'name': '杜鑫test账号cm', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 200.0, 'totalCommission': 0.0, 'totalEfficientAmount': 173.5}, {'account': 'd0d1d2d32p/fceshi059', 'accountId': '1531519697598849026', 'companyTotal': -136.61, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -136.57, 'level0WinOrLose': -136.57, 'level1Commission': 0.0, 'level1Total': -136.57, 'level1WinOrLose': -136.57, 'level2Commission': 0.0, 'level2Total': -136.57, 'level2WinOrLose': -136.57, 'level3Commission': 0.0, 'level3Total': -136.57, 'level3WinOrLose': -136.57, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 682.89, 'memberWinOrLose': 682.89, 'name': '杜鑫test账号cp', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 160.0, 'totalCommission': 0.0, 'totalEfficientAmount': 160.0}, {'account': 'd0d1d2d30g/fceshi06', 'accountId': '1531519218764521474', 'companyTotal': 6.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 6.0, 'level0WinOrLose': 6.0, 'level1Commission': 0.0, 'level1Total': 6.0, 'level1WinOrLose': 6.0, 'level2Commission': 0.0, 'level2Total': 6.0, 'level2WinOrLose': 6.0, 'level3Commission': 0.0, 'level3Total': 6.0, 'level3WinOrLose': 6.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -30.0, 'memberWinOrLose': -30.0, 'name': '杜鑫test账号ag', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 30.0, 'totalCommission': 0.0, 'totalEfficientAmount': 30.0}, {'account': 'd0d1d2d32t/fceshi063', 'accountId': '1531519714225070082', 'companyTotal': 17.88, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 17.88, 'level0WinOrLose': 17.88, 'level1Commission': 0.0, 'level1Total': 17.88, 'level1WinOrLose': 17.88, 'level2Commission': 0.0, 'level2Total': 17.88, 'level2WinOrLose': 17.88, 'level3Commission': 0.0, 'level3Total': 17.88, 'level3WinOrLose': 17.88, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -89.4, 'memberWinOrLose': -89.4, 'name': '杜鑫test账号ct', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 89.4}, {'account': 'd0d1d2d3pd/fceshi0645', 'accountId': '1531522293508120578', 'companyTotal': 0.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 0.0, 'level0WinOrLose': 0.0, 'level1Commission': 0.0, 'level1Total': 0.0, 'level1WinOrLose': 0.0, 'level2Commission': 0.0, 'level2Total': 0.0, 'level2WinOrLose': 0.0, 'level3Commission': 0.0, 'level3Total': 0.0, 'level3WinOrLose': 0.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 0.0, 'memberWinOrLose': 0.0, 'name': '杜鑫test账号pd', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 0.0}, {'account': 'd0d1d2d32v/fceshi065', 'accountId': '1531519722500431873', 'companyTotal': 20.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 20.0, 'level0WinOrLose': 20.0, 'level1Commission': 0.0, 'level1Total': 20.0, 'level1WinOrLose': 20.0, 'level2Commission': 0.0, 'level2Total': 20.0, 'level2WinOrLose': 20.0, 'level3Commission': 0.0, 'level3Total': 20.0, 'level3WinOrLose': 20.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -100.0, 'memberWinOrLose': -100.0, 'name': '杜鑫test账号cv', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 100.0}, {'account': 'd0d1d2d3px/fceshi0665', 'accountId': '1531522376018468866', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号px', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d32x/fceshi067', 'accountId': '1531519730788376577', 'companyTotal': 31.16, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 31.16, 'level0WinOrLose': 31.16, 'level1Commission': 0.0, 'level1Total': 31.16, 'level1WinOrLose': 31.16, 'level2Commission': 0.0, 'level2Total': 31.16, 'level2WinOrLose': 31.16, 'level3Commission': 0.0, 'level3Total': 31.16, 'level3WinOrLose': 31.16, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -155.8, 'memberWinOrLose': -155.8, 'name': '杜鑫test账号cx', 'numberOfBets': 2, 'parentId': '1531517351158390786', 'totalBet': 320.0, 'totalCommission': 0.0, 'totalEfficientAmount': 203.2}, {'account': 'd0d1d2d3qt/fceshi0687', 'accountId': '1531522468255408130', 'companyTotal': -4.2, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -4.2, 'level0WinOrLose': -4.2, 'level1Commission': 0.0, 'level1Total': -4.2, 'level1WinOrLose': -4.2, 'level2Commission': 0.0, 'level2Total': -4.2, 'level2WinOrLose': -4.2, 'level3Commission': 0.0, 'level3Total': -4.2, 'level3WinOrLose': -4.2, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 21.0, 'memberWinOrLose': 21.0, 'name': '杜鑫test账号qt', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d32z/fceshi069', 'accountId': '1531519738950492161', 'companyTotal': 2.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号cz', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d33a/fceshi070', 'accountId': '1531519743081881601', 'companyTotal': -2.26, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': -2.26, 'level0WinOrLose': -2.26, 'level1Commission': 0.0, 'level1Total': -2.26, 'level1WinOrLose': -2.26, 'level2Commission': 0.0, 'level2Total': -2.26, 'level2WinOrLose': -2.26, 'level3Commission': 0.0, 'level3Total': -2.26, 'level3WinOrLose': -2.26, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': 11.3, 'memberWinOrLose': 11.3, 'name': '杜鑫test账号da', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.0, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d33b/fceshi071', 'accountId': '1531519747196493826', 'companyTotal': 0.31, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 0.27, 'level0WinOrLose': 0.27, 'level1Commission': 0.0, 'level1Total': 0.27, 'level1WinOrLose': 0.27, 'level2Commission': 0.0, 'level2Total': 0.27, 'level2WinOrLose': 0.27, 'level3Commission': 0.0, 'level3Total': 0.27, 'level3WinOrLose': 0.27, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -1.39, 'memberWinOrLose': -1.39, 'name': '杜鑫test账号db', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 100.0, 'totalCommission': 0.0, 'totalEfficientAmount': 1.39}, {'account': 'd0d1d2d3tt/fceshi0765', 'accountId': '1531522809348792321', 'companyTotal': 1.99, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.01, 'memberTotal': -9.99, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号tt', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 10.0, 'totalCommission': 0.01, 'totalEfficientAmount': 10.0}, {'account': 'd0d1d2d30i/fceshi08', 'accountId': '1531519226964385794', 'companyTotal': 14.0, 'currency': 'CNY', 'level0Commission': 0.0, 'level0Total': 14.0, 'level0WinOrLose': 14.0, 'level1Commission': 0.0, 'level1Total': 14.0, 'level1WinOrLose': 14.0, 'level2Commission': 0.0, 'level2Total': 14.0, 'level2WinOrLose': 14.0, 'level3Commission': 0.0, 'level3Total': 14.0, 'level3WinOrLose': 14.0, 'levelId': 4, 'levelName': '会员', 'memberCommission': 0.0, 'memberTotal': -70.0, 'memberWinOrLose': -70.0, 'name': '杜鑫test账号ai', 'numberOfBets': 1, 'parentId': '1531517351158390786', 'totalBet': 110.0, 'totalCommission': 0.0, 'totalEfficientAmount': 70.0}]
        # Compared="account,parentId"
        # excel_report=['盈亏详情-登0-登3-会员-子查询', '/agentBackground/profitAndLoss/queryProxyProfitAndLossList', 'companyCommission,companyWinOrLose,id,payout,settlementDate,updateTime', 1, "{\n        'Content-Type': 'application/json;charset=UTF-8',\n        'LoginDiv': '555666',\n        'Account_Login_Identify': token\n    }", '[{"page":1,"limit":50,"account":"","parentId":"1531517760300163074","startTime":begin,"endTime":end}]', None, 'post', '@f"SELECT CONCAT(c.user_name,\'/\',c.login_account) AS \'账号/登入账号\',c.user_id \'下级代理ID\',\'公司总计\' AS \'公司总计\',c.currency \'货币\',SUM(c.level0_backwater_amount) \'总代佣金\',SUM(c.level0_win_or_lose) \'总代总计\',(SUM(c.level0_win_or_lose)-SUM(c.level0_backwater_amount)) \'总代输/赢\',SUM(c.level1_backwater_amount) \'一级代理佣金\',SUM(c.level1_win_or_lose) \'一级代理总计\',(SUM(c.level1_win_or_lose)-SUM(c.level1_backwater_amount)) \'一级代理输/赢\',SUM(c.level2_backwater_amount) \'二级代理佣金\',SUM(c.level2_win_or_lose) \'二级代理总计\',(SUM(c.level2_win_or_lose)-SUM(c.level2_backwater_amount)) \'二级代理输/赢\',SUM(c.level3_backwater_amount) \'三级代理佣金\',SUM(c.level3_win_or_lose) \'三级代理总计\',(SUM(c.level3_win_or_lose)-SUM(c.level3_backwater_amount)) \'三级代理输/赢\',a.role_id \'代理角色ID\',\'会员\' AS \'代理级别\',SUM(c.backwater_amount) \'会员佣金\',(SUM(c.handicap_win_or_lose)+SUM(c.backwater_amount)) \'会员总计\',SUM(c.handicap_win_or_lose) \'会员输/赢\',b.NAME \'名称\',COUNT(c.order_no) \'注单数量\',a.parent_id \'本级代理ID\',SUM(c.bet_amount)as \'总投注额\',\'总佣金\' as \'总佣金\',SUM(c.efficient_amount)as \'总有效金额\' FROM o_account_order as c left join u_user as b ON b.id=c.user_id LEFT JOIN m_account as a ON a.id=c.proxy3_id WHERE c.STATUS=2 AND c.proxy3_id=1531517760300163074 AND c.award_time IS NOT NULL AND c.settlement_time>=\'{begin}\' AND c.settlement_time<=\'{end}\' GROUP BY c.user_name,c.login_account,a.role_id,b.currency,c.user_id,c.currency ORDER BY c.login_account ASC"', 'account,parentId']
        # print(len(sport_list),len(sql_list))
        # yy=bc.report_list_Compared02(sport_list=sport_list,sql_list=sql_list, Compared=Compared,excel_report=excel_report)

