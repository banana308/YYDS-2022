import time
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import requests
import json
import base64
import random
import datetime
from concurrent.futures import ThreadPoolExecutor

#120测试环境
# URL="http://192.168.10.120:8093"
# URL="http://192.168.10.120:8093"


#rsa加密账号、密码
def rsa_encrypt(data):
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


def login_zt(URL):
    #调用登录接口
    url = str(URL) + "/system/accountLogin"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = {
        "userName":rsa_encrypt(data="Duxin001"),
        "password":rsa_encrypt(data="Bfty123456"),
        "googleCode":"123456",
        "loginDiv":222333
    }
    session=requests.session()
    response = session.post(url=url, headers=headers, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    # print(f"总台登录的接口日志：{results}")
    token=results['data']['token']
    id=results['data']['id']
    if results['data']['loginStatus']=='登录成功':
        print(f"总台登录成功,token：{token}\n")

    #过渡调用函数：
    url01 = str(URL) + "/system/userDetailByToken?"
    headers01 = {
        'Content-Type': 'application/json;charset=UTF-8',
        'LoginDiv':'222333',
        'Account_Login_Identify': token
    }
    data01 = {
        "token": token,
        "accountId": id
    }
    session = requests.session()
    response01 = session.get(url=url01, headers=headers01, params=data01)
    # 返回结果json转化
    results = json.loads(response01.text)
    D0_registered(URL=URL, token=token, ZD_list=ZD_list)



def login(URL,userName_list,password_list,securityCode_list,all_user):
    #登0~登3登录获取token
    url = str(URL) + "/system/accountLogin"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    # data = {"userName":rsa_encrypt(data=userName_list[i]),
    #         "password":rsa_encrypt(data=password_list[i]),
    #         "securityCode":securityCode_list[i],
    #         "loginDiv":555666}
    data = {"userName": rsa_encrypt(data=userName_list[i]),
            "password": rsa_encrypt(data=password_list[i]),
            "securityCode": securityCode_list[i],
            "loginDiv": 555666}
    session = requests.session()
    response = session.post(url=url, headers=headers, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    token = results['data']['token']
    id = results['data']['id']


    if results['code']==0:
        token = results['data']['token']
        id_list.append(id)
        # token_list.clear()
        token_list.append(token)
        print(f"{userName_list[i]}:{results['data']['loginStatus']},token:{token},id:{id}")
        all_user_old[i][f'登{i}的账号']=userName_list[i]
    else:
        print(f"登{i}登录的接口日志：{results}")

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
    results01 = json.loads(response01.text)
    # print(results01)



    client_user(URL=URL, token=token, id_list=id_list, loginAccount_list=loginAccount_list,all_user_new=all_user_new)
    client_password(URL=URL, token=token, id_list=id_list, password_list=password_list, content_list=content_list,all_user_new=all_user_new,all_user_old=all_user_old)
    if i==3:
        pass
    else:
        D1_D3_registered(URL=URL, token=token, ZD_list=ZD_list,i=i+1)
    return token







def D0_registered(URL,token,ZD_list):
    url = str(URL) + "/mainstation/generalAgentManagement/addGeneralAgent"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'LoginDiv':'222333',
        'Account_Login_Identify': token
    }
    data = {
        "account": ZD_list[i][i]["account"],
        "credits": ZD_list[i][i]['credits'],
        "name": ZD_list[i][i]['name'],
        "password": ZD_list[i][i]['password'],
        "securityCode": ZD_list[i][i]['securityCode'],
        "accountStatus": 0,
        "maxProfitLossPercentage": ZD_list[i][i]['maxProfitLossPercentage'],
        "minProfitLossPercentage": ZD_list[i][i]['minProfitLossPercentage'],
        "commissionAndBettingLimitCollection": [
            {
                "hcpOu": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "inplay": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "winner": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "other": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "sportId": "1"
            },
            {
                "hcpOu": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "inplay": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "winner": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "other": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "sportId": "100"
            },
            {
                "hcpOu": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "inplay": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "winner": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "other": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "sportId": "2"
            }
        ]
    }
    # print(data)
    session = requests.session()
    response = session.post(url=url, headers=headers, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    print(f"登{i}创建的接口日志：{results}\n")


    if results['data']['code']==0:
        userName_list.append(ZD_list[i][i]['account'])
        securityCode_list.append(ZD_list[i][i]['securityCode'])
        password_list.append(ZD_list[i][i]['password'])
        print(f"\033[32m登{i}的:{ZD_list[i][i]['name']},额度:{ZD_list[i][i]['credits']}\033[0m\n"
              f"\033[32m登{i}的账号：{ZD_list[i][i]['account']},密码:{ZD_list[i][i]['password']},安全码:{ZD_list[i][i]['securityCode']}\033[0m\n"
              f"\033[32m登{i}创建成功\033[0m\n")


def D1_D3_registered(URL,token,ZD_list,i):
    url = str(URL) + "/account/insertRetreatAndBetting"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'LoginDiv':'555666',
        'Account_Login_Identify': token
          }
    # print(token_list)
    data = {
        "accountInsertParam": {
            "credits": ZD_list[i][i]['credits'],
            "account": ZD_list[i][i]['account'],
            "maxProfitLossPercentage": ZD_list[i][i]['maxProfitLossPercentage'],
            "minProfitLossPercentage": ZD_list[i][i]['minProfitLossPercentage'],
            "parentProfitLossPercentage": 20,
            "accountStatus": 0,
            "name": ZD_list[i][i]['name'],
            "password": ZD_list[i][i]['password'],
            "securityCode": ZD_list[i][i]['securityCode']
        },
        "retreat": [
            {
                "hcpOu": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "inplay": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "winner": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "other": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "sportId": "1"
            },
            {
                "hcpOu": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "inplay": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "winner": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "other": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "sportId": "100"
            },
            {
                "hcpOu": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "inplay": {
                    "retreatValueA": 10,
                    "retreatValueB": 10,
                    "retreatValueC": 10,
                    "retreatValueD": 10,
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "winner": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "other": {
                    "singleBetMax": ZD_list[i][i]['singleBetMax'],
                    "singleHighest": ZD_list[i][i]['singleHighest']
                },
                "sportId": "2"
            }
        ]
    }
    session = requests.session()
    response = session.post(url=url, headers=headers, json=data)
    # 返回结果json转化
    results = json.loads(response.text)
    print(f"登{i}的创建的接口日志：{results}")

    if results['data']['code']==0:
        userName_list.append(ZD_list[i][i]['account'])
        securityCode_list.append(ZD_list[i][i]['securityCode'])
        password_list.append(ZD_list[i][i]['password'])
        print(f"\033[32m登{i}的:{ZD_list[i][i]['name']},额度:{ZD_list[i][i]['credits']}\033[0m\n"
              f"\033[32m登{i}的账号：{ZD_list[i][i]['account']},密码:{ZD_list[i][i]['password']},安全码:{ZD_list[i][i]['securityCode']}\033[0m\n"
              f"\033[32m登{i}创建成功\033[0m\n")



def client_user(URL,token,id_list,loginAccount_list,all_user_new):
    url = str(URL) + "/system/checkLoginAccount"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'LoginDiv': '555666',
        'Account_Login_Identify': token
    }
    data={
            "id": id_list[i],
            "loginAccount": loginAccount_list[i]
    }
    session = requests.session()
    response = session.post(url=url, headers=headers, json=data)
    results = json.loads(response.text)
    code = results['code']
    if code != 0:
        print(f"\033[31m登{i}的用户：{userName_list[i]}，账号查询的接口日志：{results}\033[0m")
    else:
        url01 = str(URL) + "/system/inputLoginAccount"
        headers01 = {
            'Content-Type': 'application/json;charset=UTF-8',
            'LoginDiv': '555666',
            'Account_Login_Identify': token_list[-1]
        }
        data01 = {
            "id": id_list[i],
            "loginAccount": loginAccount_list[i]
        }
        response01 = requests.post(url=url01, headers=headers01, json=data01)
        results01 = json.loads(response01.text)
        code01 = results01['code']
        if code01 == 0:
            print(f"\033[32m登{i}的用户：{userName_list[i]}，修改账号：{loginAccount_list[i]} 成功\033[0m\n")
            all_user_new[i][f'登{i}的账号'] =loginAccount_list[i]
        else:
            print(f"登{i}的用户：{userName_list[i]}，账号修改的接口日志：{id_list[i]}")




def client_password(URL,token,id_list,password_list,content_list,all_user_new,all_user_old):

    url = str(URL) + "/account/changePasswordOrStatus"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'LoginDiv': '555666',
        'Account_Login_Identify': token
    }

    data = {
            "accountId": int(id_list[i]),
            "content": rsa_encrypt(data=content_list[i]),
            "oldPassword": rsa_encrypt(data=password_list[i]),
            "type": True
    }
    session = requests.session()
    response = session.post(url=url, headers=headers, json=data)
    results = json.loads(response.text)
    code = results['code']
    if code==0:
        print(f"\033[32m登{i}的用户：{userName_list[i]}，修改密码:{password_list[i]}成功\033[0m\n")
        all_user_new[i][f"登{i}的密码"] = password_list[i]
        all_user_new[i][f"登{i}的安全码"] = securityCode_list[i]

        all_user_old[i][f"登{i}的密码"] = password_list[i]
        all_user_old[i][f"登{i}的安全码"] =securityCode_list[i]
    else:
        # print(f"用户：{userName_list[i]}，修改密码的接口日志：{results}")
        print(f"\033[31m{results}\033[0m")




