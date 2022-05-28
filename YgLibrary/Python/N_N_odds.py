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
    name = "fceshi0" + str(1)
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
    print(f"正在下注用户：fceshi0{i},toten:{toten01}")
    time.sleep(1)
    # print(f"toten:{toten}")
    return toten01



# 获取赛事信息
def get_today_odds(nub):
    global odds, ods, yy, matchId
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
    print("下注盘：" + str(ods)+"  "+"正在遍历赛事,预计需求10~15秒")
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
        sort_list_null.append(yyds)
    if len(TODAY_matchid_list)>0:
        matchId=TODAY_matchid_list
        sort_list_null.append(yyds)
    if len(EARLY_matchid_list)>0:
        matchId=EARLY_matchid_list
        sort_list_null.append(yyds)

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
        k_list=[]
        for k in range(0, len(results['data']['marketList'])):
            # print((results['data']['marketList'][k]['outcomeList'][0]))
            k_list.append((results['data']['marketList'][k]['outcomeList'][0]))
        matchid_dict[matchId[g]]=k_list
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
    # print(mixedNum_N_1," ",sr_match_list)
    # print(submit_dict)
    #直接调用下注接口下注：
    i=get_i()
    # i=(len(submit_dict))
    get_toten_01(i)
    get_submitbet_N_1(i)

    submit_list.clear()
    list_a_b.clear()
    sub_list.clear()
    sr_match_list.clear()
    ttt_list.clear()





def get_match():
    sr = random.randint(0, len(matchId) - 1)
    sr_new_match = matchId[sr]
    if sr_new_match in sr_match_list:
        # print(f"\033[31m在列表中，准备重新随机取值\033[0m""")
        get_match()
    else:
        # print(f"\033[32m不在列表中，准备写入值\033[0m")
        sr_match =sr_new_match
        outcomeList = random.randint(0, len(matchid_dict[sr_match]) - 1)
        marketId_num = random.randint(0, len(matchid_dict[sr_match][outcomeList]) - 1)
        marketId = (matchid_dict[sr_match])[outcomeList][marketId_num]

        del (matchid_dict[sr_match])[outcomeList]
        sub_list.append(marketId)
        matchid_yyds.append(sr_match)
        ttt_list.append(sr_match)
        sr_match_list.append(sr_match)

    return sr_new_match

def get_i():
    i = random.randint(0, 501)
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
    okk = [ "21","31","34","26","411","45","526","657","71", "81", "91", "101", "111", "121", "131", "141", "151", "161", "171","181", "191", "201"]


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
    if str(code)=="-100":
        print(data)
        print(f"\033[31m下注失败，重新调用接口下注,{time.sleep(3)}秒后再次下注\033[0m")
        i = get_i()
        get_submitbet_N_1(i)
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
            N_B = (list(str(date))[0] + list(str(date))[2]+list(str(date))[3])
            N_N = (yyds + ":复式串关" + list(str(date))[0] + "串" + list(str(date))[2]+list(str(date))[3])
            all_mixedNum_N_list.append(N_N)

        #已下注串关或复式串关写入：
        mixedNum_list.append(N_N)
        print( "投注"+str(N_N)+"投注成功:" +" 投注orderNo：:" + str(orderNo)+"\n")
        #循环已下注的比赛名称和盘口
        for yg in range(0,len(sub_list)):
            dd=sub_list[yg]["marketName"]
            # print(ttt_list[yg])
            # print(matchId.index(ttt_list[yg]))
            print(f"投注比赛：{aa_list[matchId.index(ttt_list[yg])]}VS{bb_list[matchId.index(ttt_list[yg])]},投注盘口：{dd}")
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
    sport_lsit.append(yyds)



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
                print(
                    "---------------------------------------------------------分割线------------------------------------------------------------------" + "\n")
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
                print(time.sleep(5))
    else:
        pass


