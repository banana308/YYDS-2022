import requests
import json
import datetime
import xlwt
import openpyxl
import threading
import time
import datetime
import random
from concurrent.futures import ThreadPoolExecutor
import time

toten_list = []
orderNo_list = []
# 赛事ID列表
INPLAY_matchid_list = []
TODAY_matchid_list = []
EARLY_matchid_list = []

INPLAY_num_list = []
TODAY_num_list = []
EARLY_num_list = []
# 最后打印列表
matchid_yyds = []
sprot_yyds = []
LAY_yyds = []
orderNo_yyds = []

#下注字典
submit_dict={}
submit_list=[{"isLive": False, "originalOdds": 0, "creditOdds": 0, "outcomeId": "", "oddsType": 0}]



# 下注相关列表
outcomeId_lsit = []
odds_list = []
oddsType_list = []
orderNo_list = []
kkkk_lsit = []
sport_lsit = []
# 写入text
aa_list=[]
bb_list=[]
cc_list = []
dd_list = []
ee_list = []
yy_list = []
num_list = []
oddt_list = []
ods_list = []

count01 = 0
count = 3


def get_toten_00(j):
    global toten, name
    # 账号的拼接
    name = "fceshi0" + str(j)
    # name="CCeshi0"+str(j)
    url = str(URL) + "/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data = {
        "userName": name,
        "password": "991444c1f732105f81fa51df09c2619d",
        "loginUrl": "http://192.168.10.120:96"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    toten = results['data']['data']['accessCode']
    # toten_list.append(toten)
    # print(f"正在下注用户：fceshi0{j}")
    # print(f"toten:{toten}")
    return toten


# 请求登录接口，获取toten
def get_toten_01(i):
    global toten01, name
    # 账号的拼接
    name = "fceshi0" + str(i)
    # name="CCeshi0"+str(j)
    url = str(URL) + "/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data = {
        "userName": name,
        "password": "991444c1f732105f81fa51df09c2619d",
        "loginUrl": "http://192.168.10.120:96"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    toten01 = results['data']['data']['accessCode']
    toten_list.append(toten01)
    print(f"正在下注用户：fceshi0{i}")
    # print(f"toten:{toten}")
    return toten01


def get_balance(number):
    url = str(URL) + "/creditUser/getUserAmount"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten_list[number]
    }
    date = {}
    response = requests.get(url=url, headers=headers01, params=date)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    balance = results['data']['balance']
    winLoseAmount = results['data']['winLoseAmount']
    # print(str(number)+"   "+"余额："+str(balance)+"  输赢："+str(winLoseAmount)+"\n")
    # 写入订单详情
    path02 = "C:\\test\\balance-01.txt"
    f = open(path02, 'a')
    f.write(
        str(number) + "   " + "余额：" + str(balance) + "  输赢：" + str(winLoseAmount) + "\n"
    )
    print(f"已完成{number}")


def get_time(number):
    for number in range(number, 0, -1):
        time.sleep(1)
        print(number)


