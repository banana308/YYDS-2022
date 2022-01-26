import datetime

import pymongo
import re

try:
    from MyExceptions import *
    from CommonFunc import CommonFunc
    from Config import *
except ModuleNotFoundError:
    from .MyExceptions import *
    from .CommonFunc import CommonFunc
    from .Config import *


class MongoFunc(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mongo_info, *args, **kwargs):
        """
        :param mongo_info: 用户名，密码，IP，端口
        """
        if not mongo_info[0]:
            self.client = pymongo.MongoClient(mongo_info[2], int(mongo_info[3]))
        else:
            self.client = pymongo.MongoClient('mongodb://{}:{}@{}:{}'.format(mongo_info[0], mongo_info[1],
                                                                             mongo_info[2], int(mongo_info[3])))
        self.mongo_info = mongo_info
        try:
            self.client.list_database_names()
        except Exception as e:
            if "timed out" in str(e):
                raise AssertionError("Err: 连接Mongo服务器失败,请检查服务器信息是否填写正确!")
        self.database = 'sport_test'
        self.my_db = self.client[self.database]

    def switch_database(self, db_name):
        self.my_db = self.client[db_name]

    def mg_select(self, table, condition_sql=None, choose_sql=None, sort=None):
        """
        mongo 通用查询
        :param table:
        :param condition_sql:
        :param choose_sql:
        :param sort:
        :return:
        """
        if condition_sql:
            return self.my_db[table].find(condition_sql, projection=choose_sql, sort=sort)
        else:
            return self.my_db[table].find(projection=choose_sql, sort=sort)

    def mg_aggregate(self, table, sql):
        """
        mongo 聚合查询
        :param table:
        :param sql:
        :return:
        """
        return list(self.my_db[table].aggregate(sql))


