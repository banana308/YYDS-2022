import requests
import json
import threading
import _thread
import datetime
import xlwt
import openpyxl
import time
import datetime
import random
import random
from concurrent.futures import ThreadPoolExecutor


num01="bDuFCeshi0400"
num=['a1b0c1d1aa', 'a1b0c1d1ba', 'a1b0c1d1bb', 'a1b0c1d1bc', 'a1b0c1d1bd', 'a1b0c1d1be', 'a1b0c1d1bf', 'a1b0c1d1bg', 'a1b0c1d1bh', 'a1b0c1d1bi', 'a1b0c1d1bj', 'a1b0c1d1bk']

toten_list=[]
name_list=["A","B","C","D"]

#120环境
# URL="http://192.168.10.120:6210"
#MDE环境
URL="https://mdesearch.betf.io"
#请求登录接口，获取toten
def get_toten(i):
    global toten,name
    name=num[i]
    # name=num
    # name = "fceshi0" + str(int(i))
    url=str(URL)+"/creditUser/creditUserLogIn"
    headers01 = {'content-type': 'application/json'}
    data ={
    "userName":name,
    # "password": "68cf63c62bc68d71fc41c028375e2f6e",
    "password":"991444c1f732105f81fa51df09c2619d",
    # "loginUrl":"http://192.168.10.120:96"
    "loginUrl":"https://mdesf.betf.io/"
    }
    response = requests.post(url=url, headers=headers01, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    #print(results)
    print(results)
    toten=results['data']['data']['accessCode']
    toten_list.append(toten)
    if results['code'] == 0:
        print("登录用户："+name)
        print("toten:" + toten)
    else:
        print(results['code'], results['message'])
    # print("登录用户：" + name)
    # print("toten:" + toten)

    return toten

def get_register01(i):
    global name01
    # name01=str(name[j])+str(int(j))
    # name01="fceshi0"+str(int(i)+1)
    name01 = "b" + str(int(i) + 1)
    url = str(URL)+"/creditUser/setCreditUserLoginAccount?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    data = {
        "loginAccount": name01,
    }
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    if results['code']==0:
        print(str(name01) + "修改账号成功")
    else:
        print(results['code'], results['message'])

def get_register02(i):
    # password="Bfty123456"
    oldPassword="Bfty123456"
    newPassword="Aa111111"
    url = str(URL)+"/creditUser/setCreditUserPassword?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    data = {
        "oldPassword": oldPassword,
        "newPassword":newPassword
    }
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    if results['code']==0:
        # print(str(name01) + "密码修改成功")
        print(str(name) + "密码修改成功")
        time.sleep(0.5)
    else:
        print(results['code'], results['message'])




threads = []
t1=threading.Thread(target=get_toten,args=())
threads.append(t1)
# t2=threading.Thread(target=get_register01,args=())
# threads.append(t2)
# t3=threading.Thread(target=get_register02,args=())
# threads.append(t3)


# if __name__=='__main__':
#     for j in range(173, len(num)):
#         print(j)
#         get_toten()
#         if j==173:
#             time.sleep(3)
#         else:
#             pass
#         try:
#             _thread.start_new_thread(get_register01, ())
#             _thread.start_new_thread(get_register02, ())
#         except:
#             print
#             "Error: unable to start thread"
#         print("---------------------------------------------------------分割线------------------------------------------------------------------")


# if __name__=='__main__':
#     for i in range(0, len(num)):
#         print(i)
#         get_toten(i)
#         get_register01(i)
#         # get_register02(i)

if __name__=='__main__':
    for i in range(0, 10):
        print(i)
        get_toten(i)
        get_register01(i)
        # get_register02(i)





# if __name__=='__main__':
#     for j in range(1, 401):
#         print(j)
#         for t in threads:
#             t.setDaemon(True)
#             t.start()
#         for t in threads:
#             t.join()

# if __name__=='__main__':
#     with ThreadPoolExecutor(max_workers=10) as t:  # 创建一个最大容纳数量为5的线程池
#         for i in range(0, len(num)):
#             task1 = t.submit(get_toten,i)
#         time.sleep(100)
#         for j in range(0,len(toten_list)):
#             task2=t.submit(get_register01,j)
#             task2=t.submit(get_register02,j)