# 获取赛事信息
def get_today_odds():
    global odds, ods, nub, yy, matchId
    # if count01 % 3 > 0:
    #     # count01-=3
    #     nub = random.randint(2, 3)
    #     print("count01%3取值：" + str(count01 % 3))
    #     print("取模随机取值：" + str(nub))
    # else:
    #     nub = 3
    #     # nub = random.randint(1, 3)
    #     print("随机早盘取值：" + str(nub))
    if nub == 1:
        ods = "滚球盘"
        yy = "INPLAY"
    if nub == 2:
        ods = "今日盘"
        yy = "TODAY"
    if nub == 3:
        ods = "早盘"
        yy = "EARLY"
    print("下注盘：" + str(ods))
    print("正在遍历赛事")
    ods_list.append(ods)
    url = str(URL) + "/creditMatchPC/matchList"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    if nub == 1 or nub == 2:
        data = {
            "sort": 2,
            "periodId": yy,
            "highlight": False,
            "marketGroupId": marketGroupId,
            "sportCategoryId": sport,
            "oddsType": 1, "tournamentIds": [],
            "matchIds": [],
            "page": 1,
            "limit": 500,
        }
    if nub == 3:
        data = {
            "sort": 2,
            "periodId": yy,
            "highlight": False,
            "marketGroupId": "100",
            "sportCategoryId": sport,
            "oddsType": 1, "tournamentIds": [],
            "matchIds": [],
            "page": 1,
            "limit": 1000,
            "dateOffset": -1}
    '''
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    odds = results['data']['data']
    oddt_list.append(odds)
    '''
    # test_01=results['data']['data'][0]['matchList'][0]['matchId']
    # print(test_01)
    # 遍历取出对应的赛事matchid
    '''
    nub==1 代表:滚球盘
    nub==2 代表:今日盘
    nub==3 代表:早盘
    '''
    if nub == 1:
        if len(INPLAY_matchid_list) == 0:
            response = requests.post(url=url, headers=headers01, json=data)
            # 返回结果json转化
            results = json.loads(response.text)
            # print(results)
            odds = results['data']['data']
            oddt_list.append(odds)
            for i in odds:
                matchlist = i['matchList']
                for matchinfo in matchlist:
                    INPLAY_matchid_list.append(matchinfo['matchId'])
                    INPLAY_num_list.append(matchinfo['totalMarketAmount'])
            print("共计赛事：" + str(len(INPLAY_matchid_list)))
        else:
            print("共计赛事：" + str(len(INPLAY_matchid_list)))
    if nub == 2:
        if len(TODAY_matchid_list) == 0:
            response = requests.post(url=url, headers=headers01, json=data)
            # 返回结果json转化
            results = json.loads(response.text)
            # print(results)
            odds = results['data']['data']
            oddt_list.append(odds)
            for i in odds:
                matchlist = i['matchList']
                for matchinfo in matchlist:
                    TODAY_matchid_list.append(matchinfo['matchId'])
                    TODAY_num_list.append(matchinfo['totalMarketAmount'])
            print("共计赛事：" + str(len(TODAY_matchid_list)))
        else:
            print("共计赛事：" + str(len(TODAY_matchid_list)))
    if nub == 3:
        if len(EARLY_matchid_list) == 0:
            response = requests.post(url=url, headers=headers01, json=data)
            # 返回结果json转化
            results = json.loads(response.text)
            # print(results)
            odds = results['data']['data']
            # print(odds)
            oddt_list.append(odds)
            for i in odds:
                matchlist = i['matchList']
                #获取球类所有的赛事ID和其所有玩法的盘口数量
                for matchinfo in matchlist:
                    EARLY_matchid_list.append(matchinfo['matchId'])
                    EARLY_num_list.append(matchinfo['totalMarketAmount'])
            print("共计赛事：" + str(len(EARLY_matchid_list)))
        else:
            print("共计赛事：" + str(len(EARLY_matchid_list)))
    if len(INPLAY_matchid_list)>0:
        matchId=INPLAY_matchid_list
    if len(TODAY_matchid_list)>0:
        matchId=TODAY_matchid_list
    if len(EARLY_matchid_list)>0:
        matchId=EARLY_matchid_list

    # matchid_yyds.append(matchId)
    # LAY_yyds.append(yy)


# 根据赛事ID，遍历每一场赛事的盘口
def get_odds(g):
    global isLive, num_outcomeId, aa, bb, cc, dd, ee, matchId, count01
    url = str(URL) + "/creditMatchPC/totalMarketList?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }

    data = {
        "matchId": matchId[g],
        "oddsType": 1,
        "sportCategoryId": "sr:sport"
    }
    # "matchId": matchId,
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    isLive = results['data']['isLive']
    # print(isLive)
    # outcomeId=results['data']['marketList'][0]['outcomeList'][0][0]['outcomeId']
    # print(outcomeId)
    num_outcomeId = len(results['data']['marketList'])
    # print(num_outcomeId)
    # print("下注盘口:" + str(num_outcomeId) + "个")
    if num_outcomeId == 0:
        print("-----------------------------------------------------------" + ods + "无法下注，请重新选择-----------------------------------------------------------")
    # 判断盘口ID，是否为0，为0重新取
    if num_outcomeId == 0:
        count01 = count01 + 1
        get_today_odds()
        get_odds()
    else:
        # 赛事里随机取出一场比赛的盘口ID,方便下注
            k=random.randint(0, len(results['data']['marketList']))
            # print(k)
            outcomeId_lsit.append(results['data']['marketList'][k]['outcomeList'][0][0]['outcomeId'])
            odds_list.append(results['data']['marketList'][k]['outcomeList'][0][0]['odds'])
            oddsType_list.append(results['data']['marketList'][k]['outcomeList'][0][0]['oddsType'])

            aa_list.append(results['data']['awayTeamName'])
            bb_list.append(results['data']['homeTeamName'])
            cc_list.append(results['data']['marketList'][k]['outcomeList'][0][0]['id'])
            dd_list.append(results['data']['marketList'][k]['outcomeList'][0][0]['marketName'])
            ee_list.append(results['data']['marketList'][k]['outcomeList'][0][0]['outcomeName'])
            # print(outcomeId_lsit)
            # print(odds_list)
            # print(oddsType_list)
    print(g)
    time.sleep(1)
    return outcomeId_lsit, odds_list, oddsType_list, isLive, num_outcomeId, matchId



