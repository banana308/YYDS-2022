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

sort_list_null=[]
matchid_dict={}
ttt_list=[]

mixedNum_N_1_number_YYds_list_01=[]
mixedNum_N_1_number_YYds_list_02 = []
mixedNum_N_1_number_YYds_list_03 = []
# 最后打印列表
matchid_yyds = []
sprot_yyds = []
LAY_yyds = []
orderNo_yyds = []

all_mixedNum_list=[]
all_mixedNum_N_list=[]

#下注字典
submit_dict={}
submit_list=[]
submit_yyds_list=[]
list_a_b=[]

mixedNum_list=[]
mixedNum_N_list=[]




# 下注相关列表
sub_list=[]
outcomeId_lsit = []
odds_list = []
oddsType_list = []
orderNo_list = []
kkkk_lsit = []
sport_lsit = []
sport_lsit_null=[]

sr_match_list=[]
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


def get_toten_00():
    global toten, name
    # 账号的拼接
    name = "fceshi0" + str(0)
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
    # name = "fceshi0" + str(i)
    name = "fceshi0" + str(i)
    # name="ht0"+str(i)
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
    print(f"正在下注用户：fceshi0{i},toten:{toten01}")
    time.sleep(1)
    # print(f"toten:{toten}")
    return toten01

def get_balance(toten01):
    global balance
    url = str(URL) + "/creditUser/getUserAmount"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten01
    }
    date = {}
    response = requests.get(url=url, headers=headers01, params=date)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    balance = results['data']['balance']
    winLoseAmount = results['data']['winLoseAmount']
    print(str(name)+"   "+"余额："+str(balance)+"  输赢："+str(winLoseAmount)+"\n")
    # 写入订单详情
    path02 = "C:\\test\\balance-01.txt"
    f = open(path02, 'a')
    f.write(
        str(name) + "   " + "余额：" + str(balance) + "  输赢：" + str(winLoseAmount) + "\n"
    )
    # print(f"已完成{number}")
    return balance






# 获取赛事信息
def get_today_odds(nub,oddsType):
    global odds, ods, yy,matchId
    # if count01 % 3 > 0:
    #     # count01-=3
    #     nub = random.randint(2, 3)
    #     print("count01%3取值：" + str(count01 % 3))
    #     print("取模随机取值：" + str(nub))
    # else:
    #     nub = 3
    #     # nub = random.randint(1, 3)
    #     print("随机早盘取值：" + str(nub))
    if oddsType==1:
        oddsType_name="欧洲盘"
    else:
        oddsType_name = "香港盘"
    if nub == 1:
        ods = "滚球盘"
        yy = "INPLAY"
    if nub == 2:
        ods = "今日盘"
        yy = "TODAY"
    if nub == 3:
        ods = "早盘"
        yy = "EARLY"
    print(f"下注盘：{str(ods)},赔率类型：{oddsType_name}，正在遍历赛事,预计需求10~15秒")
    # print(f"正在遍历赛事,预计需求10秒")
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
            "oddsType": oddsType,
            "tournamentIds": [],
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
            "oddsType": oddsType,
            "tournamentIds": [],
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
        sort_list_null.append(yyds)
    if len(TODAY_matchid_list)>0:
        matchId=TODAY_matchid_list
        sort_list_null.append(yyds)
    if len(EARLY_matchid_list)>0:
        matchId=EARLY_matchid_list
        sort_list_null.append(yyds)

    # matchid_yyds.append(matchId)
    # LAY_yyds.append(yy)
    # print(f"赛事列表赛事ID打印:{matchId}")


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
        "oddsType": oddsType,
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
    # print(matchId[g])
    # print("下注盘口:" + str(num_outcomeId) + "个")
    if num_outcomeId == 0:
        print("-----------------------------------------------------------" + ods + "无法下注，请重新选择-----------------------------------------------------------")
    # 判断盘口ID，是否为0，为0重新取
    if num_outcomeId == 0:
        count01 = count01 + 1
        get_today_odds()
        get_odds()
    else:
        # 赛事里取出本场比赛的所有盘口ID,方便下注
        # k = random.randint(0, len(results['data']['marketList']))

        #判断参数，下注香港盘
        yyds_dict={'足球':['16', '66', '18', '68', '104', '19', '20', '69', '70', '165', '176', '166', '177', '139', '152', '116', '117', '120', '127'],
                   '篮球':['223', '225', '227', '228', '66', '68', '69', '70', '303', '236', '756', '757'],
                   '网球':['188', '187', '189', '190', '191'],'排球':['204', '314'],'羽毛球':['237', '238', '237', '238'],'乒乓球':['237', '238', '237', '238'],'棒球':['246', '247'],
                   '冰球':['256', '258', '16', '18', '410', '460', '446']}

        k_list=[]
        for k in range(0, len(results['data']['marketList'])):
            if oddsType_str=='':
                k_list.append((results['data']['marketList'][k]['outcomeList'][0]))
            else:
                if results['data']['marketList'][k]['id'] in yyds_dict[j]:
                    k_list.append((results['data']['marketList'][k]['outcomeList'][0]))
                else:
                    pass
        matchid_dict[matchId[g]]=k_list
        mixedNum_N_1_number_YYds_list_01.append(len(k_list))
        aa_list.append(results['data']['awayTeamName'])
        bb_list.append(results['data']['homeTeamName'])


        # print(matchid_dict)
        # print(matchid_dict[matchId[g]])
        # matchid_dict.clear()
    time.sleep(1)
    return outcomeId_lsit, odds_list, oddsType_list, isLive, num_outcomeId, matchId


