class ConnectMysqlException(Exception):
    def __str__(self):
        return "【Err】Mysql连接超时"


class ConnectMongoException(Exception):
    def __str__(self):
        return "【Err】Mysql连接超时"


class ConnectBackendException(Exception):
    def __str__(self):
        return "【Err】管理后台连接超时"


class ParamNotExistException(Exception):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return "【Err】传参【%s】不正确" % self.param


class ValuesNotEqualException(Exception):
    def __init__(self, expect, exact):
        self.expect = expect
        self.exact = exact

    def __str__(self):
        return "【Err】数据比对不一致，期望值[%s], 实际值[%s]" % (self.expect, self.exact)


class SendCtrlCmdFailedException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "【Err】执行Ctrl指令失败: " + self.data


class WaitForExpectedValueError(Exception):
    def __init__(self, data, timeout):
        self.data = data
        self.timeout = timeout

    def __str__(self):
        return "【Err】等待%s秒后，预期结果'%s'未出现" % (self.timeout, self.data)
