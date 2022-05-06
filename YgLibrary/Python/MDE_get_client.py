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
num=['Duxin05tk', 'Duxin05tl', 'Duxin05tm', 'Duxin05tn', 'Duxin05to', 'Duxin05tp', 'Duxin05tq', 'Duxin05tr', 'Duxin05tt', 'Duxin05tv', 'Duxin05tw', 'Duxin05tx', 'Duxin05ty', 'Duxin05tz', 'Duxin05ts', 'Duxin05ua', 'Duxin05ub', 'Duxin05uc', 'Duxin05ud', 'Duxin05ue', 'Duxin05uf', 'Duxin05ug', 'Duxin05uh', 'Duxin05ui', 'Duxin05uj', 'Duxin05uk', 'Duxin05ul', 'Duxin05um', 'Duxin05un', 'Duxin05uo', 'Duxin05up', 'Duxin05uq', 'Duxin05ur', 'Duxin05ut', 'Duxin05uv', 'Duxin05ux', 'Duxin05uy', 'Duxin05uz', 'Duxin05us', 'Duxin05va', 'Duxin05vb', 'Duxin05vc', 'Duxin05vd', 'Duxin05ve', 'Duxin05vf', 'Duxin05vg', 'Duxin05vh', 'Duxin05vi', 'Duxin05vj', 'Duxin05vk', 'Duxin05vl', 'Duxin05vm', 'Duxin05vn', 'Duxin05vo', 'Duxin05vp', 'Duxin05vq', 'Duxin05vr', 'Duxin05vs', 'Duxin05vt', 'Duxin05vu', 'Duxin05vw', 'Duxin05vx', 'Duxin05vy', 'Duxin05vz', 'Duxin05wa', 'Duxin05wb', 'Duxin05wc', 'Duxin05wd', 'Duxin05we', 'Duxin05wf', 'Duxin05wg', 'Duxin05wh', 'Duxin05wi', 'Duxin05wj', 'Duxin05wk', 'Duxin05wl', 'Duxin05wm', 'Duxin05wn', 'Duxin05wo', 'Duxin05wp', 'Duxin05wq', 'Duxin05wr', 'Duxin05ws', 'Duxin05wt', 'Duxin05wu', 'Duxin05ww', 'Duxin05wy', 'Duxin05wz', 'Duxin05wv', 'Duxin05xa', 'Duxin05xb', 'Duxin05xc', 'Duxin05xd', 'Duxin05xe', 'Duxin05xf', 'Duxin05xg', 'Duxin05xh', 'Duxin05xi', 'Duxin05xj', 'Duxin05xk', 'Duxin05xl', 'Duxin05xm', 'Duxin05xn', 'Duxin05xo', 'Duxin05xp', 'Duxin05xq', 'Duxin05xr', 'Duxin05xs', 'Duxin05xt', 'Duxin05xu', 'Duxin05xw', 'Duxin05xy', 'Duxin05xv', 'Duxin05ya', 'Duxin05yb', 'Duxin05yc', 'Duxin05yd', 'Duxin05ye', 'Duxin05yf', 'Duxin05yg', 'Duxin05yh', 'Duxin05yi', 'Duxin05yj', 'Duxin05yk', 'Duxin05yl', 'Duxin05ym', 'Duxin05yn', 'Duxin05yo', 'Duxin05yp', 'Duxin05yq', 'Duxin05yr', 'Duxin05ys', 'Duxin05yt', 'Duxin05yu', 'Duxin05yv', 'Duxin05yw', 'Duxin05yx', 'Duxin05yz', 'Duxin05za', 'Duxin05zb', 'Duxin05zc', 'Duxin05zd', 'Duxin05ze', 'Duxin05zf', 'Duxin05zg', 'Duxin05zh', 'Duxin05zi', 'Duxin05zj', 'Duxin05zk', 'Duxin05zl', 'Duxin05zm', 'Duxin05zn', 'Duxin05zo', 'Duxin05zp', 'Duxin05zq', 'Duxin05zr', 'Duxin05zs', 'Duxin05zt', 'Duxin05zu', 'Duxin05zv', 'Duxin05zw', 'Duxin05zx', 'Duxin05zz']
toten_list=[]
#请求登录接口，获取toten
def get_toten(i):
    global toten,name
    # name=num[i]
    # name=num
    name = "fceshi0" + str(int(i))
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
    name01="FCeshi0"+str(int(j)+1449)
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
    for i in range(1451, 1612):
        print(i)
        get_toten(i)
        # get_register01(i)
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





