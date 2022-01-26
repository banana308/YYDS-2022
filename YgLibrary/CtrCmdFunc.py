import requests
import re
import time
try:
    from .MongoFunc import MongoFunc, DbQuery
    from .CtrlQuery import CtrlIoDocs
except ImportError:
    from MongoFunc import MongoFunc, DbQuery
    from CtrlQuery import CtrlIoDocs


class BetController(object):
    def __init__(self, mysql_info, mongo_info, host="http://27.102.134.114:8808/mock/push"):
        """
        模拟ctrl给我司推送数据
        """
        self.host = host
        self.session = requests.session()
        self.dbq = DbQuery(mysql_info, mongo_info)
        self.ctrl_docs = CtrlIoDocs(mysql_info, mongo_info)

    def data_post(self, data):
        try:
            if "<bet_settlement" in data:
                output = ""
                all_match = re.findall('(<market.+?</market>)', data)
                start = re.search('(<bet_settlement.+?<outcomes>)', data)
                for element in [all[index: index + 3] for index in range(0, len(all_match), 3)]:
                    time.sleep(5)
                    post_data = start.group(0) + ''.join(element) + '</outcomes></bet_settlement>'
                    output += str(self.session.post(self.host, params=data).content)
                return output
            else:
                return str(self.session.post(self.host, data=data).content)
        except Exception as e:
            print(e)

    @staticmethod
    def get_current_timestamp():
        return str(int(time.time() * 1000))

    def generate_settlement_str(self, match_id, certainty='1', producer='1'):
        """
        生成结算报文
        :param match_id:
        :param certainty:
        :param producer:
        :return:
        """
        data = self.dbq.get_match_data(match_id)

        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id
        output = '<bet_settlement certainty=\"%s\" ' \
                 'product=\"%s\" event_id=\"%s\" timestamp=\"%s\"><outcomes>' % (certainty, producer, data["_id"],
                                                                                 self.get_current_timestamp())
        for market in data["markets"]:
            for specifier in market["specifiers"]:
                if specifier["specifier"]:
                    output += '<market id="%s" specifiers="%s">' % (market["_id"], specifier["specifier"])
                else:
                    output += '<market id="%s">' % (market["_id"])
                for outcome in specifier["outComes"]:
                    output += '<outcome id=\"%s\" result=\"0\" void_factor=\"\"/>' % outcome['_id']
                output += '</market>'
        output += '</outcomes></bet_settlement>'
        return output

    def generate_rollback_bet_settlement_str(self, match_id, producer):
        """
        生成回滚结算报文
        :param match_id:
        :param producer:
        :return:
        """
        data = self.dbq.get_match_data(match_id)

        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id
        output = '<rollback_bet_settlement product="%s" event_id="%s" timestamp="%s">' \
                 % (producer, data["_id"], self.get_current_timestamp())

        for market in data["markets"]:
            for specifier in market["specifiers"]:
                if specifier["specifier"]:
                    output += '<market id="%s" specifiers="%s"/>' % (market["_id"], specifier["specifier"])
                else:
                    output += '<market id="%s"/>' % (market["_id"])
        output += '</rollback_bet_settlement>'
        return output

    def generate_rollback_bet_cancel_str(self, match_id, start_stamp, end_stamp, producer):
        """
        生成订单取消回滚报文
        :param match_id:
        :param start_stamp:
        :param end_stamp:
        :param producer:
        :return:
        """
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

    def generate_bet_cancel_str(self, match_id, cancel_type, producer="", start_stamp="", end_stamp="", reason="12"):
        """
        生成订单取消报文
        :param match_id:
        :param cancel_type:
        :param producer:
        :param start_stamp:
        :param end_stamp:
        :param reason:
        :return:
        """
        data = self.dbq.get_match_data(match_id)
        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id

        producer = self.dbq.get_match_data(match_id, "producer") if not producer else producer
        if not producer:
            return "Notice: 未找到对应的比赛。"
        if cancel_type != "全部":
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

    def generate_odds_change_str(self, match_id, product, sport_event_status="", match_status="", market_status="",
                                 outcome_activity="", home_score="", away_score=""):
        """
        生成赔率变更报文
        :param match_id:
        :param product:
        :param sport_event_status:
        :param match_status:
        :param market_status:
        :param outcome_activity:
        :param home_score:
        :param away_score:
        :return:
        """
        data = self.dbq.get_match_data(match_id)
        sport_event_status_dic = {"未开始": "0",
                                  "进行中": "1",
                                  "暂停": "2",
                                  "结束": "3",
                                  "关闭": "4"}
        match_status_dic = {"未开始": "0",
                            "上半场加时": "41",
                            "下半场": "2",
                            "取消": "70",
                            "1st period": "1",
                            "First break": "301",
                            "2nd period": "2",
                            "Second break": "302",
                            "Interrunpted": "80",
                            "Suspended": "81",
                            "Abandoned": "90"}
        market_status_dic = {"活动": "1",
                             "暂停，显示但不可投注": "-1",
                             "非活动，不显示": "0",
                             "取消": "-4",
                             "已结算": "-3"}
        outcome_activity_dic = {"活跃": "1",
                                "不活跃": "0"}

        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id
        ctrl_data = self.ctrl_docs.query_match_all_log(match_id)
        if not ctrl_data:
            return "Notice: 未找到对应比赛！"
        odds = re.findall("<odds_change.+?</odds_change>", ctrl_data)
        output = odds[-1]
        output = re.sub(r'product="(\d+?)', 'product="' + product, output)
        output = re.sub(r'timestamp="(.+?)"', 'timestamp="' + self.get_current_timestamp() + '"', output)
        if sport_event_status != "Default":
            output = re.sub(r'sport_event_status status="(\d+?)"', 'sport_event_status status="%s"' %
                            sport_event_status_dic[sport_event_status], output)
        if match_status != "Default":
            output = re.sub(r'match_status="(\d+?)"', 'match_status="%s"' % match_status_dic[match_status], output)
        if market_status != "Default":
            output = re.sub(r'market status="(\d+?)"', 'market status="%s"' % market_status_dic[market_status], output)
        if outcome_activity != "Default":
            output = re.sub(r'active="(\d+?)"', 'active="%s"' % outcome_activity_dic[outcome_activity], output)
        if home_score and away_score:
            if "reporting" in output:
                output = re.sub(r'home_score="(\d+?)"', 'home_score="%s"' % home_score, output)
                output = re.sub(r'away_score="(\d+?)"', 'away_score="%s"' % away_score, output)
            else:
                output = re.sub(r'<sport_event_status (.+?)/>', r'<sport_event_status \1 reporting="1" home_score="%s" '
                                                                r'away_score="%s"/>' % (home_score, away_score), output)
        if sport_event_status in ["进行中", "暂停"] and not home_score:
            if "reporting" not in output:
                output = re.sub(r'<sport_event_status (.+?)/>', r'<sport_event_status \1 reporting="1" home_score="0" '
                                                                r'away_score="0"/>', output)
        return output
