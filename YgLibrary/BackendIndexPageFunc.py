# -*- coding:utf-8 -*-

try:
    from .MysqlFunc import MysqlCommonQuery
    from .CommonFunc import CommonFunc
    from .MyExceptions import *
    from .Backend import Backend
    from .Config import *
except Exception:
    from MysqlFunc import MysqlCommonQuery
    from CommonFunc import CommonFunc
    from MyExceptions import *
    from Backend import Backend
    from Config import *


class BackendIndexPageFuncOfMysql(MysqlCommonQuery):
    """
    管理后台首页相关的MYSQL功能
    """
    def __init__(self, mysql_info, *args, **kwargs):
        super().__init__(mysql_info)
        self.cf = CommonFunc()


class BackendIndexPageFuncOfInterface(Backend):
    """
        管理后台的用户管理模块，接口相关的功能
    """
    def __init__(self, mysql_info, backend_url="http://192.168.10.11:8082"):
        super().__init__(mysql_info, backend_url)
        self.mysql = BackendIndexPageFuncOfMysql(mysql_info)
