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
num=['d0d1d2d30a', 'd0d1d2d30b', 'd0d1d2d30c', 'd0d1d2d30d', 'd0d1d2d30e', 'd0d1d2d30f', 'd0d1d2d30g', 'd0d1d2d30h', 'd0d1d2d30i', 'd0d1d2d30j', 'd0d1d2d30k', 'd0d1d2d30l', 'd0d1d2d30m', 'd0d1d2d30n', 'd0d1d2d30o', 'd0d1d2d30p', 'd0d1d2d30q', 'd0d1d2d30r', 'd0d1d2d30s', 'd0d1d2d30t', 'd0d1d2d30u', 'd0d1d2d30v', 'd0d1d2d30w', 'd0d1d2d30x', 'd0d1d2d30y', 'd0d1d2d30z', 'd0d1d2d31a', 'd0d1d2d31b', 'd0d1d2d31c', 'd0d1d2d31d', 'd0d1d2d31e', 'd0d1d2d31f', 'd0d1d2d31g', 'd0d1d2d31h', 'd0d1d2d31i', 'd0d1d2d31j', 'd0d1d2d31k', 'd0d1d2d31l', 'd0d1d2d31m', 'd0d1d2d31n', 'd0d1d2d31o', 'd0d1d2d31p', 'd0d1d2d31q', 'd0d1d2d31r', 'd0d1d2d31s', 'd0d1d2d31t', 'd0d1d2d31u', 'd0d1d2d31v', 'd0d1d2d31w', 'd0d1d2d31x', 'd0d1d2d31y', 'd0d1d2d31z', 'd0d1d2d32a', 'd0d1d2d32b', 'd0d1d2d32c', 'd0d1d2d32d', 'd0d1d2d32e', 'd0d1d2d32f', 'd0d1d2d32g', 'd0d1d2d32h', 'd0d1d2d32i', 'd0d1d2d32j', 'd0d1d2d32k', 'd0d1d2d32l', 'd0d1d2d32m', 'd0d1d2d32n', 'd0d1d2d32o', 'd0d1d2d32p', 'd0d1d2d32q', 'd0d1d2d32r', 'd0d1d2d32s', 'd0d1d2d32t', 'd0d1d2d32u', 'd0d1d2d32v', 'd0d1d2d32w', 'd0d1d2d32x', 'd0d1d2d32y', 'd0d1d2d32z', 'd0d1d2d33a', 'd0d1d2d33b', 'd0d1d2d33c', 'd0d1d2d33d', 'd0d1d2d33e', 'd0d1d2d33f', 'd0d1d2d33g', 'd0d1d2d33h', 'd0d1d2d33i', 'd0d1d2d33j', 'd0d1d2d33k', 'd0d1d2d33l', 'd0d1d2d33m', 'd0d1d2d33n', 'd0d1d2d33o', 'd0d1d2d33p', 'd0d1d2d33q', 'd0d1d2d33r', 'd0d1d2d33s', 'd0d1d2d33t', 'd0d1d2d33u', 'd0d1d2d33v', 'd0d1d2d33w', 'd0d1d2d33x', 'd0d1d2d33y', 'd0d1d2d33z', 'd0d1d2d34a', 'd0d1d2d34b', 'd0d1d2d34c', 'd0d1d2d34d', 'd0d1d2d34e', 'd0d1d2d34f', 'd0d1d2d34g', 'd0d1d2d34h', 'd0d1d2d34i', 'd0d1d2d34j', 'd0d1d2d34k', 'd0d1d2d34l', 'd0d1d2d34m', 'd0d1d2d34n', 'd0d1d2d34o', 'd0d1d2d34p', 'd0d1d2d34q', 'd0d1d2d34r', 'd0d1d2d34s', 'd0d1d2d34t', 'd0d1d2d34u', 'd0d1d2d34v', 'd0d1d2d34w', 'd0d1d2d34x', 'd0d1d2d34y', 'd0d1d2d34z', 'd0d1d2d35a', 'd0d1d2d35b', 'd0d1d2d35c', 'd0d1d2d35d', 'd0d1d2d35e', 'd0d1d2d35f', 'd0d1d2d35g', 'd0d1d2d35h', 'd0d1d2d35i', 'd0d1d2d35j', 'd0d1d2d35k', 'd0d1d2d35l', 'd0d1d2d35m', 'd0d1d2d35n', 'd0d1d2d35o', 'd0d1d2d35p', 'd0d1d2d35q', 'd0d1d2d35r', 'd0d1d2d35s', 'd0d1d2d35t', 'd0d1d2d35u', 'd0d1d2d35v', 'd0d1d2d35w', 'd0d1d2d35x', 'd0d1d2d35y', 'd0d1d2d35z', 'd0d1d2d36a', 'd0d1d2d36b', 'd0d1d2d36c', 'd0d1d2d36d', 'd0d1d2d36e', 'd0d1d2d36f', 'd0d1d2d36g', 'd0d1d2d36h', 'd0d1d2d36i', 'd0d1d2d36j', 'd0d1d2d36k', 'd0d1d2d36l', 'd0d1d2d36m', 'd0d1d2d36n', 'd0d1d2d36o', 'd0d1d2d36p', 'd0d1d2d36q', 'd0d1d2d36r', 'd0d1d2d36s', 'd0d1d2d36t', 'd0d1d2d36u', 'd0d1d2d36v', 'd0d1d2d36w', 'd0d1d2d36x', 'd0d1d2d36y', 'd0d1d2d36z', 'd0d1d2d37a', 'd0d1d2d37b', 'd0d1d2d37c', 'd0d1d2d37d', 'd0d1d2d37e', 'd0d1d2d37f', 'd0d1d2d37g', 'd0d1d2d37h', 'd0d1d2d37i', 'd0d1d2d37j', 'd0d1d2d37k', 'd0d1d2d37l', 'd0d1d2d37m', 'd0d1d2d37n', 'd0d1d2d37o', 'd0d1d2d37p', 'd0d1d2d37q', 'd0d1d2d37r', 'd0d1d2d37s', 'd0d1d2d37t', 'd0d1d2d37u', 'd0d1d2d37v', 'd0d1d2d37w', 'd0d1d2d37x', 'd0d1d2d37y', 'd0d1d2d37z', 'd0d1d2d38a', 'd0d1d2d38b', 'd0d1d2d38c', 'd0d1d2d38d', 'd0d1d2d38e', 'd0d1d2d38f', 'd0d1d2d38g', 'd0d1d2d38h', 'd0d1d2d38i', 'd0d1d2d38j', 'd0d1d2d38k', 'd0d1d2d38l', 'd0d1d2d38m', 'd0d1d2d38n', 'd0d1d2d38o', 'd0d1d2d38p', 'd0d1d2d38q', 'd0d1d2d38r', 'd0d1d2d38s', 'd0d1d2d38t', 'd0d1d2d38u', 'd0d1d2d38v', 'd0d1d2d38w', 'd0d1d2d38x', 'd0d1d2d38y', 'd0d1d2d38z', 'd0d1d2d39a', 'd0d1d2d39b', 'd0d1d2d39c', 'd0d1d2d39d', 'd0d1d2d39e', 'd0d1d2d39f', 'd0d1d2d39g', 'd0d1d2d39h', 'd0d1d2d39i', 'd0d1d2d39j', 'd0d1d2d39k', 'd0d1d2d39l', 'd0d1d2d39m', 'd0d1d2d39n', 'd0d1d2d39o', 'd0d1d2d39p', 'd0d1d2d39q', 'd0d1d2d39r', 'd0d1d2d39s', 'd0d1d2d39t', 'd0d1d2d39u', 'd0d1d2d39v', 'd0d1d2d39w', 'd0d1d2d39x', 'd0d1d2d39y', 'd0d1d2d39z']
toten_list=[]
name_list=["A","B","C","D"]
#请求登录接口，获取toten
def get_toten(i):
    global toten,name
    name=num[i]
    # name=num
    # name = "fceshi0" + str(int(i))
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

def get_register01(i):
    global name01
    # name01=str(name[j])+str(int(j))
    name01="fceshi0"+str(int(i)+261)
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

def get_register02(i):
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
    for i in range(0, 260):
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