#获取下注时的参数字典化
def get_submit_dict(mixedNum_N_1,a,b):
    for i in range((int(a)), int(b)):
        list = {"isLive": False, "originalOdds": 0, "creditOdds": 0, "outcomeId": "", "oddsType": 0}
        submit_list.append(list)
        if i == (int(a)):
            (submit_list[i]["isLive"]) = False
            (submit_list[i]["originalOdds"]) = (int(odds_list[i]) + 0.05)
            (submit_list[i]["creditOdds"]) = odds_list[i]
            (submit_list[i]["outcomeId"]) = outcomeId_lsit[i]
            (submit_list[i]["oddsType"]) = oddsType_list[i]
            pass
        else:
            (submit_list).append(list)
            (submit_list[i]["isLive"]) = False
            (submit_list[i]["originalOdds"]) = (int(odds_list[i]) + 0.05)
            (submit_list[i]["creditOdds"]) = odds_list[i]
            (submit_list[i]["outcomeId"]) = outcomeId_lsit[i]
            (submit_list[i]["oddsType"]) = oddsType_list[i]
    submit_dict[mixedNum_N_1] = submit_list
    submit_list.clear()



#串关传参参数化：
def get_N_1():
    global mixedNum_N_1,mixedNum_betAmount

    mixedNum_betAmount=10

    mixedNum_N_1_number=15
    #生成最大可支持的串关数（2-63）串1
    N_1_number_list=[]
    for N_1_number in range(2,mixedNum_N_1_number+1):
        N_1_number_list.append(N_1_number)

    for N_1_num in N_1_number_list:
        # 2串1：
        if int(N_1_num) == 2:
            mixedNum_N_1 = str(N_1_num) + "_1_0" + str(mixedNum_betAmount)
            get_submit_dict(mixedNum_N_1, 0, N_1_num)
            get_submitbet_N_1(mixedNum_N_1, submit_dict[mixedNum_N_1])
        else:
            for k in range(0, len(N_1_number_list) - 1):
            # 3串1~若干串1
                if int(N_1_num)==int(N_1_number_list[k]+1):
                    mixedNum_N_1=str(N_1_num)+"_1_0"+str(mixedNum_betAmount)
                    get_submit_dict(mixedNum_N_1,N_1_number_list[k],int(N_1_num)+int(N_1_number_list[k]))
                    get_submitbet_N_1(mixedNum_N_1, submit_dict[mixedNum_N_1])
                else:
                    break


