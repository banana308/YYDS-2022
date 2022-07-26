import pymysql
import time
try:
    from .CommonFunc import CommonFunc
    from .MyExceptions import *
    from .Config import *
except ModuleNotFoundError:
    from CommonFunc import CommonFunc
    from MyExceptions import *
    from Config import *
except ImportError:
    from CommonFunc import CommonFunc
    from MyExceptions import *
    from Config import *


class MysqlFunc(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, *args, **kwargs):
        self.connect = pymysql.connect(host=mysql_info[0], user=mysql_info[1], password=mysql_info[2], database='bfty_credit', charset='utf8', port=int(mysql_info[3]), autocommit=True)
        self.cursor = self.connect.cursor()

    # 关闭数据库
    def close_db(self):
        """
        关闭数据库
        :return:
        """
        self.cursor.close()
        self.connect.close()

    def query_data(self, sql, db_name='bfty_credit'):
        """
        数据查询
        :param sql:
        :param db_name:
        :return:
        """
        # print(sql)
        try:
            self.change_db(db_name)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except pymysql.Error as e:
            print(e)
            print(AssertionError, "查询结果为空")
            return
        return res

    def update_data(self, sql, db_name='business_order'):
        """
        修改
        :param sql:
        :param db_name:
        :return:
        """
        try:
            self.change_db(db_name)
            self.cursor.execute(sql)
            self.connect.commit()
        except Exception:
            raise(AssertionError, "修改失败！")

    def change_db(self, db_name):
        try:
            self.connect.select_db(db_name)
        except Exception as e:
            print(e)


# @cls_main_deco()
class MysqlCommonQuery(MysqlFunc):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, *args, **kwargs):
        super().__init__(mysql_info)
        self.cf = CommonFunc()

    def get_status_from_order(self, order_no):
        """
        从注单主表获取注单状态
        :param order_no:
        :return:
        """
        sql = "select status from o_account_order where order_no='%s'" % order_no
        rtn = self.query_data(sql, 'bfty_credit')
        return rtn[0][0]

    def get_status_from_order_detail(self, order_no, match_id):
        """
        从注单详情表中获取子注单状态
        :param order_no:
        :param match_id:
        :return:
        """
        sql = "select sub_order_status from o_account_order_detail where order_no='%s' and match_id like '%%%s%%'" % \
              (order_no, match_id)
        return self.query_data(sql, 'bfty_credit')[0][0]

    def wait_until_order_status_changed(self, status, order_no, match_id="", if_detail="否", retry_time=15):
        """
        等待直到注单状态变更为指定状态
        :param status:
        :param order_no:
        :param match_id:
        :param if_detail:
        :param retry_time:
        :return:
        """
        for loop in range(retry_time):
            if if_detail == "是":
                try:
                    code = int(self.get_status_from_order_detail(order_no, match_id))
                except TypeError:
                    print(f"查询状态失败，注单编号：{order_no}")
                    return False
            else:
                code = int(self.get_status_from_order(order_no))
            if status not in (-1, -2):
                if code in (-1, -2):
                    return False
            if code != int(status):
                time.sleep(1)
            else:
                return True
        else:
            return False

    def get_agent_id(self, agent_login_account):
        """
        获取代理线ID
        :param agent_login_account:
        :return:
        """
        sql = f"select id from m_account where login_account='{agent_login_account}'"
        return self.query_data(sql)[0][0]

    def get_agent_account_name_by_id(self, agent_id):
        """
        获取代理名称
        :param agent_id:
        :return:
        """
        sql = f"select account from m_account where id='{agent_id}'"
        return self.query_data(sql)[0][0]

    def get_all_order_no(self, status="", without_abnormal=False):
        """
        获取所有的注单编号
        :param status: 注单状态：
        :param without_abnormal: 是否包括异常订单 True | False
        :return:
        """
        sql = "select order_no from o_account_order where 1=1"
        if status:
            sql += f" and status={status}"
        if without_abnormal:
            sql += " and operator is NULL"
        return self.query_data(sql)

    def get_role_id(self, agent_login_account):
        """
        获取代理的角色ID
        :param agent_login_account:
        :return:
        """
        sql = f'select role_id from m_account where login_account="{agent_login_account}"'
        return self.query_data(sql)[0][0]


if __name__ == "__main__":
    ms_info = ['192.168.10.120', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']

    mysql = MysqlCommonQuery(ms_info)
    # mysql.get_merchant_name_list_sql("星耀一代1")
    # print(mysql.get_home_merchant_number_sql("星耀一代A"))
    # print(mysql.get_branch_user_list_sql("星耀一代A"))
