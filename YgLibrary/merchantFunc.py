import requests
import hashlib

try:
    from .MysqlFunc import MysqlCommonQuery
except ImportError or ModuleNotFoundError:
    from MysqlFunc import MysqlCommonQuery


class MerchantFunc(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, merchant_url, *args):
        self.host = merchant_url
        self.mysql = MysqlCommonQuery(mysql_info)
        self.session_1 = requests.session()
        self.session_2 = requests.session()

    def login_client(self, user_name, password):
        """
        注册或登录
        :param password:
        :param user_name:
        :return:
        """
        headers = {"Content-Type": "application/json"}
        url = self.host + "/creditUser/creditUserLogIn"
        params = {"userName": user_name, "password": hashlib.md5(bytes(password, encoding='utf-8')).hexdigest()}
        rtn = self.session_2.post(url, json=params, headers=headers, timeout=60)
        content = rtn.json()
        if content["message"] != "OK":
            return "登录或注册失败，原因：\n" + content["message"]
        return content["code"]


if __name__ == "__main__":
    url1 = 'http://192.168.10.120:7210'
    mysql_info1 = ['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']
    mf = MerchantFunc(mysql_info1, url1)
    print(mf.login_client("XyUser001", "Ygty123456"))
