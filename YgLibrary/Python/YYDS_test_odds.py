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

toten_list=[]
orderNo_list=[]
#赛事ID列表
INPLAY_matchid_list = []
TODAY_matchid_list = []
EARLY_matchid_list = []
#下注相关列表
outcomeId_lsit=[]
odds_list=[]
oddsType_list=[]
orderNo_list=[]
kkkk_lsit=[]
#写入text
cc_list=[]
dd_list=[]
ee_list=[]
num_list=[]
oddt_list=[]
ods_list=[]

count01 = 0
count = 3

#120测试环境
URL="http://192.168.10.120:6210"
#sky本地
# URL="http://192.168.10.196:8095"
#58测试环境
# URL="http://192.168.10.236:6210"


#请求登录接口，获取toten
def get_toten(j):
    global toten,name
    name="FCeshi0"+str(j)
    # name="CCeshi0"+str(j)
    url=str(URL) +"/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data ={
    "userName":name,
    "password":"991444c1f732105f81fa51df09c2619d",
    "loginUrl":"http://192.168.10.120:96"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    #print(results)
    toten=results['data']['data']['accessCode']
    toten_list.append(toten)
    print(f"正在下注用户：FCeshi0{j}")
    print(f"toten:{toten}")
    return toten

def get_balance(number):
    url = str(URL)+"/creditUser/getUserAmount"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten_list[number]
    }
    date={}
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
        str(number)+"   "+"余额："+str(balance)+"  输赢："+str(winLoseAmount)+"\n"
    )
    print(f"已完成{number}")


def get_time(number):
    for number in range(number,0,-1):
        time.sleep(1)
        print(number)


