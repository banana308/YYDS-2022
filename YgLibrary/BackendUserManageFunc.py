# -*- coding:utf-8 -*-
import json

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


class BackendUserManageFuncOfMysql(MysqlCommonQuery):
    """
    管理后台的用户管理模块，MYSQL相关的功能
    """

    def __init__(self, mysql_info, *args, **kwargs):
        super().__init__(mysql_info, *args, **kwargs)
        self.cf = CommonFunc()

    def get_agent_report_data_detail_sql(self, agent_account, start_diff_unit=None, end_diff_unit=None):
        """
        报表中的明细
        """
        role_id = self.get_role_id(agent_account)
        father_role_id = int(role_id) - 1
        water_str = f'level{father_role_id}_retreat_proportion-level{role_id}_retreat_proportion'
        start_time = self.cf.get_md_search_time(start_diff_unit)[0] if start_diff_unit or start_diff_unit == 0 else ""
        end_time = self.cf.get_md_search_time(end_diff_unit)[0] if end_diff_unit or start_diff_unit == 0 else ""
        time_str = f" and a.create_time between '{start_time}' and '{end_time}'" if \
            start_diff_unit or start_diff_unit == 0 else ""
        risk_str = f"level{role_id}_actual_percentage"

        sql = f"select DATE_FORMAT(CONVERT_TZ(a.create_time,'+0:00','-4:00'),'%Y-%m-%d') as '日期',b.account " \
              f"as '代理账号',b.name as '名称',sum(bet_amount) as '下注金额',sum(win_or_lose) as '输赢',sum((bet_amount * " \
              f"level3_retreat_proportion)) as '代理退水',sum(win_or_lose+(bet_amount * level3_retreat_proportion)) " \
              f"as '最终输赢',sum(bet_amount * ({water_str})) as '吃水',sum(-(win_or_lose * {risk_str} )+ " \
              f"(bet_amount * ({water_str}))) as '代理最终输赢' from m_account_unsettlement_amount_record a join " \
              f"m_account b on a.account_id=b.id where b.login_account='{agent_account}' {time_str} group by " \
              f"DATE_FORMAT(CONVERT_TZ(a.create_time,'+0:00','-4:00'),'%Y-%m-%d') order by " \
              f"DATE_FORMAT(CONVERT_TZ(a.create_time,'+0:00','-4:00'),'%Y-%m-%d') desc"
        print(sql)
        return self.query_data(sql, 'bfty_credit')

    def get_agent_report_data_total_sql(self, agent_account, start_diff_unit=None, end_diff_unit=None):
        """
        报表中的总计
        """
        role_id = int(self.get_role_id(agent_account))
        water_str = f'level{role_id - 1}_retreat_proportion-level{role_id}_retreat_proportion'
        start_time = self.cf.get_md_search_time(start_diff_unit)[0] if start_diff_unit or start_diff_unit == 0 else ""
        end_time = self.cf.get_md_search_time(end_diff_unit)[0] if end_diff_unit or start_diff_unit == 0 else ""
        time_str = f" and a.create_time between '{start_time}' and '{end_time}'" if \
            start_diff_unit or start_diff_unit == 0 else ""
        sql = f"select sum(bet_amount * ({water_str})) as '总吃水',round(sum(-(win_or_lose * " \
              f"level{role_id}_actual_percentage )+ " \
              f"(bet_amount * ({water_str}))),2) as '最终输赢' from m_account_unsettlement_amount_record a join " \
              f"m_account b on a.account_id=b.id where b.login_account='{agent_account}' {time_str}"
        return self.query_data(sql, 'bfty_credit')

    def get_agent_list_data_sql(self, agent_account, name="", status="", login_account=""):
        """
        代理商管理列表数据
        """
        role_id = int(self.get_role_id(agent_account))
        water_str = '+'.join([f"level{index}_retreat_proportion" for index in range(role_id, 4)])
        risk_str = '+'.join([f"level{index}_actual_percentage" for index in range(role_id + 1, 4)])
        name_str = "" if not name else f" and b.name='{name}' "
        status_str = "" if not status else f" and account_status='{status}' "
        login_account_str = "" if not login_account else f" and login_account='{login_account}' "
        sql = f"select any_value(b.account) as '代理商账号',any_value(b.name) as '名称',any_value(login_account) " \
              f"as '登入账号',any_value(quota_mode) as '额度模式','人民币',any_value(credits) as '信用额度'," \
              f"any_value(available_quota) as '可用额度',0 as '会员人数',round(sum(if(a.payment_status=0,-win_or_lose-(-" \
              f"(win_or_lose * " \
              f"({risk_str}) )+ (bet_amount * ({water_str}))),0)),2) as '未结算金额',account_status as '账户状态'," \
              f"DATE_FORMAT(CONVERT_TZ(b.create_time,'+0:00','-4:00'), '%Y-%m-%d %H:%i:%s') as '新增日期' from " \
              f"m_account b left join m_account_unsettlement_amount_record a on a.account_id=b.id left join " \
              f"m_account_credits c on b.id=c.account_id where b.id in (select c.id from m_account c join m_account " \
              f"d where c.parent_id=d.id and d.login_account='{agent_account}' and c.role_id < 4) {status_str} " \
              f"{name_str} {login_account_str} group by b.account order by b.create_time"
        return self.query_data(sql, 'bfty_credit')