#循环打印新老账号：
def get_for():
    print("老账号全部打印:")
    for i in range(0,len(all_user_old)):
        print(f"\033[34m{all_user_old[i]}\033[0m")
        if i==3:
            print(f"\n\n")

    print("新账号全部打印:")
    for i in range(0, len(all_user_new)):
        print(f"\033[31m{all_user_new[i]}\033[0m")






if __name__=='__main__':
    # MDE环境
    URL="https://mdesearch.betf.best"

    all_user_old=[{},{},{},{}]
    all_user_new = [{},{},{},{}]
    token_list=[]
    id_list=[]
    userName_list=[]
    password_list=[]
    securityCode_list=[]
    #账号界面的新账号设置列表
    loginAccount_list=['yyds01','yyds02','yyds03','yyds04']
    #修改密码界面的新密码设置列表
    content_list=['Bfta123456','Bfty123456','Bfty123456','Bfty123456']

    ZD_list = [
              {0:{"credits": 100000000, "account": 'x8',
                  "name": '测试总代', "password": 'Bfty123456', "securityCode": 'Bf123456',
                  "maxProfitLossPercentage": 90, "minProfitLossPercentage": 80,
                  "singleHighest": 100000, "singleBetMax": 50000}},

              {1:{"credits": 40000000, "account": 'x8y1',
                  "name": '测试登1', "password": 'Bfty123456', "securityCode": 'Bf123456',
                  "maxProfitLossPercentage": 70, "minProfitLossPercentage": 60,
                  "parentProfitLossPercentage": 20,
                  "singleHighest": 100000, "singleBetMax": 50000}},

              {2: {"credits": 35000000, "account": 'x8y1y2',
                   "name": '测试登2', "password": 'Bfty123456', "securityCode": 'Bf123456',
                   "maxProfitLossPercentage": 50, "minProfitLossPercentage": 40,
                   "parentProfitLossPercentage": 20,
                   "singleHighest": 100000, "singleBetMax": 50000}},

              {3: {"credits": 30000000, "account": 'x8y1y2y3',
                   "name": '测试登3', "password": 'Bfty123456', "securityCode": 'Bf123456',
                   "maxProfitLossPercentage": 30, "minProfitLossPercentage": 20,
                   "parentProfitLossPercentage":20,
                   "singleHighest": 100000, "singleBetMax": 50000}}
               ]


    for i in range(0,4):
        if i==0:
            login_zt(URL)
            login(URL, userName_list, password_list, securityCode_list,all_user_old)
        else:
            login(URL, userName_list, password_list, securityCode_list,all_user_old)
            if i==3:
                get_for()