#获取下注时selections的参数字典化
def get_submit_dict(mixedNum_N_1,a,b):
    global sr_match
    # print(mixedNum_N_1)
    list_a_b.append(a)
    list_a_b.append(b)
    # 方法1,遍历赛事取值
    for p in range(0, int(N_1_num)):
        get_match()
    if N_1_num == 2:
        pass
    else:
        num_01 = (sum(mixedNum_N_1_number_YYds_list_02))
        num_02 = (sum(mixedNum_N_1_number_YYds_list_03))
        print(f"比赛数量：{str(len(matchId))}")
        print(f"\n测试盘口预校验{num_01}，与实际比较{num_02}")



    #根据赛事ID，就行传参组装取值
    for yu in range((int(a)), int(b)):
        list = {"isLive": False, "originalOdds": 0, "creditOdds": 0, "outcomeId": "", "oddsType": 0}
        submit_list.append(list)

        if yu == (int(a)):
            yu = yu - int(a)
            (submit_list[yu]["originalOdds"]) = (int(sub_list[yu]["odds"]) + 0.05)
            (submit_list[yu]["creditOdds"]) = sub_list[yu]["odds"]
            (submit_list[yu]["outcomeId"]) = sub_list[yu]["outcomeId"]
            (submit_list[yu]["oddsType"]) = sub_list[yu]["oddsType"]

        else:
            yu = yu - int(a)
            (submit_list[yu]["originalOdds"]) = (int(sub_list[yu]["odds"]) + 0.05)
            (submit_list[yu]["creditOdds"]) = sub_list[yu]["odds"]
            (submit_list[yu]["outcomeId"]) = sub_list[yu]["outcomeId"]
            (submit_list[yu]["oddsType"]) = sub_list[yu]["oddsType"]

        LAY_yyds.append(sub_list[yu]["marketName"])

    submit_dict[mixedNum_N_1] = submit_list
    print(submit_dict[mixedNum_N_1])
    # print(mixedNum_N_1," ",sr_match_list)
    # print(submit_dict)
    #直接调用下注接口下注：
    i=get_i()
    # i=(len(submit_dict))
    get_toten_01(i)
    get_balance(toten01)
    get_submitbet_N_1(i)

    submit_list.clear()
    list_a_b.clear()
    sub_list.clear()
    sr_match_list.clear()
    ttt_list.clear()





