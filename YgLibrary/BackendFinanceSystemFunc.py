# -*- coding:utf-8 -*-
from datetime import datetime

try:
    from .MysqlFunc import MysqlCommonQuery
    from .CommonFunc import CommonFunc
    from .MyExceptions import *
    from .Backend import Backend
except Exception:
    from MysqlFunc import MysqlCommonQuery
    from CommonFunc import CommonFunc
    from MyExceptions import *
    from Backend import Backend


class FinanceSystemFuncOfMysql(MysqlCommonQuery):
    """
    管理后台财务系统模块MYSQL相关功能
    """
    def __init__(self, mysql_info, *args, **kwargs):
        super().__init__(mysql_info, args, kwargs)
        self.cf = CommonFunc()


class FinanceSystemFunc(Backend):
    """
        管理后台的用户管理模块，接口相关的功能
    """

    def __init__(self, mysql_info, backend_url="http://192.168.10.11:8083"):
        self.mysql_info = mysql_info
        super().__init__(mysql_info, backend_url)
        self.mysql = FinanceSystemFuncOfMysql(self.mysql_info)
