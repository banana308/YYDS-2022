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
num=['bDuFCeshi0667', 'dDuFCeshi0668', 'bDuFCeshi0669', 'bDuFCeshi0670', 'bDuFCeshi0671', 'aDuFCeshi0672', 'bDuFCeshi0673', 'aDuFCeshi0674', 'cDuFCeshi0675', 'aDuFCeshi0676']
toten_list=[]
#请求登录接口，获取toten
def get_toten(open):
    global toten,name
    name=num[open]
    # name=num
    # name = "FCeshi0" + str(int(j))
    url="http://192.168.10.120:6210/creditUser/creditUserLogIn"
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
    if results['code'] == 0:
        print("登录用户："+name)
        print("toten:" + toten)
    else:
        print(results['code'], results['message'])
    # print("登录用户：" + name)
    # print("toten:" + toten)

    return toten

def get_register01(j):
    global name01
    name01="FCeshi0"+str(int(j)+991)
    # name01="FCeshi0"+str(int(j)+201)
    url = "http://192.168.10.120:6210/creditUser/setCreditUserLoginAccount?"
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

def get_register02(j):
    password="Bfty123456"
    url = "http://192.168.10.120:6210/creditUser/setCreditUserPassword?"
    headers01 = {
        'content-type': 'application/json',
        'lang': 'ZH',
        'accessCode': toten
    }
    data = {
        "oldPassword": password,
        "newPassword":password
    }
    response = requests.get(url=url, headers=headers01, params=data)
    # 返回结果json转化
    results = json.loads(response.text)
    if results['code']==0:
        print(str(name01) + "密码修改成功")
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


if __name__=='__main__':
    for i in range(0, len(num)):
        print(i)
        get_toten(i)
        get_register01(i)
        get_register02(i)







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