def get_match():
    # if len(matchId) < 10:
    #     print(f"剩余赛事数量：{len(matchId)}，剩余赛事：{matchId}")
    sr_new_match=random.choice(matchId)
    # sr=random.randint(0,len(matchId)-1)
    # sr_new_match=matchId[sr]
    if sr_new_match in sr_match_list:
        # print(f"\033[31m在列表中，准备重新随机取值\033[0m""")
        get_match()
    else:
        # print(f"\033[32m不在列表中，准备写入值\033[0m")
        sr_match=sr_new_match
        if len(matchid_dict[sr_match]) == 0:
            print(f"\033[32m此场比赛{sr_match}，盘口值为{len(matchid_dict[sr_match])}，即将重新取值\033[0m")
            del matchId[matchId.index(sr_match)]
            get_match()
        else:
            outcomeList = random.randint(0, len(matchid_dict[sr_match]) - 1)
            marketId_num = random.randint(0, len(matchid_dict[sr_match][outcomeList]) - 1)
            marketId = (matchid_dict[sr_match])[outcomeList][marketId_num]

            del (matchid_dict[sr_match])[outcomeList]
            mixedNum_N_1_number_YYds_list_03.append(1)
            sub_list.append(marketId)
            matchid_yyds.append(sr_match)
            ttt_list.append(sr_match)
            sr_match_list.append(sr_match)
    return sr_new_match

def get_i():
    i = random.randint(1, 71)
    i_list = []
    if i in i_list:
        get_i()
    else:
        pass
    return i





