import requests
import json
import re
import time
import xmltodict
import random
import datetime
# try:
#     from .MongoFunc import DbQuery
#     from .MyExceptions import *
#     from .CommonFunc import CommonFunc
#     from .MysqlFunc import MysqlCommonQuery
# except ImportError:
from MongoFunc import DbQuery
from MyExceptions import *
from CommonFunc import CommonFunc
from MysqlFunc import MysqlCommonQuery,MysqlFunc


class CtrlIoDocs(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info):
        requests.packages.urllib3.disable_warnings()
        self.ctrl_host = "https://iodocs.betradar.com/processReq"
        self.head = {"acctoken": ""}
        self.session = requests.session()
        self.api_key = 'p5cb4BenaHxKRM3kUO'
        self.dbq = DbQuery(mysql_info, mongo_info)
        self.mysql = MysqlCommonQuery(mysql_info)


    def query_match_all_log(self, event_id):
        """
        获取比赛的全log
        :param event_id:
        :return: msg
        """
        data = {
            'httpMethod': 'GET',
            'oauth': '',
            'methodUri': '/xmllog/events/{event_id}/messages',
            'accessToken': '',
            'json': json.dumps({"event_id": "sr:match:" + event_id}),
            'locations': json.dumps({"event_id": "path"}),
            'values[1]': "sr:match:" + event_id,
            'apiKey': 'p5cb4BenaHxKRM3kUO',
            'apiSecret': '',
            'apiName': 'ufstaging',
            'apiUsername': '',
            'apiPassword': ""
        }
        rtn = requests.post(url=self.ctrl_host, data=data, verify=False, stream=True)
        data = rtn.json()
        return data['response'].replace("\\", "")

    def get_match_detail(self, event_id):
        """
        获取比赛的详情
        :param event_id:
        :return: msg
        """
        data = {
            'httpMethod': 'GET',
            'oauth': '',
            'methodUri': '/sports/{language}/sport_events/{urn_type}:{id}/summary.xml',
            'accessToken': '',
            'json': json.dumps({"language": "en", "id": event_id, "urn_type": "sr:match"}),
            'locations': json.dumps({"language": "path", "id": "path", "urn_type": "path"}),
            'values[1]': 'en',
            'values[2]': event_id,
            'values[3]': 'sr:match',
            'apiKey': 'p5cb4BenaHxKRM3kUO',
            'apiSecret': '',
            'apiName': 'ufstaging',
            'apiUsername': '',
            'apiPassword': ""
        }
        rtn = requests.post(url=self.ctrl_host, data=data, verify=False)
        data = rtn.json()
        return data["response"]

    def get_match_result_data(self, match_id):
        """
        获取比赛结果信息数据
        :param match_id:
        :return:
        """
        data = self.query_match_all_log(match_id)
        all_settlement = re.findall("<bet_settlement.*?</bet_settlement>", data)
        if not all_settlement:
            return None
        settlement_data = all_settlement[0]
        for index, settlement in enumerate(all_settlement[1:]):
            if 'certainty="2"' in settlement_data and 'certainty="1"' in settlement:
                continue
            settlement_data = settlement
        return json.loads(json.dumps(xmltodict.parse(settlement_data)))["bet_settlement"]

    @staticmethod
    def get_outcome_result(match_result_data, market_id, outcome_id):
        """
        获取投注项的中奖结果
        :param match_result_data:
        :param market_id:
        :param outcome_id:
        :return:
        """
        print(match_result_data)
        for market in match_result_data["outcomes"]["market"]:
            if market["@id"] == market_id:
                for outcome in market["outcome"]:
                    if outcome["@id"] == outcome_id:
                        result = outcome["@result"]
                        if "@void_factor" not in outcome.keys():
                            return result
                        void_factor = outcome["@void_factor"]
                        if not void_factor:
                            return result
                        # 全退，走盘
                        if result == '0' and void_factor == '1.0':
                            return "5"
                        # 赢一半
                        elif result == '1' and void_factor == '0.5':
                            return "3"
                        # 输一半
                        elif result == '0' and void_factor == '0.5':
                            return "4"
                        else:
                            print("result is: " + result + ", void_factor is:" + void_factor)
                            return "Notice: 没有遇到这种情况"
        return None