class DbQuery(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, mongo_info, *args, **kwargs):
        self.mongo_info = mongo_info
        self.mg = MongoFunc(self.mongo_info)
        self.cf = CommonFunc()

    def get_match_info(self, match_id):
        """
        按格式返回比赛详细信息
        :param match_id:
        :return:
        """
        data = self.get_match_data(match_id)
        if not data:
            return "Sorry: [%s]未找到比赛数据" % match_id

        output = ["体育类型： (%s), id: (%s) " % (data["tournamentSportName"], data["tournamentSportId"]),
                  "联赛： (%s), id:  (%s)" % (data["tournamentName"], data["tournamentCategoryId"]),
                  "比赛： (%s), id: (%s)" % (data["homeTeamName"] + "  VS  " + data["awayTeamName"], data["_id"]),
                  "比赛预计开始时间： " + str(data["matchScheduled"]), "比赛状态： " + data["matchStatus"], "盘口信息如下： "]

        for market in data["markets"]:
            output.append("\t盘口名称:(%s) , 盘口id:(%s), producer:(%s)" % (market["marketName"], market["marketId"],
                                                                      market["producer"]))
            output.append("\t\tSpecifier：")
            for specifier in market["specifiers"]:
                output.append("\t\t\tSpecifier is: (%s), id: (%s)" % (specifier["specifier"], specifier["specifierId"]))
                for outcome in specifier["outComes"]:
                    probabilities = 'None' if 'probabilities' not in outcome.keys() else outcome["probabilities"]
                    odds = 'None' if 'odds' not in outcome else outcome["odds"]
                    output.append("\t\t\t\t投注项名称： (%s), outcomeId: (%s), 赔率：(%s), 中奖概率:(%s),是否可下注:(%s)" %
                                  (outcome["name"], outcome["outcomeId"], odds, probabilities, outcome["isActive"]))
        return "\n".join(output)

    def get_match_data(self, match_id, key=""):
        """
        获取比赛信息数据
        :param match_id:
        :param key:
        :return:
        """
        select_dic = {"_id": 1,
                      "matchStatus": 1,
                      "matchScheduled": 1,
                      "homeTeamName": 1,
                      "awayTeamName": 1,
                      "tournamentName": 1,
                      "tournamentCateoryName": 1,
                      "tournamentSportName": 1,
                      "markets": 1,
                      "bookStatus": 1,
                      "createTime": 1,
                      "producer": 1,
                      "neutralGroundFlag": 1,
                      "updateTime": 1,
                      "awayScore": 1,
                      "eventTime": 1,
                      "homeScore": 1,
                      "period": 1,
                      "periodScores": 1,
                      "tournamentCategoryId": 1,
                      "tournamentSportId": 1,
                      "tournamentSportCategoryId": 1}
        try:
            # return self.mg.mg_select("soccer_match", {"_id": {"$regex": "^.*%s.*$" % match_id}}, select_dic)[0]
            ft = {"_id": re.compile(str(match_id))}
            data = self.mg.mg_select("soccer_match", ft, select_dic)
            return data[0] if not key else data[0][key]
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_market_or_outcome_name(data, opt_id, specifier='', opt_type='outcome'):
        """
        获取盘口或投注项名称
        :param data: 比赛结果数据，调用get_match_data返回
        :param opt_id:
        :param opt_type:  outcome|market
        :param specifier:
        :return:
        """
        if opt_type == "market":
            for market in data["markets"]:
                if market["_id"] == opt_id:
                    return market["marketName"]
            return "Notice: 没有找到%s对应的market数据" % opt_id
        else:
            for market in data["markets"]:
                # specifier_map_nr = market["specifierMap"]["mapnr"]
                if specifier:
                    for spf in market["specifiers"]:
                        if spf["specifier"] == specifier:
                            for out_come in spf["outComes"]:
                                if out_come["_id"] == opt_id:
                                    return out_come["name"]
                    return "Notice: 没有找到%s对应的投注选项" % opt_id
                else:
                    for out_come in market["specifiers"][0]["outComes"]:
                        if out_come["_id"] == opt_id:
                            return out_come["name"]
            return "Notice: 没有找到对应的数据"

    def get_outcome_info_by_id(self, match_id, market_id, outcome_id):
        """
        通过投注项ID，查询对应的specifier 和投注项简化ID
        :param match_id:
        :param market_id:
        :param outcome_id:
        :return:
        """
        match_data = self.get_match_data(match_id, "markets")
        match_status = self.get_match_data(match_id, "matchStatus")

        for market in match_data:
            if market["marketId"] == market_id:
                for specifier in market["specifiers"]:
                    is_favourite = specifier["isFavourite"]
                    for out_come in specifier["outComes"]:
                        if out_come["outcomeId"] == outcome_id:
                            return specifier["specifier"], out_come["_id"], is_favourite, out_come["isActive"], \
                                   "0.66", market["status"], specifier["status"], match_status, out_come["odds"]
        raise AssertionError("【ERR】未找到该投注项,投注项ID: %s" % outcome_id)

    def get_league_name_list_sql(self, sport_type):
        """
        获取联赛名称列表
        :param sport_type:
        :return:
        """
        select_dic = {"_id": 1,
                      "englishName": 1,
                      "chineseName": 1}
        try:
            ft = {"sportNameZh": re.compile(sport_type)}
            data = self.mg.mg_select("tournament", ft, select_dic)
            name_list = []
            [name_list.append(item["chineseName"]) for item in data]
            return name_list
        except Exception as e:
            print(e)
            return None

    def get_market_and_specifier_status(self, outcome_info):
        """
        获取soccer match表中的market或specifier的status值
        :param outcome_info:
        :return: market status|specifier status|specifier isActive
        """
        outcome_id = outcome_info[1]["outcome_id"]
        # grep = re.search(r".+?:(\d+?)_(\d+?)_", outcome_id)
        outcome_match_id = outcome_info[0]
        outcome_market_id = outcome_info[1]["market_id"]
        rtn = self.get_outcome_info_by_id(outcome_match_id, outcome_market_id, outcome_id)
        outcome_specifier = rtn[0]

        # outcome_id_simple = rtn[1]
        markets = self.get_match_data(outcome_match_id, "markets")
        for market in markets:
            if market["marketId"] == outcome_market_id:
                market_status = market["status"]
                for specifier in market["specifiers"]:
                    if not outcome_specifier:
                        return market_status, specifier["status"], specifier["isActive"]
                    else:
                        if outcome_specifier == specifier["specifier"]:
                            return market_status, specifier["status"], specifier["isActive"]
                else:
                    raise AssertionError("[ERR]没有找到对应的specifier")
        else:
            raise AssertionError("[ERR]没有找到对应的盘口")

    def get_outcome_origin_odds(self, outcome_info):
        """
        获取投注项原始赔率
        :param outcome_info:
        :return: origin odds
        """
        outcome_id = outcome_info[1]["outcome_id"]
        # grep = re.search(r".+?:(\d+?)_(\d+?)_", outcome_id)
        outcome_match_id = outcome_info[0]
        outcome_market_id = outcome_info[1]["market_id"]

        match_data = self.get_match_data(outcome_match_id, "markets")

        for market in match_data:
            if market["marketId"] == outcome_market_id:
                for specifier in market["specifiers"]:
                    for out_come in specifier["outComes"]:
                        if out_come["outcomeId"] == outcome_id:
                            return out_come["odds"]
        raise AssertionError(f"没有找到该投注项：{outcome_info}")

    def get_client_today_match_list_sql(self, sport_name):
        """
        获取客户端今日比赛列表
        :param sport_name:
        :return:
        """
        md_start_date, md_end_date = self.cf.get_md_search_time()
        now = self.cf.get_current_time().strftime("%Y-%m-%d-%H-%M-%S").split("-")
        now = datetime.datetime(int(now[0]), int(now[1]), int(now[2]), int(now[3]), int(now[4]), int(now[5]))
        if sport_name == "足球":
            sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                  "$lt": md_end_date,
                                                  '$gt': now},
                               "matchStatus": "not_started",
                               "tournamentSportId": str(small_sport_id_dic[sport_name]),
                               "mainActiveMarket": {'$gte': 2},
                               "isLive": None}},
                   {'$project': {'_id': 1, 'matchScheduled': 1}}]
        else:
            sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                  "$lt": md_end_date,
                                                  '$gt': now},
                               "matchStatus": "not_started",
                               "tournamentSportId": str(small_sport_id_dic[sport_name]),
                               "activeMarket": {'$gt': 0},
                               "isLive": None}},
                   {'$project': {'_id': 1, 'matchScheduled': 1}}]
        print(sql)
        rtn = self.mg.mg_aggregate('soccer_match', sql)
        return len(rtn)

    def get_client_today_tournament_list_num_msql(self, sport_name):
        """
        获取客户端今日联赛数量
        :param sport_name:
        :return:
        """
        md_start_date, md_end_date = self.cf.get_md_search_time()
        now = self.cf.get_current_time().strftime("%Y-%m-%d-%H-%M-%S").split("-")
        now = datetime.datetime(int(now[0]), int(now[1]), int(now[2]), int(now[3]), int(now[4]), int(now[5]))
        if sport_name == "足球":
            sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                  "$lt": md_end_date,
                                                  '$gt': now},
                               "matchStatus": "not_started",
                               "tournamentSportCategoryId": str(sport_id_dic[sport_name]),
                               "mainActiveMarket": {'$gte': 2},
                               "isLive": None}},
                   {'$group': {"_id": "$tournamentId",
                               "count": {"$sum": 1},
                               "name": {"$first": "$tournamentName"}}},
                   {"$sort": {"count": -1}}]
        else:
            sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                  "$lt": md_end_date,
                                                  '$gt': now},
                               "matchStatus": "not_started",
                               "tournamentSportCategoryId": str(sport_id_dic[sport_name]),
                               "activeMarket": {'$gt': 0},
                               "isLive": None}},
                   {'$group': {"_id": "$tournamentId",
                               "count": {"$sum": 1},
                               "name": {"$first": "$tournamentName"}}},
                   {"$sort": {"count": -1}}]
        data = self.mg.mg_aggregate('soccer_match', sql)
        tournament_num = len(data)
        tournament_detail = []
        [tournament_detail.append((item["name"], item["count"])) for item in data]
        return tournament_num, tournament_detail

    def get_client_live_match_list_msql(self, sport_name):
        """
        获取客户端滚球比赛列表中
        :param sport_name:
        :return:
        """
        sql = [{"$match": {"matchStatus": "live",
                           "tournamentSportId": str(small_sport_id_dic[sport_name]),
                           "isLive": True}},
               {'$project': {'_id': 1, 'matchScheduled': 1}}]
        return len(self.mg.mg_aggregate('soccer_match', sql))

    def get_client_live_tournament_list_num_msql(self, sport_name):
        """
        获取客户端滚球联赛及其下的比赛数量
        :param sport_name:
        :return:
        """
        sql = [{"$match": {"matchStatus": "live",
                           "tournamentSportCategoryId": str(sport_id_dic[sport_name]),
                           "isLive": True}},
               {'$group': {"_id": "$tournamentId",
                           "count": {"$sum": 1},
                           "name": {"$first": "$tournamentName"}}},
               {"$sort": {"count": -1}}]
        data = self.mg.mg_aggregate('soccer_match', sql)
        tournament_num = len(data)
        tournament_detail = []
        [tournament_detail.append((item["name"], item["count"])) for item in data]
        return tournament_num, tournament_detail

    def get_client_pre_match_list_msql(self, sport_name, diff=""):
        """
        获取客户端早盘比赛列表中
        :param sport_name:
        :param diff
        :return:
        """
        if not diff:
            md_start_date, md_end_date = self.cf.get_md_search_time(1)
            if sport_name == "足球":
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportId": str(small_sport_id_dic[sport_name]),
                                   "mainActiveMarket": {'$gte': 2},
                                   "isLive": {"$ne": True}, 'markets': {"$ne": None}}},
                       {'$project': {'_id': 1, 'matchScheduled': 1}}]
            else:
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportId": str(small_sport_id_dic[sport_name]),
                                   "activeMarket": {'$gt': 0},
                                   "isLive": {"$ne": True}, 'markets': {"$ne": None}}},
                       {'$project': {'_id': 1, 'matchScheduled': 1}}]
        elif int(diff) > 7:
            md_start_date, md_end_date = self.cf.get_md_search_time(int(diff))
            if sport_name == "足球":
                sql = [{"$match": {"matchScheduled": {"$gt": md_start_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportId": str(small_sport_id_dic[sport_name]),
                                   "mainActiveMarket": {'$gte': 2},
                                   "isLive": {"$ne": True}, 'markets': {"$ne": None}}},
                       {'$project': {'_id': 1, 'matchScheduled': 1}}]
            else:
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportId": str(small_sport_id_dic[sport_name]),
                                   "activeMarket": {'$gt': 0},
                                   "isLive": {"$ne": True}, 'markets': {"$ne": None}}},
                       {'$project': {'_id': 1, 'matchScheduled': 1}}]
        else:
            md_start_date, md_end_date = self.cf.get_md_search_time(int(diff))
            if sport_name == "足球":
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                      "$lt": md_end_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportId": str(small_sport_id_dic[sport_name]),
                                   "mainActiveMarket": {'$gte': 2},
                                   "isLive": {"$ne": True}, 'markets': {"$ne": None}}},
                       {'$project': {'_id': 1, 'matchScheduled': 1}}]
            else:
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                      "$lt": md_end_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportId": str(small_sport_id_dic[sport_name]),
                                   "activeMarket": {'$gt': 0},
                                   "isLive": {"$ne": True}, 'markets': {"$ne": None}}},
                       {'$project': {'_id': 1, 'matchScheduled': 1}}]
        print(sql)
        return len(self.mg.mg_aggregate('soccer_match', sql))

    def get_client_pre_tournament_list_num_msql(self, sport_name, diff=0):
        """
        获取客户端早盘联赛及其下的比赛数量
        :param sport_name:
        :param diff： 0为所有，否则为具体某一天
        :return:
        """
        if diff == 0:
            md_start_date, md_end_date = self.cf.get_md_search_time(1)
            if sport_name == "足球":
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportCategoryId": str(sport_id_dic[sport_name]),
                                   "mainActiveMarket": {'$gte': 2},
                                   "isLive": False}},
                       {'$group': {"_id": "$tournamentId",
                                   "count": {"$sum": 1},
                                   "name": {"$first": "$tournamentName"}}},
                       {"$sort": {"count": -1}}]
            else:
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportCategoryId": str(sport_id_dic[sport_name]),
                                   "activeMarket": {'$gt': 0},
                                   "isLive": False}},
                       {'$group': {"_id": "$tournamentId",
                                   "count": {"$sum": 1},
                                   "name": {"$first": "$tournamentName"}}},
                       {"$sort": {"count": -1}}]
        else:
            md_start_date, md_end_date = self.cf.get_md_search_time(diff)
            if sport_name == "足球":
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                      "$lt": md_end_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportCategoryId": str(sport_id_dic[sport_name]),
                                   "mainActiveMarket": {'$gte': 2},
                                   "isLive": False}},
                       {'$group': {"_id": "$tournamentId",
                                   "count": {"$sum": 1},
                                   "name": {"$first": "$tournamentName"}}},
                       {"$sort": {"count": -1}}]
            else:
                sql = [{"$match": {"matchScheduled": {"$gte": md_start_date,
                                                      "$lt": md_end_date},
                                   "matchStatus": "not_started",
                                   "tournamentSportCategoryId": str(sport_id_dic[sport_name]),
                                   "activeMarket": {'$gte': 2},
                                   "isLive": False}},
                       {'$group': {"_id": "$tournamentId",
                                   "count": {"$sum": 1},
                                   "name": {"$first": "$tournamentName"}}},
                       {"$sort": {"count": -1}}]
        data = self.mg.mg_aggregate('soccer_match', sql)
        tournament_num = len(data)
        tournament_detail = []
        [tournament_detail.append((item["name"], item["count"])) for item in data]
        return tournament_num, tournament_detail

    def get_ended_match_list_msql(self, diff, sport_name, if_h5=False):
        """
        获取已关闭的比赛列表
        """
        md_start_date, md_end_date = self.cf.get_md_search_time(diff)
        if if_h5:
            sql = [{'$match': {"matchScheduled": {"$gte": md_start_date, "$lt": md_end_date},
                               "tournamentSportId": {"$eq": small_sport_id_dic[sport_name]},
                               "periodScores": {"$ne": None},
                               "matchStatus": {"$in": ["ended", "closed", "abandoned", "cancelled"]}}},
                   {'$project': {
                       "_id": 1
                   }}]
        else:
            sql = [{'$match': {"matchScheduled": {"$gte": md_start_date, "$lt": md_end_date},
                               "tournamentSportId": {"$eq": small_sport_id_dic[sport_name]},
                               "matchStatus": {"$in": ["ended", "closed", "abandoned", "cancelled"]}}},
                   {'$project': {
                       "_id": 1
                   }}]
        print(sql)
        return self.mg.mg_aggregate('soccer_match', sql)

    def get_match_list_msql(self, diff, sport_name):
        """
        获取比赛列表
        """
        md_start_date, md_end_date = self.cf.get_md_search_time(diff)
        sql = [{'$match': {"matchScheduled": {"$gte": md_start_date, "$lt": md_end_date},
                           "tournamentSportId": {"$eq": small_sport_id_dic[sport_name]}}},
               {'$project': {
                   "_id": 1
               }}]
        return self.mg.mg_aggregate('soccer_match', sql)

    def get_match_score_msql(self, match_id):
        sql = [{"$match": {"_id": match_id}},
               {'$project': {'tournamentSportId': 1, 'periodStatisticsMap': 1, 'periodScores': 1}}]
        return self.mg.mg_aggregate('soccer_match', sql)

    def get_match_score_msql_new(self, match_id, if_closed=True):
        """
        查询比赛信息
        :param match_id
        :param if_closed: True 筛选closed的比赛| False 不筛选比赛状态
        """
        if if_closed:
            sql = [{"$match": {"_id": match_id, "matchStatus": {"$in": ["closed", "ended"]}}},
                   {'$project': {'tournamentSportId': 1, 'periodStatisticsMap': 1, 'periodScores': 1,
                                 "homeTeamNameDic": 1, "awayTeamNameDic": 1, "tournamentNameDic": 1,
                                 "matchStatus": 1, "matchScheduled": 1, "periodDescription": 1}}]
        else:
            sql = [{"$match": {"_id": match_id}},
                   {'$project': {'tournamentSportId': 1, 'periodStatisticsMap': 1, 'periodScores': 1,
                                 "homeTeamNameDic": 1, "awayTeamNameDic": 1, "tournamentNameDic": 1,
                                 "matchStatus": 1, "matchScheduled": 1, "periodDescription": 1}}]
        print(sql)
        return self.mg.mg_aggregate('soccer_match', sql)

    def get_match_result_sql(self, sport_name="足球", date_diff=0, if_h5=False, source_type="总台"):
        """
        获取总台赛果
        :param date_diff: 日期偏移
        :param sport_name:
        :param if_h5:  True|False  h5会过滤掉periodScores为空的比赛
        :param source_type:  总台|h5|pc  h5会过滤掉periodScores为空的比赛
        :return:
        """
        rtn = self.get_ended_match_list_msql(date_diff, sport_name, if_h5)
        return [self.get_match_result_data_sql(match_data["_id"], False, source_type) for match_data in rtn]

    def get_match_result_data_sql(self, match_id, if_closed=True, source_type="总台"):
        """
        获取指定比赛的比分列表,包括部分比赛属性：即赛果数据
        :param match_id
        :param if_closed: True 筛选closed的比赛| False 不筛选比赛状态
        :param source_type:  总台|h5|pc  h5会过滤掉periodScores为空的比赛
        """
        rtn = self.get_match_score_msql_new(match_id, if_closed)
        if len(rtn) == 0:
            return
        match_data = rtn[0]
        period_score = {}
        match_status = None
        p1_score = ""
        p2_score = ""
        p3_score = ""
        p4_score = ""
        p5_score = ""
        p6_score = ""
        p7_score = ""
        p8_score = ""
        p9_score = ""
        half_corner_number_list_1st = ""
        half_corner_number_list_2nd = ""
        corner_number_list = ""
        half_card_score_list_1st = ""
        half_card_score_list_2nd = ""
        card_number_list = ""
        penalty_score = ""
        extra_score_list = ""
        half_score_list_1st = ""
        half_score_list_2nd = ""
        full_score_list = ""
        set_score_list = ""
        first_five = ""
        p1_des_list = ["上半场", "第一节", "第一盘", "第1局"]
        p2_des_list = ["下半场", "第二节", "第二盘", "第2局"]
        p3_des_list = ["加时", "第三节", "第三盘", "第3局"]
        p4_des_list = ["点球", "第四节", "第四盘", "第4局", "加时"]
        p5_des_list = ["加时", "第五盘", "第5局", "点球"]
        p6_des_list = ["第6局"]
        p7_des_list = ["第7局"]
        p8_des_list = ["第8局"]
        p9_des_list = ["第9局"]
        p10_des_list = ["加时"]

        home_team_name = match_data["homeTeamNameDic"]["zh"]
        away_team_name = match_data["awayTeamNameDic"]["zh"]
        if "tournamentNameDic" not in match_data:
            tournament_name = match_data["tournamentName"]
        else:
            tournament_name = match_data["tournamentNameDic"]["zh"]

        sport_id = match_data["tournamentSportId"]
        match_id = match_data["_id"]
        status = match_data["matchStatus"]
        match_date = datetime.datetime.strftime(match_data["matchScheduled"] + datetime.timedelta(hours=-4),
                                                "%Y-%m-%d %H:%M:%S")
        if status == "abandoned":
            match_status = "比赛中止"
        elif status in ("closed", "ended"):
            match_status = "已完成"
        elif status == "cancelled":
            match_status = "比赛取消"
            if sport_id == small_sport_id_dic["足球"]:
                back_str = [""] * 11
            elif sport_id == small_sport_id_dic["乒乓球"]:
                back_str = [""] * 9
            elif sport_id == small_sport_id_dic["网球"]:
                back_str = [""] * 7
            elif sport_id == small_sport_id_dic["棒球"]:
                back_str = [""] * 12
            elif sport_id == small_sport_id_dic["篮球"]:
                back_str = [""] * 8
            elif sport_id == small_sport_id_dic["羽毛球"]:
                back_str = [""] * 5
            elif sport_id == small_sport_id_dic["冰上曲棍球"]:
                back_str = [""] * 5
            else:
                back_str = [""] * 7
            return [match_id, match_date, tournament_name, home_team_name, away_team_name, match_status, back_str]

        if "periodScores" in match_data:
            full_score_list = [0, 0]
            half_score_list_1st = [0, 0]
            half_score_list_2nd = [0, 0]
            half_score_flag_1st = False
            half_score_flag_2nd = False
            set_score_list = [0, 0]

            period_data = match_data["periodScores"]
            for period in period_data:
                period_score.update({str(period["periodDescription"]): {"zh": period['periodDescription'],
                                                                        "home": period['homeScore'],
                                                                        "away": period['awayScore']}})
            home_all_score = away_all_score = 0
            for value in match_data['periodScores']:
                home_all_score += int(value["homeScore"])
                away_all_score += int(value["awayScore"])

            # 遍历每一条period score
            for period_data in match_data['periodScores']:
                home_score = int(period_data["homeScore"])
                away_score = int(period_data["awayScore"])
                # 如果是足球篮球，区分上下半场，全场不包括加时赛
                if sport_id == small_sport_id_dic["足球"]:
                    if period_data["periodDescription"] in p1_des_list:
                        half_score_flag_1st = True
                        half_score_list_1st = [home_score, away_score]
                    elif period_data["periodDescription"] in p2_des_list:
                        half_score_flag_2nd = True
                        half_score_list_2nd = [home_score, away_score]
                    elif period_data["periodDescription"] in p3_des_list:
                        extra_score_list = [home_score, away_score]
                    elif period_data["periodDescription"] in p4_des_list:
                        penalty_score = [home_score, away_score]
                    if period_data["periodDescription"] in p1_des_list + p2_des_list:
                        full_score_list[0] += home_score
                        full_score_list[1] += away_score
                # 篮球分上下半场，全场包括加时赛
                elif sport_id == small_sport_id_dic["篮球"]:
                    if period_data["periodDescription"] in p1_des_list + p2_des_list:
                        if period_data["periodDescription"] in p1_des_list:
                            p1_score = [home_score, away_score]
                        if period_data["periodDescription"] in p2_des_list:
                            p2_score = [home_score, away_score]
                        half_score_flag_1st = True
                        half_score_list_1st[0] += home_score
                        half_score_list_1st[1] += away_score
                    elif period_data["periodDescription"] in p3_des_list + p4_des_list:
                        if period_data["periodDescription"] in p3_des_list:
                            p3_score = [home_score, away_score]
                        if period_data["periodDescription"] in p4_des_list:
                            p4_score = [home_score, away_score]
                        half_score_flag_2nd = True
                        half_score_list_2nd[0] += home_score
                        half_score_list_2nd[1] += away_score
                    elif period_data["periodDescription"] in p5_des_list:
                        extra_score_list = [home_score, away_score]
                    full_score_list[0] += home_score
                    full_score_list[1] += away_score
                # 冰棍球全场不包括加时
                elif sport_id == small_sport_id_dic["冰上曲棍球"]:
                    if period_data["periodDescription"] in p1_des_list + p2_des_list + p3_des_list:
                        full_score_list[0] += home_score
                        full_score_list[1] += away_score
                        half_score_flag_1st = True
                    if period_data["periodDescription"] in p1_des_list:
                        p1_score = [home_score, away_score]
                    elif period_data["periodDescription"] in p2_des_list:
                        p2_score = [home_score, away_score]
                    elif period_data["periodDescription"] in p3_des_list:
                        p3_score = [home_score, away_score]
                    elif period_data["periodDescription"] in p4_des_list:
                        extra_score_list = [home_score, away_score]
                    elif period_data["periodDescription"] in p5_des_list:
                        penalty_score = [home_score, away_score]
                elif sport_id in [small_sport_id_dic["羽毛球"], small_sport_id_dic["乒乓球"],
                                  small_sport_id_dic["网球"], small_sport_id_dic["排球"], small_sport_id_dic["棒球"]]:
                    half_score_flag_1st = True
                    first_five = [0, 0]
                    if home_score > away_score:
                        full_score_list[0] += 1
                    elif home_score < away_score:
                        full_score_list[1] += 1

                    # 乒乓球、网球：局比分、盘比分
                    set_score_list[0] += home_score
                    set_score_list[1] += away_score

                    # 棒球：前五局
                    if period_data[
                        "periodDescription"] in p1_des_list + p2_des_list + p3_des_list + p4_des_list + p5_des_list:
                        first_five[0] += home_score
                        first_five[1] += away_score

                    if period_data["periodDescription"] in p1_des_list:
                        p1_score = [home_score, away_score]
                    elif period_data["periodDescription"] in p2_des_list:
                        p2_score = [home_score, away_score]
                    elif period_data["periodDescription"] in p3_des_list:
                        p3_score = [home_score, away_score]

                    if sport_id == small_sport_id_dic["乒乓球"]:
                        if period_data["periodDescription"] in p4_des_list:
                            p4_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p5_des_list:
                            p5_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p6_des_list:
                            p6_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p7_des_list:
                            p7_score = [home_score, away_score]
                    elif sport_id == small_sport_id_dic["网球"]:
                        if period_data["periodDescription"] in p4_des_list:
                            p4_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p5_des_list:
                            p5_score = [home_score, away_score]
                    elif sport_id == small_sport_id_dic["棒球"]:
                        if period_data["periodDescription"] in p4_des_list:
                            p4_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p5_des_list:
                            p5_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p6_des_list:
                            p6_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p7_des_list:
                            p7_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p8_des_list:
                            p8_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p9_des_list:
                            p9_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p10_des_list:
                            extra_score_list = [home_score, away_score]
                            # 棒球全场包括加时赛
                            full_score_list[0] += home_score
                            full_score_list[1] += away_score
                    elif sport_id == small_sport_id_dic["排球"]:
                        if period_data["periodDescription"] in p4_des_list:
                            p4_score = [home_score, away_score]
                        elif period_data["periodDescription"] in p5_des_list:
                            p5_score = [home_score, away_score]
            if not (half_score_flag_1st or half_score_flag_2nd):
                full_score_list = ""
            half_score_list_1st = "" if not half_score_flag_1st else half_score_list_1st
            half_score_list_2nd = "" if not half_score_flag_2nd else half_score_list_2nd

        if "periodStatisticsMap" in match_data:
            corner_number_list = [0, 0]
            card_number_list = [0, 0]
            # print(f"bb : {half_corner_number_list_2nd}")
            for index, name in enumerate(["1st half", "2nd half"]):
                # 有periodStatisticsMap字段
                if name in match_data["periodStatisticsMap"]:
                    if name == "1st half":
                        half_corner_number_list_1st = [0, 0]
                        half_card_score_list_1st = [0, 0]
                    else:
                        half_corner_number_list_2nd = [0, 0]
                        half_card_score_list_2nd = [0, 0]
                    # 计算角球
                    for corner_data in match_data["periodStatisticsMap"][name]:
                        if corner_data["homeAway"] == "Home":
                            corner_number_list[0] += corner_data["corner"] if "corner" in corner_data else 0
                            if name == "1st half":
                                half_corner_number_list_1st[0] += corner_data[
                                    "corner"] if "corner" in corner_data else 0
                            if name == "2nd half":
                                half_corner_number_list_2nd[0] += corner_data[
                                    "corner"] if "corner" in corner_data else 0
                        else:
                            corner_number_list[1] += corner_data["corner"] if "corner" in corner_data else 0
                            if name == "1st half":
                                half_corner_number_list_1st[1] += corner_data[
                                    "corner"] if "corner" in corner_data else 0
                            if name == "2nd half":
                                half_corner_number_list_2nd[1] += corner_data[
                                    "corner"] if "corner" in corner_data else 0
                    # 计算罚牌
                    for index2, color in enumerate(["yellow", "red", "yellowRed"]):
                        for card_data in match_data["periodStatisticsMap"][name]:
                            # 若有该颜色，则相应的增加罚牌数
                            if color in card_data:
                                if index2 == 0:
                                    if card_data["homeAway"] == "Home":
                                        card_number_list[0] += card_data[color]
                                        if name == "1st half":
                                            half_card_score_list_1st[0] += card_data[color]
                                        if name == "2nd half":
                                            half_card_score_list_2nd[0] += card_data[color]
                                    else:
                                        card_number_list[1] += card_data[color]
                                        if name == "1st half":
                                            half_card_score_list_1st[1] += card_data[color]
                                        if name == "2nd half":
                                            half_card_score_list_2nd[1] += card_data[color]
                                else:
                                    if card_data["homeAway"] == "Home":
                                        card_number_list[0] += card_data[color] * 2
                                        if name == "1st half":
                                            half_card_score_list_1st[0] += card_data[color] * 2
                                        if name == "2nd half":
                                            half_card_score_list_2nd[0] += card_data[color] * 2
                                    else:
                                        card_number_list[1] += card_data[color] * 2
                                        if name == "1st half":
                                            half_card_score_list_1st[1] += card_data[color] * 2
                                        if name == "2nd half":
                                            half_card_score_list_2nd[1] += card_data[color] * 2
        # print(f"cc : {half_corner_number_list_2nd}")

        key_list = list(period_score.keys())
        key_list.sort()

        # if match_status == "比赛中止":
        if sport_id == small_sport_id_dic["足球"]:
            if half_score_list_2nd == "" or half_score_list_1st == "":
                full_score_list = ""
            if half_corner_number_list_2nd == "" or half_corner_number_list_1st == "":
                corner_number_list = ""
            if half_card_score_list_2nd == "" or half_card_score_list_1st == "":
                card_number_list = ""
        elif sport_id == small_sport_id_dic["篮球"]:
            if p2_score == "":
                half_score_list_1st = ""
            if p4_score == "":
                half_score_list_2nd = ""
                full_score_list = ""

        score_data = []
        if sport_id == small_sport_id_dic["足球"]:
            score_data = [half_score_list_1st, half_score_list_2nd, full_score_list, half_corner_number_list_1st,
                          half_corner_number_list_2nd, corner_number_list, half_card_score_list_1st,
                          half_card_score_list_2nd, card_number_list, extra_score_list, penalty_score]
        elif sport_id == small_sport_id_dic["篮球"]:
            score_data = [p1_score, p2_score, p3_score, p4_score, half_score_list_1st, half_score_list_2nd,
                          extra_score_list, full_score_list]
        elif sport_id == small_sport_id_dic["乒乓球"]:
            score_data = [p1_score, p2_score, p3_score, p4_score, p5_score, p6_score, p7_score, full_score_list,
                          set_score_list]
        elif sport_id == small_sport_id_dic["网球"]:
            score_data = [p1_score, p2_score, p3_score, p4_score, p5_score, full_score_list, set_score_list]
        elif sport_id == small_sport_id_dic["羽毛球"]:
            score_data = [p1_score, p2_score, p3_score, full_score_list, set_score_list]
        elif sport_id == small_sport_id_dic["排球"]:
            score_data = [p1_score, p2_score, p3_score, p4_score, p5_score, full_score_list, set_score_list]
        elif sport_id == small_sport_id_dic["冰上曲棍球"]:
            score_data = [p1_score, p2_score, p3_score, extra_score_list, full_score_list]
        elif sport_id == small_sport_id_dic["棒球"]:
            score_data = [p1_score, p2_score, p3_score, p4_score, p5_score, p6_score, p7_score, p8_score,
                          p9_score, first_five, extra_score_list, full_score_list]
        if source_type == 'h5':
            score_data = list(filter(lambda x: x, score_data))
            return [match_id, match_date, tournament_name, home_team_name, away_team_name, score_data]
        else:
            return [match_id, match_date, tournament_name, home_team_name, away_team_name, match_status, score_data]

    def get_order_result_score(self, match_id, market_id, specifier_id):
        """
        获取注单中的赛果比分
        :param match_id:
        :param market_id:
        :param specifier_id:
        """
        # 全场、半场
        full_score_market_list = [1, 2, 3, 10, 11, 12, 13, 15, 16, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29, 31, 32,
                                  33, 34, 35, 36, 37, 45, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 186, 188,
                                  199, 219, 223, 225, 227, 228, 229, 251, 256, 258, 314, 546, 547]
        half_score_market_list = [47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 63, 64, 66, 68, 69, 70, 71,
                                  74, 75, 76, 77, 78, 79, 81, 81, 542]
        # 角球
        corner_score_market_list = [165, 166, 169, 170, 171, 172]
        half_corner_score_market_list = [176, 177, 180, 181, 182, 183]
        # 总得分
        all_score_market_list = [187, 189, 190, 191, 237, 238, 406, 410]
        # 点球
        penalty_score_market_list = [123, 127]
        # 加时
        over_time_score_market_list = [2, 3, 113, 116, 117, 119, 120, 406, 410]
        # 阶段比分
        period_score_market_list = [104, 202, 203, 204, 236, 245, 246, 247, 248, 303, 304, 756, 757]
        # 罚牌
        card_market_list = [139, 142, 143, 144]
        half_card_market_list = [152, 155, 156, 157]

        nr_period_score = None
        over_time_score = ""
        period_score_dic = {}
        period_score = {}
        all_score = ""
        full_score = ""
        half_score = ""
        penalty_score = ""
        # 罚牌数，角球数
        card_number_list = [0, 0]
        corner_number_list = [0, 0]
        half_corner_number_list = [0, 0]
        half_card_score_list = [0, 0]

        rtn = self.get_match_score_msql_new(match_id)
        if len(rtn) == 0:
            return []
        match_score = rtn[0]
        sport_id = match_score["tournamentSportId"]
        if "periodScores" in match_score:
            period_data = match_score["periodScores"]
            for period in period_data:
                period_score.update({str(period["number"]): {"zh": period['periodDescription'],
                                                             "home": period['homeScore'],
                                                             "away": period['awayScore']}})
            home_all_score = away_all_score = 0
            for value in match_score['periodScores']:
                home_all_score += int(value["homeScore"])
                away_all_score += int(value["awayScore"])
            all_score = f"{home_all_score} - {away_all_score}"

            full_score_list = [0, 0]
            half_score_list = [0, 0]
            # 遍历每一条period score
            for period_data in match_score['periodScores']:
                # 如果是足球篮球，区分上下半场，全场不包括加时赛
                if sport_id == small_sport_id_dic["足球"]:
                    if period_data["number"] == 1:
                        half_score_list = [period_data["homeScore"], period_data["awayScore"]]
                    if period_data["number"] in (1, 2):
                        full_score_list[0] += int(period_data["homeScore"])
                        full_score_list[1] += int(period_data["awayScore"])
                # 篮球分上下半场，全场包括加时赛
                elif sport_id == small_sport_id_dic["篮球"]:
                    if period_data["number"] in (1, 2):
                        half_score_list[0] += int(period_data["homeScore"])
                        half_score_list[1] += int(period_data["awayScore"])
                    full_score_list[0] += int(period_data["homeScore"])
                    full_score_list[1] += int(period_data["awayScore"])
                # 冰棍球全场不包括加时
                elif sport_id == small_sport_id_dic["冰上曲棍球"]:
                    if ("加时" not in period_data['periodDescription']) and ("点球" not in
                                                                           period_data['periodDescription']):
                        full_score_list[0] += int(period_data["homeScore"])
                        full_score_list[1] += int(period_data["awayScore"])
                elif sport_id in [small_sport_id_dic["羽毛球"], small_sport_id_dic["乒乓球"],
                                  small_sport_id_dic["网球"], small_sport_id_dic["排球"]]:
                    if int(period_data["homeScore"]) > int(period_data["awayScore"]):
                        full_score_list[0] += 1
                    elif int(period_data["homeScore"]) < int(period_data["awayScore"]):
                        full_score_list[1] += 1
                # 棒球全场包括加时赛
                # elif sport_id == small_sport_id_dic["棒球"]:
                else:
                    full_score_list[0] += int(period_data["homeScore"])
                    full_score_list[1] += int(period_data["awayScore"])

            half_score = f'{half_score_list[0]} - {half_score_list[1]}'
            full_score = f'{full_score_list[0]} - {full_score_list[1]}'
            for score in match_score["periodScores"]:
                if score["periodDescription"] == "点球":
                    penalty_score = f"{score['homeScore']} - {score['awayScore']}"

        if "periodStatisticsMap" in match_score:
            for index, name in enumerate(["1st half", "2nd half"]):
                # 有periodStatisticsMap字段
                if name in match_score["periodStatisticsMap"]:
                    # 计算角球
                    for corner_data in match_score["periodStatisticsMap"][name]:
                        if corner_data["homeAway"] == "Home":
                            corner_number_list[0] += corner_data["corner"] if "corner" in corner_data else 0
                            if name == "1st half":
                                half_corner_number_list[0] += corner_data["corner"] if "corner" in corner_data else 0
                        else:
                            corner_number_list[1] += corner_data["corner"] if "corner" in corner_data else 0
                            if name == "1st half":
                                half_corner_number_list[1] += corner_data["corner"] if "corner" in corner_data else 0
                    # 计算罚牌
                    for index2, color in enumerate(["yellow", "red", "yellowRed"]):
                        for card_data in match_score["periodStatisticsMap"][name]:
                            # 若有该颜色，则相应的增加罚牌数
                            if color in card_data:
                                if index2 == 0:
                                    if card_data["homeAway"] == "Home":
                                        card_number_list[0] += card_data[color]
                                        if name == "1st half":
                                            half_card_score_list[0] += card_data[color]
                                    else:
                                        card_number_list[1] += card_data[color]
                                        if name == "1st half":
                                            half_card_score_list[1] += card_data[color]
                                else:
                                    if card_data["homeAway"] == "Home":
                                        card_number_list[0] += card_data[color] * 2
                                        if name == "1st half":
                                            half_card_score_list[0] += card_data[color] * 2
                                    else:
                                        card_number_list[1] += card_data[color] * 2
                                        if name == "1st half":
                                            half_card_score_list[1] += card_data[color] * 2
        card_score = f"{card_number_list[0]} - {card_number_list[1]}"
        corner_score = f"{corner_number_list[0]} - {corner_number_list[1]}"
        half_card_score = f"{half_card_score_list[0]} - {half_card_score_list[1]}"
        half_corner_score = f"{half_corner_number_list[0]} - {half_corner_number_list[1]}"

        key_list = list(period_score.keys())
        key_list.sort()
        for key in key_list:
            if "加时" in period_score[key]["zh"]:
                over_time_score = f'{period_score[key]["home"]} - {period_score[key]["away"]}'
            else:
                period_score_dic[key] = f'{period_score[key]["home"]} - {period_score[key]["away"]}'
        reg_result = re.search(r"nr=([\d.]+)", specifier_id)

        if reg_result and period_score_dic and (int(market_id) in period_score_market_list):
            nr = str(reg_result.group(1))
            nr_period_score = period_score_dic[nr]
        # 比分
        score_list = []
        if int(market_id) in full_score_market_list and full_score:
            score_list.append(full_score)
        if int(market_id) in half_score_market_list and half_score:
            score_list.append(half_score)
        if int(market_id) in corner_score_market_list and corner_score:
            score_list.append(corner_score)
        if int(market_id) in penalty_score_market_list and penalty_score:
            score_list.append(penalty_score)
        if int(market_id) in all_score_market_list and all_score:
            score_list.append(all_score)
        if int(market_id) in over_time_score_market_list and over_time_score:
            score_list.append(over_time_score)
        if int(market_id) in period_score_market_list and nr_period_score:
            score_list.append(nr_period_score)
        if int(market_id) in card_market_list and card_score:
            score_list.append(card_score)
        if int(market_id) in half_corner_score_market_list and half_corner_score:
            score_list.append(half_corner_score)
        if int(market_id) in half_card_market_list and half_card_score:
            score_list.append(half_card_score)
        return score_list


if __name__ == "__main__":
    db = DbQuery(['app', '123456', '192.168.10.120', '27017'])
    print(db.get_order_result_score("sr:match:24834044", "181", "sr:match:24834044_181__736"))
