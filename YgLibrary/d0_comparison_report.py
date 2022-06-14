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
        # 获取 工作簿对象
        workbook = openpyxl.load_workbook(excel[0])
        print("读取表格成功")
        # shenames = workbook.get_sheet_names()
        shenames = workbook.sheetnames
        print("整个表格所有表名:", shenames)  # ['各省市', '测试表']

        for gg in range(0,1):
            gg=shenames[gg]
        # for gg in shenames:
            # 获取该表相应的行数和列数
            worksheet= workbook[shenames[shenames.index(gg)]]
            rows = worksheet.max_row
            columns = worksheet.max_column
            print(f"所在\033[32m（{shenames[0]}）\033[0m组成有： {rows}行  {columns}列")
            content_A2 = worksheet.cell(2, 1).value
            if content_A2!=None:
                # for i in range(2, int(rows)+1):
                for i in range(2, 4):
                    excel_report = []
                    for j in range(2, int(columns)-2):
                        report=worksheet.cell(i,j).value
                        excel_report.append(report)
                        # print(excel_report)
                    # print(excel_report)
                    # print(excel_report)
                    self.login(URL=URL, begin=begin, end=end, excel_report=excel_report)
                    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    if sport_all_error==[]:
                        worksheet.cell(i,int(columns)-2,("测试通过"+"\n"+now))
                    else:
                        worksheet.cell(i, int(columns)-2, ("测试不通过"+"\n"+now))
                        worksheet.cell(i, int(columns)-1, str(sport_error))
                        worksheet.cell(i, int(columns), str(sport_all_error))
            else:
                continue
        workbook.save(filename=save_excel[0])
        workbook.close()

    def login(self,URL, begin, end,excel_report):
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
        else:
            self.sport_report02(URL=URL, token=token, excel_report=excel_report, begin=begin, end=end)



    def sport_report01(self,URL, token, excel_report, begin, end):
        global sportId_list

        url = str(URL)+(excel_report[1])
        headers=eval(excel_report[4])
        data=eval(excel_report[5])[0]
        session = requests.session()
        # print(headers)
        # print(data)

        method_list=["post"]
        if excel_report[7]==method_list[0]:
            response = session.post(url=url, headers=headers, json=data)
        else:
            response = session.get(url=url, headers=headers, params=data)
        results = json.loads(response.text)
        yyds = results['data']['data']
        sportId_list = []
        # print(yyds)

        str_sum=excel_report[2]
        sport_report_list=[]
        if excel_report[2]!=None:
            ppxt_lsit=str_sum.split(",")
            # print(ppxt_lsit)
            for i in range(0,len(yyds)):
                for j in ppxt_lsit:
                    # print(j)
                    del yyds[i][j]
                sport_report_list.append(yyds[i])
            #     print(yyds[i])
            # print(len(yyds[0]))
        else:
            pass

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
                data=eval(excel_report[5])[0]
                session = requests.session()
                method_list = ["post"]

                if excel_report[7] == method_list[0]:
                    response = session.post(url=url, headers=headers, json=data)
                else:
                    response = session.get(url=url, headers=headers, params=data)
                results = json.loads(response.text)
                yyds = results['data']['data']
                for i in yyds:
                    sportId_list.append(i[excel_report[6]])
                # print(sportId_list)
            else:
                url = str(URL) + url
                sportId_yyds_lsit=[]
                for sportId in sportId_list:
                    data = eval(excel_report[5])[1]
                    data[excel_report[6]]=sportId
                    session = requests.session()
                    method_list = ["post"]

                    if excel_report[7] == method_list[0]:
                        response = session.post(url=url, headers=headers, json=data)
                    else:
                        response = session.get(url=url, headers=headers, params=data)
                    results = json.loads(response.text)
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
        for i in range(0, len(report02_list)):
            str_sum = excel_report[2]
            if excel_report[2] != None:
                ppxt_lsit = str_sum.split(",")
                # print(ppxt_lsit)
                for j in ppxt_lsit:
                    # print(sportId_yyds_lsit[i])
                    del report02_list[i][j]
            sport_report_list.append(report02_list[i])
        # print(sport_report_list)


        sport_report_dict= []
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

    def report_list_Compared01(self,sport_list,sql_list,Compared):

        for i in range(0, len(sport_list)):
            for j in range(0, len(sql_list)):
                # print(sql_list)
                # print(sport_list)
                if sport_list[i][Compared] == sql_list[j][Compared]:
                    if sport_list[i] == sql_list[j]:
                        print(sport_list[i][Compared],"数据对比正确：" + str(sport_list[i]) + "/" + str(sql_list[j]))
                        break
                    else:
                        print(sport_list[i])
                        print(sql_list[j])
                        for report in range(0, len(sql_list[j])):
                            yyds_list = list(sql_list[i].keys())
                            if sport_list[i][yyds_list[report]] == sql_list[j][yyds_list[report]]:
                                print(sport_list[i][Compared], str(yyds_list[report]),"数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                            else:
                                if sport_list[i][yyds_list[report]] == float(sql_list[j][yyds_list[report]]):
                                    print(sport_list[i][Compared], str(yyds_list[report]),"数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                else:
                                    sport_all_error.append(str(sport_list[i][Compared]) + "/" + str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str({sport_list[i][Compared]}) + "/" + (str({sql_list[j][Compared]})))
                                    print("\033[31m" + sport_list[i][Compared], str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]) + "\033[0m")
                else:
                    sport_error.append(str(sport_list[i][Compared])+"的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比："+str({sport_list[i][Compared]})+"/"+(str({sql_list[j][Compared]})))

    def report_list_Compared02(self, sport_list,sql_list, Compared):
            for i in range(0, len(sport_list)):
                for j in range(0, len(sql_list)):
                    ppxt_lsit =Compared.split(",")
                    if sport_list[i][ppxt_lsit[0]] == sql_list[j][ppxt_lsit[0]]:
                        if sport_list[i][ppxt_lsit[1]] == sql_list[j][ppxt_lsit[1]]:
                            if sport_list[i] == sql_list[j]:
                                print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]),"数据对比正确：" + str(sport_list[i]) + "/" + str(sql_list[j]))
                                break
                            else:
                                print(f"sport_list:{sport_list[i]}")
                                print(f"sql_list:{sql_list[j]}")
                                for report in range(0, len(sql_list[j])):
                                    yyds_list = list(sql_list[i].keys())
                                    if sport_list[i][yyds_list[report]] == sql_list[j][yyds_list[report]]:
                                        pass
                                        print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]), str(yyds_list[report]),"数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                    else:
                                        if sport_list[i][yyds_list[report]] == float(sql_list[j][yyds_list[report]]):
                                            pass
                                            print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]), str(yyds_list[report]), "数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                        else:
                                            sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])) + "/" + str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" +  str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                            print("\033[31m" + str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str( sql_list[j][yyds_list[report]]) + "\033[0m")
                        else:
                            sport_error.append(str(sport_list[i][ppxt_lsit[1]]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str({sport_list[i][ppxt_lsit[1]]}) + "/" + (str({sql_list[j][ppxt_lsit[1]]})))
                    else:
                        sport_error.append(str(sport_list[i][ppxt_lsit[0]]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str({sport_list[i][ppxt_lsit[0]]}) + "/" + (str({sql_list[j][ppxt_lsit[0]]})))


    def report_list_Compared03(self, sport_list,sql_list, Compared):
            # print(sport_list)
            # print(sql_list)
            for i in range(0, len(sport_list)):
                for j in range(0, len(sql_list)):
                    str_sum = Compared
                    ppxt_lsit = str_sum.split(",")
                    # print(ppxt_lsit)
                    if sport_list[i][ppxt_lsit[0]] == sql_list[j][ppxt_lsit[0]]:
                        if sport_list[i][ppxt_lsit[1]] == sql_list[j][ppxt_lsit[1]]:
                            if sport_list[i][ppxt_lsit[2]] == sql_list[j][ppxt_lsit[2]]:
                                if sport_list[i] == sql_list[j]:
                                    print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])+"-"+str(sport_list[i][ppxt_lsit[2]]),"数据对比正确：" + str(sport_list[i]) + "/" + str(sql_list[j]))
                                    break
                                else:
                                    print(f"sport_list:{sport_list[i]}")
                                    print(f"sql_list:{sql_list[j]}")
                                    for report in range(0, len(sql_list[j])):
                                        yyds_list = list(sql_list[i].keys())
                                        if sport_list[i][yyds_list[report]] == sql_list[j][yyds_list[report]]:
                                            pass
                                            print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])+"-"+str(sport_list[i][ppxt_lsit[2]]), str(yyds_list[report]),"数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                        else:
                                            if sport_list[i][yyds_list[report]] == float(sql_list[j][yyds_list[report]]):
                                                pass
                                                print(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])+"-"+str(sport_list[i][ppxt_lsit[2]]), str(yyds_list[report]), "数据对比正确：" + str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                            else:
                                                sport_all_error.append(str(str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]])) +"-"+str(sport_list[i][ppxt_lsit[2]])+ "/" + str(yyds_list[report]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" +  str(sport_list[i][yyds_list[report]]) + "/" + str(sql_list[j][yyds_list[report]]))
                                                print("\033[31m" + str(sport_list[i][ppxt_lsit[0]])+"-"+str(sport_list[i][ppxt_lsit[1]]+"-"+str(sport_list[i][ppxt_lsit[2]]), str(yyds_list[report]),"数据对比错误：" + str(sport_list[i][yyds_list[report]]) + "/" + str( sql_list[j][yyds_list[report]]) + "\033[0m"))
                            else:
                                sport_error.append(str(sport_list[i][ppxt_lsit[2]]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str({sport_list[i][ppxt_lsit[2]]}) + "/" + (str({sql_list[j][ppxt_lsit[2]]})))
                        else:
                            sport_error.append(str(sport_list[i][ppxt_lsit[1]]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str({sport_list[i][ppxt_lsit[1]]}) + "/" + (str({sql_list[j][ppxt_lsit[1]]})))
                    else:
                        sport_error.append(str(sport_list[i][ppxt_lsit[0]]) + "的数据对比错误,请检查SQL查询的字段与接口字段数据是否一致,数据对比：" + str({sport_list[i][ppxt_lsit[0]]}) + "/" + (str({sql_list[j][ppxt_lsit[0]]})))


    def sport_report_sql(self,begin,end,excel_report,sport_report_dict,sport_report_list):
        if excel_report[3] == 1:
            sql = eval(excel_report[8])
            sort_num = self.my.query_data(sql, db_name='bfty_credit')
            # print(sql)

        else:
            num_list=[]
            sum_yyds=excel_report[8]
            yyds=sum_yyds.split(",")
            for sport_id in sportId_list:
                sort_num_list = []
                if len(yyds) == 1:
                    sql = eval(excel_report[8])
                    sort_num = self.my.query_data(sql, db_name='bfty_credit')
                    num_list.append(sort_num_list)
                else:
                    sql01 = eval(excel_report[8])[0]
                    sql02 = eval(excel_report[8])[1]
                    sort_num01 = self.my.query_data(sql01, db_name='bfty_credit')
                    sort_num02 = self.my.query_data(sql02, db_name='bfty_credit')
                    sort_num_list.append(sort_num01)
                    sort_num_list.append(sort_num02)
                    # print(sql01)
                    # print(sql02)
                    # print(sort_num01,sort_num02)
                    num_list.append(sort_num_list)
            sort_num=num_list
            # print(sort_num)

        sport_sql_list = sport_report_dict
        sql_sport_list = []
        self.Compared_report(sort_num=sort_num,sport_list=sport_report_list,sql_name_list=sport_sql_list,sql_list=sql_sport_list,Compared=excel_report[9],report_name=excel_report[0]+"  "+excel_report[1],excel_report=excel_report)

    def Compared_report(self, sort_num, sport_list, sql_name_list, sql_list, Compared, report_name, excel_report):
        global sport_error, sport_all_error,yyds01

        sport_error = []
        sport_all_error = []
        # print(excel_report[3])
        str_num=Compared
        yyds01=str_num.split(",")
        if excel_report[3] == 1:
            for i in range(0, len(sort_num)):
                sql_dict = {}
                for j in range(0, len(sort_num[i])):
                    if type(sort_num[i][j]) == type('str'):
                        yy_num = sort_num[i][j]
                    else:
                        yy_num = float(sort_num[i][j])
                    sql_dict[sql_name_list[j]] = yy_num
                sql_list.append(sql_dict)
            if len(yyds01)==1:
                self.report_list_Compared01(sport_list=sport_list, sql_list=sql_list, Compared=Compared)
            elif len(yyds01)==2:
                self.report_list_Compared02(sport_list=sport_list, sql_list=sql_list, Compared=Compared)
            else:
                self.report_list_Compared03(sport_list=sport_list, sql_list=sql_list, Compared=Compared)
        else:
            for i in range(0, len(sort_num)):
                for j in range(0, len(sort_num[i])):
                    for l in range(0, len(sort_num[i][j])):
                        # print(sort_num[i][j][l])
                        sql_dict = {}
                        for g in range(0,len(sort_num[i][j][l])):
                            if type(sort_num[i][j][l][g]) == type('str'):
                                yy_num = sort_num[i][j][l][g]
                            else:
                                yy_num = float(sort_num[i][j][l][g])
                            sql_dict[sql_name_list[g]] = yy_num
                        sql_list.append(sql_dict)
            if len(yyds01)==1:
                self.report_list_Compared01(sport_list=sport_list, sql_list=sql_list, Compared=Compared)
            elif len(yyds01)==2:
                self.report_list_Compared02(sport_list=sport_list, sql_list=sql_list, Compared=Compared)
            else:
                self.report_list_Compared03(sport_list=sport_list, sql_list=sql_list, Compared=Compared)

        if sport_all_error == []:
            print(f"\033[32m代理{Dl_list[pkk]}的{report_name}，接口数据比对全部正确\033[0m")
        else:
            print(f"\033[31m代理{Dl_list[pkk]}的{report_name}，数据错误，需要比对\033[0m")
            sport_all_error.append(sport_list[0])
            sport_all_error.append(sql_list[0])
            print(f"\033[33m{sport_error}033[0m")









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
        sport_report_list = []
        Dl_list=["d0","d10","d2","d3"]
        excel = [r"C:\test\d0_comparison_report.xlsx",0]
        save_excel = ["C:\\test\\d0_comparison_report.xlsx"]



        # yyds=cc.login(URL=URL,begin="2022-06-04",end="2022-06-10")
        # ppds=bc.sport_report_sql(begin="2022-06-04 00:00:00",end="2022-06-10 23:59:59")

        list=[]

        ccds=cc.reading_Excel(excel=excel, save_excel=save_excel,begin="2022-06-04",end="2022-06-10", URL=URL)