#串关mixedNum传参参数化：
def get_N_1(mixedNum_betAmount,mixedNum_N_1_number,bet_type):
    global mixedNum_N_1,N_1_num


    #串关和复式串关判定传参
    bet_type_dict={"单关":1,"串关":2,"复式串关":3}
    # if bet_type in list(bet_type_dict.values()):
    #     if int(bet_type)==1:
    #         mixedNum_N_1 = "1_1_0_"+ str(mixedNum_betAmount)
    #         get_submit_dict(mixedNum_N_1=mixedNum_N_1, a=0, b=1)


    #生成最大可支持的串关数（2-63）串1
    N_1_number_list=[]
    for N_1_number in range(2,int(mixedNum_N_1_number)+1):
        N_1_number_list.append(N_1_number)
    print(N_1_number_list)

    num_NN_lsit = [{"复式3串4":["2_3_0","3_4_1"]},{"复式4串11":["2_6_0","3_4_0","4_11_1"]},{"复式5串25": ["2_10_0", "3_10_0", "4_5_0", "5_26_1"]},{"复式6串57": ["2_15_0", "3_20_0", "4_15_0","5_6_0","6_57_1"]}]
    num_NN_A=[]
    #2串1~N串1
    if len(N_1_number_list) == 1:
        N_1_num=N_1_number_list[0]
        print(f"只有:{str(N_1_num)}串1")
        mixedNum_N_1 = str(N_1_num) + "_1_0_" + str(mixedNum_betAmount)
        get_submit_dict(mixedNum_N_1=mixedNum_N_1, a=sum(N_1_number_list[0:N_1_number_list.index(N_1_num)]),b=sum(N_1_number_list[0:((N_1_number_list.index(N_1_num)) + 1)]))
    else:
        for N_1_num in N_1_number_list:
            if int(N_1_num)==2:
                print(f"正在循环拼接:{str(N_1_num)}串1")
                mixedNum_N_1 = str(N_1_num) + "_1_0_" + str(mixedNum_betAmount)
                get_submit_dict(mixedNum_N_1=mixedNum_N_1, a=sum(N_1_number_list[0:N_1_number_list.index(N_1_num)]),b=sum(N_1_number_list[0:((N_1_number_list.index(N_1_num)) + 1)]))
            else:
                print(f"正在循环拼接:{str(N_1_num)}串1")
                mixedNum_N_1 = str(N_1_num) + "_1_0_" + str(mixedNum_betAmount)
                get_submit_dict(mixedNum_N_1=mixedNum_N_1, a=sum(N_1_number_list[0:N_1_number_list.index(N_1_num)]),b=sum(N_1_number_list[0:((N_1_number_list.index(N_1_num)) + 1)]))
                for yydm in range(N_1_number_list[0],int(N_1_num)+1):
                    num_NN_A.append(yydm)
                    if int(N_1_num)>=7:
                        break
                    #判断字典里的数据长度：
                    if len(list(list((num_NN_lsit[N_1_num-3]).values())[0][yydm-2]))==5:
                        num_1=str(yydm)
                        num_2=str(list(list((num_NN_lsit[N_1_num-3]).values())[0][yydm-2])[2])
                        num_3=list(list((num_NN_lsit[N_1_num-3]).values())[0][yydm-2])[-1]
                        num_4=mixedNum_betAmount
                        if yydm==int(N_1_num):
                            print(f"正在循环拼接:复式串关{num_1}串{num_2}")
                        else:
                            print(f"正在循环拼接:复式串关{num_1}串1*{num_2}")
                    else:
                        num_1=str(yydm)
                        num_2 =f"{str(list(list((num_NN_lsit[N_1_num-3]).values())[0][yydm-2])[2])}{str(list(list((num_NN_lsit[N_1_num-3]).values())[0][yydm-2])[3])}"
                        num_3 =list(list((num_NN_lsit[N_1_num-3]).values())[0][yydm-2])[-1]
                        num_4 =mixedNum_betAmount
                        if yydm == int(N_1_num):
                            print(f"正在循环拼接:复式串关{num_1}串{num_2}")
                        else:
                            print(f"正在循环拼接:复式串关{num_1}串1*{num_2}")

                    mixedNum_N_1 = f"{num_1}_{num_2}_{num_3}_{num_4}"
                    a = sum(N_1_number_list) + sum(N_1_number_list[0:N_1_number_list.index(N_1_num)]) + sum(num_NN_A)
                    b=sum(N_1_number_list)+sum(N_1_number_list[0:((N_1_number_list.index(N_1_num)) + 1)])+sum(num_NN_A)
                    get_submit_dict(mixedNum_N_1=mixedNum_N_1, a=a,b=b)