def sprot_yyds():
    global sport, marketGroupId,yyds
    if j == a or j=="足球":
        sport = "sr:sport:1"
        marketGroupId = "100"
        yyds = "足球"
        print("正在下注球类：" + "足球")
    if j == (a + 1) or j=="篮球":
        sport = "sr:sport:2"
        marketGroupId = "200"
        yyds = "篮球"
        print("正在下注球类：" + "篮球")

    if j == (a + 2) or j=="网球":
        sport = "sr:sport:5"
        marketGroupId = "300"
        yyds = "网球"
        print("正在下注球类：" + "网球")

    if j == (a + 3) or j=="排球":
        sport = "sr:sport:23"
        marketGroupId = "400"
        yyds = "排球"
        print("正在下注球类：" + "排球")

    if j == (a + 4) or j=="羽毛球":
        sport = "sr:sport:31"
        marketGroupId = "500"
        yyds = "羽毛球"
        print("正在下注球类：" + "羽毛球")

    if j == (a + 5) or j=="乒乓球":
        sport = "sr:sport:20"
        marketGroupId = "600"
        yyds = "乒乓球"
        print("正在下注球类：" + "乒乓球")

    if j == (a + 6) or j=="棒球":
        sport = "sr:sport:3"
        marketGroupId = "700"
        yyds = "棒球"
        print("正在下注球类：" + "棒球")

    if j == (a + 7) or j=="冰球":
        sport = "sr:sport:4"
        marketGroupId = "900"
        yyds = "冰球"
        print("正在下注球类：" + "冰球")



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

    # get_toten_00()
    # sprot_yyds(a=0,j="篮球")
    # get_today_odds(nub=3)
    # for g in range(0, len(matchId)):
    #     get_odds(g)
    # # with ThreadPoolExecutor(max_workers=50) as t1:  # 创建一个最大容纳数量为5的线程池
    # #         print(f"正在取得{len(matchId)}场每场比赛随机盘口值,预计需要等待{len(matchId)/25}秒")
    # #         for g in range(0, len(matchId)):
    # #             task2 = t1.submit(get_odds, g)
    # #             # get_odds(g)




    # 球类参数
    # sport="sr:sport:4"
    # marketGroupId="900"

    # 取值范围：
    a = 0
    b = 8
    user_num = 0
    j="篮球"
    for j in range(a, b):
        get_toten_00()
        sprot_yyds()
        # sprot_yyds(a=j,j="足球")
        get_today_odds(nub=3)
        if (len(sort_list_null))==0:
            print(f"{yyds}没有赛事,无法下注,已跳过\n-------------------------------------------------------")
            sport_lsit_null.append(yyds)
            # if j == (b - 1):
            if j == "篮球":
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
                print("共计所有下注订单:" + str(orderNo_yyds))
                print("共计所有下注订单数量:" + str(len(orderNo_yyds)))
            # continue
        else:
                with ThreadPoolExecutor(max_workers=50) as t1:  # 创建一个最大容纳数量为5的线程池
                    # for g in range(0, 10):
                    print(f"正在取得{len(matchId)}场每场比赛的盘口值,预计需要等待{len(matchId)/25}秒")
                    for g in range(0, len(matchId)):
                        task2 = t1.submit(get_odds, g)
                        # get_odds(g)
                # 下注串关

                mixedNum_betAmount = 10
                mixedNum_N_1_number = 6
                if len(matchId)>=mixedNum_N_1_number:
                    mixedNum_N_1_number=mixedNum_N_1_number
                else:
                    mixedNum_N_1_number=len(matchId)
                get_N_1(mixedNum_betAmount=mixedNum_betAmount, mixedNum_N_1_number=mixedNum_N_1_number, bet_type=1)
    # #下注串关
    # mixedNum_betAmount=10
    # mixedNum_N_1_number=6
    # get_N_1(mixedNum_betAmount=mixedNum_betAmount,mixedNum_N_1_number=mixedNum_N_1_number,bet_type=1)




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
