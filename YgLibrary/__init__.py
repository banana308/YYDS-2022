import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from BackendUserManageFunc import BackendUserManageFuncOfMysql
from BackendUserManageFunc import AgentBackendUserManageFuncOfInterface
from YgClient import YgClient, ClientFuncOfMysql
from CommonFunc import CommonFunc
from MongoFunc import DbQuery
from BackendOperateFunc import OperateFuncOfMysql, OperateFuncOfInterface
from BackendReportFunc import ReportFuncOfMysql, ReportFuncOfInterface
from BackendOrderFunc import OrderFuncOfMysql, OrderFuncOfInterface


class YgLibrary(ReportFuncOfMysql, ClientFuncOfMysql, OrderFuncOfMysql, OperateFuncOfMysql,
                BackendUserManageFuncOfMysql, CommonFunc, DbQuery, ReportFuncOfInterface, OperateFuncOfInterface,
                OrderFuncOfInterface, AgentBackendUserManageFuncOfInterface, YgClient):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, client_host, backend_host):
        ReportFuncOfMysql.__init__(self, mysql_info, mongo_info)
        ReportFuncOfInterface.__init__(self, mysql_info, backend_host)
        CommonFunc.__init__(self)
        DbQuery.__init__(self, mongo_info)
        YgClient.__init__(self, mysql_info, mongo_info, client_host)
