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

from Computational_N_N import SQL_report_ods,betting_odds





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
                # for i in range(4, rows+1):
                for i in range(4, rows+1):
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
                        worksheet.cell(i,int(columns)-2,("测试通过"+"\n"+now))
                        worksheet.cell(i, int(columns) - 1, "")
                        worksheet.cell(i, int(columns), "")
                    else:
                        Failed=Failed+1
                        worksheet.cell(i, int(columns)-2, ("测试不通过"+"\n"+now))
                        worksheet.cell(i, int(columns)-1, str(sport_error))
                        worksheet.cell(i, int(columns), str(sport_all_error))
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
        # print(yyds)

        str_sum=excel_report[2]
        sport_report_list=[]

        for i in range(0,len(yyds)):
            if excel_report[2] != None:
                ppxt_lsit = str_sum.split(",")
                for j in ppxt_lsit:
                    # print(j)
                    del yyds[i][j]
            sport_report_list.append(yyds[i])


        sport_report_dict = []
        for key,value in yyds[0].items():
            sport_report_dict.append(key)
        # print(sport_report_dict)

        time_list=[" 00:00:00"," 23:59:59"]
        self.tt.sport_report_sql(begin=begin+time_list[0], end=end+time_list[1],excel_report=excel_report,sport_report_dict=sport_report_dict,sport_report_list=sport_report_list)
        return sport_report_dict


    def sport_report02(self,URL, token, excel_report, begin, end):
        global sportId_list,sportId_yyds_lsit

        sportId_list = []
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

                for i in yyds:
                    if i[excel_report[6]]=='串关':
                        pass
                    else:
                        sportId_list.append(i[excel_report[6]])
                print(sportId_list)
            else:
                url = str(URL) + url
                sportId_yyds_lsit=[]
                for sportId in sportId_list:
                    data = eval(excel_report[5])[1]
                    if excel_report[0]=="未完成交易-登0-登3-会员-查看订单详情-子查询":
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
                        if excel_report[0]=="未完成交易-登0-登3-会员-查看订单详情-子查询":

                            # print(results)
                            # print(results['data']['data'])
                            # print(results['data']['totalData'])
                            # print(results['data']['totalData']['betAmount'])
                            if results['data']['data'] == []:
                                pass
                            else:
                                yydt = results['data']['totalData']['betAmount']
                                yyds=results['data']['data']
                                # print(yyds)
                                for ppds in range(0,len(yyds)):
                                    data =yyds[ppds]['bettingTime']
                                    data = data.replace("T", " ")
                                    data = data.replace(".000Z", "")
                                    yyds[ppds]['bettingTime']=data
                                    yyds[ppds]['Total_Amount']=yydt
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

        sport_report_list = []
        str_sum = excel_report[2]
        for i in range(0, len(report02_list)):
            if excel_report[0] == "未完成交易-登0-登3-会员-查看订单详情-子查询":
                for options in report02_list[i]['options']:
                    del options['matchTime']
            if excel_report[2] != None:
                ppxt_lsit = str_sum.split(",")
                # print(ppxt_lsit)
                for j in ppxt_lsit:
                    # print(sportId_yyds_lsit[i])
                    del report02_list[i][j]
            sport_report_list.append(report02_list[i])


        print(sport_report_list)
        sport_report_dict= []
        for key, value in sportId_yyds_lsit[0][0].items():
            sport_report_dict.append(key)
        # print(sport_report_dict)



        time_list = [" 00:00:00", " 23:59:59"]
        self.tt.sport_report_sql(begin=begin + time_list[0], end=end + time_list[1], excel_report=excel_report,sport_report_dict=sport_report_dict, sport_report_list=sport_report_list)
        return sportId_list

    def sport_report03(self, URL, token, excel_report, begin, end):
        global sportId_list, sportId_yyds_lsit

        sportId_list = []
        sportId_yyds_lsit=[]
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

                for i in yyds:
                    if i[excel_report[6]] == '串关':
                        pass
                    elif excel_report[0] in interface_list:
                        sportId_list.append(i[excel_report[6]])
                        sportId_list.append(i['accountId'])
                        roid_list.append(i['levelId'])
                        # print(sportId_list,roid_list)
                    else:
                        sportId_list.append(i[excel_report[6]])

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

    def report_list_Compared01(self,sport_list,sql_list,Compared,excel_report):
        if sport_list!= [] and sql_list!= []:
            yyds_list = []
            for key, value in sport_list[0].items():
                yyds_list.append(key)
            for i in range(0, len(sport_list)):
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
                                # print("走到了这里")
                                correct_list.append(sql_list[j])
                                print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]),"数据对比正确：" + str(sport_list[i]) + "/" + str(sql_list[j]))
                                break
                            else:
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
                                            if excel_report[0] in options_list:
                                                self.options_report(A=sport_list[i][ppxt_lsit[0]],B=sport_list[i][ppxt_lsit[1]],C=yyds_list[report],D=sport_list[i][yyds_list[report]],E=sql_list[j][yyds_list[report]])
                                        else:
                                            sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])) + "/" +yyth + "/"+str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" +  str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                            print("\033[31m" + str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]+"-"+yyth), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str( sql_list[j][yyds_list[report]]) +"\033[0m",type(sport_list[i][yyds_list[report]]),type(sql_list[j][yyds_list[report]]))
                                            if excel_report[0] in options_list:
                                                self.options_report(A=sport_list[i][ppxt_lsit[0]],B=sport_list[i][ppxt_lsit[1]], C=yyds_list[report],D=sport_list[i][yyds_list[report]], E=sql_list[j][yyds_list[report]])
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
            for i in range(0, len(sport_list)):
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
        print(f"\033[32m{A}-{B},{C}：数据对比开始\033[0m")
        aa_list = []
        for key, value in D.items():
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
                            f"\033[31m{A}-{B},{C}数据对比错误：{D[ykk][i]}/{E[ykk][i]},{type(D[ykk][i])}/{type(E[ykk][i])}\033[0m")
        print(f"\033[32m{A}-{B},{C}：数据对比结束\033[0m")

    def sport_report_sql(self,begin,end,excel_report,sport_report_dict,sport_report_list):
        global options_list

        num_list = []
        sort_num_list = []
        mix_number=[]
        options_list = []
        sum_yyds = excel_report[8]
        yyds = sum_yyds.split("@")
        if yyds[0]=='':
            del yyds[0]
        if excel_report[3] == 1:
            if len(yyds) == 1:
                if str(yyds[0])[0]=="f":
                    sql = eval(yyds[0])
                else:
                    sql=yyds[0]
                sort_num = self.my.query_data(sql, db_name='bfty_credit')
                # print(sort_num)
                mix_number.append("1-1")
            else:
                sql01 = eval(yyds[0])
                sql02 = eval(yyds[1])
                sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                sort_num_list.append(sort_num01)
                sort_num_list.append(sort_num02)

                num_list.append(sort_num_list)
                sort_num = num_list
                mix_number.append("2-2")
        elif excel_report[3] == 2:
            for all in sportId_list:
                sort_num_list = []
                if len(yyds) == 1:
                    sql = eval(yyds[0])
                    sort_num = self.my.query_data(sql, db_name='bfty_credit')
                    num_list.append(sort_num)
                    if num_list[0] ==():
                        del num_list[0]
                    mix_number.append("2-1")
                elif len(yyds) == 2:
                    sql01 = eval(yyds[0])
                    sql02 = eval(yyds[1])
                    sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                    sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                    sort_num_list.append(sort_num01)
                    sort_num_list.append(sort_num02)
                    num_list.append(sort_num_list)
                    mix_number.append("2-2")
                else:
                    if excel_report[0]=="未完成交易-登0-登3-会员-查看订单详情-子查询":
                        yyrt_list = []
                        order_list=[]
                        sql01=eval(yyds[1])
                        sql=eval(yyds[0])
                        sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                        sort_num=self.my.query_data(sql, db_name='bfty_credit')
                        for i in sort_num01:
                            order_list.append(i[0])
                        for all_order_no in order_list:
                            sql02 = eval(yyds[2])
                            sql03 = eval(yyds[3])
                            sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                            sort_num03 = self.my.query_data(sql03, db_name='bfty_credit')
                            #拼接元祖参数
                            yyrt_list.append(sort_num02[0])
                            if order_list.index(all_order_no)==0:
                                ggg=yyrt_list[0]+sort_num[0]
                                yyrt_list[0]=ggg
                                # print("拼接打印：",yyrt_list)
                            aa_list = []
                            jkk_list = []
                            for key, value in sport_report_list[0]['options'][0].items():
                                aa_list.append(key)
                            print(sort_num03)
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
                            # print(jkk_list)
                        options_list.append(jkk_list)
                        print(options_list)
                        num_list.append(yyrt_list)
                        # print(num_list)
            sort_num = num_list
            mix_number.append("2-1")
        else:
            for all in sportId_list:
                sort_num_list = []
                if len(yyds) == 1:
                    if excel_report[0] in interface_list:
                        num=int(proxy_id_list[sportId_list.index(all)])
                        sql = eval(yyds[0])
                        sort_num = self.my.query_data(sql, db_name='bfty_credit')
                        num_list.append(sort_num)
                        if num_list[0] == ():
                            del num_list[0]
                        mix_number.append("2-1")
                else:
                    sql01 = eval(yyds[0])
                    sql02 = eval(yyds[1])
                    sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                    sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                    sort_num_list.append(sort_num01)
                    sort_num_list.append(sort_num02)
                    num_list.append(sort_num_list)
            mix_number.append("2-2")
            sort_num = num_list


        sport_sql_list = sport_report_dict
        sql_sport_list = []
        # print(sort_num)
        # print(f"SQL数据：{sort_num}\n接口数据：{sport_report_list}\n-----------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------")
        self.Compared_report(sort_num=sort_num,sport_list=sport_report_list,sql_name_list=sport_sql_list,sql_list=sql_sport_list,Compared=excel_report[9],report_name=excel_report[0]+"  "+excel_report[1],excel_report=excel_report,mix=mix_number)

    def Compared_report(self, sort_num, sport_list, sql_name_list, sql_list, Compared, report_name, excel_report,mix):
        global sport_error, sport_all_error,yyds01,correct_list
        correct_list=[]
        sport_error = []
        sport_all_error = []
        # print(excel_report[3])
        str_num=Compared
        yyds01=str_num.split(",")
        print(f"正在执行{excel_report[0]}-{excel_report[1]}")
        print(sort_num[1])
        print(mix[0])
        print(sql_name_list)
        if mix[0]==str('1-1'):
            print(sort_num)
            print(sort_num[0])
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
                        else:
                            yy_num=sort_num[i][j]
                    else:
                        yy_num = float(sort_num[i][j])
                    sql_dict[sql_name_list[j]] = yy_num
                sql_list.append(sql_dict)
        # print(sql_list)
        if mix[0]==str('2-1'):
            print(sort_num)
            print(sort_num[0])
            print(sort_num[0][0])
            count = 0
            for i in range(0, len(sort_num)):
                for j in range(0,len(sort_num[i])):
                    sql_dict = {}
                    for g in range(0,len(sort_num[i][j])):
                        if str(type(sort_num[i][j][g]))in type_list:
                            if sql_name_list[g] in int_list:
                                yy_num = int(sort_num[i][j][g])
                            elif sort_num[i][j][g] == "options":
                                 yy_num=options_list[i]
                                 print(i,j,g)
                            elif str(type(sort_num[i][j][g]))==type(None):
                                yy_num = sort_num[i][j][g]
                            else:
                                yy_num = str(sort_num[i][j][g])
                        else:
                            yy_num = float(sort_num[i][j][g])
                        sql_dict[sql_name_list[g]] = yy_num
                    sql_list.append(sql_dict)
            print(sql_list[1])
            print(sport_list[1])
        if mix[0]==str('2-2'):
            print(sort_num)
            print(sort_num[0])
            print(sort_num[0][0])
            print(sort_num[0][0][0])
            for i in range(0, len(sort_num)):
                for j in range(0, len(sort_num[i])):
                    for l in range(0, len(sort_num[i][j])):
                        print(sort_num[i][j][l])
                        sql_dict = {}
                        for g in range(0,len(sort_num[i][j][l])):
                            if str(type(sort_num[i][j][l][g])) in type_list:
                                if sql_name_list[g] in int_list:
                                    yy_num = int(sort_num[i][j][l][g])
                                elif str(type(sort_num[i][j][l][g])) == type(None):
                                    yy_num = sort_num[i][j][l][g]
                                else:
                                    yy_num = str(sort_num[i][j][l][g])
                            else:
                                yy_num = float(sort_num[i][j][l][g])
                            sql_dict[sql_name_list[g]] = yy_num
                        sql_list.append(sql_dict)
        print(sql_list[1])
        print(sport_list[1])

        if len(yyds01)==1:
            self.report_list_Compared01(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)
        elif len(yyds01)==2:
            self.report_list_Compared02(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)
        else:
            self.report_list_Compared03(sport_list=sport_list, sql_list=sql_list, Compared=Compared,excel_report=excel_report)

        if len(sport_list) == len(correct_list):
            print(f"\033[32m代理{Dl_list[pkk]}的{report_name}，接口数据比对全部正确\033[0m")
        else:
            print(f"\033[31m代理{Dl_list[pkk]}的{report_name}，数据错误，需要比对,{len(sport_list)},{len(correct_list)}\033[0m")
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
        module_list = ["总投注-混合串关-主查询","总投注-混合串关-子查询(查询其注单号，包含的比赛)","未完成交易-登0-主查询","未完成交易-登0-登3-会员-子查询","未完成交易-登0-登3-会员-查看订单详情-子查询"]
        interface_list=["未完成交易-登0-主查询"]
        roid_list=[]
        proxy_id_list=['0','1','2','3']
        int_list=['levelId','numberOfBets',"betType"]
        type_list=["<class 'str'>", "<class 'datetime.datetime'>", "<class 'NoneType'>", "<class 'int'>"]
        sport_report02_list=[]
        options_list=['未完成交易-登0-登3-会员-查看订单详情-子查询']


        # yyds=cc.login(URL=URL,begin="2022-06-04",end="2022-06-10")
        # ppds=bc.
        # (begin="2022-06-04 00:00:00",end="2022-06-10 23:59:59")

        #调用本地Exce读取数据
        ccds=cc.reading_Excel(excel=excel, save_excel=save_excel,begin="2022-06-04",end="2022-06-15", URL=URL)