#获取赛事信息
def get_today_odds():
    global odds,ods,nub,yy
    if count01%3>0:
        #count01-=3
        nub=random.randint(2, 3)
        print("count01%3取值："+str(count01%3))
        print("取模随机取值：" + str(nub))
    else:
        nub=3
        #nub = random.randint(1, 3)
        print("随机早盘取值："+str(nub))
    if nub==1:
        ods="滚球盘"
        yy="INPLAY"
    if nub==2:
        ods="今日盘"
        yy="TODAY"
    if nub==3:
        ods="早盘"
        yy = "EARLY"
    print("下注盘：" + str(ods))
    ods_list.append(ods)
    url = "http://192.168.10.120:6210/creditMatchPC/matchList"
    headers01 = {
        'content-type': 'application/json',
        'lang':'ZH',
        'accessCode':toten
    }
    if nub==1 or nub==2:
        data = {
            "sort": 2,
            "periodId": yy,
            "highlight": False,
            "marketGroupId": "100",
            "sportCategoryId": "sr:sport:1",
            "oddsType": 1,
            "tournamentIds": [],
            "matchIds": [],
            "page": 1,
            "limit": 500}
    if nub==3:
        data = {
            "sort": 2,
            "periodId": yy,
            "highlight": False,
            "marketGroupId": "100",
            "sportCategoryId": "sr:sport:1",
            "oddsType": 1,
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
    #test_01=results['data']['data'][0]['matchList'][0]['matchId']
    #print(test_01)
    # 遍历取出对应的赛事matchid
    '''
    nub==1 代表:滚球盘
    nub==2 代表:今日盘
    nub==3 代表:早盘
    '''
    if nub==1:
        if len(INPLAY_matchid_list)==0:
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
            print("共计赛事：" + str(len(INPLAY_matchid_list)))
        else:
            print("共计赛事：" + str(len(INPLAY_matchid_list)))
    if nub==2:
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
            print("共计赛事：" + str(len(TODAY_matchid_list)))
        else:
            print("共计赛事：" + str(len(TODAY_matchid_list)))
    if nub==3:
        if len(EARLY_matchid_list) == 0:
            response = requests.post(url=url, headers=headers01, json=data)
            # 返回结果json转化
            results = json.loads(response.text)
            # print(results)
            odds = results['data']['data']
            oddt_list.append(odds)
            for i in odds:
                matchlist=i['matchList']
                for matchinfo in matchlist:
                    EARLY_matchid_list.append(matchinfo['matchId'])
            print("共计赛事：" + str(len(EARLY_matchid_list)))
        else:
            print("共计赛事：" + str(len(EARLY_matchid_list)))
#根据赛事ID，遍历每一场赛事的盘口
def get_odds():
    global isLive,num_outcomeId,aa,bb,cc,dd,ee,matchId,count01
    #设置随机数，记录已下注的比赛
    '''
    if nub==1:
        num = len(INPLAY_matchid_list)
        if num==0:
            get_today_odds()
            get_odds()
        else:
            number = random.randint(0, num - 1)
            if number in num_list:
                get_odds()
            else:
                #print(INPLAY_matchid_list[number])
                matchId = INPLAY_matchid_list[number]
                num_list.append(INPLAY_matchid_list[number])
                print("下注赛事ID：" + str(matchId))
    if nub==2:
        num = len(TODAY_matchid_list)
        if num==0:
            get_today_odds()
            get_odds()
        else:
            number = random.randint(0, num - 1)
            if number in num_list:
                get_odds()
            else:
                #print(TODAY_matchid_list[number])
                matchId = TODAY_matchid_list[number]
                num_list.append(TODAY_matchid_list[number])
                print("下注赛事ID：" + str(matchId))

    if nub==3:
        num = len(EARLY_matchid_list)
        number = random.randint(0, num-1)
        if number in num_list:
            get_odds()
        else:
            matchId = EARLY_matchid_list[number]
            num_list.append(EARLY_matchid_list[number])
            print("下注赛事ID：" + str(matchId))
    '''


    url = "http://192.168.10.120:6210/creditMatchPC/totalMarketList?"
    headers01 = {
        'content-type': 'application/json',
        'lang':'ZH',
        'accessCode':toten
    }
    data = {
        "matchId":"sr:match:31002137",
        "oddsType":1,
        "sportCategoryId":"sr:sport"
    }
    #"matchId": matchId,
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    #print(results)
    isLive = results['data']['isLive']
    #print(isLive)

    '''
    #outcomeId=results['data']['marketList'][0]['outcomeList'][0][0]['outcomeId']
    # print(outcomeId)
    num_outcomeId=len(results['data']['marketList'])
    #print(num_outcomeId)
    print("下注盘口:" + str(num_outcomeId) + "个")
    if num_outcomeId==0:
        print("-----------------------------------------------------------"+ods+"无法下注，请重新选择-----------------------------------------------------------")
    #判断盘口ID，是否为0，为0重新取

    if num_outcomeId==0:
            count01=count01+1
            get_today_odds()
            get_odds()
    else:
        # 遍历取出盘口ID,方便下注
        for i in range(0,len(results['data']['marketList'])):
            outcomeId_lsit.append(results['data']['marketList'][i]['outcomeList'][0][0]['outcomeId'])
            odds_list.append(results['data']['marketList'][i]['outcomeList'][0][0]['odds'])
            oddsType_list.append(results['data']['marketList'][i]['outcomeList'][0][0]['oddsType'])

            aa = results['data']['awayTeamName']
            bb = results['data']['homeTeamName']
            cc_list.append(results['data']['marketList'][i]['outcomeList'][0][0]['betOutComeName'])
            dd_list.append(results['data']['marketList'][i]['outcomeList'][0][0]['marketName'])
            ee_list.append(results['data']['marketList'][i]['outcomeList'][0][0]['outcomeName'])
        #print(outcomeId_lsit)
        #print(odds_list)
        #print(oddsType_list)
        print("下注赛事：" + aa+"VS"+bb)
        print("-------------------------------------------------------分割线--------------------------------------------------")
    return outcomeId_lsit,odds_list,oddsType_list,isLive,num_outcomeId,matchId
    '''

#下注
def get_submitbet(pkk):
    global betAmount
    betAmount="10"
    url = str(URL)+"/creditBet/submit"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode':toten_list[pkk]
    }
    # data = {
    # "oddsChangeType":1,
    # "betAmount":betAmount,
    # "betType":0,
    # "betId":1641955081804,
    # "selections":[
    # {
    # # "isLive":isLive,
    # "isLive": False,
    # "originalOdds": 2.38,
    # "creditOdds":  2.33,
    # "outcomeId": "sr:match:31002137_18_total=3.25_12",
    # "oddsType": 1
    # }],
    # # "mixedNum": ["1_1_0_10"],
    # "mixedNum": ["6_57_1_10"],
    # "browserFingerprintId":"5ec55c2d078b1b2f30986bb78a518511",
    # "terminal":"pc",
    # "betIp":"192.168.10.120"
    # }
    data={
        "oddsChangeType": 1,
        "mixedNum": ["6_57_1_10"],
        # "mixedNum": ["1_1_0_100"],
        # "mixedNum": ["6_1_0_10"],
        "betId": 1642830114658,
        "selections": [
            {"isLive": False, "originalOdds": 2.01, "creditOdds": 1.96,
             "outcomeId": "sr:match:30675429_18_total=2.25_12", "oddsType": 1},
            {"isLive": False, "originalOdds": 1.98, "creditOdds": 1.93,
             "outcomeId": "sr:match:30675433_18_total=2.25_13", "oddsType": 1},
            {"isLive": False, "originalOdds": 1.86, "creditOdds": 1.81,
             "outcomeId": "sr:match:30675435_18_total=2.75_12", "oddsType": 1},
            {"isLive": False, "originalOdds": 1.85, "creditOdds": 1.8,
             "outcomeId": "sr:match:30675437_18_total=2.75_13", "oddsType": 1},
            {"isLive": False, "originalOdds": 1.73, "creditOdds": 1.68,
             "outcomeId": "sr:match:27977204_18_total=2.75_12", "oddsType": 1},
            {"isLive": False, "originalOdds": 1.63, "creditOdds": 1.58, "outcomeId": "sr:match:28748058_18_total=2_12",
             "oddsType": 1}
        ],
        "browserFingerprintId": "5ec55c2d078b1b2f30986bb78a518511",
        "terminal": "pc",
        "betIp": "192.168.10.120"
    }
    # ['28176710', '28176712', '28382106', '28382104', '28382470', '27751480']
    # match_list = ['28892786', '28892780', '28892776', '27958254', '27958268', '27958262']
    # ['31043649', '31384331', '31275647', '31275651', '27772262', '27772260']

    '''
    "originalOdds":(int(odds_list[i])+0.05),
    "creditOdds":odds_list[i],
    "outcomeId":outcomeId_lsit[i],
    "oddsType":oddsType_list[i]
    '''
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    code=results['code']
    orderNo=results['data']['orderNo']
    orderNo_list.append(orderNo)
    if code==0:
        # print(str(name)+"投注成功")
        print(str(pkk) + "投注成功:")
        print("---------------------------------------------------------分割线------------------------------------------------------------------")
    else:
        print(code,results['message'])
        exit()
    '''
    #print(results)
    orderNo=results['data']['orderNo']
    orderNo_list.append(orderNo)
    print("{正在下注用户："+name,"已成功投注项："+str((i+1))," 正在投注项："+"未开启多线程"," 未投注项："+str((num_outcomeId-i-1))+" 投注orderNo："+str(orderNo)+"}"+"\n")

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    now01=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # 写入订单号
    path01 = "C:\\test\\get_test\\order_no\\" + name+ ".txt"
    f = open(path01, 'a')
    f.write(orderNo+ "\n")

    # 写入订单详情
    path02 = "C:\\test\\get_test\\order_no_test\\" + name+ ".txt"
    f = open(path02, 'a')
    f.write(
        "投注比赛ID："+matchId+"\n" +
        "投注比赛 ：" + aa + "VS" + bb + "\n" +
        "投注时间 ：" + now + "\n" +
        "投注金额 ：" + betAmount + "\n" +
        "投注盘口ID :" + outcomeId_lsit[i] + "\n" +
        "投注盘口： " + cc_list[i] + "-" + dd_list[i] + "-" + ee_list[i] + "\n" +
        "投注赔率: " + str(odds_list[i]) + "\n"+
        "orderNo: " + orderNo+ "\n" + "\n"
    )
    if i==(int(num_outcomeId)-1):
        print("已下注比赛ID："+str(matchId))
        print("已下注比赛订单号："+str(orderNo_list))
        print("已下注比赛盘口ID："+str(outcomeId_lsit))
        print("---------------------------------------------------------分割线------------------------------------------------------------------"+"\n")
        # 写入比赛ID：
        path01 = "C:\\test\\get_test\\matchid\\" + name + now01 + ".txt"
        f = open(path01, 'a')
        f.write(matchId + "\n")
        #写入比赛ID
        path01 = "C:\\test\\get_test\\matchid.txt"
        f = open(path01, 'a')
        f.write(matchId + "\n")
        # 清空下注相关列表
        outcomeId_lsit.clear()
        odds_list.clear()
        oddsType_list.clear()
        orderNo_list.clear()
        kkkk_lsit.clear()
        cc_list.clear()
        dd_list.clear()
        ee_list.clear()
    '''