# 串关下注
def get_submitbet_N_1(i):
    i=i-1
    url = str(URL) + "/creditBet/submit"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten01
    }
    data = {
        "oddsChangeType": 1,
        "mixedNum": list(submit_dict.keys())[i],
        "betId": 1645442141712,
        "selections": list(submit_dict.values())[i],
        "browserFingerprintId": "7edc374f0171b1b63a0c2556544cdef3",
        "terminal": "pc",
        "betIp": "192.168.10.120"}

    response = requests.post(url=url, headers=headers01, json=data)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now01 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # 返回结果json转化
    results = json.loads(response.text)
    code = results['code']
    orderNo = results['data']['orderNo']
    orderNo_list.append(orderNo)
    orderNo_yyds.append(orderNo)
    if code == 0:
        date=list(submit_dict.keys())[i]
        print(list(str(date)))
        N_N=(list(str(date))[0] + "串" + list(str(date))[1])
        print(str(i) + "投注"+str(N_N)+"成功:" + "  投注比赛：" + aa_list[i] + "VS" + bb_list[i] + "  " + dd_list[i] + "(" + ee_list[i] + ")" + "-" + cc_list[i] + " 投注orderNo：:" + str(orderNo))
        print("---------------------------------------------------------分割线------------------------------------------------------------------")
        # 写入订单详情
        path010 = "C:\\test\\get_test\\order_no.txt"
        f = open(path010, 'a')
        if i == 0:
            f.write("--------------------------------------------------"+str(yyds)+str(now)+"--------------------------------------------------")
            f.write(orderNo+"\n")
        else:
            f.write(orderNo + "\n")
    else:
        print(code, results['message'])
        exit()
    # print(results)
    print("{已下注成功用户：" + name, "已成功投注比赛：" + str((i + 1)), " 正在投注比赛：" + "未开启多线程"," 未投投注比赛：" + str((len(matchId) - i - 1)) + " 投注orderNo：" + str(orderNo) + "}" + "\n")



    # 写入订单号

    path01 = "C:\\test\\get_test\\order_no\\" + name + ".txt"
    f = open(path01, 'a')
    f.write(orderNo+"\n")
    # 写入订单详情
    path02 = "C:\\test\\get_test\\order_no_test\\" + name + ".txt"
    f = open(path02, 'a')
    f.write(
        "投注球类：" + yyds + "\n" +
        "投注比赛ID：" + matchId[i] + "\n" +
        "投注比赛 ：" + aa_list[i] + "VS" + bb_list[i] + "\n" +
        "投注时间 ：" + now + "\n" +
        "投注金额 ：" + betAmount + "\n" +
        "投注盘口ID :" + outcomeId_lsit[i] + "\n" +
        "投注盘口： " + dd_list[i] + "-" + ee_list[i] + "-" + cc_list[i] + "\n" +
        "投注赔率: " + str(odds_list[i]) + "\n" +
        "orderNo: " + orderNo + "\n" + "\n"
    )
    if i == (len(matchId) - 1):
        print("已下注比赛球类：" + str(sport_lsit))
        print("已下注比赛ID：" + str(matchId[i]))
        print("已下注比赛订单号：" + str(orderNo_list))
        print("已下注比赛盘口ID：" + str(outcomeId_lsit))
        print(
            "---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
        # 写入比赛ID：
        path01 = "C:\\test\\get_test\\matchid\\" + yyds + now01 + ".txt"
        f = open(path01, 'a')
        f.write("投注球类：" + yyds + "-" + str(matchId[i]) + "-" + "\n" + "投注盘口数量：1" )
        # 写入比赛ID
        path01 = "C:\\test\\get_test\\matchid.txt"
        f = open(path01, 'a')
        f.write(
            "投注球类：" + yyds + "\n" +
            "投注比赛ID：" + str(matchId[i]) + "\n" +
            "投注时间：" + str(now) + "\n" +
            "投注盘口数量：1" + "\n" + "\n"
        )
        # 清空下注相关列表
        toten_list.clear()
        outcomeId_lsit.clear()
        odds_list.clear()
        oddsType_list.clear()
        orderNo_list.clear()
        kkkk_lsit.clear()
        cc_list.clear()
        dd_list.clear()
        ee_list.clear()
        INPLAY_matchid_list.clear()
        TODAY_matchid_list.clear()
        EARLY_matchid_list.clear()

        INPLAY_num_list.clear()
        TODAY_num_list.clear()
        EARLY_num_list.clear()


# 复式串关下注
def get_submitbet_N_N_N(i):
    global betAmount
    i = int(i) - 1
    betAmount = "10"
    url = str(URL) + "/creditBet/submit"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten01
    }
    data = {
        "oddsChangeType": 1,
        "mixedNum": ["1_1_0_10"],
        # "mixedNum": ["6_1_0_10"],
        # "mixedNum": ["6_57_1_10"],
        "betId": 1645442141712,
        "selections": [
            {"isLive": False,
             "originalOdds": (int(odds_list[i]) + 0.05),
             "creditOdds": odds_list[i],
             "outcomeId": outcomeId_lsit[i],
             "oddsType": oddsType_list[i]
             }
        ],
        "browserFingerprintId": "7edc374f0171b1b63a0c2556544cdef3",
        "terminal": "pc",
        "betIp": "192.168.10.120"
    }

    response = requests.post(url=url, headers=headers01, json=data)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now01 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # 返回结果json转化
    results = json.loads(response.text)
    code = results['code']
    orderNo = results['data']['orderNo']
    orderNo_list.append(orderNo)
    orderNo_yyds.append(orderNo)
    if code == 0:
        print(str(i) + "投注成功:" + "  投注比赛：" + aa_list[i] + "VS" + bb_list[i] + "  " + dd_list[i] + "(" + ee_list[i] + ")" + "-" + cc_list[i] + " 投注orderNo：:" + str(orderNo))
        print("---------------------------------------------------------分割线------------------------------------------------------------------")
        # 写入订单详情
        path010 = "C:\\test\\get_test\\order_no.txt"
        f = open(path010, 'a')
        if i == 0:
            f.write("--------------------------------------------------"+str(yyds)+str(now)+"--------------------------------------------------")
            f.write(orderNo+"\n")
        else:
            f.write(orderNo + "\n")
    else:
        print(code, results['message'])
        exit()
    # print(results)
    print("{已下注成功用户：" + name, "已成功投注比赛：" + str((i + 1)), " 正在投注比赛：" + "未开启多线程"," 未投投注比赛：" + str((len(matchId) - i - 1)) + " 投注orderNo：" + str(orderNo) + "}" + "\n")



    # 写入订单号

    path01 = "C:\\test\\get_test\\order_no\\" + name + ".txt"
    f = open(path01, 'a')
    f.write(orderNo+"\n")
    # 写入订单详情
    path02 = "C:\\test\\get_test\\order_no_test\\" + name + ".txt"
    f = open(path02, 'a')
    f.write(
        "投注球类：" + yyds + "\n" +
        "投注比赛ID：" + matchId[i] + "\n" +
        "投注比赛 ：" + aa_list[i] + "VS" + bb_list[i] + "\n" +
        "投注时间 ：" + now + "\n" +
        "投注金额 ：" + betAmount + "\n" +
        "投注盘口ID :" + outcomeId_lsit[i] + "\n" +
        "投注盘口： " + dd_list[i] + "-" + ee_list[i] + "-" + cc_list[i] + "\n" +
        "投注赔率: " + str(odds_list[i]) + "\n" +
        "orderNo: " + orderNo + "\n" + "\n"
    )
    if i == (len(matchId) - 1):
        print("已下注比赛球类：" + str(sport_lsit))
        print("已下注比赛ID：" + str(matchId[i]))
        print("已下注比赛订单号：" + str(orderNo_list))
        print("已下注比赛盘口ID：" + str(outcomeId_lsit))
        print(
            "---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
        # 写入比赛ID：
        path01 = "C:\\test\\get_test\\matchid\\" + yyds + now01 + ".txt"
        f = open(path01, 'a')
        f.write("投注球类：" + yyds + "-" + str(matchId[i]) + "-" + "\n" + "投注盘口数量：1" )
        # 写入比赛ID
        path01 = "C:\\test\\get_test\\matchid.txt"
        f = open(path01, 'a')
        f.write(
            "投注球类：" + yyds + "\n" +
            "投注比赛ID：" + str(matchId[i]) + "\n" +
            "投注时间：" + str(now) + "\n" +
            "投注盘口数量：1" + "\n" + "\n"
        )
        # 清空下注相关列表
        toten_list.clear()
        outcomeId_lsit.clear()
        odds_list.clear()
        oddsType_list.clear()
        orderNo_list.clear()
        kkkk_lsit.clear()
        cc_list.clear()
        dd_list.clear()
        ee_list.clear()
        INPLAY_matchid_list.clear()
        TODAY_matchid_list.clear()
        EARLY_matchid_list.clear()

        INPLAY_num_list.clear()
        TODAY_num_list.clear()
        EARLY_num_list.clear()



def sprot_yyds():
    global sport, marketGroupId, a, yyds
    if j == a:
        sport = "sr:sport:1"
        marketGroupId = "100"
        yyds = "足球"
        print("正在下注球类：" + "足球")
        sport_lsit.append(yyds)

    if j == (a + 1):
        sport = "sr:sport:2"
        marketGroupId = "200"
        yyds = "蓝球"
        print("正在下注球类：" + "蓝球")
        sport_lsit.append(yyds)
    if j == (a + 2):
        sport = "sr:sport:5"
        marketGroupId = "300"
        yyds = "网球"
        print("正在下注球类：" + "网球")
        sport_lsit.append(yyds)
    if j == (a + 3):
        sport = "sr:sport:23"
        marketGroupId = "400"
        yyds = "排球"
        print("正在下注球类：" + "排球")
        sport_lsit.append(yyds)

    if j == (a + 4):
        sport = "sr:sport:31"
        marketGroupId = "500"
        yyds = "羽毛球"
        print("正在下注球类：" + "羽毛球")
        sport_lsit.append(yyds)
    if j == (a + 5):
        sport = "sr:sport:20"
        marketGroupId = "600"
        yyds = "乒乓球"
        print("正在下注球类：" + "乒乓球")
        sport_lsit.append(yyds)
    if j == (a + 6):
        sport = "sr:sport:3"
        marketGroupId = "700"
        yyds = "棒球"
        print("正在下注球类：" + "棒球")
        sport_lsit.append(yyds)
    if j == (a + 7):
        sport = "sr:sport:4"
        marketGroupId = "900"
        yyds = "冰球"
        print("正在下注球类：" + "冰球")
        sport_lsit.append(yyds)


if __name__ == '__main__':
    URL = "http://192.168.10.120:6210"
    '''
    @足球："sr:sport:1"  "100"
    @蓝球："sr:sport:2"  "200"
    @网球： "sr:sport:5" "300"
    @排球："sr:sport:23" "400"
    @羽毛球："sr:sport:31"  "500"
    @乒乓球："sr:sport:20"  "600"
    @棒球： "sr:sport:3" "700"
    @冰球： "sr:sport:4" "900"




    nub==1 代表:滚球盘
    nub==2 代表:今日盘
    nub==3 代表:早盘
    '''
    # 球类参数
    # sport="sr:sport:4"
    # marketGroupId="900"
    # 下注盘参数
    nub = 3
    # 取值范围：
    a = 1
    b = 2

    for j in range(a, b):
        get_toten_00(j)
        sprot_yyds()
        get_today_odds()
        with ThreadPoolExecutor(max_workers=10) as t1:  # 创建一个最大容纳数量为5的线程池
            for g in range(0, len(matchId)):
                task2 = t1.submit(get_odds, g)
                # get_odds(g)
        get_N_1()
        # # num_outcomeId
        for i in range(0, len(matchId)):
            i = i + 1
            get_toten_01(i)
            get_submitbet_N_1(i)
        if j == (b - 1):
            # 写入比赛ID
            path01 = "C:\\test\\get_test\\matchid.txt"
            f = open(path01, 'a')
            f.write(
                "---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
            print("已下注所有比赛球类：" + str(sport_lsit))
            print("已下注所有比赛ID：" + str(matchid_yyds))
            print("共所有计下注盘：" + str(LAY_yyds))
            print("共计所有下注订单:" + str(orderNo_yyds))
            print("共计所有下注订单数量:" + len(orderNo_yyds))



'''
if __name__ == '__main__':
    # 120测试环境
    # URL = "http://192.168.10.120:96"
    # sky本地
    # URL="http://192.168.10.196:8095"
    # 58测试环境
    # URL="http://192.168.10.236:6210"
    # 120测试环境
    URL = "http://192.168.10.120:6210"

    with ThreadPoolExecutor(max_workers=10) as t:  # 创建一个最大容纳数量为5的线程池
        for j in range(0, 1001):
            task1 = t.submit(get_toten, j)
        get_time(60)
        print(len(toten_list))
        print(toten_list)
        get_time(10)
        with ThreadPoolExecutor(max_workers=3) as t1:  # 创建一个最大容纳数量为5的线程池
            for i in range(0, len(toten_list)):
                task2 = t1.submit(get_submitbet, i)
                # task2 = t1.submit(get_balance,i
            get_time(180)
            print(orderNo_list)
            print(len(orderNo_list))
'''
