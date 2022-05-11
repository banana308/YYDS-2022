import openpyxl,xlrd
from os.path import  join,abspath,dirname
import requests,json,time
import openpyxl




def test_01():
    global toten,name
    name="y1y2y3y4a1"
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
    code=results['data']['code']
    message=results['data']['message']
    print(code,message)

    assert code == 0