class MasterBackendUserManageFuncOfInterface(Backend):
    """
        总台管理后台的用户管理模块，接口相关的功能
    """

    def __init__(self, mysql_info, backend_url="http://192.168.10.11:8083", *args, **kwargs):
        self.mysql_info = mysql_info
        super().__init__(mysql_info, backend_url)
        self.mysql = BackendUserManageFuncOfMysql(self.mysql_info)


class AgentBackendUserManageFuncOfInterface(Backend):
    """
        代理管理后台的用户管理模块，接口相关的功能
    """

    def __init__(self, mysql_info, backend_url="http://192.168.10.11:8083", *args, **kwargs):
        self.mysql_info = mysql_info
        self.host = backend_url
        super().__init__(mysql_info, backend_url)
        self.mysql = BackendUserManageFuncOfMysql(self.mysql_info)
        self.account_status_dic = {"启用": 0, "停用": 2, "只能看账": 1, "禁止登入": 3}
        self.sql = BackendUserManageFuncOfMysql(mysql_info)

    def get_agent_list_detail(self, status="", name="", login_account="", sort=""):
        """
        获取代理商管理中的列表数据
        :param status: 启用 | 停用 | 只能看账 | 禁止登入
        :param name:
        :param login_account:
        :param sort: 信用额度 | 可用额度 | 会员人数 | 新增日期
        """
        sort_dic = {"信用额度": "", "可用额度": "", "会员人数": "", "新增日期": ""}
        url = self.host + "/account/queryAccountList"
        params = {"page": 1,
                  "limit": 200,
                  "accountStatus": self.account_status_dic[status] if status else "",
                  "name": name if name else "",
                  "loginAccount": login_account if login_account else "",
                  "sortBy": "" if not sort else sort_dic[sort],
                  "sortParameter": ""}
        rtn = self.session.post(url, json=params, headers=self.head_bd)
        data_list = [[item["account"], item["name"], item["loginAccount"], item["quotaModeName"], item["currency"],
                      item["credits"], item["availableQuota"], item["memberAmount"], item["unsettledAmount"],
                      item["accountStatusName"], item["accountStatus"], item["createTime"]]
                     for item in rtn.json()["data"]["data"]]
        return data_list

    def get_agent_list_total(self):
        """
        代理商管理：获取下级代理未结算金额总计
        """
        url = self.host + "/settlementAmount/querySubordinateUnsettledAmountTotal"
        rtn = self.session.post(url, headers=self.head_bd)
        return rtn.json()["data"]

    def change_agent_user_status(self, account, status):
        """
        代理商管理：修改代理商账户状态
        :param account:
        :param status: 启用 | 停用 | 只能看账 | 禁止登入
        """
        url = self.host + "/account/changePasswordOrStatus"
        acc_id = self.sql.get_agent_id(account)
        params = {"type": 'false', "accountId": acc_id, "content": self.account_status_dic[status]}
        rtn = self.session.post(url, json=params, headers=self.head_bd)
        if rtn.json()["data"]["message"] != 'OK':
            raise ValueError("改变状态失败！")

    def get_agent_credit_range(self):
        """
        获取代理商剩余占成数范围
        """
        url = self.host + "/percentage/queryPercentageRange"
        rtn = self.session.get(url, headers=self.head_bd).json()["data"]
        return rtn["subordinateProfitLossPercentage"], rtn["highestProfitLossPercentage"]

    def _get_agent_user_detail(self, account):
        """
        获取代理商详情中的原始数据
        """
        url = self.host + "/account/getAccountIdDetailsInfo"
        acc_id = self.sql.get_agent_id(account)
        params = {"accountId": acc_id}
        return self.session.get(url, params=params, headers=self.head_bd).json()["data"]

    def get_agent_user_detail_config(self, account):
        """
        获取代理商详情中的用户详细设定
        """
        credit_range = self.get_agent_credit_range()
        rtn = self._get_agent_user_detail(account)
        key = rtn["accountDetailsInfoVO"]
        data = [key["account"], key["name"], key["securityCode"], key["quotaModeName"], key["availableQuota"],
                key["credits"], *credit_range, key["thisLevelProfitLossPercentage"],
                key["subordinateProfitLossPercentage"], key["highestProfitLossPercentage"]]
        return data

    def get_agent_user_detail_water(self, account):
        """
        获取代理商详情中的返水和限额
        """
        rtn = self._get_agent_user_detail(account)
        key = rtn["retreatAndBettingVO"]
        data = []
        for index in range(3):
            data.append([key[index]["hcpOu"]["retreatValueA"], key[index]["hcpOu"]["retreatValueB"],
                         key[index]["hcpOu"]["retreatValueC"], key[index]["hcpOu"]["retreatValueD"],
                         key[index]["hcpOu"]["singleHighest"], key[index]["hcpOu"]["singleBetMax"],
                         key[index]["inplay"]["retreatValueA"], key[index]["inplay"]["retreatValueB"],
                         key[index]["inplay"]["retreatValueC"], key[index]["inplay"]["retreatValueD"],
                         key[index]["inplay"]["singleHighest"], key[index]["inplay"]["singleBetMax"],
                         key[index]["winner"]["singleHighest"], key[index]["winner"]["singleBetMax"],
                         key[index]["other"]["singleHighest"], key[index]["other"]["singleBetMax"]])
        return data

    def get_agent_user_detail(self, account, start_diff_unit="", end_diff_unit=""):
        """
        获取代理商详情中的用户详细设定
        :param account:
        :param start_diff_unit:
        :param end_diff_unit
        """
        url = self.host + "/settlementAmount/querySettlementAmountList"
        acc_id = self.sql.get_agent_id(account)
        params = {"accountId": acc_id,
                  "startingTime": "" if not start_diff_unit else self.cf.get_md_date_by_now(diff=start_diff_unit),
                  "endTime": "" if not end_diff_unit else self.cf.get_md_date_by_now(diff=end_diff_unit),
                  "page": 1,
                  "limit": 200}
        rtn = self.session.post(url, params=params, headers=self.head_bd).json()["data"]
        data = [[item["createTime"], item["account"], item["name"], item["betAmount"], item["bettingWinOrLose"],
                 item["retreatAmount"], item["winOrLoseInTheEnd"], item["drinkingWater"], item["agentWinsOrLoses"],
                 item["paymentStatus"]] for item in rtn["data"]]
        return data

    def get_agent_user_operation_record(self, account, start_diff_unit="", end_diff_unit="", operation_type=""):
        """
        获取代理商详情中的查看记录
        :param account:
        :param start_diff_unit:
        :param end_diff_unit:
        :param operation_type:  修改密码 | 新增账号 | 更改状态
        """
        operation_type_dic = {"修改密码": "01", "新增账号": "11", "更改状态": "22"}
        url = self.host + "/operation/queryOperationRecord"
        acc_id = self.sql.get_agent_id(account)
        params = {"accountId": acc_id,
                  "category": operation_type_dic[operation_type],
                  "startingTime": "" if not start_diff_unit else self.cf.get_md_date_by_now(diff=start_diff_unit),
                  "endTime": "" if not end_diff_unit else self.cf.get_md_date_by_now(diff=end_diff_unit),
                  "page": 1,
                  "limit": 200}
        rtn = self.session.post(url, params=params, headers=self.head_bd).json()["data"]
        data = [[item["createTime"], item["operator"], item["categoryName"]] for item in rtn["data"]]
        return data

    def get_agent_user_credit_record(self, account, start_diff_unit="", end_diff_unit=""):
        """
        获取代理商详情中的额度修改记录
        :param account:
        :param start_diff_unit:
        :param end_diff_unit:
        """
        url = self.host + "/quotaAllocation/queryQuotaAllocationList"
        acc_id = self.sql.get_agent_id(account)
        params = {"accountId": acc_id,
                  "startingTime": "" if not start_diff_unit else self.cf.get_md_date_by_now(diff=start_diff_unit),
                  "endTime": "" if not end_diff_unit else self.cf.get_md_date_by_now(diff=end_diff_unit),
                  "page": 1,
                  "limit": 200}
        rtn = self.session.post(url, params=params, headers=self.head_bd).json()["data"]
        data = [[item["createTime"], item["credits"], item["categoryName"], item["amount"], item["operator"]] for
                item in rtn["data"]]
        return data

    def get_agent_sub_list_detail(self, name="", login_account=""):
        """
        获取子账号管理中的列表数据
        :param name:
        :param login_account:
        """
        url = self.host + "/subAccount/subAccountList"
        params = {"page": 1,
                  "limit": 200,
                  "name": name if name else "",
                  "loginAccount": login_account if login_account else ""}
        rtn = self.session.post(url, json=params, headers=self.head_bd)
        data_list = [[item["loginAccount"], item["name"], item["roleId"], item["createTime"]]
                     for item in rtn.json()["data"]["data"]]
        return data_list

    def get_agent_sub_user_detail(self, account):
        """
        获取子账号详情中的用户详细设定
        :param account:
        """
        url = self.host + "/subAccount/subAccountDetail"
        acc_id = self.sql.get_agent_id(account)
        params = {"subId": acc_id}
        rtn = self.session.get(url, params=params, headers=self.head_bd).json()["data"]
        data = [rtn["roleName"], rtn["roleId"], rtn["loginAccount"], rtn["account"], rtn["securityCode"],
                rtn["createTime"], rtn["lastLoginTime"], rtn["lastPasswordUpdateTime"]]
        return data

    def update_agent_sub_user_base_info(self, account, role="", name="", security_code=""):
        """
        修改子账号详情中的用户详细设定
        :param account:
        :param role: 查看权限|全部权限
        :param name:
        :param security_code:
        """
        role_dic = {"全部权限": "5", "查看权限": "4"}
        url = self.host + "/subAccount/newSubAccount"
        acc_id = self.sql.get_agent_id(account)
        origin_data = self.get_agent_sub_user_detail(account)
        name = origin_data[3] if not name else name
        role_id = origin_data[1] if not role else role_dic[role]
        params = {"id": acc_id,
                  "isNew": "false",
                  "name": name,
                  "roleId": role_id}
        rtn = self.session.get(url, params=params, headers=self.head_bd).json()["data"]
        if rtn["message"] != "OK":
            raise AssertionError(rtn["message"])

    def update_agent_sub_user_manage_list(self, account, account_str="", is_new='false'):
        """
        修改子账号可管理的账户
        :param account:
        :param account_str:  要管理的账户字符串，以 "|"分隔
        :param is_new: 新建传true，默认为false
        """
        all_agent_user = self.get_agent_user_list_to_manage()
        account_str_all = '|'.join([item[0] for item in all_agent_user])
        account_list = account_str.split("|")
        account_id_list = list(map(self.sql.get_agent_id, account_list))
        url = self.host + "/subAccount/manageAccountInput"
        acc_id = self.sql.get_agent_id(account)
        params = {"subId": acc_id,
                  "isNew": is_new,
                  "selectAll": "true" if account_str == account_str_all else "false",
                  "nextIds": account_id_list}
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()
        if rtn["message"] != "OK":
            raise AssertionError(rtn["message"])

    def add_agent_sub_user(self, role_type, login_account, name, password, security, account_num=100):
        """
        修改子账号可管理的账户
        :param role_type: 查看权限 | 全部权限
        :param login_account:
        :param name:
        :param password:
        :param security:
        :param account_num:  要管理的账户个数，100为全部
        :return account_list: 管理的账号account 列表
        """
        role_dic = {"全部权限": "5", "查看权限": "4"}
        all_agent_user = self.get_agent_user_list_to_manage()
        url = self.host + "/subAccount/newSubAccount"
        params = {"isNew": "true",
                  "loginAccount": login_account,
                  "name": name,
                  "password": password,
                  "roleId": role_dic[role_type],
                  "securityCode": security}
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()
        if rtn["message"] != "OK":
            raise AssertionError(rtn["message"])
        sub_account_id = rtn["data"]["account"]
        account_str = '|'.join([item[0] for item in all_agent_user]) if int(account_num) == 100 \
            else '|'.join([item[0] for item in all_agent_user[:account_num]])
        account_list = [item[0] for item in all_agent_user] if int(account_num) == 100 else \
            [item[0] for item in all_agent_user[:account_num]]
        if len(all_agent_user) == int(account_num) or int(account_num) == 100:
            self.update_agent_sub_user_manage_list(sub_account_id, account_str, 'true')
        else:
            self.update_agent_sub_user_manage_list(sub_account_id, account_str, 'false')
        return account_list

    def get_agent_user_list_to_manage(self):
        """
        获取创建子账号中的可管理账户列表
        """
        url = self.host + "/subAccount/manageAccount"
        params = {"limit": 50,
                  "isNew": "true",
                  "page": 1}
        rtn = self.session.post(url, json=params, headers=self.head_bd).json()["data"]
        data_list = [[item["account"], item["name"], item["loginAccount"], item["id"]] for item in
                     rtn["manageAccountsPage"]["data"]]
        return data_list

    def get_credit_left_from_add_agent_page(self):
        """
        从创建代理界面获取剩余额度
        """
        url = self.host + "/account/queryCredits"
        rtn = self.session.get(url, headers=self.head_bd).json()
        return rtn["data"]

    def get_percent_range_from_add_agent_page(self):
        """
        从创建代理界面获取剩余占成数范围
        """
        url = self.host + "/percentage/queryPercentageRange"
        rtn = self.session.get(url, headers=self.head_bd).json()["data"]
        lowest = rtn["highestProfitLossPercentage"] if int(rtn["subordinateProfitLossPercentage"]) == 100 else \
            rtn["subordinateProfitLossPercentage"]
        return lowest, rtn["highestProfitLossPercentage"]

    def get_retreat_and_betting_details_info(self, top_parent_account, self_account, sport_type):
        """
        从创建代理界面获取返水和限额可选值
        :param top_parent_account: 所属的登0账号
        :param self_account: 自身account
        :param sport_type: 体育类型： 足球|篮球|其它
        """
        role_id = self.sql.get_role_id(self_account)
        account_id = self.sql.get_agent_id(top_parent_account)
        url = self.host + "/retreat/queryRetreatAndBettingDetailsInfo?accountId=" + str(account_id)
        print(url)
        rtn = self.session.get(url, headers=self.head_bd).json()["data"]
        sport_index_dic = {"足球": 0, "篮球": 1, "其它": 2}
        total_data = []
        print(rtn)
        if int(role_id) == 0:
            url = self.host + "/handicapBackwater/getHandicapEachLevelBackwater"
            retreat = self.session.get(url, headers=self.head_bd).json()["data"]
            for item in [rtn[sport_index_dic[sport_type]]["hcpOu"], rtn[sport_index_dic[sport_type]]["inplay"]]:
                total_data.append([retreat["retreatValueA"], retreat["retreatValueB"], retreat["retreatValueC"],
                                   retreat["retreatValueD"], item["singleHighest"], item["singleBetMax"]])
            for item in [rtn[sport_index_dic[sport_type]]["winner"], rtn[sport_index_dic[sport_type]]["other"]]:
                total_data.append([item["singleHighest"], item["singleBetMax"]])
        else:
            for item in [rtn[sport_index_dic[sport_type]]["hcpOu"], rtn[sport_index_dic[sport_type]]["inplay"]]:
                total_data.append([item["retreatValueA"], item["retreatValueB"], item["retreatValueC"],
                                   item["retreatValueD"], item["singleHighest"], item["singleBetMax"]])
            for item in [rtn[sport_index_dic[sport_type]]["winner"], rtn[sport_index_dic[sport_type]]["other"]]:
                total_data.append([item["singleHighest"], item["singleBetMax"]])
        return total_data

    def add_agent_user(self, top_parent_account, focus_type, self_account, **args):
        """
        添加下级代理
        :param top_parent_account: 所属的登0账号
        :param self_account: 自身account
        :param focus_type: 测试关注点： 用户详细设定|退水和限额
        :return account:
        """
        url = self.host + "/account/insertRetreatAndBetting"
        sport_dic = {"足球": "1", "篮球": "2", "其它": "100"}
        # if focus_type == "用户详细设定":
        # retreat_bet_data = self.get_retreat_and_betting_details_info(top_parent_account, self_account, "足球")
        account = args["account"] if "account" in args else f'{self.cf.generate_string("大写字母", 2)}' \
                                                            f'{self.cf.generate_string("小写字母", 4)}' \
                                                            f'{self.cf.generate_string("数字", 4)}'
        name = args["name"] if "name" in args else self.cf.generate_string("小写字母", 8)
        password = args["account"] if "account" in args else f'{self.cf.generate_string("大写字母", 2)}' \
                                                             f'{self.cf.generate_string("小写字母", 4)}' \
                                                             f'{self.cf.generate_string("数字", 4)}'
        security_code = args["account"] if "account" in args else f'{self.cf.generate_string("大写字母", 2)}' \
                                                                  f'{self.cf.generate_string("小写字母", 4)}' \
                                                                  f'{self.cf.generate_string("数字", 4)}'
        quota_mode_dic = {"自动恢复": "1", "余额浮动": "2"}
        credit_range = self.get_percent_range_from_add_agent_page()
        credit_amount = args["amount"] if "credit" in args else 1
        percent_self = args["percent_self"] if "percent_self" in args else 5
        percent_son = args["percent_son"] if "percent_son" in args else int(credit_range[1]) - percent_self
        percent_self_max = args["percent_self_max"] if "percent_self_max" in args else 10
        force_switch = args["force_switch"] if "force_switch" in args else "false"

        if force_switch == "true":
            force_1 = args["force_1"] if "force_1" in args else 10
            force_2 = args["force_2"] if "force_2" in args else 10
            force_3 = args["force_3"] if "force_3" in args else 10
        else:
            force_1 = ""
            force_2 = ""
            force_3 = ""

        limit_data = [self.get_retreat_and_betting_details_info(top_parent_account, self_account, sport) for sport
                      in ["足球", "篮球", "其它"]]
        params = {"accountInsertParam": {"account": account,
                                         "name": name,
                                         "securityCode": security_code,
                                         "password": password,
                                         "accountStatus": "",
                                         "currency": "CNY",
                                         "credits": credit_amount,
                                         "quotaMode": quota_mode_dic[args["quota_mode"]]
                                         if "quota_mode" in args else quota_mode_dic["自动恢复"],
                                         "quotaModeName": "",
                                         "agentRemainAmount": "",
                                         "balance": "",
                                         "exchangeRate": "",
                                         "availableQuota": "",
                                         "thisLevelProfitLossPercentage": percent_self,
                                         "subordinateProfitLossPercentage": percent_son,
                                         "highestProfitLossPercentage": percent_self_max,
                                         "proxy1ProfitLossPercentage": force_1,
                                         "proxy2ProfitLossPercentage": force_2,
                                         "proxy3ProfitLossPercentage": force_3,
                                         "powerSwitch": force_switch},
                  "retreat": [{"sportId": "1",
                               "hcpOu": {"retreatValueA": limit_data[0][0][0][0],
                                         "retreatValueB": limit_data[0][0][1][0],
                                         "retreatValueC": limit_data[0][0][2][0],
                                         "retreatValueD": limit_data[0][0][3][0],
                                         "singleHighest": limit_data[0][0][4],
                                         "singleBetMax": limit_data[0][0][5]},
                               "inplay": {"retreatValueA": limit_data[0][1][0][0],
                                          "retreatValueB": limit_data[0][1][1][0],
                                          "retreatValueC": limit_data[0][1][2][0],
                                          "retreatValueD": limit_data[0][1][3][0],
                                          "singleHighest": limit_data[0][1][4],
                                          "singleBetMax": limit_data[0][1][5]},
                               "winner": {"retreatValueA": "", "retreatValueB": "", "retreatValueC": "",
                                          "retreatValueD": "", "singleHighest": limit_data[0][2][0],
                                          "singleBetMax": limit_data[0][2][1]},
                               "other": {"retreatValueA": "", "retreatValueB": "", "retreatValueC": "",
                                         "retreatValueD": "", "singleHighest": limit_data[0][3][0],
                                         "singleBetMax": limit_data[0][3][1]}},
                              {"sportId": "2", "hcpOu": {"retreatValueA": limit_data[2][0][0][0],
                                                         "retreatValueB": limit_data[2][0][1][0],
                                                         "retreatValueC": limit_data[2][0][2][0],
                                                         "retreatValueD": limit_data[2][0][3][0],
                                                         "singleHighest": limit_data[2][0][4],
                                                         "singleBetMax": limit_data[2][0][5]},
                               "inplay": {"retreatValueA": limit_data[2][1][0][0],
                                          "retreatValueB": limit_data[2][1][1][0],
                                          "retreatValueC": limit_data[2][1][2][0],
                                          "retreatValueD": limit_data[2][1][3][0],
                                          "singleHighest": limit_data[2][1][4],
                                          "singleBetMax": limit_data[2][1][5]},
                               "winner": {"retreatValueA": "", "retreatValueB": "", "retreatValueC": "",
                                          "retreatValueD": "", "singleHighest": limit_data[2][2][0],
                                          "singleBetMax": limit_data[2][2][1]},
                               "other": {"retreatValueA": "", "retreatValueB": "", "retreatValueC": "",
                                         "retreatValueD": "", "singleHighest": limit_data[2][3][0],
                                         "singleBetMax": limit_data[2][3][1]}},
                              {"sportId": "100", "hcpOu": {"retreatValueA": limit_data[1][0][0][0],
                                                           "retreatValueB": limit_data[1][0][1][0],
                                                           "retreatValueC": limit_data[1][0][2][0],
                                                           "retreatValueD": limit_data[1][0][3][0],
                                                           "singleHighest": limit_data[1][0][4],
                                                           "singleBetMax": limit_data[1][0][5]},
                               "inplay": {"retreatValueA": limit_data[1][1][0][0],
                                          "retreatValueB": limit_data[1][1][1][0],
                                          "retreatValueC": limit_data[1][1][2][0],
                                          "retreatValueD": limit_data[1][1][3][0],
                                          "singleHighest": limit_data[1][1][4],
                                          "singleBetMax": limit_data[1][1][5]},
                               "winner": {"retreatValueA": "", "retreatValueB": "", "retreatValueC": "",
                                          "retreatValueD": "", "singleHighest": limit_data[1][2][0],
                                          "singleBetMax": limit_data[1][2][1]},
                               "other": {"retreatValueA": "", "retreatValueB": "", "retreatValueC": "",
                                         "retreatValueD": "", "singleHighest": limit_data[1][3][0],
                                         "singleBetMax": limit_data[1][3][1]}}]}
        if "sport" in args:
            for index, item in enumerate(params["retreat"]):
                if item["sportId"] == sport_dic[args["sport"]]:
                    sport_index = {"足球": 0, "篮球": 2, "其它": 1}[args["sport"]]
                    print(2222)
                    print(sport_index)
                    change_data = {"sportId": sport_dic[args["sport"]],
                                   "hcpOu": {
                                       "retreatValueA": limit_data[sport_index][0][0][0] if 'value1' not in args else
                                       args["value1"],
                                       "retreatValueB": limit_data[sport_index][0][1][0] if 'value2' not in args else
                                       args["value2"],
                                       "retreatValueC": limit_data[sport_index][0][2][0] if 'value3' not in args else
                                       args["value3"],
                                       "retreatValueD": limit_data[sport_index][0][3][0] if 'value4' not in args else
                                       args["value4"],
                                       "singleHighest": limit_data[sport_index][0][4] if 'value5' not in args
                                       else args["value5"],
                                       "singleBetMax": limit_data[sport_index][0][5] if 'value6' not in args
                                       else args["value6"]},
                                   "inplay": {
                                       "retreatValueA": limit_data[sport_index][1][0][0] if 'value7' not in args else
                                       args["value7"],
                                       "retreatValueB": limit_data[sport_index][1][1][0] if 'value8' not in args else
                                       args["value8"],
                                       "retreatValueC": limit_data[sport_index][1][2][0] if 'value9' not in args else
                                       args["value9"],
                                       "retreatValueD": limit_data[sport_index][1][3][0] if 'value10' not in args else
                                       args["value10"],
                                       "singleHighest": limit_data[sport_index][1][4] if 'value11' not in args else
                                       args["value11"],
                                       "singleBetMax": limit_data[sport_index][1][5] if 'value12' not in args else
                                       args["value12"]},
                                   "winner": {"retreatValueA": "",
                                              "retreatValueB": "",
                                              "retreatValueC": "",
                                              "retreatValueD": "",
                                              "singleHighest": limit_data[sport_index][2][0]
                                              if 'value13' not in args else args["value13"],
                                              "singleBetMax": limit_data[sport_index][2][1]
                                              if 'value14' not in args else args["value14"]},
                                   "other": {"retreatValueA": "", "retreatValueB": "", "retreatValueC": "",
                                             "retreatValueD": "", "singleHighest": limit_data[sport_index][3][0]
                                             if 'value15' not in args else args["value15"],
                                             "singleBetMax": limit_data[sport_index][3][1]
                                             if 'value16' not in args else args["value16"]}}
                    params["retreat"][index] = change_data
                    break
        rtn = self.session.post(url, json=params, headers=self.head_bd)
        if rtn.json()["data"]["message"] != "OK":
            raise AssertionError(f'创建代理失败，原因： {rtn.json()["data"]["message"] }')
        return account