class BetController(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mysql_info, mongo_info, *args):
        """
        模拟ctrl给我司推送数据
        """
        self.bc_host = "http://192.168.10.10:8808/mock/message"
        self.session = requests.session()
        self.dbq = DbQuery(mongo_info)
        # self.ctrl_docs = CtrlIoDocs(mysql_info, mongo_info)
        self.cf = CommonFunc()
        self.mysql = MysqlCommonQuery(mysql_info)
        self.my = MysqlFunc(mysql_info)

    def data_post(self, data):
        try:
            if "<bet_settlement" in data:
                print("发送指令内容为："+str(data))
                # print(data)
                output = ""
                # all_match = re.findall('(<market.+?</market>)', data)
                # start = re.search('(<bet_settlement.+?<outcomes>)', data)

                rtn = self.session.post(self.bc_host, data=data).content.decode()
                if rtn != "OK":
                    raise SendCtrlCmdFailedException("发送指令失败: " + rtn)
                output += rtn

                # for element in [all_match[index: index + 5] for index in range(0, len(all_match), 5)]:
                #     # time.sleep(1)
                #     post_data = start.group(0) + ''.join(element) + '</outcomes></bet_settlement>'
                #     # data = {"xmlString": post_data}
                #     rtn = self.session.post(self.bc_host, data=data).content.decode()
                #     if rtn != "OK":
                #         raise SendCtrlCmdFailedException("发送指令失败: " + rtn)
                #     output += rtn
                return output
            else:
                print("指令内容为：\n", data)
                rtn = self.session.post(self.bc_host, data=data).content.decode()
                if rtn != "OK":
                    raise SendCtrlCmdFailedException("发送指令失败: " + rtn)
                return rtn
        except Exception as e:
            return str(e)

    @staticmethod
    def get_current_timestamp():
        return str(int(time.time() * 1000))

    # def generate_settlement_str(self, match_id, certainty='1', producer=''):
    #     global result,void_factor,void_reason,result_list,void_factor_list
    #     """
    #     生成结算报文     2022.01.04  增加结算结果参数,生成该比赛所有盘口的报文
    #     :param match_id:
    #     :param certainty:
    #     :param producer:
    #     :return:
    #     """
    #     producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
    #     data = self.dbq.get_match_data(match_id)
    #
    #     if not data:
    #         return "Sorry: [%s]未找到比赛数据" % match_id
    #     output = '<bet_settlement certainty=\"%s\" ' \
    #              'product=\"%s\" event_id=\"%s\" timestamp=\"%s\"><outcomes>' % (certainty, producer, data["_id"],
    #                                                                              self.get_current_timestamp())
    #     for market in data["markets"]:
    #         for specifier in market["specifiers"]:
    #             if specifier["specifier"]:
    #                 output += '<market id="%s" specifiers="%s">' % (market["_id"], specifier["specifier"])
    #             else:
    #                 output += '<market id="%s">' % (market["_id"])
    #             for outcome in specifier["outComes"]:
    #                 result_list=[1,0,1,0,0,0]
    #                 void_factor_list=[0,0,0.5,0.5,1,1]
    #                 if i==5:
    #                     void_reason=['3','5','7','9','10','11','12','13']
    #                     # nub = random.randint(0, 0)
    #                     nub=0
    #                     # print(f"已取到值：{result_list[i]},{void_factor_list[i]},{void_reason[nub]}")
    #                     output += '<market id="%s" void_reason="%s">' % (market["_id"], void_reason[nub])
    #                 else:
    #                     pass
    #                 # void_reason = '10'
    #                 # result =0
    #                 # void_factor =0
    #                 # result = random.choice(result_list)
    #                 # void_factor = random.choice(void_factor_list)
    #                 result=result_list[i]
    #                 void_factor=void_factor_list[i]
    #                 output += f'<outcome id=\"%s\" result=\"{result}\" void_factor=\"{void_factor}\"/>' % outcome['_id']
    #             output += '</market>'
    #     output += '</outcomes></bet_settlement>'
    #     return output


    def generate_settlement_str_by_orderNo_number(self):
        # 获取串关order_no的订单
        sql = f"SELECT order_no FROM `bfty_credit`.o_account_order  WHERE `status`=1 AND login_account LIKE 'fceshi%'"
        sort_num= self.my.query_data(sql, db_name='bfty_credit')
        order_no=list(sort_num)
        return order_no




    def generate_settlement_str_by_count_orderNo(self, order_no=""):
        global sort_num
        """
        通过订单号，获取注单的比赛ID
        ：param order_no:
        :param sort: 默认是0   串关中可根据sort指定某个投注项
        """
        #获取串关order_no的比赛ID
        sql=f"SELECT match_id FROM `bfty_credit`.o_account_order_match_update  WHERE order_no='{order_no}' AND sub_order_status='1' "
        sort_num = self.my.query_data(sql, db_name='bfty_credit')
        return sort_num

    def generate_settlement_str_by_match_count(self, order_no=""):

        """
        通过订单号，获取注单的数量，用以sort传参使用
        ：param order_no:
        :param sort: 默认是0   串关中可根据sort指定某个投注项
        """
        #获取串关order_no的比赛ID
        sql=f"SELECT match_id FROM `bfty_credit`.o_account_order_match_update  WHERE order_no='{order_no}'"
        match_count = self.my.query_data(sql, db_name='bfty_credit')
        return match_count

    def generate_settlement_str_by_match_time(self, order_no):

        """
        通过订单号，获取注单的比赛时间，用以match_time传参使用
        ：param order_no:
        :param match_time: 默认是0   串关中可根据sort指定某个投注项
        """
        #获取串关order_no的比赛时间
        sql=f"SELECT match_time FROM `bfty_credit`.o_account_order_match  WHERE order_no='{order_no}'"
        match_time = self.my.query_data(sql, db_name='bfty_credit')
        return match_time




    @staticmethod
    def split_outcome_id(outcome_info):
        '''
        网球波胆盘口增加判断        sr:match:33574697_199_variant=sr:correct_score:bestof:3_sr:correct_score:bestof:3:4
        :param outcome_info:
        :return:
        '''
        outcome_list = outcome_info.split('_')
        if len(outcome_list) > 4:  # 部分波胆数据加的判断
            specifiers = outcome_list[2] + '_' + outcome_list[3]
            outcome_id = outcome_list[4] + '_' + outcome_list[5]

        else:
            specifiers = outcome_list[2]
            outcome_id = outcome_list[3]
        match_id = outcome_list[0]
        mark_id = outcome_list[1]
        return match_id, mark_id, specifiers, outcome_id



    def generate_settlement_str_by_orderNo(self, order_no, sort=0, certainty='2', producer='', result=None,result_handicap=None):
        """
        通过注单号生成对应盘口或Specifier级别的结算报文
        :param order_no:
        :param sort: 默认是0   串关中可根据sort指定某个投注项
        :param outcomeId: sr:match:31975609_18_total=3_12
        :param certainty:
        :param producer:消息生产者(1-滚球,3-早盘)
        :param result: 输|赢|赢一半|输一半|走盘
        :return:
        """
        # 获取order_no的注单类型
        sql = f"SELECT bet_type FROM `bfty_credit`.o_account_order  WHERE order_no='{order_no}' AND status='1' "
        match_num = self.my.query_data(sql, db_name='bfty_credit')
        match_num = int(match_num[0][0])

        #获取order_no的主队比赛名称
        sql = f"SELECT home_team_name FROM `bfty_credit`.o_account_order_match  WHERE order_no='{order_no}' "
        home_team_name = self.my.query_data(sql, db_name='bfty_credit')
        home_match_num = (home_team_name[sort][0])
        # 获取order_no的客队比赛名称
        sql = f"SELECT away_team_name FROM `bfty_credit`.o_account_order_match  WHERE order_no='{order_no}' "
        away_team_name = self.my.query_data(sql, db_name='bfty_credit')
        away_match_num = (away_team_name[sort][0])

        sql_str = f"SELECT a.spliced_outcome_id FROM `bfty_credit`.`o_account_order_match` as a " \
                  f"LEFT JOIN o_account_order_match_update as b   ON (a.order_no=b.order_no AND a.match_id=b.match_id) WHERE a.`order_no` = '{order_no}' AND b.sub_order_status='1'"

        # sql_str = f"SELECT spliced_outcome_id FROM `bfty_credit`.`o_account_order_match`  WHERE `order_no` = '{order_no}'"
        query_data = list(self.my.query_data(sql=sql_str, db_name='bfty_credit'))
        if (len(query_data)-1)>=int(sort):
            sort=sort
            print(f"\033[32m未做处理：{sort}\033[0m")
        else:
            sort=len(query_data)-1
            print(f"\033[31m已做减一的处理：{sort}\033[0m")
        # print(query_data,sort)
        outcomeId = query_data[sort][0]
        match_id, mark_id, specifiers, outcome_id = self.split_outcome_id(outcomeId)
        outcome_list=[]
        outcome_list.extend([match_id, mark_id, specifiers, outcome_id])
        # print(outcome_list)





        # 所有球类，大小盘，让球的market_id
        match_dict = {"sr:sport:1": ["16", "18", "66", "68"], "sr:sport:2": ["223", "225", "66", "68"],
                      "sr:sport:5": ["188", "314"], "sr:sport:23": ["237", "238"], "sr:sport:31": ["237", "238"],
                      "sr:sport:20": ["237", "238"], "sr:sport:3": ["256", "258"], "sr:sport:4": ["16", "18"]}
        """
                @通过订单号，查sport_id和market_id的值，判断是否在字典里，来判定是否让球和大小盘
                ：sport_id：球类ID
                ：market_id：盘口类型ID
                """
        # 获取订单order_no的sport_id和market_id
        sql = f"SELECT sport_id,market_id FROM `bfty_credit`.o_account_order_match  WHERE  spliced_outcome_id='{outcomeId}'"
        sort_num = self.my.query_data(sql, db_name='bfty_credit')
        # print(sort_num)
        # print(list(sort_num)[0][1],list(sort_num)[0][0])
        # name_sport=list(sort_num)[0][0]
        # print(name_sport)
        # print(match_dict[str(name_sport)])

        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        if list(sort_num)[0][1] in match_dict[str(list(sort_num)[0][0])]:
            print("\033[31m在让球、大小球中\033[0m")
            if result_handicap == None:
                result_handicap_list = ["输", "赢", "赢一半", "输一半", "走盘", '取消']
                result_handicap = random.choice(result_handicap_list)
                print(outcomeId)
            if result_handicap == "输":
                result_str = 'result=\"0\"'
                result = ("\033[31m输\033[0m")
            elif result_handicap == "赢":
                result = ("\033[32m赢\033[0m")
                result_str = 'result=\"1\"'
            elif result_handicap == "赢一半":
                result_str = 'result=\"1\" void_factor=\"0.5\"'
                result = ("\033[32m赢一半\033[0m")
            elif result_handicap == "输一半":
                result_str = 'result=\"0\" void_factor=\"0.5\"'
                result = ("\033[34m输一半\033[0m")
            elif result_handicap == "走盘" or result_handicap == "取消":
                result_str = 'result=\"0\" void_factor=\"1\"'
                if result_handicap == "走盘":
                    result = ("\033[33m走盘\033[0m")
            else:
                raise AssertionError("Result_handicap 输入的值错误。")

        else:
            print("\033[32m不在让球、大小球中\033[0m")
            if result == None:
                result_list = ["输", "赢", "赢一半", "输一半", '取消']
                result = random.choice(result_list)
            if result == "走盘":
                raise AssertionError(f"Result 不能输入走盘,只能输入[输, 赢, 赢一半, 输一半, 取消]")
            if result == "输" or result_handicap == "输":
                result_str = 'result=\"0\"'
                result = ("\033[31m输\033[0m")
            elif result == "赢" or result_handicap == "赢":
                result = ("\033[32m赢\033[0m")
                result_str = 'result=\"1\"'
            elif result == "赢一半" or result_handicap == "赢一半":
                result_str = 'result=\"1\" void_factor=\"0.5\"'
                result = ("\033[32m赢一半\033[0m")
            elif result == "输一半" or result_handicap == "输一半":
                result_str = 'result=\"0\" void_factor=\"0.5\"'
                result = ("\033[34m输一半\033[0m")
            elif result_handicap == "走盘" or result == '取消' or result_handicap == "取消":
                result_str = 'result=\"0\" void_factor=\"1\"'
            else:
                raise AssertionError("Result或Result_handicap 输入的值错误。")

        data = self.dbq.get_match_data(match_id)
        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id
        output = '<bet_settlement certainty=\"%s\" ' \
                 'product=\"%s\" event_id=\"%s\" timestamp=\"%s\"><outcomes>' % (certainty, producer, data["_id"],
                                                                                 self.get_current_timestamp())

        # 查询注单的类型和预结算盘口结果
        if match_num == 1:
            print(f'查询的注单类型为：【单注】,当前正在结算比赛ID为：{match_id},当前正在结算比赛为：\033[32m{home_match_num}VS{away_match_num}\033[0m,当前正在结算的盘口赛果为：{result}')
        if match_num == 2:
            print(f'查询的注单类型为：【串关】,剩余未结算比赛数量为：{len(query_data) - sort - 1}, 当前正在结算比赛ID为：{match_id},当前正在结算比赛为：\033[32m{home_match_num}VS{away_match_num}\033[0m,当前正在结算的盘口赛果为：{result}')
        if match_num == 3:
            print(f'查询的注单类型为：【复式串关】,剩余未结算比赛数量为：{len(query_data) - sort - 1}, 当前正在结算比赛ID为：{match_id},当前正在结算比赛为：\033[32m{home_match_num}VS{away_match_num}\033[0m,当前正在结算的盘口赛果为：{result}')

        if outcomeId:
            grep = re.search(r"^.+?_(\d+?)_(.*)_(.+?)$", outcomeId)
            outcome_market_id = grep.group(1)
            outcome_specifier = outcome_list[2]
            outcome_id_simple = outcome_list[3]

            for market in data["markets"]:
                if outcome_market_id == market["_id"]:
                    for specifier in market["specifiers"]:
                        # 若注单投注项有specifier
                        if outcome_specifier:
                            # 盘口项有specifier，且与投注项一致，则加
                            if specifier["specifier"] and specifier["specifier"] == outcome_specifier:
                                if result == '取消':
                                    # 3=无法核实结果,5=取消赛事,7=弃权或者取消资格取消,9=对手未露面或者退场,10=赛事废弃,11赛事推迟
                                    cancle_reason = {'无法核实结果': '3', '取消赛事': '5', '弃权或者取消资格取消': '7', '对手未露面或者退场': '9',
                                                     '赛事废弃': '10', '赛事推迟': '11'}
                                    cancle_key = ['无法核实结果', '取消赛事', '弃权或者取消资格取消', '对手未露面或者退场', '赛事废弃', '赛事推迟']
                                    key = random.choice(cancle_key)
                                    output += '<market id="%s" specifiers="%s" void_reason="%s">' % (
                                    market["_id"], specifier["specifier"], cancle_reason[key])
                                else:
                                    output += '<market id="%s" specifiers="%s">' % (
                                    market["_id"], specifier["specifier"])
                                for outcome in specifier["outComes"]:
                                    if str(outcome["_id"]) == str(outcome_id_simple):
                                        output += '<outcome id=\"%s\" %s/>' % (outcome['_id'], result_str)
                                    else:
                                        output += '<outcome id=\"%s\" result=\"0\"/>' % outcome['_id']
                                output += '</market>'
                                output += '</outcomes></bet_settlement>'
                                return output
                        # 若注单投注项无specifier
                        else:
                            if result == '取消':
                                cancle_reason = {'无法核实结果': '3', '取消赛事': '5', '弃权或者取消资格取消': '7', '对手未露面或者退场': '9',
                                                 '赛事废弃': '10', '赛事推迟': '11'}
                                cancle_key = ['无法核实结果', '取消赛事', '弃权或者取消资格取消', '对手未露面或者退场', '赛事废弃', '赛事推迟']
                                key = random.choice(cancle_key)
                                print(f"取消类型：{key}")
                                output += '<market id="%s" void_reason="%s">' % (market["_id"], cancle_reason[key])
                            else:
                                output += '<market id="%s">' % (market["_id"])
                            for outcome in specifier["outComes"]:
                                if int(outcome["_id"]) == int(outcome_id_simple):
                                    output += '<outcome id=\"%s\" %s/>' % (outcome['_id'], result_str)
                                else:
                                    output += '<outcome id=\"%s\" result=\"0\"/>' % outcome['_id']
                            output += '</market>'
                            output += '</outcomes></bet_settlement>'
                            return output
        else:
            for market in data["markets"]:
                for specifier in market["specifiers"]:
                    if specifier["specifier"]:
                        output += '<market id="%s" specifiers="%s">' % (market["_id"], specifier["specifier"])
                    else:
                        output += '<market id="%s">' % (market["_id"])
                    for outcome in specifier["outComes"]:
                        output += '<outcome id=\"%s\" result=\"0\"/>' % outcome['_id']
                    output += '</market>'
            output += '</outcomes></bet_settlement>'

            return output
        raise AssertionError("ERR：在数据库中未找到投注项ID与注单中的投注项ID相同的项。")

    def generate_rollback_bet_settlement_str(self, match_id, outcome_info=(), producer=""):
        """
        生成回滚结算报文
        :param match_id:
        :param producer:
        :param outcome_info:
        :return:
        """

        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        data = self.dbq.get_match_data(match_id)

        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id
        output = '<rollback_bet_settlement product="%s" event_id="%s" timestamp="%s">' \
                 % (producer, data["_id"], self.get_current_timestamp())

        outcome_id = outcome_info[1]["outcome_id"]
        grep = re.search(r"^.+?_(\d+?)_(.*)_(.+?)$", outcome_id)
        outcome_market_id = grep.group(1)
        outcome_specifier = outcome_info[1]["specifier"]
        # outcome_id_simple = outcome_info[1]["outcome_id_simple"]

        for market in data["markets"]:
            if outcome_market_id == market["_id"]:
                if outcome_specifier:
                    for specifier in market["specifiers"]:
                        if specifier["specifier"] and specifier["specifier"] == outcome_specifier:
                            output += '<market id="%s" specifiers="%s"/>' % (market["_id"], specifier["specifier"])
                            output += '</rollback_bet_settlement>'
                            return output
                else:
                    output += '<market id="%s"/>' % market["_id"]
                    output += '</rollback_bet_settlement>'
                    return output
        else:
            raise AssertionError("没找到对应的项")

    # def generate_rollback_bet_settlement_str(self, match_id, producer=''):
    #     """
    #     生成回滚结算报文
    #     :param match_id:
    #     :param producer:
    #     :return:
    #     """
    #     producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
    #     data = self.dbq.get_match_data(match_id)
    #
    #     if not data:
    #         return "Sorry: [%s]未找到比赛数据" % match_id
    #     output = '<rollback_bet_settlement product="%s" event_id="%s" timestamp="%s">' \
    #              % (producer, data["_id"], self.get_current_timestamp())
    #
    #     for market in data["markets"]:
    #         for specifier in market["specifiers"]:
    #             if specifier["specifier"]:
    #                 output += '<market id="%s" specifiers="%s"/>' % (market["_id"], specifier["specifier"])
    #             else:
    #                 output += '<market id="%s"/>' % (market["_id"])
    #     output += '</rollback_bet_settlement>'
    #     return output

    def generate_rollback_bet_cancel_str(self, match_id, start_stamp, end_stamp, producer=""):
        """
        生成订单取消回滚报文
        :param match_id:
        :param start_stamp:
        :param end_stamp:
        :param producer:
        :return:
        """
        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        if not producer:
            return "Notice: 未找到对应的比赛。"
        data = self.dbq.get_match_data(match_id)
        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id
        output = '<rollback_bet_cancel end_time="%s" event_id="%s" product="%s" start_time="%s" timestamp=' \
                 '"%s">' % (end_stamp, data["_id"], producer, start_stamp, self.get_current_timestamp())

        for market in data["markets"]:
            for specifier in market["specifiers"]:
                if specifier["specifier"]:
                    output += '<market id="%s" specifiers="%s"/>' % (market["_id"], specifier["specifier"])
                else:
                    output += '<market id="%s"/>' % (market["_id"])

        output += '</rollback_bet_cancel>'
        return output

    def send_bet_settlement(self, match_id, outcome_info=(), certainty='2', producer='', result="输"):
        """
        注单结算
        :param match_id:
        :param outcome_info:  是否取消所有：是|否
        :param certainty: 1|2
        :param producer:  1|3
        :param result:  输|赢|赢一半|输一半|走盘
        :return:
        """
        # producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        # if not producer:
        #     raise AssertionError("Notice: 未找到对应的比赛。")
        data = self.generate_settlement_str_by_order(match_id, outcome_info, certainty, producer, result)
        print("返回结果为: %s" % self.data_post(data))

    def send_bet_settlement_allmarkets(self, match_id, certainty='2', producer=''):
        """
        注单结算-比赛所有盘口发送结算
        :param match_id:
        :param certainty: 1|2
        :param producer:  1|3
        :return:
        """
        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        if not producer:
            raise AssertionError("Notice: 未找到对应的比赛。")
        data = self.generate_settlement_str(match_id, certainty=certainty, producer=producer)
        print("返回结果为: %s" % self.data_post(data))

    def send_bet_cancel(self, match_id, cancel_all, start_stamp="", end_stamp="", reason="12"):
        """
        注单取消
        :param match_id:
        :param cancel_all:  是否取消所有：是|否
        :param start_stamp:
        :param end_stamp:
        :param reason:  3无法核实结果|5取消赛事|7比赛结束因为对方弃权或取消资格|9竞争对手已退休或未露面|10赛事弃废|11赛事推迟|
                        12 不正确的赔率|13 不正确的统计|||15 客户端结算需要|8 赛事平局（下注多场赛事都是平局）|16开始的投手转换
        :return:
        """
        data = self.generate_bet_cancel_str(match_id, cancel_all, start_stamp=start_stamp, end_stamp=end_stamp,
                                            reason=reason)
        print(data)
        self.data_post(data)

    def send_bet_cancel_rollback(self, match_id, start_stamp, end_stamp):
        """
        注单取消回滚
        :param match_id:
        :param start_stamp:
        :param end_stamp:
        :return:
        """
        data = self.generate_rollback_bet_cancel_str(match_id, start_stamp, end_stamp)
        print(data)
        self.data_post(data)

    def send_bet_settlement_rollback(self, match_id, outcome_info=(), producer=""):
        """
        注单结算回滚
        :param match_id:
        :param producer:
        :param outcome_info:
        :return:
        """
        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        data = self.generate_rollback_bet_settlement_str(match_id, outcome_info, producer)
        print(self.data_post(data))

    def send_odds_change(self, match_id, outcome_info, producer="", specifier_status="", outcome_activity="", odds=""):
        """
        赔率变更
        :param match_id:
        :param outcome_info:
        :param producer:
        :param specifier_status:  是|否
        :param outcome_activity:   是|否
        :param odds:
        :return:
        """
        data = self.generate_odds_change_str(match_id, outcome_info, producer, specifier_status, outcome_activity, odds)
        print(data)
        self.data_post(data)

    def generate_bet_cancel_str(self, match_id, cancel_all="是", producer="3", start_stamp="", end_stamp="",
                                reason="12"):
        """
        生成订单取消报文
        :param match_id:
        :param cancel_all:  是否取消所有：是|否
        :param producer:    1|3，default:3
        :param start_stamp:
        :param end_stamp:
        :param reason:  3无法核实结果|5取消赛事|7比赛结束因为对方弃权或取消资格|9竞争对手已退休或未露面|10赛事弃废|11赛事推迟|
                        12 不正确的赔率|13 不正确的统计|||15 客户端结算需要|8 赛事平局（下注多场赛事都是平局）|16开始的投手转换
        :return:
        """
        data = self.dbq.get_match_data(match_id)
        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id

        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        if not producer:
            return "Notice: 未找到对应的比赛。"
        if cancel_all != "是":
            output = '<bet_cancel end_time="%s" event_id="%s" product="%s" start_time="%s" timestamp=' \
                     '"%s">' % (end_stamp, data["_id"], producer, start_stamp, self.get_current_timestamp())
        else:
            output = '<bet_cancel event_id="%s" product="%s" timestamp=' \
                     '"%s">' % (data["_id"], producer, self.get_current_timestamp())

        for market in data["markets"]:
            for specifier in market["specifiers"]:
                if specifier["specifier"]:
                    output += '<market id="%s" specifiers="%s" void_reason="%s"/>' % \
                              (market["_id"], specifier["specifier"], reason)

                else:
                    output += '<market id="%s" void_reason="%s"/>' % (market["_id"], reason)
        output += '</bet_cancel>'
        return output

    def generate_bet_stop_str(self, match_id, producer, market_set, market_status):
        """
        生成停止下注报文
        :param match_id:
        :param producer:
        :param market_set:
        :param market_status:
        :return:
        """
        data = self.dbq.get_match_data(match_id)
        market_status_dic = {"活跃": "0",
                             "暂停": "2"}
        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id
        return '<bet_stop groups="%s" market_status="%s" product="%s" event_id="%s" timestamp="%s"/>' \
               % (market_set, market_status_dic[market_status], producer, data["_id"], self.get_current_timestamp())

    @staticmethod
    def generate_fixture_change_str(match_id, change_type, producer):
        change_type_dic = {"新增": "1",
                           "开始时间改变": "2",
                           "比赛已经关闭": "3",
                           "比赛形式改变": "4",
                           "直播改变": "5"}
        return '<fixture_change event_id="sr:match:%s" change_type="%s" product="%s"/>' \
               % (match_id, change_type_dic[change_type], producer)

    def generate_odds_change_str(self, match_id, outcome_info, producer="", specifier_status="", outcome_activity="",
                                 odds=""):
        """
        生成赔率变更报文
        :param match_id:
        :param outcome_info:
        :param producer:
        :param specifier_status: 活动|暂停|非活动|已结算
        :param outcome_activity: 是|否
        :param odds:
        :return:
        """
        specifier_status_dic = {"活动": "1", "暂停，显示但不可投注": "-1", "非活动，不显示": "0", "取消": "-4", "已结算": "-3"}
        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        match_status_dic = {"not_started": "0", "live": "6"}

        # data = self.dbq.get_match_data(match_id)
        # outcome_id = outcome_info[1]["outcome_id"]
        outcome_match_id = outcome_info[0]
        # outcome_market_id = outcome_info[1]["market_id"]
        # outcome_market_status = outcome_info[1]["market_status"]
        outcome_market_simple_id = outcome_info[1]["market_id_simple"]
        outcome_specifier = outcome_info[1]["specifier"]
        outcome_id_simple = outcome_info[1]["outcome_id_simple"]
        outcome_odds = outcome_info[1]["odds"]
        outcome_active = outcome_info[1]["is_active"]
        outcome_specifier_status = outcome_info[1]["specifier_status"]
        # match_id_simple = outcome_info[1]["match_id_simple"]
        outcome_probabilities = outcome_info[1]["probabilities"]
        outcome_match_status = match_status_dic[outcome_info[1]["match_status"]]

        outcome_specifier_status = outcome_specifier_status if not specifier_status else \
            specifier_status_dic[specifier_status]
        outcome_odds = outcome_odds if not odds else odds
        if outcome_activity:
            out_active = "1" if outcome_activity == "是" else "0"
        else:
            out_active = "1" if outcome_active else "0"
        timestamp = self.cf.get_timestamp()
        output = '<odds_change product="%s" event_id="%s" timestamp="%s">' \
                 '<sport_event_status status="0" match_status="%s"/><odds>' % (producer, outcome_match_id, timestamp,
                                                                               outcome_match_status)
        is_favourite = ' favourite="1" ' if outcome_info[1]["is_favourite"] else ""
        specifier = 'specifiers="%s"' % outcome_specifier
        output += '<market %s status="%s" id="%s" %s><outcome id="%s" odds="%s" probabilities="%s" ' \
                  'active="%s"/></market>' \
                  % (is_favourite, outcome_specifier_status, outcome_market_simple_id, specifier,
                     outcome_id_simple, outcome_odds, outcome_probabilities, out_active)
        output += '</odds></odds_change>'
        return output

    def send_message_to_datasourse(self, order_no="", sort=0, certainty='2', result=None,result_handicap=None):

        """
        注单结算
        :param order_no:
        :param sort:  单注/串关
        :param certainty:  1|3
        :param result:  输|赢|赢一半|输一半|走盘
        :return:
        """
        sort_num_old = bc.generate_settlement_str_by_count_orderNo(order_no=order_no)
        sort_num=len(sort_num_old)
        message=''
        if int(sort_num)>1:
            sort_num_list=[]
            for num in range(0,int(sort_num)):
                sort_num_list.append(num)
            for sort in sort_num_list:
                # sql =f"SELECT a.spliced_outcome_id FROM `bfty_credit`.`o_account_order_match` as a " \
                #   f"LEFT JOIN o_account_order_match_update as b   ON (a.order_no=b.order_no AND a.match_id=b.match_id) WHERE a.`order_no` = '{order_no}' AND b.sub_order_status='1'"
                # sort_num_old = self.my.query_data(sql, db_name='bfty_credit')
                # sort_num_new = len(sort_num_old)
                #
                # if sort_num_new==len(sort_num_list):
                #     # print(f"正在循环的sort：{sort},获取新的sort：{sort_num_new}，列表原数据{sort_num_list}")
                #     message = bc.generate_settlement_str_by_orderNo(order_no=order_no, sort=int(sort), certainty=certainty,result=result)
                # else:
                #     break
                message = bc.generate_settlement_str_by_orderNo(order_no=order_no, sort=int(sort), certainty=certainty, result=result,result_handicap=result_handicap)
                if not message:
                    raise AssertionError("Notice: 未找到对应的比赛。")
                print("接受返回结果为: %s" % self.data_post(data=message)+"\n")
        else:
            if (int(sort_num))==0:
                #获取比赛ID
                match_num=bc.generate_settlement_str_by_match_count( order_no=order_no)
                # 获取比赛时间
                match_time=bc.generate_settlement_str_by_match_time(order_no=order_no)
                num_list = []
                match_id_lsit=[]
                match_id_time_list=[]
                for time_num in range(0,int(len(match_num))):
                    num_list.append(time_num)
                for number in num_list:
                    match_time_0=(match_time[number][0])
                    now_time=datetime.datetime.now()
                    new_time=match_time_0+datetime.timedelta(minutes=150)
                    if now_time>new_time:
                        match_id_lsit.append(match_num[number][0])
                        match_id_time_list.append((match_time[number][0]).strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        pass
                print("\033[31m该笔订单，包含已结束的比赛，无法结算比赛ID：\033[0m"+str(match_id_lsit)+"\n"+"\033[31m无法结算比赛时间：\033[0m"+str(match_id_time_list))
            else:
                if (int(sort_num))==1:
                    sort=0
                    message = bc.generate_settlement_str_by_orderNo(order_no=order_no, sort=sort, certainty=certainty, result=result,result_handicap=result_handicap)
                    if not message:
                        raise AssertionError("Notice: 未找到对应的比赛。")
                    print("接受返回结果为: %s" % self.data_post(data=message)+"\n")





if __name__ == "__main__":
    #120环境
    mongo_inf = ['app', '123456', '192.168.10.120', '27017']
    mysql_inf = ['192.168.10.121', 'root', 's3CDfgfbFZcFEaczstX1VQrdfRFEaXTc', '3306']
    #MDE环境
    # mongo_inf = ['sport_test', 'BB#gCmqf3gTO5777', '35.194.233.30', '27017']
    # mysql_inf = ['35.194.233.30', 'root', 'BB#gCmqf3gTO5b*', '3306']


    # mf = MongoFunc(mongo_inf)
    bc = BetController(mysql_inf, mongo_inf)
    # bc.generate_odds_change_str("25061200", )

    # dataInfo = ['sr:match:27885068', {"market_id_simple": 16,"specifier":'hcp=0', "outcome_id_simple":1714, "odds": 2.000, "is_active": True, "is_favourite":True,
    #                                   "specifier_status": 0, "probabilities": '0.46', "match_status": 'not_started'}]
    # odds_change = bc.generate_odds_change_str(match_id='sr:match:27885068',outcome_info=dataInfo)         # 生成赔率更新指令
    # print(odds_change)

    # match_list = bc.mysql.get_unsettled_order_matchID()
    # print(match_list)

    # match_list = ['33520247', '33703527', '29658234', '33570511', '33506455', '33493633']
    # for matchId in match_list:
    #     for i in range(len(match_list)):
    #         settled_message = bc.generate_settlement_str(match_id=matchId, certainty='1', producer='3')  # 生成单注结算指令
    #         # print(result,void_factor)
    #         if result==1 and  void_factor==0:
    #             print("\033[32m<!--赢--!>\033[0m")
    #         if result==0 and  void_factor==0:
    #             print("\033[31m<!--输--!>\033[0m")
    #         if result==1 and  void_factor==0.5:
    #             print("\033[32m<!--赢一半--!>\033[0m")
    #         if result==0 and  void_factor==0.5:
    #             print("\033[34m<!--输一半--!>\033[0m")
    #         if result==0 and  void_factor==1 and i!=5:
    #             print("\033[33m<!--走盘--!>\033[0m")
    #         if i==5:
    #             print("\033[35m<!--退款--!>\033[0m")
    #         print(settled_message)
    #     print("-----------------------------------------------------------------------------------------"+str(matchId)+"----------------------------------------------------------------")

    # new_order_list=[]
    # # order_list = ['XC9ZyPDAMNBt', 'XC9RnJAYRv4y']
    # order_list = ['XC9ZyPDAMNBt']
    # for order_no in order_list:
    #     settled_message = bc.generate_settlement_str_by_orderNo(order_no=order_no, sort=0, certainty='2', producer='3',result=None) # 生成注单结算指令
    #
    # #     new_order_list.append(settled_message)
    # # print(new_order_list)

    order_list=['XChTqgUMpDyp', 'XCkMJLaem29r', 'XCkMLZMYyht8', 'XCkMMxnxNbBK', 'XCkMMLKjzvg8', 'XCkMN9g3Hx6V', 'XCkMNrDG59VS', 'XCkMNFexdiak', 'XCkMUaeErMuP', 'XCkMXhfms2tv', 'XCM5vxTC6iBn', 'XCM5BY8rMUKc', 'XCMyYmpgJwkj', 'XCPiWXLfmiwS', 'XCPiXWvMDf6d', 'XCPiYTkCasqZ', 'XCPiZN2cdkQ5', 'XCPj2VNTDLiR', 'XCPj3VBbNVxA', 'XCPj4URsGi3r', 'XCPj5XbTWx34', 'XCPj6VcgGi8w', 'XCPj7W8iPfM3', 'XCPj8VxgmDNf', 'XCPja5yKwZiY', 'XCPjbPTRW75j', 'XCPjcLs8PhbG', 'XCPjdMADFDfs', 'XCPjf4qmTdzr', 'XCPjhiEE2xGs', 'XCPjm5DYR3qU', 'XCPjn5DPiPKV', 'XCPjrNrn2aZA', 'XCPmgEWbTeiX', 'XCPmiF9UT5Xu', 'XCPmkyijYZdF', 'XCPmpmvEBuqx', 'XCPmqk9sHUWX', 'XCPmrixUVkdQ', 'XCPmsm24Le9g', 'XCPmuS45u97m', 'XCPmvY9qz6Ri', 'XCPmwXD3hyXK', 'XCPmy4UHNrmD', 'XCPmzqXzRCEn', 'XCPmAB3BUvTS', 'XCPmBBTmQGQF', 'XCPmD3DtfHBr', 'XCPmDZHZfquh', 'XCPmEXDPu6mp', 'XCPpcaWtsnx4', 'XCPpdsUq2FB9', 'XCPpexuBsS2b', 'XCPpfwhVufer', 'XCPphnT7LqFY', 'XCPpimjTUvZs', 'XCPpkdSAjTT8', 'XCPpm9GH9nvD', 'XCPpn7zAzznE', 'XCPpp8bbRjBm', 'XCPpq5hV9NhZ', 'XCPpr4Fbf6YC', 'XCPprZ94pRcn', 'XCPpsV38YJpJ', 'XCPptRzzjinS', 'XCPpvNQYCgQ6', 'XCPpwQ5SN5SH', 'XCPpxR4bNn3m', 'XD5qGMcyV5em', 'XD5rQHMK3Cpa', 'XD5t3quxQSQz', 'XD5tnabj6gZK', 'XD5tWkSkfEvE', 'XD5ujWB5sug8', 'XD5uHXNfYTtW', 'XD5uMgrr5fV6', 'XD5uNg9dT26h', 'XD5uPtynrFFp', 'XD5uQyFSvMCa', 'XD5uRBNQ7bXE', 'XD5uTgKsRrig', 'XD5uUwTfSDWq', 'XD5uVCk4bTQC', 'XD5uXcA5kF25', 'XD5uYgkHcepV', 'XD5uZjCT6NVX', 'XD5v2nLqaStg', 'XD5v3rJ5tCka', 'XD5v4CGuKvWg', 'XD5v5MKAv55Z', 'XD5v6QntPxWR', 'XD5v7Vn45Dij', 'XD5v8Z9ruetp', 'XD5va98NnYvj', 'XD5vc87YBwzB', 'XD5vdfLfGPBa', 'XD5veAdzSFeK', 'XD5vi6d9y6wt', 'XD5vj3vFWZjb', 'XD5vk8n3J6Ca', 'XD5vmwYqcweF', 'XD5vrAtnaQEe', 'XD5vsJE7ZFtq', 'XD5vtPqxDdPG', 'XD5vuHhcFjqY', 'XD5vy5judnYw', 'XD5vN736wqZn', 'XD5ygbr5bpgw', 'XD5yhqugnTtk', 'XD5yip72N4dV', 'XD5yjjtDRbPi', 'XD5ykfzAVbEg', 'XD5ymcut2pPP', 'XD5yn9xdgxeX', 'XD5yp7nzyBFW', 'XD5yqcAeGJKR', 'XD5yr9qabuaa', 'XD5ys6KtbPCk', 'XD5yt3ER8Uww', 'XD5ytZGdtAeL', 'XD5yw8rvMsAs', 'XD5yx5GpESuD', 'XD5yy3tABRVn', 'XD5yz7arRryp', 'XD5yA8HrRbuS', 'XD5yBazdTh5z', 'XD5yC8aLrwYK', 'XD5yD8ZsXpiE', 'XD5yEdCiWJMT', 'XD5yHJTsWGks', 'XD5yJJur5hWe', 'XD5yKEMLp3JA', 'XD5yLzUHWbmS', 'XD5yQSRmLxWG', 'XD5yRQ5U2vzF', 'XD5ySNVsUHDU', 'XD5yTH7nK6DM', 'XD5yWK22aThP', 'XD5BG4ZGR5MQ', 'XD5C7LitXPgW', 'XD5C8Pzv6vXx', 'XD5C9KA4PWfx', 'XD5CaHf3iyYk', 'XD5CbGBkzUpx', 'XD5CcDPPyBPM', 'XD5CdyUaSvkh', 'XD5CeuQPdjp9', 'XD5CfrPmbdJp', 'XD5CgtMxWA4X', 'XD5ChMMxXrBu', 'XD5CjbuxhtRF', 'XD5CYRx5zdkK', 'XD5CZQgMKjid', 'XD5D2KMdUwFJ', 'XD5D3Gnh696P', 'XD5D4Ccgiy7x', 'XD5D5ykvr3Mw', 'XD5D6uDL5i4F', 'XD5D7pVzGwWa', 'XD5D8kFgzpjc', 'XD5D9i7cMkiX', 'XD5DafkJCJcM', 'XD5DbdrfEiXE', 'XD5Dc8wLTitq', 'XD5Dei5iqrFw', 'XD5DfnmtprG2', 'XD5DgkZg2AZV', 'XD5Dhi8UpLNM', 'XD5DijYLDimh', 'XD5DjipV9PpN', 'XD5DktZPWBqb', 'XD5Dmt5z9RBb', 'XD5DprhYCPwy', 'XD5DsPS8v8qt', 'XD5DwU4NnVft', 'XD5FHBK2pFs4', 'XD5FJG7Y3ba4', 'XD5FKCTDprUv', 'XD5FLzqmPJ7S', 'XD5FMx7k2K6T', 'XD5FNtJD5Cs8', 'XD5FPpGjJZuw', 'XD5FQjhX4BvN', 'XD5FRg2u7jLR', 'XD5FSdHhCSux', 'XD5FT9RB5uza', 'XD5FU5Fiabpr', 'XD5FV2EgSPbW', 'XD5FVYSGAV4t', 'XD5FWVESFtJ8', 'XD5FXSz2Lmkc', 'XD5FYQfcqr8e', 'XD5FZNqKsZ8F', 'XD5G2NkNYGdw', 'XD5G3NvkBsSM', 'XD5G4Lw25z8w', 'XD5G6LZ4sJAR', 'XD5G9Stny9pi', 'XD5GdWnG6era', 'XD5GUWy9g2MZ', 'XD5GVXRG4nqQ', 'XD5GWUzdhEZG', 'XD5GXSn84SKx', 'XD5GYMfFif4H', 'XD5GZGv6scLE', 'XD5H2BMkGWi5', 'XD5H3xCePqQS', 'XD5H4yJfAP4Y', 'XD5H5vrsQXDE', 'XD5H6tiZd5FM', 'XD5H7pjX9wqe', 'XD5H8kWa2DTC', 'XD5H9j6B8mkH', 'XD5HafYLN3Hy', 'XD5HbdvjPhiy', 'XD5HcdtNpEzQ', 'XD5HdbUb4UkV', 'XD5He9xf3tf4', 'XD5Hf9LmYvH9', 'XD5Hge6pE7KM', 'XD5HhbK5eJJZ', 'XD5HmmXtGEbQ', 'XD5HrsA85nhv', 'XD5JBEAmADEG', 'XD5JCDDSzYMs', 'XD5JDEtSk4zX', 'XD5JEA7Dh5kX', 'XD5JFvAWWLdG', 'XD5JGqFB6PqH', 'XD5JHkcsDsU5', 'XD5JJfvWfS2H', 'XD5JKbPHCxCA', 'XD5JL83N9tQv', 'XD5JM538K5De', 'XD5JMZDzaYMV', 'XD5JNY339FYR', 'XD5JPVwGN9kk', 'XD5JQU5w32YY', 'XD5JRRFqQSAG', 'XD5JSPxxzkBM', 'XD5JTMAgYwia', 'XD5JUJXJVuJH', 'XD5JVMeUCYQE', 'XD5JXGRwxRQe', 'XD5K3ZEAXn6G', 'XD5K82MW5p5E', 'XD5SqcHST2zy', 'XD5SsVhKpHcJ', 'XD5StSGga3R2', 'XD5SuPdpFgH4', 'XD5SvLsJsXeT', 'XD5SwKR4TUse', 'XD5SxJGdNv7f', 'XD5SyKdUrMyN', 'XD5SzGuauWKi', 'XD5SADuS4tm7', 'XD5SBzK453qD', 'XD5SCwnPDTMu', 'XD5SDtSjQTxr', 'XD5SEuAY2sEJ', 'XD5SFrNdhzKY', 'XD5SGpGBt9mX', 'XD5SHn3uSKaG', 'XD5SJkVvEdXa', 'XD5SKj2aHsax', 'XD5SLjT9S3V4', 'XD5SMiuqgUfS', 'XD5STVGDXnVL', 'XD5SY4Zzjqnc', 'XD5TchG8CzKE', 'XD5Tfi9bpqmY', 'XD5TgdJBmfAA', 'XD5ThdDYc5Tt', 'XD5Ti9bYDzLm', 'XD5Tj6PdQUF5', 'XD5Tk32ccaLU', 'XD5TkXEvFKuQ', 'XD5TmUjtVFRW', 'XD5TnRAPYmP7', 'XD5TpNsnM6CQ', 'XD5TqKgXb22m', 'XD5TrH9Dmwg9', 'XD5TsF4Marsv', 'XD5TtBN58czU', 'XD5TuBhmSkwn', 'XD5TvzJhJcps', 'XD5Twy5qeeph', 'XD5TxtSUCeCq', 'XD5TyvNushQK', 'XD5TzvhdAcQy', 'XD5TAuLAUhMg', 'XD5TBxhSq2fg', 'XD5TECivJKGn', 'XD5TJBAeSB6X']
    for order_no in order_list:
        print(f"共有 ",str(len(order_list))+" 笔结算注单,"+"正在结算第 "+str(order_list.index(order_no)+1)+" 笔注单："+str(order_no))
        message = bc.send_message_to_datasourse(order_no=str(order_no), sort=0, certainty="2",result=None,result_handicap=None)  # 生成注单结算指令
        print("已完成注单："+str(order_list.index(order_no)+1)+"  "+"未完成注单"+str(len(order_list)-(order_list.index(order_no)+1))+"\n"+"----------------------------------------------------------------------------------------------------------------"+"\n"+"\n")

    # data = bc.generate_settlement_str_by_orderNo(order_no='XCrZUaMY8ht8',sort=0,result="取消")
    # print(data)

    # order_list = ['XB4TpiA5pMYZ']
    # for order_no in order_list:
    #     print("共有 " + str(len(order_list)) + " 笔结算注单," + "正在结算第 " + str(order_list.index(order_no) + 1) + " 笔注单：" + str(order_no))
    #     message = bc.send_message_to_datasourse(order_no=str(order_no), sort=0, certainty="2", result="赢")  # 生成注单结算指令
    #     print("已完成注单：" + str(order_list.index(order_no) + 1) + "  " + "未完成注单" + str(
    #         len(order_list) - (order_list.index(order_no) + 1)) + "\n"
    #           + "----------------------------------------------------------------------------------------------------------------" + "\n" + "\n")