if __name__=='__main__':
    # for j in range(704, 1001):
    #     get_toten(j)
    #     # get_balance(j)
    #     get_submitbet()

    # print(orderNo_list)
    # print(len(orderNo_list))
        with ThreadPoolExecutor(max_workers=10) as t:  # 创建一个最大容纳数量为5的线程池
            for j in range(0, 1001):
                task1 = t.submit(get_toten,j)
            get_time(80)
            print(len(toten_list))
            print(toten_list)
            get_time(10)
            with ThreadPoolExecutor(max_workers=3) as t1:  # 创建一个最大容纳数量为5的线程池
                for i in range(0, len(toten_list)):
                    task2 = t1.submit(get_submitbet,i)
                    # task2 = t1.submit(get_balance,i
                get_time(180)
                print(orderNo_list)
                print(len(orderNo_list))














'''
if __name__=='__main__':
    for j in range(34,38):
        get_toten()
        get_today_odds()
        get_odds()
        #num_outcomeId
        for i in range(0,int(num_outcomeId)):
            get_submitbet()
        if j==37:
            # 写入比赛ID
            path01 = "C:\\test\\get_test\\matchid.txt"
            f = open(path01, 'a')
            f.write("---------------------------------------------------------分割线------------------------------------------------------------------"+"\n")
            print("已下注比赛ID："+str(num_list))
            print("共计下注比赛：" + str(len(num_list))+"场")
            print("共计下注盘："+str(ods_list))
'''