# 串关下注
def get_submitbet_N_1(i):

    global count02
    betAmount=mixedNum_betAmount



    #串关快捷列表
    okk = [ "21","34","411","526","657","71", "81", "91", "101", "111", "121", "131", "141", "151", "161", "171","181", "191", "201"]


    url = str(URL) + "/creditBet/submit"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten01
    }

    #下注参数化拼接
    # print(submit_dict)
    # mixedNum = list(submit_dict.keys())[i]
    # selections = submit_yyds_list[i]
    # print(mixedNum,'\n',selections)

    # print(submit_dict)
    mixedNum = list(submit_dict.keys())[-1]
    # selections = submit_yyds_list[i]
    selections = submit_dict[(list(submit_dict.keys())[-1])]
    # print(mixedNum, '\n', selections)
    data = {
        "oddsChangeType": 1,
        "mixedNum": [mixedNum],
        "betId": 1645442141712,
        "selections": selections,
        "browserFingerprintId": "7edc374f0171b1b63a0c2556544cdef3",
        "terminal": "pc",
        "betIp": "192.168.10.120"}
    # print(data)
    response = requests.post(url=url, headers=headers01, json=data)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now01 = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # if (str(N_1_num)+list(str(list(submit_dict.keys())[-1]))[2]+list(str(list(submit_dict.keys())[-1]))[3]) in okk:
    #     time.sleep(5)

    # 返回结果json转化
    results = json.loads(response.text)
    # print(results)
    code = results['code']
    if str(code)!="0":
        print(data)
        print(f"\033[31m下注失败，重新调用接口下注,{time.sleep(3)}秒后再次下注\033[0m")
        i = get_i()
        get_submitbet_N_1(i)
    else:
        time.sleep(1)
    orderNo = results['data']['orderNo']
    # print(orderNo)
    orderNo_list.append(orderNo)
    orderNo_yyds.append(orderNo)
    # time.sleep(1)
    if code == 0:
        date=list(submit_dict.keys())[-1]
        if list(str(date))[3] == "_":
            if list(str(date))[4] =="0":
                N_B=str(N_1_num)+list(str(date))[2]
                N_N=(yyds+":"+list(str(date))[0] + "串" + list(str(date))[2])
                all_mixedNum_list.append(N_N)
            else:
                N_B=(list(str(date))[0] + list(str(date))[2])
                N_N = (yyds + ":复式串关" + list(str(date))[0] + "串" + list(str(date))[2])
                all_mixedNum_N_list.append(N_N)
        else:
            if list(str(date))[2] == "_":
                N_B = str(N_1_num) + list(str(date))[3]
                N_N = (yyds + ":复式串关" + (str(N_1_num)) + "串" + list(str(date))[3])
                all_mixedNum_N_list.append(N_N)
            else:
                N_B = (list(str(date))[0] + list(str(date))[2]+list(str(date))[3])
                N_N = (yyds + ":复式串关" + list(str(date))[0] + "串" + list(str(date))[2]+list(str(date))[3])
                all_mixedNum_N_list.append(N_N)

        #已下注串关或复式串关写入：
        mixedNum_list.append(N_N)
        print( "投注"+str(N_N)+"投注成功:" +" 投注orderNo：:" + str(orderNo)+"\n")
        #循环已下注的比赛名称和盘口
        for yg in range(0,len(sub_list)):
            dd=sub_list[yg]["marketName"]
            oddsType_name=submit_dict[mixedNum][yg]["oddsType"]
            if oddsType_name == 1:
                oddsType_name = "\033[32m欧洲盘\033[0m"
            else:
                oddsType_name = "\033[33m香港盘\033[0m"
            print(f"投注比赛：{aa_list[matchId.index(ttt_list[yg])]}VS{bb_list[matchId.index(ttt_list[yg])]},投注盘口：{dd},赔率类型:{oddsType_name}")
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
    count02=0
    count02=count02+1
    print("{已下注成功用户：" + name, "已投注串关："+str(mixedNum_list)+"已成功投注注单：" + str(len(mixedNum_list)), " 正在投注比赛：" + "未开启多线程"," 未投投注比赛：" + str((len(matchId) - len(mixedNum_list) - 1)) + " 投注orderNo：" + str(orderNo) + "}" + "\n")




    # 写入订单号
    path01 = "C:\\test\\get_test\\order_no\\" + name + ".txt"
    f = open(path01, 'a')
    f.write(orderNo+"\n")
    # 写入订单详情
    # path02 = "C:\\test\\get_test\\order_no_test\\" + name + ".txt"
    # f = open(path02, 'a')
    # # "投注类型：" + N_N + "\n" +
    # f.write(
    #     "投注球类：" + yyds + "\n" +
    #     "投注比赛ID：" + matchId[i] + "\n" +
    #     "投注比赛 ：" + aa_list[i] + "VS" + bb_list[i] + "\n" +
    #     "投注时间 ：" + now + "\n" +
    #     "投注金额 ：" + betAmount + "\n" +
    #     "投注盘口ID:" + outcomeId_lsit[i] + "\n" +
    #     "投注盘口： " + dd_list[i] + "-" + ee_list[i] + "-" + cc_list[i] + "\n"+
    #     "orderNo: " + orderNo + "\n" + "\n"
    # )
    if int(N_1_num)==mixedNum_N_1_number:
        if N_B in okk:
                print("已下注比赛球类：" + str(yyds))
                print("已下注串关类型：" + str(mixedNum_list))
                print("已下注比赛ID：" + str(sr_match_list))
                print("已下注比赛订单号：" + str(orderNo_list))
                print("---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
                get_print()
                # # 写入比赛ID：
                # path01 = "C:\\test\\get_test\\matchid\\" + yyds + now01 + ".txt"
                # f = open(path01, 'a')
                # f.write("投注球类：" + yyds + "-" + str(matchId[i]) + "-" + "\n" + "投注盘口数量：1" )
                # # 写入比赛ID
                # path01 = "C:\\test\\get_test\\matchid.txt"
                # f = open(path01, 'a')
                # f.write(
                #     "投注球类：" + yyds + "\n" +
                #     "投注比赛ID：" + str(matchId[i]) + "\n" +
                #     "投注时间：" + str(now) + "\n" +
                #     "投注盘口数量：1" + "\n" + "\n"
                # )
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
                sort_list_null.clear()
                mixedNum_list.clear()
                sr_match_list.clear()
                submit_dict.clear()
                sport_lsit.append(yyds)
                print(time.sleep(5))
    else:
        pass


def sprot_yyds(j):
    global sport, marketGroupId,yyds
    if j=="足球":
        sport = "sr:sport:1"
        marketGroupId = "100"
        yyds = "足球"
    if j=="篮球":
        sport = "sr:sport:2"
        marketGroupId = "200"
        yyds = "篮球"

    if j=="网球":
        sport = "sr:sport:5"
        marketGroupId = "300"
        yyds = "网球"

    if j=="排球":
        sport = "sr:sport:23"
        marketGroupId = "400"
        yyds = "排球"

    if j=="羽毛球":
        sport = "sr:sport:31"
        marketGroupId = "500"
        yyds = "羽毛球"

    if j=="乒乓球":
        sport = "sr:sport:20"
        marketGroupId = "600"
        yyds = "乒乓球"

    if j=="棒球":
        sport = "sr:sport:3"
        marketGroupId = "700"
        yyds = "棒球"

    if j=="冰球":
        sport = "sr:sport:4"
        marketGroupId = "900"
        yyds = "冰球"
    print(f"\033[32m---------------------------------------------------------正在下注球类:{yyds}---------------------------------------------------------------------\033[0m")
    mixedNum_N_1_number_YYds_list_01.clear()
    mixedNum_N_1_number_YYds_list_02.clear()
    mixedNum_N_1_number_YYds_list_03.clear()



def get_print():
    if j =="冰球":
        # 写入比赛ID
        path01 = "C:\\test\\get_test\\matchid.txt"
        f = open(path01, 'a')
        f.write(
            "---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
        print("已下注比赛球类：" + str(sport_lsit))
        print("未下注比赛球类：" + str(sport_lsit_null))
        print("已下注所有串关：" + str(all_mixedNum_list))
        print("已下注所有复式串关：" + str(all_mixedNum_N_list))
        print("已下注所有比赛ID：" + str(matchid_yyds))
        print("共所有计下注盘：" + str(LAY_yyds))
        print("共计所有下注订单:" + "\n"+str(orderNo_yyds))
        print("共计所有下注订单数量:" + str(len(orderNo_yyds)))


if __name__ == '__main__':
    #120环境
    # URL = "http://192.168.10.120:6210"
    # MDE环境
    URL = "https://mdesearch.betf.io"
    print(URL)
    '''
        @足球："sr:sport:1"  "100"
        @篮球："sr:sport:2"  "200"
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

    # 取值范围：

    # user_num = 0
    # j="篮球"
    j_lsit=["足球","篮球","网球","排球","羽毛球","乒乓球","棒球","冰球"]
    # j_lsit=["篮球","网球","排球","羽毛球","乒乓球","棒球","冰球"]
    # j_lsit=["乒乓球",  "冰球"]
    for j in j_lsit:
        sprot_yyds(j)
        get_toten_00()
        #赔率类型随机：1代表：欧洲盘，2代表：香港盘
        oddsType_str='香港盘'
        # oddsType = random.randint(1, 2)
        oddsType = 2
        get_today_odds(nub=3,oddsType=oddsType)
        if (len(sort_list_null))==0:
            print(f"{yyds}没有赛事,无法下注,已跳过\n-------------------------------------------------------")
            sport_lsit_null.append(yyds)
            get_print()
            continue
        else:
            with ThreadPoolExecutor(max_workers=50) as t1:  # 创建一个最大容纳数量为5的线程池
                # for g in range(0, 10):
                print(f"正在取得{len(matchId)}场每场比赛的盘口值,预计需要等待{len(matchId)/25}秒")
                for g in range(0, len(matchId)):
                    task2 = t1.submit(get_odds, g)
                    # get_odds(g)
        # 下注串关
        mixedNum_betAmount = 10
        mixedNum_N_1_number =10

        # print(time.sleep(5),end='')
        mixedNum_N_1_number_dict={"2":2,"3":9,"4":16,"5":25,"6":36,"7":7,"8":8,"9":9,"10":10,"11":11,"12":13,"13":13,"14":14,"15":15,"16":16,"17":17}
        if len(matchId) > 1:
            if len(matchId)<=4:
                mixedNum_N_1_number = 2
                get_N_1(mixedNum_betAmount=mixedNum_betAmount, mixedNum_N_1_number=mixedNum_N_1_number, bet_type=1)
            if len(matchId)>4:
                for kHH in range(2,mixedNum_N_1_number+1):
                    mixedNum_N_1_number_YYds_list_02.append(mixedNum_N_1_number_dict[str(kHH)])
                    # print(mixedNum_N_1_number_YYds_list_02)
                    if sum(mixedNum_N_1_number_YYds_list_01)-sum(mixedNum_N_1_number_YYds_list_02)<25:
                        print(f"{sum(mixedNum_N_1_number_YYds_list_02)}<={sum(mixedNum_N_1_number_YYds_list_01)},kHH:{kHH}")
                        mixedNum_N_1_number =kHH-2
                        # print(f"取得mixedNum_N_1_number={mixedNum_N_1_number}")
                        del mixedNum_N_1_number_YYds_list_02[-1]
                        if len(mixedNum_N_1_number_YYds_list_02)>1:
                            del mixedNum_N_1_number_YYds_list_02[-1]
                        break
                    if sum(mixedNum_N_1_number_YYds_list_01)-sum(mixedNum_N_1_number_YYds_list_02)<40:
                        print(f"{sum(mixedNum_N_1_number_YYds_list_02)}<={sum(mixedNum_N_1_number_YYds_list_01)},kHH:{kHH}")
                        mixedNum_N_1_number = kHH-1
                        del mixedNum_N_1_number_YYds_list_02[-1]
                        # print(f"取得mixedNum_N_1_number={mixedNum_N_1_number}")
                        break
                    else:
                        pass
                print(f"取得mixedNum_N_1_number={mixedNum_N_1_number}")
                get_N_1(mixedNum_betAmount=mixedNum_betAmount, mixedNum_N_1_number=mixedNum_N_1_number, bet_type=1)
        else:
            print(f"{yyds}赛事低于2场,无法下注串关,已跳过\n-------------------------------------------------------")
            sport_lsit_null.append(yyds)
            get_print()
            continue

        if int(mixedNum_N_1_number)<2:
            print(f"{yyds}赛事程序计算,无法下注串关,已跳过\n-------------------------------------------------------")
            sport_lsit_null.append(yyds)
            get_print()
            continue








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
