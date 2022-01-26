# -*- coding:utf-8 -*-

import requests
import time

try:
    from .MysqlFunc import MysqlCommonQuery
    from .CommonFunc import CommonFunc
    from .MyExceptions import *
    from .Config import *
    from .MongoFunc import DbQuery
except Exception:
    from MysqlFunc import MysqlCommonQuery
    from CommonFunc import CommonFunc
    from MyExceptions import *
    from Config import *
    from MongoFunc import DbQuery

sport_name_id_dic = {}
for value in sport_id_dic.items():
    sport_name_id_dic[value[1]] = value[0]


class Backend(object):
    """
    总台
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    mysql = ""

    def __init__(self, mysql_info, backend_url="http://192.168.10.11:6100", *args, **kwargs):
        self.session = requests.session()
        self.auth_url = backend_url
        self.head_bd = {"Authorization": ""}
        self.cf = CommonFunc()
        self.args = args

    def login_main(self, uname, pwd='Ygty123456', security_code="", login_type="总台"):
        """
        登录总台
        :param uname:
        :param pwd:
        :param security_code:
        :param login_type: 总台|代理
        :return:
        """
        login_div_dic = {"总台": "222333", "代理": "555666"}
        url = self.auth_url + "/system/accountLogin"
        data = {"userName": self.cf.rsa_encrypt(uname),
                "password": self.cf.rsa_encrypt(pwd),
                "securityCode": security_code,
                "loginDiv": login_div_dic[login_type]}
        self.head_bd["loginDiv"] = login_div_dic[login_type]
        for loop in range(3):
            try:
                rsp = self.session.post(url, json=data, timeout=600)
                if rsp.json()["message"] != 'OK' or not rsp.json()["data"]:
                    return rsp.json()["message"]
                self.head_bd["Account_Login_Identify"] = rsp.json()["data"]["token"]
                return
            except ConnectionError:
                time.sleep(2)
                continue
            except Exception as e:
                print(e)
        raise ConnectBackendException()


if __name__ == "__main__":
    mysql_info = ['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']
    mongo_info = ['app', '123456', '192.168.10.120', '27017']
    bk = Backend(mysql_info)

    # 赛果
    bk.login_main("Xingyao123", "Abc123456")
