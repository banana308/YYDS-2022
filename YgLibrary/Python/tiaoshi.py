



# yyts_tuple=(('d0d1/d10', '1531517033355976705', '公司总计', 'CNY', "Decimal('-0.10')", "Decimal('-928.21')", "Decimal('-928.11')", "Decimal('-0.10')", "Decimal('-928.21')", "Decimal('-928.11')", "Decimal('-0.09')", "Decimal('-928.20')", "Decimal('-928.11')", "Decimal('0.20')", "Decimal('-927.91')", "Decimal('-928.11')", '1', '一级代理', "Decimal('0.27')", "Decimal('4640.91')", "Decimal('4640.64')", '杜鑫登1', 70, '1531516017847869442', "Decimal('5800.00')", '总佣金', "Decimal('4121.69')"),)
#
# for i in yyts_tuple[0]:
#     if i=='公司总计':
#         bbt=('已替换公司总计',)
#         yyts_tuple=yyts_tuple[0][0:2]+bbt+yyts_tuple[0][3:]
#     elif i =='总佣金':
#         bbt =('已替换总佣金',)
#         yyts_tuple = yyts_tuple[0:25]+bbt+(yyts_tuple[-1],)
# print(yyts_tuple)



# name=['account', 'betAmount', 'betIp', 'betIpAddress', 'betResult', 'betTimeStr', 'betType', 'level0Commission', 'level0CommissionRatio', 'level0Percentage', 'level0Total', 'level0WinOrLose', 'level1Commission', 'level1CommissionRatio', 'level1Percentage', 'level1Total', 'level1WinOrLose', 'level2Commission', 'level2CommissionRatio', 'level2Percentage', 'level2Total', 'level2WinOrLose', 'level3Commission', 'level3CommissionRatio', 'level3Percentage', 'level3Total', 'level3WinOrLose', 'memberCommission', 'memberCommissionRatio', 'memberTotal', 'memberWinOrLose', 'name', 'options', 'orderNo', 'settlementTimeStr', 'sportId', 'sportType', 'validAmount', 'winOrLose', ' total_level0Commission', ' total_level0Total', ' total_level0WinOrLose', ' total_level1Commission', ' total_level1Total', ' total_level1WinOrLose', ' total_level2Commission', ' total_level2Total', ' total_level2WinOrLose', ' total_level3Commission', ' total_level3Total', ' total_level3WinOrLose', ' total_memberCommission', ' total_memberTotal', ' total_memberWinOrLose', ' total_validAmount', ' total_winOrLose']
# name_value=('d0d1d2d30c/fceshi02', "Decimal('150.00')", '192.168.10.120', '局域网', '赢', "datetime.datetime(2022, 6, 15, 2, 26, 54)", 3, "Decimal('0.00')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('-62.85')", "Decimal('-62.85')", "Decimal('0.00')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('-62.85')", "Decimal('-62.85')", "Decimal('0.00')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('-62.85')", "Decimal('-62.85')", "Decimal('0.00')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('-62.85')", "Decimal('-62.85')", "Decimal('0.00')", "Decimal('0.0000')", "Decimal('314.27')", "Decimal('314.27')", '杜鑫test账号ac', 'options', 'XFB75iQbakKD', "datetime.datetime(2022, 6, 15, 2, 38, 22)", 'sr:sport:1', '足球', "Decimal('150.00')", "Decimal('314.27')", "Decimal('190.00')", "Decimal('0.00')", "Decimal('-54.85')", "Decimal('-54.85')", "Decimal('0.00')", "Decimal('-54.85')", "Decimal('-54.85')", "Decimal('0.00')", "Decimal('-54.85')", "Decimal('-54.85')", "Decimal('0.00')", "Decimal('-54.85')", "Decimal('-54.85')", "Decimal('0.00')", "Decimal('274.27')", "Decimal('274.27')", "Decimal('190.00')", "Decimal('274.27')")
# name_dict={}
#
# print(len(name),len(name_value))
# for i in range(0,len(name)):
#     name_dict[name[i]]=name_value[i]
# print(name_dict)



# str_list=['46465456465644564']
#
# z_m_num01=["0","1","2","3","4","5","6","7","8","9"]
# vv_id=[]
# for i in str_list:
#     i=list(i)
#     for j in i:
#         if j in z_m_num01:
#             pass
#         else:
#             vv_id.append(0)
#             print("这是一个代理账号")

# agent_id="75674567674"
# agent_id_list=['agent_id']
# if agent_id_list[0]=='agent_id':
#     yyy="asdasda"+agent_id
#     print(yyy)

# sum02=(("Decimal('0.00')", '澳大利亚全国超级联赛,南澳大利亚', '足球'),)
# tournamentId= sum02[0][1]
# username = sum02[0][2]
# # sum02 = float(sum02[0][0])
#
#
# vv_id = []
# agent_id=5
# if vv_id== []:
#     agent_id = agent_id
#     print(agent_id)


# def www(agent_id,member_id,sportId,marketId,tournamentId,matchId):
#     total_tuple=(agent_id,member_id,sportId,marketId,tournamentId,matchId)
#     print(total_tuple)
#     print("它来呢：",matchId)
#     xxx_list=['agent_id','member_id','sportId','marketId','tournamentId','matchId']
#     total_list=[]
#     for jj in  total_tuple:
#         if jj=='' or jj=="":
#             print(jj)
#             pass
#         else:
#             total_list.append(xxx_list[total_tuple.index(jj)])
#             print(total_list)
#
# www(agent_id='',member_id='',sportId='',marketId='',tournamentId='',matchId='sr:match:33725427')

# sportId_sql_list=[]
# sport_num_sql_list=[]
# sort_num=[(('1531516017847869442', '0'),), (('1531517033355976705', '1'),), (('1531517351158390786', '2'),), (('1531517760300163074', '3'),)]
#
# for sportId in sort_num:
#     sportId_sql_list.append(sportId[0][0])
#     sport_num_sql_list.append(sportId[0][1])
# print(sportId_sql_list)
# print(sport_num_sql_list)
#
#
#
# del sportId_sql_list[0:2]
# print(sportId_sql_list)





# yyrt_list=[]
# ppt=(('d0d1d2d30v/fceshi021', "Decimal('10.00')", '192.168.10.120', '局域网', '未结算', 2, "datetime.datetime(2022, 6, 15, 2, 35, 57)", "Decimal('0.20')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('0.0000')", "Decimal('0.20')", "Decimal('0.0000')", '杜鑫test账号av', 'options', 'XFBaaCfa4EEt', '足球'),)
# yyd=(("Decimal('20.00')",),)
#
# yyrt_list.append(ppt[0])
# print(yyrt_list)
# ggg = yyrt_list[0] + yyd[0]
#
# print(type(yyrt_list[0]))
# print(type(yyd[0]))
import math

# orderNo_list=[{'awayTeamName': 'KPV科科拉'}]

yyds_list = [{'awayTeamName': 'KPV科科拉', 'betScore': None, 'homeTeamName': '图尔库', 'marketName': '上半场 - KPV科科拉 大/小',
              'matchTime': '2022-06-18 08:00:00', 'matchType': '早盘', 'odds': 1.8, 'oddsType': '2',
              'orderNo': 'XFBaaCfa4EEt', 'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '芬兰甲级联赛'},
             {'awayTeamName': '里本泰德', 'betScore': None, 'homeTeamName': 'CA Paranaense PR', 'marketName': '双重机会',
              'matchTime': '2022-06-28 20:30:00', 'matchType': '早盘', 'odds': 2.04, 'oddsType': '1',
              'orderNo': 'XFBaaCfa4EEt', 'outcomeName': '和局或 里本泰德', 'specifier': '', 'tournamentName': '国际俱乐部解放者杯'},
             {'awayTeamName': '卢旺达爱国军', 'betScore': None, 'homeTeamName': '警察(卢旺达)', 'marketName': '卢旺达爱国军 胜利退款',
              'matchTime': '2022-06-16 09:00:00', 'matchType': '早盘', 'odds': 3.0, 'oddsType': '1',
              'orderNo': 'XFBaaCfa4EEt', 'outcomeName': '警察(卢旺达)', 'specifier': '', 'tournamentName': '卢旺达国家足球联赛'},
             {'awayTeamName': 'Future FC', 'betScore': None, 'homeTeamName': 'Enppi Club', 'marketName': '总入球',
              'matchTime': '2022-06-18 13:00:00', 'matchType': '早盘', 'odds': 1.97, 'oddsType': '1',
              'orderNo': 'XFBaaCfa4EEt', 'outcomeName': '2-3', 'specifier': 'variant=sr:goal_range:7+',
              'tournamentName': '埃及足球甲级联赛'},
             {'awayTeamName': '罗沙里奧中央', 'betScore': None, 'homeTeamName': '沙士菲', 'marketName': '上半场 - 两队都进球',
              'matchTime': '2022-06-20 18:00:00', 'matchType': '早盘', 'odds': 4.55, 'oddsType': '1',
              'orderNo': 'XFMvmSzEyMM9', 'outcomeName': '是', 'specifier': '', 'tournamentName': '阿根廷足球甲级联赛'},
             {'awayTeamName': '水原三星', 'betScore': None, 'homeTeamName': 'Jeonbuk Hyundai Motors',
              'marketName': '独赢 & 大/小', 'matchTime': '2022-06-22 06:00:00', 'matchType': '早盘', 'odds': 3.95,
              'oddsType': '1', 'orderNo': 'XFMvmSzEyMM9', 'outcomeName': '全北现代 & 小 2.5', 'specifier': 'total=2.5',
              'tournamentName': '韩国K1联赛'},
             {'awayTeamName': '卡皮拉', 'betScore': None, 'homeTeamName': '努尔米耶尔维', 'marketName': '上半场 - 大/小',
              'matchTime': '2022-06-18 11:00:00', 'matchType': '早盘', 'odds': 2.31, 'oddsType': '1',
              'orderNo': 'XFMvmSzEyMM9', 'outcomeName': '大1.5', 'specifier': 'total=1.5',
              'tournamentName': '芬兰乙级联赛，A组'},
             {'awayTeamName': '绿色古利', 'betScore': None, 'homeTeamName': '南墨尔本', 'marketName': '南墨尔本 胜利退款',
              'matchTime': '2022-06-24 05:30:00', 'matchType': '早盘', 'odds': 1.66, 'oddsType': '1',
              'orderNo': 'XFMvM9hrnt25', 'outcomeName': '和局', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛,维多利亚'},
             {'awayTeamName': 'Nomme Kalju FC', 'betScore': None, 'homeTeamName': '塔林弗罗拉',
              'marketName': '上半场 - Nomme Kalju FC 不失球', 'matchTime': '2022-06-19 10:15:00', 'matchType': '早盘',
              'odds': 1.54, 'oddsType': '1', 'orderNo': 'XFMvM9hrnt25', 'outcomeName': '不是', 'specifier': '',
              'tournamentName': '爱沙尼亚足球甲级联赛'},
             {'awayTeamName': '艾尔古纳', 'betScore': None, 'homeTeamName': '马斯里足球俱乐部', 'marketName': '马斯里足球俱乐部 大/小',
              'matchTime': '2022-06-18 13:00:00', 'matchType': '早盘', 'odds': 2.19, 'oddsType': '1',
              'orderNo': 'XFMvM9hrnt25', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '埃及足球甲级联赛'},
             {'awayTeamName': 'Orgryte IS', 'betScore': None, 'homeTeamName': 'Jonkopings Sodra IF',
              'marketName': 'Jonkopings Sodra IF 最高进球数半场', 'matchTime': '2022-06-28 13:00:00', 'matchType': '早盘',
              'odds': 3.45, 'oddsType': '1', 'orderNo': 'XFMvQKQsUhG5', 'outcomeName': '上半场', 'specifier': '',
              'tournamentName': '瑞典超甲级联赛'}, {'awayTeamName': 'Atlas FC', 'betScore': None, 'homeTeamName': 'CF America',
                                             'marketName': 'Atlas FC 不失球获胜', 'matchTime': '2022-07-02 22:05:00',
                                             'matchType': '早盘', 'odds': 4.95, 'oddsType': '1',
                                             'orderNo': 'XFMvQKQsUhG5', 'outcomeName': '是', 'specifier': '',
                                             'tournamentName': '墨西哥甲级联赛，春季赛'},
             {'awayTeamName': '北桥公牛', 'betScore': None, 'homeTeamName': '黑镇市', 'marketName': '黑镇市 单/双',
              'matchTime': '2022-06-26 01:00:00', 'matchType': '早盘', 'odds': 1.81, 'oddsType': '1',
              'orderNo': 'XFMvQKQsUhG5', 'outcomeName': '双', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛,新南威尔士'},
             {'awayTeamName': '抵抗FC', 'betScore': None, 'homeTeamName': '奥林匹亚会', 'marketName': '上半场 - 波胆',
              'matchTime': '2022-06-19 16:30:00', 'matchType': '早盘', 'odds': 3.65, 'oddsType': '1',
              'orderNo': 'XFMvQKQsUhG5', 'outcomeName': '1:0', 'specifier': '', 'tournamentName': '巴拉圭甲级联赛，春季赛'},
             {'awayTeamName': 'Oita Trinita', 'betScore': None, 'homeTeamName': '栃木SC', 'marketName': '栃木SC 单/双',
              'matchTime': '2022-06-18 05:00:00', 'matchType': '早盘', 'odds': 2.23, 'oddsType': '1',
              'orderNo': 'XFMvVpuzS566', 'outcomeName': '单', 'specifier': '', 'tournamentName': '日本乙级联赛'},
             {'awayTeamName': '申察勒斯联合', 'betScore': None, 'homeTeamName': '瓜勒瓜伊楚', 'marketName': '让球',
              'matchTime': '2022-06-17 14:45:00', 'matchType': '早盘', 'odds': 1.95, 'oddsType': '1',
              'orderNo': 'XFMvVpuzS566', 'outcomeName': '瓜勒瓜伊楚 ', 'specifier': 'hcp=0.5',
              'tournamentName': '阿根廷全国足球甲级联赛'},
             {'awayTeamName': '柔佛', 'betScore': None, 'homeTeamName': '吉打', 'marketName': '上半场 - 双重机会',
              'matchTime': '2022-06-19 09:00:00', 'matchType': '早盘', 'odds': 1.21, 'oddsType': '1',
              'orderNo': 'XFMvVpuzS566', 'outcomeName': '和局或 柔佛', 'specifier': '', 'tournamentName': '马来西亚超级联赛'},
             {'awayTeamName': 'Newcastle Olympic FC', 'betScore': None, 'homeTeamName': 'Lake Macquarie FC',
              'marketName': 'Lake Macquarie FC 胜利退款', 'matchTime': '2022-06-26 00:00:00', 'matchType': '早盘',
              'odds': 4.15, 'oddsType': '1', 'orderNo': 'XFMvVpuzS566', 'outcomeName': '和局', 'specifier': '',
              'tournamentName': '澳大利亚全国超级联赛,新南威尔士州北部'},
             {'awayTeamName': '城南足球俱乐部', 'betScore': None, 'homeTeamName': '金泉尚武足球俱乐部',
              'marketName': '上半场 - 城南足球俱乐部 不失球', 'matchTime': '2022-06-21 06:00:00', 'matchType': '早盘', 'odds': 1.76,
              'oddsType': '1', 'orderNo': 'XFMvVpuzS566', 'outcomeName': '是', 'specifier': '',
              'tournamentName': '韩国K1联赛'},
             {'awayTeamName': '伊朗', 'betScore': None, 'homeTeamName': '英格兰', 'marketName': '上半场 - 大/小',
              'matchTime': '2022-11-21 09:00:00', 'matchType': '早盘', 'odds': 1.53, 'oddsType': '1',
              'orderNo': 'XFMw3aGzr68w', 'outcomeName': '大0.5/1', 'specifier': 'total=0.75', 'tournamentName': '国际世界杯'},
             {'awayTeamName': 'Tegevajaro Miyazaki', 'betScore': None, 'homeTeamName': '鸟取飞翔', 'marketName': '鸟取飞翔 大/小',
              'matchTime': '2022-06-19 00:00:00', 'matchType': '早盘', 'odds': 2.45, 'oddsType': '1',
              'orderNo': 'XFMw3aGzr68w', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '日本丙级联赛'},
             {'awayTeamName': '格林诺奇骑士', 'betScore': None, 'homeTeamName': '南霍巴特', 'marketName': '大/小',
              'matchTime': '2022-06-18 00:00:00', 'matchType': '早盘', 'odds': 1.52, 'oddsType': '1',
              'orderNo': 'XFMw3aGzr68w', 'outcomeName': '大2.5/3', 'specifier': 'total=2.75',
              'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚'},
             {'awayTeamName': 'HIFK赫尔辛基', 'betScore': None, 'homeTeamName': 'Tampereen Ilves', 'marketName': '两队都进球',
              'matchTime': '2022-06-22 11:00:00', 'matchType': '早盘', 'odds': 1.71, 'oddsType': '1',
              'orderNo': 'XFMw3aGzr68w', 'outcomeName': '是', 'specifier': '', 'tournamentName': '芬兰超级联赛'},
             {'awayTeamName': '格但斯克 莱吉亚', 'betScore': None, 'homeTeamName': 'Wisla Plock', 'marketName': '双重机会',
              'matchTime': '2022-07-17 09:00:00', 'matchType': '早盘', 'odds': 1.49, 'oddsType': '1',
              'orderNo': 'XFMw3aGzr68w', 'outcomeName': '和局或 格但斯克 莱吉亚', 'specifier': '', 'tournamentName': '波兰甲级联赛'},
             {'awayTeamName': '费恩夏普', 'betScore': None, 'homeTeamName': '斯莱戈流浪', 'marketName': '上半场 - 单/双',
              'matchTime': '2022-06-18 14:45:00', 'matchType': '早盘', 'odds': 1.62, 'oddsType': '1',
              'orderNo': 'XFMw3aGzr68w', 'outcomeName': '双', 'specifier': '', 'tournamentName': '爱尔兰足球超级联赛'},
             {'awayTeamName': '砂劳越', 'betScore': None, 'homeTeamName': '雪兰莪', 'marketName': '波胆',
              'matchTime': '2022-06-19 09:00:00', 'matchType': '早盘', 'odds': 25.95, 'oddsType': '1',
              'orderNo': 'XFMwaige8Gdh', 'outcomeName': '4:0', 'specifier': '', 'tournamentName': '马来西亚超级联赛'},
             {'awayTeamName': '布法罗', 'betScore': None, 'homeTeamName': '克利夫兰', 'marketName': '大/小',
              'matchTime': '2022-06-17 19:00:00', 'matchType': '早盘', 'odds': 2.26, 'oddsType': '1',
              'orderNo': 'XFMwaige8Gdh', 'outcomeName': '大4.5', 'specifier': 'total=4.5',
              'tournamentName': '美国足球全国超级联赛'},
             {'awayTeamName': '格罗德诺涅曼', 'betScore': None, 'homeTeamName': 'FC特兰斯迈', 'marketName': '格罗德诺涅曼 单/双',
              'matchTime': '2022-06-18 08:30:00', 'matchType': '早盘', 'odds': 1.84, 'oddsType': '1',
              'orderNo': 'XFMwaige8Gdh', 'outcomeName': '单', 'specifier': '', 'tournamentName': '白俄罗斯足球超级联赛'},
             {'awayTeamName': 'FC Cincinnati', 'betScore': None, 'homeTeamName': 'Philadelphia Union',
              'marketName': '上半场 - 角球让球', 'matchTime': '2022-06-18 19:30:00', 'matchType': '早盘', 'odds': 1.31,
              'oddsType': '1', 'orderNo': 'XFMwaige8Gdh', 'outcomeName': '费城联 ', 'specifier': 'hcp=0.5',
              'tournamentName': '美国职业足球大联盟'},
             {'awayTeamName': 'Broadmeadow Magic FC', 'betScore': None, 'homeTeamName': 'Cooks Hill United',
              'marketName': 'Cooks Hill United 单/双', 'matchTime': '2022-06-18 00:30:00', 'matchType': '早盘', 'odds': 2.0,
              'oddsType': '1', 'orderNo': 'XFMwaige8Gdh', 'outcomeName': '单', 'specifier': '',
              'tournamentName': '澳大利亚全国超级联赛,新南威尔士州北部'},
             {'awayTeamName': '墨尔本骑士', 'betScore': None, 'homeTeamName': '海德堡联', 'marketName': '大/小',
              'matchTime': '2022-06-19 01:00:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1',
              'orderNo': 'XFMwaige8Gdh', 'outcomeName': '大2.5', 'specifier': 'total=2.5',
              'tournamentName': '澳大利亚全国超级联赛,维多利亚'},
             {'awayTeamName': 'Maitland FC', 'betScore': None, 'homeTeamName': 'Valentine FC',
              'marketName': 'Valentine FC 大/小', 'matchTime': '2022-06-26 00:00:00', 'matchType': '早盘', 'odds': 2.5,
              'oddsType': '1', 'orderNo': 'XFMwaige8Gdh', 'outcomeName': '大1.5', 'specifier': 'total=1.5',
              'tournamentName': '澳大利亚全国超级联赛,新南威尔士州北部'},
             {'awayTeamName': '阿德莱得城', 'betScore': None, 'homeTeamName': '阿德莱科梅兹', 'marketName': '让球',
              'matchTime': '2022-06-18 01:30:00', 'matchType': '早盘', 'odds': 2.11, 'oddsType': '1',
              'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '阿德莱科梅兹 ', 'specifier': 'hcp=0',
              'tournamentName': '澳大利亚全国超级联赛,南澳大利亚'},
             {'awayTeamName': 'Lillestrom SK', 'betScore': None, 'homeTeamName': 'Stroemsgodset IF',
              'marketName': '两个半场 小1.5', 'matchTime': '2022-06-26 12:00:00', 'matchType': '早盘', 'odds': 1.36,
              'oddsType': '1', 'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '不是', 'specifier': 'total=1.5',
              'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '阿东那', 'betScore': None, 'homeTeamName': '欧克莱卡诺', 'marketName': '阿东那 单/双',
              'matchTime': '2022-06-18 05:30:00', 'matchType': '早盘', 'odds': 1.63, 'oddsType': '1',
              'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '双', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛,维多利亚'},
             {'awayTeamName': '锡尔克堡', 'betScore': None, 'homeTeamName': '宁比', 'marketName': '上半场 - 宁比 大/小',
              'matchTime': '2022-07-17 08:00:00', 'matchType': '早盘', 'odds': 2.25, 'oddsType': '1',
              'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '丹麦超级联赛'},
             {'awayTeamName': 'Stabaek IF', 'betScore': None, 'homeTeamName': '斯达', 'marketName': 'Stabaek IF 单/双',
              'matchTime': '2022-06-19 09:00:00', 'matchType': '早盘', 'odds': 1.92, 'oddsType': '1',
              'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '单', 'specifier': '', 'tournamentName': '挪威甲级联赛'},
             {'awayTeamName': '瓦萨', 'betScore': None, 'homeTeamName': 'HIFK赫尔辛基', 'marketName': 'HIFK赫尔辛基 胜利退款',
              'matchTime': '2022-06-18 16:00:00', 'matchType': '早盘', 'odds': 1.54, 'oddsType': '1',
              'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '瓦萨', 'specifier': '', 'tournamentName': '芬兰超级联赛'},
             {'awayTeamName': '格林诺奇骑士', 'betScore': None, 'homeTeamName': '南霍巴特', 'marketName': '独赢 & 两队都进球',
              'matchTime': '2022-06-18 00:00:00', 'matchType': '早盘', 'odds': 5.75, 'oddsType': '1',
              'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '南霍巴特 & 不是', 'specifier': '',
              'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚'},
             {'awayTeamName': '阳光海岸流浪者', 'betScore': None, 'homeTeamName': '潘尼苏拉', 'marketName': '双重机会&两队都进球',
              'matchTime': '2022-06-25 02:00:00', 'matchType': '早盘', 'odds': 2.95, 'oddsType': '1',
              'orderNo': 'XFMwbsgh9GZp', 'outcomeName': '潘尼苏拉/和局 & 不是', 'specifier': '',
              'tournamentName': '澳大利亚全国超级联赛，昆士兰州'},
             {'awayTeamName': '艾尔古纳', 'betScore': None, 'homeTeamName': '马斯里足球俱乐部', 'marketName': '马斯里足球俱乐部 赢两个半场',
              'matchTime': '2022-06-18 13:00:00', 'matchType': '早盘', 'odds': 5.55, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '是', 'specifier': '', 'tournamentName': '埃及足球甲级联赛'},
             {'awayTeamName': '江原', 'betScore': None, 'homeTeamName': '仁川联队', 'marketName': '江原 赢任何半场',
              'matchTime': '2022-06-22 06:30:00', 'matchType': '早盘', 'odds': 1.49, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '韩国K1联赛'},
             {'awayTeamName': 'Maitland FC', 'betScore': None, 'homeTeamName': 'Adamstown Rosebud FC',
              'marketName': '独赢', 'matchTime': '2022-06-18 00:00:00', 'matchType': '早盘', 'odds': 15.95, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '亚当斯敦 玫瑰花蕾', 'specifier': '',
              'tournamentName': '澳大利亚全国超级联赛,新南威尔士州北部'},
             {'awayTeamName': 'Kristiansund BK', 'betScore': None, 'homeTeamName': '洛辛堡', 'marketName': '上半场 - 单/双',
              'matchTime': '2022-06-25 12:00:00', 'matchType': '早盘', 'odds': 1.98, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '单', 'specifier': '', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': 'Vissel Kobe', 'betScore': None, 'homeTeamName': 'Kashiwa Reysol',
              'marketName': 'Vissel Kobe 不失球获胜', 'matchTime': '2022-06-18 06:00:00', 'matchType': '早盘', 'odds': 1.13,
              'oddsType': '1', 'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '不是', 'specifier': '',
              'tournamentName': '日本J联赛'},
             {'awayTeamName': '竞赛会', 'betScore': None, 'homeTeamName': '甘拿斯亚', 'marketName': '最高进球数半场',
              'matchTime': '2022-06-20 18:00:00', 'matchType': '早盘', 'odds': 3.15, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '相同', 'specifier': '', 'tournamentName': '阿根廷足球甲级联赛'},
             {'awayTeamName': '珀斯光荣(青年)', 'betScore': None, 'homeTeamName': '弗罗瑞特', 'marketName': '珀斯光荣(青年) 进球数',
              'matchTime': '2022-06-25 03:00:00', 'matchType': '早盘', 'odds': 2.45, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '1', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '澳大利亚全国超级联赛,西澳大利亚'},
             {'awayTeamName': '堪培拉奥林匹克', 'betScore': None, 'homeTeamName': '西堪培拉流浪者', 'marketName': '独赢 & 大/小',
              'matchTime': '2022-06-18 00:15:00', 'matchType': '早盘', 'odds': 6.35, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '西堪培拉流浪者 & 大 3.5', 'specifier': 'total=3.5',
              'tournamentName': '澳大利亚全国超级联赛, 首都足球'},
             {'awayTeamName': 'Poland', 'betScore': None, 'homeTeamName': '墨西哥', 'marketName': '墨西哥 不失球',
              'matchTime': '2022-11-22 12:00:00', 'matchType': '早盘', 'odds': 1.35, 'oddsType': '1',
              'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '国际世界杯'},
             {'awayTeamName': '华沙莱吉亚', 'betScore': None, 'homeTeamName': 'Korona Kielce',
              'marketName': 'Korona Kielce 胜利退款', 'matchTime': '2022-07-16 14:30:00', 'matchType': '早盘', 'odds': 1.42,
              'oddsType': '1', 'orderNo': 'XFMwdJYS6pRL', 'outcomeName': '华沙莱吉亚', 'specifier': '',
              'tournamentName': '波兰甲级联赛'},
             {'awayTeamName': '莫尔德', 'betScore': None, 'homeTeamName': '汉坎', 'marketName': '上半场 - 两队都进球',
              'matchTime': '2022-07-03 12:00:00', 'matchType': '早盘', 'odds': 3.6, 'oddsType': '1',
              'orderNo': 'XH4tnppwcB5S', 'outcomeName': '是', 'specifier': '', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': 'RS派瑞加', 'betScore': None, 'homeTeamName': '塞阿腊竞技CE', 'marketName': '塞阿腊竞技CE 进球数',
              'matchTime': '2022-06-25 14:00:00', 'matchType': '早盘', 'odds': 18.95, 'oddsType': '1',
              'orderNo': 'XH4tnppwcB5S', 'outcomeName': '3+', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '巴西丙级联赛'},
             {'awayTeamName': '卡尔斯塔德足球发展', 'betScore': None, 'homeTeamName': '泰比', 'marketName': '独赢 & 大/小',
              'matchTime': '2022-06-26 10:00:00', 'matchType': '早盘', 'odds': 9.95, 'oddsType': '1',
              'orderNo': 'XH4tpwUvkur9', 'outcomeName': '泰比 & 大 3.5', 'specifier': 'total=3.5',
              'tournamentName': '瑞典足球乙级联赛-北部'},
             {'awayTeamName': '纽约欧洲青年足球会', 'betScore': None, 'homeTeamName': '威斯特彻斯特火焰', 'marketName': '纽约欧洲青年足球会 大/小',
              'matchTime': '2022-06-25 19:30:00', 'matchType': '早盘', 'odds': 1.58, 'oddsType': '1',
              'orderNo': 'XH4tpwUvkur9', 'outcomeName': '大1.5', 'specifier': 'total=1.5',
              'tournamentName': '美国美足联乙级联赛'},
             {'awayTeamName': '坡州市民足球俱乐部', 'betScore': None, 'homeTeamName': 'Pocheon Citizen FC',
              'marketName': '双重机会&两队都进球', 'matchTime': '2022-06-25 04:00:00', 'matchType': '早盘', 'odds': 2.85,
              'oddsType': '1', 'orderNo': 'XH4tpwUvkur9', 'outcomeName': 'Pocheon Citizen FC/和局 & 不是', 'specifier': '',
              'tournamentName': '韩国全国联赛'},
             {'awayTeamName': '艾斯潘诺拉', 'betScore': None, 'homeTeamName': 'CD Provincial Ovalle FC',
              'marketName': '独赢 & 大/小', 'matchTime': '2022-06-25 15:00:00', 'matchType': '早盘', 'odds': 8.95,
              'oddsType': '1', 'orderNo': 'XH4tqDHMbME8', 'outcomeName': 'CD Provincial Ovalle FC & 大 1.5',
              'specifier': 'total=1.5', 'tournamentName': '智利杯'},
             {'awayTeamName': 'SP卡皮瓦里亚诺', 'betScore': None, 'homeTeamName': 'EC Xv de Novembro Piracicaba SP U20',
              'marketName': '哪队进球', 'matchTime': '2022-06-25 09:00:00', 'matchType': '早盘', 'odds': 1.79,
              'oddsType': '1', 'orderNo': 'XH4tqDHMbME8', 'outcomeName': '两支队', 'specifier': '',
              'tournamentName': '巴西U20圣保罗州联赛'},
             {'awayTeamName': '罗斯郡', 'betScore': None, 'homeTeamName': '赫斯', 'marketName': '上半场 - 独赢',
              'matchTime': '2022-07-30 10:00:00', 'matchType': '早盘', 'odds': 2.18, 'oddsType': '1',
              'orderNo': 'XH4tqDHMbME8', 'outcomeName': '赫斯', 'specifier': '', 'tournamentName': '苏格兰足球超级联赛'},
             {'awayTeamName': '坡州市民足球俱乐部', 'betScore': None, 'homeTeamName': 'Pocheon Citizen FC',
              'marketName': 'Pocheon Citizen FC 不失球获胜', 'matchTime': '2022-06-25 04:00:00', 'matchType': '早盘',
              'odds': 1.21, 'oddsType': '1', 'orderNo': 'XH4trLAT6HrC', 'outcomeName': '不是', 'specifier': '',
              'tournamentName': '韩国全国联赛'},
             {'awayTeamName': '京波罗 狮子', 'betScore': None, 'homeTeamName': 'Olympia Warriors Hobart', 'marketName': '波胆',
              'matchTime': '2022-07-01 05:00:00', 'matchType': '早盘', 'odds': 29.95, 'oddsType': '1',
              'orderNo': 'XH4trLAT6HrC', 'outcomeName': '2:1', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚'},
             {'awayTeamName': '沙士菲', 'betScore': None, 'homeTeamName': '防卫者', 'marketName': '上半场 - 两队都进球',
              'matchTime': '2022-06-25 14:30:00', 'matchType': '早盘', 'odds': 4.65, 'oddsType': '1',
              'orderNo': 'XH4trLAT6HrC', 'outcomeName': '是', 'specifier': '', 'tournamentName': '阿根廷足球甲级联赛'},
             {'awayTeamName': 'FC Hegelmann Kaunas', 'betScore': None, 'homeTeamName': 'FK Riteriai',
              'marketName': '最高进球数半场', 'matchTime': '2022-06-25 12:00:00', 'matchType': '早盘', 'odds': 3.1,
              'oddsType': '1', 'orderNo': 'XH4tsTZhRY8Z', 'outcomeName': '相同', 'specifier': '',
              'tournamentName': '立陶宛甲级联赛'},
             {'awayTeamName': 'IK Brage', 'betScore': None, 'homeTeamName': 'Vasteras SK',
              'marketName': 'IK Brage 最高进球数半场', 'matchTime': '2022-07-03 07:00:00', 'matchType': '早盘', 'odds': 3.3,
              'oddsType': '1', 'orderNo': 'XH4tsTZhRY8Z', 'outcomeName': '上半场', 'specifier': '',
              'tournamentName': '瑞典超甲级联赛'},
             {'awayTeamName': '蒙特港', 'betScore': None, 'homeTeamName': '华奇巴托', 'marketName': '双重机会',
              'matchTime': '2022-06-26 17:30:00', 'matchType': '早盘', 'odds': 1.3, 'oddsType': '1',
              'orderNo': 'XH4tsTZhRY8Z', 'outcomeName': '华奇巴托 或 蒙特港', 'specifier': '', 'tournamentName': '智利杯'},
             {'awayTeamName': 'Vejle BK', 'betScore': None, 'homeTeamName': 'FC Helsingoer', 'marketName': '双重机会&大/小',
              'matchTime': '2022-07-22 11:00:00', 'matchType': '早盘', 'odds': 3.45, 'oddsType': '1',
              'orderNo': 'XH4tsTZhRY8Z', 'outcomeName': '赫尔辛格/和局 & 小 2.5', 'specifier': 'total=2.5',
              'tournamentName': '丹麦甲级联赛'},
             {'awayTeamName': '塞尔维亚', 'betScore': None, 'homeTeamName': '喀麦隆', 'marketName': '总入球',
              'matchTime': '2022-11-28 06:00:00', 'matchType': '早盘', 'odds': 2.0, 'oddsType': '1',
              'orderNo': 'XH4tui96bET3', 'outcomeName': '2-3', 'specifier': 'variant=sr:goal_range:7+',
              'tournamentName': '国际世界杯'},
             {'awayTeamName': '雷尼桑格迪', 'betScore': None, 'homeTeamName': '曼尼', 'marketName': '独赢 & 两队都进球',
              'matchTime': '2022-06-25 09:00:00', 'matchType': '早盘', 'odds': 4.25, 'oddsType': '1',
              'orderNo': 'XH4tui96bET3', 'outcomeName': '曼尼 & 不是', 'specifier': '', 'tournamentName': '冰岛女子足球乙级联赛'},
             {'awayTeamName': '美洲太阳', 'betScore': None, 'homeTeamName': '塔夸里足球俱乐部', 'marketName': '塔夸里足球俱乐部 胜利退款',
              'matchTime': '2022-06-27 19:15:00', 'matchType': '早盘', 'odds': 1.57, 'oddsType': '1',
              'orderNo': 'XH4tui96bET3', 'outcomeName': '美洲太阳', 'specifier': '', 'tournamentName': '巴拉圭甲级联赛，春季赛'},
             {'awayTeamName': 'Stabaek IF', 'betScore': None, 'homeTeamName': '莫庄达伦', 'marketName': '波胆',
              'matchTime': '2022-07-03 09:00:00', 'matchType': '早盘', 'odds': 24.95, 'oddsType': '1',
              'orderNo': 'XH4tui96bET3', 'outcomeName': '3:0', 'specifier': '', 'tournamentName': '挪威甲级联赛'},
             {'awayTeamName': '史查禾', 'betScore': None, 'homeTeamName': '摩丘内尔', 'marketName': '独赢 & 两队都进球',
              'matchTime': '2022-06-25 10:00:00', 'matchType': '早盘', 'odds': 2.36, 'oddsType': '1',
              'orderNo': 'XH4tvH6zePjG', 'outcomeName': '摩丘内尔 & 是', 'specifier': '', 'tournamentName': '挪威丙级联赛第6组'},
             {'awayTeamName': 'Houston Dynamo', 'betScore': None, 'homeTeamName': 'Portland Timbers',
              'marketName': '最高进球数半场', 'matchTime': '2022-06-29 22:30:00', 'matchType': '早盘', 'odds': 3.45,
              'oddsType': '1', 'orderNo': 'XH4tvH6zePjG', 'outcomeName': '相同', 'specifier': '',
              'tournamentName': '美国职业足球大联盟'},
             {'awayTeamName': '科斯塔德', 'betScore': None, 'homeTeamName': '斯泰恩雪儿', 'marketName': '净胜球数',
              'matchTime': '2022-06-25 08:00:00', 'matchType': '早盘', 'odds': 79.95, 'oddsType': '1',
              'orderNo': 'XH4tvH6zePjG', 'outcomeName': '斯泰恩雪儿 3+', 'specifier': 'variant=sr:winning_margin:3+',
              'tournamentName': '挪威丙级联赛第5组'},
             {'awayTeamName': '阿玛盖尔', 'betScore': None, 'homeTeamName': '桑德捷斯基', 'marketName': '上半场 - 双重机会',
              'matchTime': '2022-07-22 13:00:00', 'matchType': '早盘', 'odds': 1.85, 'oddsType': '1',
              'orderNo': 'XH4tvH6zePjG', 'outcomeName': '和局或 阿玛盖尔', 'specifier': '', 'tournamentName': '丹麦甲级联赛'},
             {'awayTeamName': 'Club Leon', 'betScore': None, 'homeTeamName': 'Atletico San Luis',
              'marketName': '上半场 - 平局退款', 'matchTime': '2022-07-03 18:00:00', 'matchType': '早盘', 'odds': 1.91,
              'oddsType': '1', 'orderNo': 'XH4twRCJJjzs', 'outcomeName': '利昂', 'specifier': '',
              'tournamentName': '墨西哥甲级联赛，春季赛'},
             {'awayTeamName': '雷海姆', 'betScore': None, 'homeTeamName': '孔斯温厄尔', 'marketName': '双重机会&大/小',
              'matchTime': '2022-07-04 12:00:00', 'matchType': '早盘', 'odds': 1.94, 'oddsType': '1',
              'orderNo': 'XH4twRCJJjzs', 'outcomeName': '孔斯温厄尔/和局 & 大 1.5', 'specifier': 'total=1.5',
              'tournamentName': '挪威甲级联赛'},
             {'awayTeamName': 'Ceramica Cleopatra', 'betScore': None, 'homeTeamName': 'Zamalek SC',
              'marketName': '上半场 - Ceramica Cleopatra 大/小', 'matchTime': '2022-06-28 15:30:00', 'matchType': '早盘',
              'odds': 2.75, 'oddsType': '1', 'orderNo': 'XH4twRCJJjzs', 'outcomeName': '大0.5', 'specifier': 'total=0.5',
              'tournamentName': '埃及足球甲级联赛'},
             {'awayTeamName': 'Sogndal IL', 'betScore': None, 'homeTeamName': 'KFUM奥斯陆', 'marketName': '双重机会',
              'matchTime': '2022-07-03 09:00:00', 'matchType': '早盘', 'odds': 1.36, 'oddsType': '1',
              'orderNo': 'XH4twRCJJjzs', 'outcomeName': 'KFUM奥斯陆 或 桑恩达', 'specifier': '', 'tournamentName': '挪威甲级联赛'},
             {'awayTeamName': 'Club Santos Laguna', 'betScore': None, 'homeTeamName': 'Puebla FC',
              'marketName': '最后进球的球队', 'matchTime': '2022-07-08 22:05:00', 'matchType': '早盘', 'odds': 1.7,
              'oddsType': '1', 'orderNo': 'XH4ty9kNZtkE', 'outcomeName': '普埃布拉', 'specifier': '',
              'tournamentName': '墨西哥甲级联赛，春季赛'},
             {'awayTeamName': '阿贾梅斯特拉', 'betScore': None, 'homeTeamName': '利斯萨桑德拉', 'marketName': '平局退款',
              'matchTime': '2022-06-25 11:30:00', 'matchType': '早盘', 'odds': 2.5, 'oddsType': '1',
              'orderNo': 'XH4ty9kNZtkE', 'outcomeName': '阿贾梅斯特拉', 'specifier': '', 'tournamentName': '象牙海岸科特迪瓦足球甲级联赛'},
             {'awayTeamName': '萨尔门托', 'betScore': None, 'homeTeamName': '普拉腾斯', 'marketName': '第1个进球',
              'matchTime': '2022-06-26 14:30:00', 'matchType': '早盘', 'odds': 1.82, 'oddsType': '1',
              'orderNo': 'XH4ty9kNZtkE', 'outcomeName': '普拉腾斯', 'specifier': 'goalnr=1', 'tournamentName': '阿根廷足球甲级联赛'},
             {'awayTeamName': 'Stade Reims', 'betScore': None, 'homeTeamName': '马赛', 'marketName': '最高进球数半场',
              'matchTime': '2022-08-07 14:00:00', 'matchType': '早盘', 'odds': 3.55, 'oddsType': '1',
              'orderNo': 'XH4ty9kNZtkE', 'outcomeName': '相同', 'specifier': '', 'tournamentName': '法国甲级联赛'},
             {'awayTeamName': '阿德萊德奧林匹克', 'betScore': None, 'homeTeamName': '南阿德莱得黑豹', 'marketName': '两队都进球',
              'matchTime': '2022-07-02 01:30:00', 'matchType': '早盘', 'odds': 2.6, 'oddsType': '1',
              'orderNo': 'XH4ty9kNZtkE', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛,南澳大利亚'},
             {'awayTeamName': 'IFK Varnamo', 'betScore': None, 'homeTeamName': '华保斯', 'marketName': '双重机会',
              'matchTime': '2022-07-03 09:00:00', 'matchType': '早盘', 'odds': 1.51, 'oddsType': '1',
              'orderNo': 'XH4tziKmwazz', 'outcomeName': '华保斯 或和局', 'specifier': '', 'tournamentName': '瑞典超级联赛'},
             {'awayTeamName': '阿梅尼奥', 'betScore': None, 'homeTeamName': '圣米格尔', 'marketName': '圣米格尔 两个半场都进球',
              'matchTime': '2022-06-25 14:30:00', 'matchType': '早盘', 'odds': 1.14, 'oddsType': '1',
              'orderNo': 'XH4tziKmwazz', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '阿根廷乙级联赛'},
             {'awayTeamName': 'Tampereen Ilves', 'betScore': None, 'homeTeamName': 'HIFK赫尔辛基',
              'marketName': 'HIFK赫尔辛基 进球数', 'matchTime': '2022-07-04 11:00:00', 'matchType': '早盘', 'odds': 2.45,
              'oddsType': '1', 'orderNo': 'XH4tziKmwazz', 'outcomeName': '1', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '芬兰超级联赛'},
             {'awayTeamName': '安山木槿花足球俱乐部', 'betScore': None, 'homeTeamName': 'Chungnam Asan FC',
              'marketName': 'Chungnam Asan FC 不失球获胜', 'matchTime': '2022-06-25 05:00:00', 'matchType': '早盘',
              'odds': 2.7, 'oddsType': '1', 'orderNo': 'XH4tziKmwazz', 'outcomeName': '是', 'specifier': '',
              'tournamentName': '韩国职业足球乙级联赛'},
             {'awayTeamName': '北京国安', 'betScore': None, 'homeTeamName': '沧州雄狮', 'marketName': '北京国安 大/小',
              'matchTime': '2022-06-25 04:30:00', 'matchType': '早盘', 'odds': 1.64, 'oddsType': '1',
              'orderNo': 'XH4tziKmwazz', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '中国超级联赛'},
             {'awayTeamName': '格兰库拉', 'betScore': None, 'homeTeamName': '坦佩雷-维纳尔长寿猫', 'marketName': '双重机会',
              'matchTime': '2022-06-29 12:00:00', 'matchType': '早盘', 'odds': 1.24, 'oddsType': '1',
              'orderNo': 'XH4tAsAs8bqT', 'outcomeName': '坦佩雷-维纳尔长寿猫 或 格兰库拉', 'specifier': '',
              'tournamentName': '芬兰乙级联赛，B组'},
             {'awayTeamName': 'Eintracht Frankfurt', 'betScore': None, 'homeTeamName': '皇家马德里',
              'marketName': 'Eintracht Frankfurt 最高进球数半场', 'matchTime': '2022-08-10 15:00:00', 'matchType': '早盘',
              'odds': 1.86, 'oddsType': '1', 'orderNo': 'XH4tAsAs8bqT', 'outcomeName': '相同', 'specifier': '',
              'tournamentName': '国际俱乐部欧洲超级杯'},
             {'awayTeamName': '卡尔斯塔德足球发展', 'betScore': None, 'homeTeamName': '泰比', 'marketName': '泰比 最高进球数半场',
              'matchTime': '2022-06-26 10:00:00', 'matchType': '早盘', 'odds': 3.6, 'oddsType': '1',
              'orderNo': 'XH4tAsAs8bqT', 'outcomeName': '上半场', 'specifier': '', 'tournamentName': '瑞典足球乙级联赛-北部'},
             {'awayTeamName': '马瑙斯', 'betScore': None, 'homeTeamName': '圣保罗博塔弗戈', 'marketName': '圣保罗博塔弗戈 胜利退款',
              'matchTime': '2022-06-26 10:00:00', 'matchType': '早盘', 'odds': 1.73, 'oddsType': '1',
              'orderNo': 'XH4tAsAs8bqT', 'outcomeName': '和局', 'specifier': '', 'tournamentName': '巴西丙级联赛'},
             {'awayTeamName': 'Shandong Luneng Srl', 'betScore': None, 'homeTeamName': 'Zhejiang Professional Srl',
              'marketName': '上半场 - 波胆', 'matchTime': '2022-06-25 01:00:00', 'matchType': '早盘', 'odds': 39.95,
              'oddsType': '1', 'orderNo': 'XH4tAsAs8bqT', 'outcomeName': '2:0', 'specifier': '',
              'tournamentName': '模拟现实联盟China Super League SRL'},
             {'awayTeamName': 'CE弗洛雷斯塔', 'betScore': None, 'homeTeamName': '費罗维里亚CE', 'marketName': '大/小',
              'matchTime': '2022-06-26 16:00:00', 'matchType': '早盘', 'odds': 1.74, 'oddsType': '1',
              'orderNo': 'XH4tBzMprQXb', 'outcomeName': '大1.5/2', 'specifier': 'total=1.75',
              'tournamentName': '巴西丙级联赛'},
             {'awayTeamName': '路易维尔城', 'betScore': None, 'homeTeamName': '哈特福德体育会', 'marketName': '上半场 - 路易维尔城 大/小',
              'matchTime': '2022-06-25 13:00:00', 'matchType': '早盘', 'odds': 1.61, 'oddsType': '1',
              'orderNo': 'XH4tBzMprQXb', 'outcomeName': '大0.5', 'specifier': 'total=0.5',
              'tournamentName': '美国足球联赛冠军杯'},
             {'awayTeamName': 'Leeds United', 'betScore': None, 'homeTeamName': 'Southampton FC',
              'marketName': '上半场 - 波胆', 'matchTime': '2022-08-13 10:00:00', 'matchType': '早盘', 'odds': 12.95,
              'oddsType': '1', 'orderNo': 'XH4tBzMprQXb', 'outcomeName': '2:0', 'specifier': '',
              'tournamentName': '英格兰英超'},
             {'awayTeamName': '奥萨讷', 'betScore': None, 'homeTeamName': '费德列斯达', 'marketName': '平局退款',
              'matchTime': '2022-07-04 12:00:00', 'matchType': '早盘', 'odds': 1.19, 'oddsType': '1',
              'orderNo': 'XH4tBzMprQXb', 'outcomeName': '费德列斯达', 'specifier': '', 'tournamentName': '挪威甲级联赛'},
             {'awayTeamName': 'Sarpsborg 08', 'betScore': None, 'homeTeamName': '汉坎', 'marketName': '净胜球数',
              'matchTime': '2022-06-26 12:00:00', 'matchType': '早盘', 'odds': 4.75, 'oddsType': '1',
              'orderNo': 'XH4tBzMprQXb', 'outcomeName': '汉坎 1', 'specifier': 'variant=sr:winning_margin:3+',
              'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '斯特林海姆', 'betScore': None, 'homeTeamName': '拉纳FK', 'marketName': '单/双',
              'matchTime': '2022-06-25 08:00:00', 'matchType': '早盘', 'odds': 1.87, 'oddsType': '1',
              'orderNo': 'XH4tCH4ChWyL', 'outcomeName': '单', 'specifier': '', 'tournamentName': '挪威丙级联赛第5组'},
             {'awayTeamName': 'FC Dallas', 'betScore': None, 'homeTeamName': 'Austin FC',
              'marketName': 'Austin FC 赢两个半场', 'matchTime': '2022-06-25 21:00:00', 'matchType': '早盘', 'odds': 5.35,
              'oddsType': '1', 'orderNo': 'XH4tCH4ChWyL', 'outcomeName': '是', 'specifier': '',
              'tournamentName': '美国职业足球大联盟'},
             {'awayTeamName': '阿赫利', 'betScore': None, 'homeTeamName': '史莫哈足球俱乐部', 'marketName': '独赢 & 大/小',
              'matchTime': '2022-06-29 15:30:00', 'matchType': '早盘', 'odds': 16.95, 'oddsType': '1',
              'orderNo': 'XH4tCH4ChWyL', 'outcomeName': '史莫哈足球俱乐部 & 小 1.5', 'specifier': 'total=1.5',
              'tournamentName': '埃及足球甲级联赛'},
             {'awayTeamName': 'KF Fjardabyggd', 'betScore': None, 'homeTeamName': '雷克雅维克活力',
              'marketName': 'KF Fjardabyggd 不失球', 'matchTime': '2022-06-25 10:00:00', 'matchType': '早盘', 'odds': 1.02,
              'oddsType': '1', 'orderNo': 'XH4tCH4ChWyL', 'outcomeName': '不是', 'specifier': '',
              'tournamentName': '冰岛女子足球乙级联赛'},
             {'awayTeamName': 'AC Horsens', 'betScore': None, 'homeTeamName': 'FC Copenhagen',
              'marketName': '上半场 - 平局退款', 'matchTime': '2022-07-17 10:00:00', 'matchType': '早盘', 'odds': 1.14,
              'oddsType': '1', 'orderNo': 'XH4tCH4ChWyL', 'outcomeName': '哥本哈根', 'specifier': '',
              'tournamentName': '丹麦超级联赛'},
             {'awayTeamName': 'Pouso Alegre MG', 'betScore': None, 'homeTeamName': '卡尔登塞', 'marketName': '总入球',
              'matchTime': '2022-06-25 15:00:00', 'matchType': '早盘', 'odds': 1.97, 'oddsType': '1',
              'orderNo': 'XH4tDR3rw8fn', 'outcomeName': '2-3', 'specifier': 'variant=sr:goal_range:7+',
              'tournamentName': '巴西丁级联赛'},
             {'awayTeamName': '曼立联', 'betScore': None, 'homeTeamName': '卧龙岗狼队', 'marketName': '双重机会',
              'matchTime': '2022-06-25 04:00:00', 'matchType': '早盘', 'odds': 1.57, 'oddsType': '1',
              'orderNo': 'XH4tDR3rw8fn', 'outcomeName': '和局或 曼立联', 'specifier': '',
              'tournamentName': '澳大利亚全国超级联赛,新南威尔士'},
             {'awayTeamName': '沙士菲', 'betScore': None, 'homeTeamName': '防卫者', 'marketName': '防卫者 不失球获胜',
              'matchTime': '2022-06-25 14:30:00', 'matchType': '早盘', 'odds': 1.31, 'oddsType': '1',
              'orderNo': 'XH4tDR3rw8fn', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '阿根廷足球甲级联赛'},
             {'awayTeamName': 'Eastern Company SC', 'betScore': None, 'homeTeamName': '艾尔古纳', 'marketName': '艾尔古纳 单/双',
              'matchTime': '2022-06-27 13:00:00', 'matchType': '早盘', 'odds': 1.74, 'oddsType': '1',
              'orderNo': 'XH4tDR3rw8fn', 'outcomeName': '双', 'specifier': '', 'tournamentName': '埃及足球甲级联赛'},
             {'awayTeamName': 'Bate Borisov', 'betScore': None, 'homeTeamName': '格罗德诺涅曼',
              'marketName': '上半场 - 格罗德诺涅曼 不失球', 'matchTime': '2022-06-25 14:00:00', 'matchType': '早盘', 'odds': 1.73,
              'oddsType': '1', 'orderNo': 'XH4tDR3rw8fn', 'outcomeName': '是', 'specifier': '',
              'tournamentName': '白俄罗斯足球超级联赛'},
             {'awayTeamName': 'America FC MG', 'betScore': None, 'homeTeamName': '法林明高RJ', 'marketName': '独赢 & 大/小',
              'matchTime': '2022-06-25 18:00:00', 'matchType': '早盘', 'odds': 2.28, 'oddsType': '1',
              'orderNo': 'XH4tDR3rw8fn', 'outcomeName': '法林明高RJ & 大 2.5', 'specifier': 'total=2.5',
              'tournamentName': '巴西甲级联赛'},
             {'awayTeamName': '阿尔维达特(约旦)', 'betScore': None, 'homeTeamName': '费萨里', 'marketName': '上半场 - 阿尔维达特(约旦) 不失球',
              'matchTime': '2022-06-25 13:30:00', 'matchType': '早盘', 'odds': 1.33, 'oddsType': '1',
              'orderNo': 'XH4tF8z2kSWS', 'outcomeName': '是', 'specifier': '', 'tournamentName': '约旦足球联赛'},
             {'awayTeamName': '年轻非洲人体育俱乐部', 'betScore': None, 'homeTeamName': '姆贝亚城', 'marketName': '净胜球数',
              'matchTime': '2022-06-25 09:00:00', 'matchType': '早盘', 'odds': 6.55, 'oddsType': '1',
              'orderNo': 'XH4tF8z2kSWS', 'outcomeName': '姆贝亚城 1', 'specifier': 'variant=sr:winning_margin:3+',
              'tournamentName': '坦桑尼亚超级联赛'},
             {'awayTeamName': '西堪培拉流浪者', 'betScore': None, 'homeTeamName': '古玛老虎', 'marketName': '单/双',
              'matchTime': '2022-06-25 01:00:00', 'matchType': '早盘', 'odds': 1.83, 'oddsType': '1',
              'orderNo': 'XH4tF8z2kSWS', 'outcomeName': '单', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛, 首都足球'},
             {'awayTeamName': '诺丁汉森林', 'betScore': None, 'homeTeamName': 'Newcastle United',
              'marketName': 'Newcastle United 单/双', 'matchTime': '2022-08-06 10:00:00', 'matchType': '早盘', 'odds': 1.77,
              'oddsType': '1', 'orderNo': 'XH4tF8z2kSWS', 'outcomeName': '双', 'specifier': '',
              'tournamentName': '英格兰英超'},
             {'awayTeamName': '堪培拉奥林匹克', 'betScore': None, 'homeTeamName': '贝尔康纳联', 'marketName': '堪培拉奥林匹克 单/双',
              'matchTime': '2022-06-25 01:00:00', 'matchType': '早盘', 'odds': 1.87, 'oddsType': '1',
              'orderNo': 'XH4tF8z2kSWS', 'outcomeName': '单', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛, 首都足球'},
             {'awayTeamName': '伊斯特恩沙伯', 'betScore': None, 'homeTeamName': '卡帕拉巴', 'marketName': '单/双',
              'matchTime': '2022-06-26 05:30:00', 'matchType': '早盘', 'odds': 1.84, 'oddsType': '1',
              'orderNo': 'XH4tF8z2kSWS', 'outcomeName': '单', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛，昆士兰州'},
             {'awayTeamName': 'SC克里西乌马', 'betScore': None, 'homeTeamName': 'PE瑙蒂科', 'marketName': '上半场 - 独赢 & 两队都进球',
              'matchTime': '2022-06-29 18:00:00', 'matchType': '早盘', 'odds': 3.7, 'oddsType': '1',
              'orderNo': 'XH4tGimVuX6R', 'outcomeName': 'PE瑙蒂科 & 不是', 'specifier': '', 'tournamentName': '巴西乙级联赛'},
             {'awayTeamName': '布里斯班市FC', 'betScore': None, 'homeTeamName': '洛根利泰柠', 'marketName': '布里斯班市FC 不失球获胜',
              'matchTime': '2022-07-06 05:30:00', 'matchType': '早盘', 'odds': 5.15, 'oddsType': '1',
              'orderNo': 'XH4tGimVuX6R', 'outcomeName': '是', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛，昆士兰州'},
             {'awayTeamName': '河岸奥林匹克', 'betScore': None, 'homeTeamName': 'Olympia Warriors Hobart',
              'marketName': '大/小 & 两队都进球', 'matchTime': '2022-06-25 02:00:00', 'matchType': '早盘', 'odds': 1.63,
              'oddsType': '1', 'orderNo': 'XH4tGimVuX6R', 'outcomeName': '大 2.5 & 是', 'specifier': 'total=2.5',
              'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚'},
             {'awayTeamName': 'Manchester United', 'betScore': None, 'homeTeamName': 'Brentford FC',
              'marketName': '上半场 - 独赢 & 大/小', 'matchTime': '2022-08-13 10:00:00', 'matchType': '早盘', 'odds': 11.95,
              'oddsType': '1', 'orderNo': 'XH4tGimVuX6R', 'outcomeName': '布伦特福德 & 大 1.5', 'specifier': 'total=1.5',
              'tournamentName': '英格兰英超'},
             {'awayTeamName': 'Trelleborgs FF', 'betScore': None, 'homeTeamName': 'Halmstads BK',
              'marketName': 'Trelleborgs FF 赢任何半场', 'matchTime': '2022-06-28 13:00:00', 'matchType': '早盘', 'odds': 2.5,
              'oddsType': '1', 'orderNo': 'XH4tGimVuX6R', 'outcomeName': '是', 'specifier': '',
              'tournamentName': '瑞典超甲级联赛'},
             {'awayTeamName': 'VfB Stuttgart', 'betScore': None, 'homeTeamName': 'Werder Bremen', 'marketName': '让球',
              'matchTime': '2022-08-13 09:30:00', 'matchType': '早盘', 'odds': 1.72, 'oddsType': '1',
              'orderNo': 'XH4tGimVuX6R', 'outcomeName': '云达不莱梅 ', 'specifier': 'hcp=0', 'tournamentName': '德国足球甲级联赛'},
             {'awayTeamName': '斯吉德', 'betScore': None, 'homeTeamName': '赖乌福斯', 'marketName': '斯吉德 赢两个半场',
              'matchTime': '2022-06-26 09:00:00', 'matchType': '早盘', 'odds': 1.02, 'oddsType': '1',
              'orderNo': 'XH4tHvZ6WTjE', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '挪威甲级联赛'},
             {'awayTeamName': 'PE瑙蒂科', 'betScore': None, 'homeTeamName': 'MG通布斯人', 'marketName': '上半场 - PE瑙蒂科 大/小',
              'matchTime': '2022-06-26 10:00:00', 'matchType': '早盘', 'odds': 2.55, 'oddsType': '1',
              'orderNo': 'XH4tHvZ6WTjE', 'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '巴西乙级联赛'},
             {'awayTeamName': 'Puebla FC', 'betScore': None, 'homeTeamName': 'Mazatlan FC',
              'marketName': 'Puebla FC 单/双', 'matchTime': '2022-07-01 22:05:00', 'matchType': '早盘', 'odds': 1.98,
              'oddsType': '1', 'orderNo': 'XH4tHvZ6WTjE', 'outcomeName': '单', 'specifier': '',
              'tournamentName': '墨西哥甲级联赛，春季赛'},
             {'awayTeamName': '珀斯SC', 'betScore': None, 'homeTeamName': '阿马达尔', 'marketName': '珀斯SC 不失球',
              'matchTime': '2022-06-25 03:00:00', 'matchType': '早盘', 'odds': 3.95, 'oddsType': '1',
              'orderNo': 'XH4tHvZ6WTjE', 'outcomeName': '是', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛,西澳大利亚'},
             {'awayTeamName': '赫尔辛堡', 'betScore': None, 'homeTeamName': 'Malmo FF', 'marketName': 'Malmo FF 最高进球数半场',
              'matchTime': '2022-06-27 13:00:00', 'matchType': '早盘', 'odds': 2.12, 'oddsType': '1',
              'orderNo': 'XH4tHvZ6WTjE', 'outcomeName': '下半场', 'specifier': '', 'tournamentName': '瑞典超级联赛'},
             {'awayTeamName': '苏德多克', 'betScore': None, 'homeTeamName': '菲力斯', 'marketName': '上半场 - 让球',
              'matchTime': '2022-06-25 14:30:00', 'matchType': '早盘', 'odds': 1.48, 'oddsType': '1',
              'orderNo': 'XH4tHvZ6WTjE', 'outcomeName': '菲力斯 ', 'specifier': 'hcp=0.25', 'tournamentName': '阿根廷乙级联赛'},
             {'awayTeamName': '格兰库拉', 'betScore': None, 'homeTeamName': '坦佩雷-维纳尔长寿猫', 'marketName': '哪队进球',
              'matchTime': '2022-06-29 12:00:00', 'matchType': '早盘', 'odds': 4.95, 'oddsType': '1',
              'orderNo': 'XH4tJUEc6Sxn', 'outcomeName': '仅 坦佩雷-维纳尔长寿猫', 'specifier': '', 'tournamentName': '芬兰乙级联赛，B组'},
             {'awayTeamName': 'Manchester United', 'betScore': None, 'homeTeamName': 'Brentford FC',
              'marketName': 'Manchester United 胜利退款', 'matchTime': '2022-08-13 10:00:00', 'matchType': '早盘',
              'odds': 1.76, 'oddsType': '1', 'orderNo': 'XH4tJUEc6Sxn', 'outcomeName': '和局', 'specifier': '',
              'tournamentName': '英格兰英超'}, {'awayTeamName': 'IFK Goteborg', 'betScore': None, 'homeTeamName': '天狼星',
                                           'marketName': '上半场 - IFK Goteborg 大/小', 'matchTime': '2022-06-27 13:00:00',
                                           'matchType': '早盘', 'odds': 2.02, 'oddsType': '1', 'orderNo': 'XH4tJUEc6Sxn',
                                           'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '瑞典超级联赛'},
             {'awayTeamName': 'PE瑙蒂科', 'betScore': None, 'homeTeamName': 'MG通布斯人', 'marketName': 'MG通布斯人 赢任何半场',
              'matchTime': '2022-06-26 10:00:00', 'matchType': '早盘', 'odds': 1.57, 'oddsType': '1',
              'orderNo': 'XH4tJUEc6Sxn', 'outcomeName': '是', 'specifier': '', 'tournamentName': '巴西乙级联赛'},
             {'awayTeamName': '北爱尔兰', 'betScore': None, 'homeTeamName': '挪威', 'marketName': '上半场 - 让球',
              'matchTime': '2022-07-07 15:00:00', 'matchType': '早盘', 'odds': 1.7, 'oddsType': '1',
              'orderNo': 'XH4tJUEc6Sxn', 'outcomeName': '挪威 ', 'specifier': 'hcp=-1', 'tournamentName': '国际欧洲锦标赛，女子'},
             {'awayTeamName': '阿尔维达特(约旦)', 'betScore': None, 'homeTeamName': '费萨里', 'marketName': '上半场 - 独赢',
              'matchTime': '2022-06-25 13:30:00', 'matchType': '早盘', 'odds': 4.35, 'oddsType': '1',
              'orderNo': 'XH4tJUEc6Sxn', 'outcomeName': '费萨里', 'specifier': '', 'tournamentName': '约旦足球联赛'},
             {'awayTeamName': 'AC Ajaccio', 'betScore': None, 'homeTeamName': 'Olympique Lyon',
              'marketName': '上半场 - 让球', 'matchTime': '2022-08-07 14:00:00', 'matchType': '早盘', 'odds': 2.25,
              'oddsType': '1', 'orderNo': 'XH4tL4REXVDW', 'outcomeName': '里昂 ', 'specifier': 'hcp=-0.75',
              'tournamentName': '法国甲级联赛'},
             {'awayTeamName': 'National Bank of Egypt SC', 'betScore': None, 'homeTeamName': '阿拉伯建筑',
              'marketName': '上半场 - 双重机会', 'matchTime': '2022-06-28 13:00:00', 'matchType': '早盘', 'odds': 1.36,
              'oddsType': '1', 'orderNo': 'XH4tL4REXVDW', 'outcomeName': '和局或 National Bank of Egypt SC',
              'specifier': '', 'tournamentName': '埃及足球甲级联赛'},
             {'awayTeamName': '悉尼联队', 'betScore': None, 'homeTeamName': '洛克达尔', 'marketName': '独赢 & 大/小',
              'matchTime': '2022-06-26 01:00:00', 'matchType': '早盘', 'odds': 3.65, 'oddsType': '1',
              'orderNo': 'XH4tL4REXVDW', 'outcomeName': '洛克达尔 & 小 3.5', 'specifier': 'total=3.5',
              'tournamentName': '澳大利亚全国超级联赛,新南威尔士'},
             {'awayTeamName': 'PR巴拉纳', 'betScore': None, 'homeTeamName': 'RJ葡萄牙人竞技', 'marketName': '净胜球数',
              'matchTime': '2022-06-25 14:00:00', 'matchType': '早盘', 'odds': 19.95, 'oddsType': '1',
              'orderNo': 'XH4tL4REXVDW', 'outcomeName': 'RJ葡萄牙人竞技 3+', 'specifier': 'variant=sr:winning_margin:3+',
              'tournamentName': '巴西丁级联赛'},
             {'awayTeamName': '巴黎圣日耳曼', 'betScore': None, 'homeTeamName': 'Clermont Foot 63', 'marketName': '上半场 - 让球',
              'matchTime': '2022-08-07 14:00:00', 'matchType': '早盘', 'odds': 2.32, 'oddsType': '1',
              'orderNo': 'XH4tL4REXVDW', 'outcomeName': '克莱蒙特 ', 'specifier': 'hcp=0.25', 'tournamentName': '法国甲级联赛'},
             {'awayTeamName': 'Lillestrom SK', 'betScore': None, 'homeTeamName': 'Stroemsgodset IF',
              'marketName': '独赢 & 大/小', 'matchTime': '2022-06-26 12:00:00', 'matchType': '早盘', 'odds': 7.35,
              'oddsType': '1', 'orderNo': 'XH4tL4REXVDW', 'outcomeName': '斯托姆加斯特 & 大 3.5', 'specifier': 'total=3.5',
              'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '塞尔维亚', 'betScore': None, 'homeTeamName': '喀麦隆', 'marketName': '最高进球数半场',
              'matchTime': '2022-11-28 06:00:00', 'matchType': '早盘', 'odds': 3.3, 'oddsType': '1',
              'orderNo': 'XH4tMn8tMBbV', 'outcomeName': '上半场', 'specifier': '', 'tournamentName': '国际世界杯'},
             {'awayTeamName': 'Osters IF', 'betScore': None, 'homeTeamName': 'IF Brommapojkarna',
              'marketName': '双重机会&两队都进球', 'matchTime': '2022-06-27 13:00:00', 'matchType': '早盘', 'odds': 2.34,
              'oddsType': '1', 'orderNo': 'XH4tMn8tMBbV', 'outcomeName': '布洛马波卡纳/和局 & 是', 'specifier': '',
              'tournamentName': '瑞典超甲级联赛'},
             {'awayTeamName': '乌拉圭', 'betScore': None, 'homeTeamName': 'Portugal', 'marketName': '乌拉圭 最高进球数半场',
              'matchTime': '2022-11-28 15:00:00', 'matchType': '早盘', 'odds': 2.8, 'oddsType': '1',
              'orderNo': 'XH4tMn8tMBbV', 'outcomeName': '下半场', 'specifier': '', 'tournamentName': '国际世界杯'},
             {'awayTeamName': '富川FC', 'betScore': None, 'homeTeamName': 'Busan I Park', 'marketName': '富川FC 胜利退款',
              'matchTime': '2022-06-26 05:00:00', 'matchType': '早盘', 'odds': 1.94, 'oddsType': '1',
              'orderNo': 'XH4tMn8tMBbV', 'outcomeName': '和局', 'specifier': '', 'tournamentName': '韩国职业足球乙级联赛'},
             {'awayTeamName': '维京古', 'betScore': None, 'homeTeamName': '雷克雅未克足球俱乐部', 'marketName': '维京古 胜利退款',
              'matchTime': '2022-07-02 12:00:00', 'matchType': '早盘', 'odds': 1.46, 'oddsType': '1',
              'orderNo': 'XH4tMn8tMBbV', 'outcomeName': '雷克雅未克足球俱乐部', 'specifier': '', 'tournamentName': '冰岛足球超级联赛'},
             {'awayTeamName': 'Bayern Munich', 'betScore': None, 'homeTeamName': 'RB Leipzig',
              'marketName': '大/小 & 两队都进球', 'matchTime': '2022-07-30 14:30:00', 'matchType': '早盘', 'odds': 8.75,
              'oddsType': '1', 'orderNo': 'XH4tMn8tMBbV', 'outcomeName': '大 2.5 & 不是', 'specifier': 'total=2.5',
              'tournamentName': '德国超级杯'},
             {'awayTeamName': 'Weston Workers FC', 'betScore': None, 'homeTeamName': 'Lake Macquarie FC',
              'marketName': 'Lake Macquarie FC 进球数', 'matchTime': '2022-06-29 05:00:00', 'matchType': '早盘', 'odds': 2.6,
              'oddsType': '1', 'orderNo': 'XH4tMn8tMBbV', 'outcomeName': '1', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '澳大利亚全国超级联赛,新南威尔士州北部'},
             {'awayTeamName': '金泉尚武足球俱乐部', 'betScore': None, 'homeTeamName': '浦项制铁', 'marketName': '浦项制铁 赢两个半场',
              'matchTime': '2022-06-26 06:00:00', 'matchType': '早盘', 'odds': 5.35, 'oddsType': '1',
              'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '是', 'specifier': '', 'tournamentName': '韩国K1联赛'},
             {'awayTeamName': '新泻天鹅', 'betScore': None, 'homeTeamName': '横滨', 'marketName': '横滨 单/双',
              'matchTime': '2022-06-26 05:00:00', 'matchType': '早盘', 'odds': 1.97, 'oddsType': '1',
              'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '单', 'specifier': '', 'tournamentName': '日本乙级联赛'},
             {'awayTeamName': '埃尔盐', 'betScore': None, 'homeTeamName': '艾沙赫', 'marketName': '艾沙赫 赢任何半场',
              'matchTime': '2022-06-25 11:00:00', 'matchType': '早盘', 'odds': 1.73, 'oddsType': '1',
              'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '约旦足球联赛'},
             {'awayTeamName': '哥斯达黎加', 'betScore': None, 'homeTeamName': '西班牙', 'marketName': '上半场 - 大/小',
              'matchTime': '2022-11-23 12:00:00', 'matchType': '早盘', 'odds': 1.48, 'oddsType': '1',
              'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '大0.5/1', 'specifier': 'total=0.75', 'tournamentName': '国际世界杯'},
             {'awayTeamName': 'Charlotte FC', 'betScore': None, 'homeTeamName': 'CF Montreal',
              'marketName': 'CF Montreal 角球数范围', 'matchTime': '2022-06-25 19:30:00', 'matchType': '早盘', 'odds': 3.2,
              'oddsType': '1', 'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '5-6',
              'specifier': 'variant=sr:point_range:7+', 'tournamentName': '美国职业足球大联盟'},
             {'awayTeamName': 'Hjs', 'betScore': None, 'homeTeamName': 'VJS', 'marketName': 'Hjs 大/小',
              'matchTime': '2022-06-29 11:30:00', 'matchType': '早盘', 'odds': 1.87, 'oddsType': '1',
              'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '大1.5', 'specifier': 'total=1.5',
              'tournamentName': '芬兰乙级联赛，B组'},
             {'awayTeamName': '伊浩特斯IK', 'betScore': None, 'homeTeamName': '格雷伯斯塔德', 'marketName': '格雷伯斯塔德 两个半场都进球',
              'matchTime': '2022-06-26 10:00:00', 'matchType': '早盘', 'odds': 3.5, 'oddsType': '1',
              'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '是', 'specifier': '', 'tournamentName': '瑞典丙级联赛-北哥特兰地区'},
             {'awayTeamName': '韩国', 'betScore': None, 'homeTeamName': '乌拉圭', 'marketName': '韩国 最高进球数半场',
              'matchTime': '2022-11-24 09:00:00', 'matchType': '早盘', 'odds': 4.35, 'oddsType': '1',
              'orderNo': 'XH4tNxPmFwjz', 'outcomeName': '上半场', 'specifier': '', 'tournamentName': '国际世界杯'},
             {'awayTeamName': '特鲁瓦', 'betScore': None, 'homeTeamName': '蒙彼利埃', 'marketName': '第1个进球',
              'matchTime': '2022-08-07 14:00:00', 'matchType': '早盘', 'odds': 2.17, 'oddsType': '1',
              'orderNo': 'XH4tPGuL87R3', 'outcomeName': '特鲁瓦', 'specifier': 'goalnr=1', 'tournamentName': '法国甲级联赛'},
             {'awayTeamName': 'Aberdeen FC', 'betScore': None, 'homeTeamName': 'Celtic Glasgow',
              'marketName': '上半场 - Celtic Glasgow 不失球', 'matchTime': '2022-07-31 11:30:00', 'matchType': '早盘',
              'odds': 1.3, 'oddsType': '1', 'orderNo': 'XH4tPGuL87R3', 'outcomeName': '是', 'specifier': '',
              'tournamentName': '苏格兰足球超级联赛'},
             {'awayTeamName': '甲府风林', 'betScore': None, 'homeTeamName': '山口雷法', 'marketName': '山口雷法 进球数',
              'matchTime': '2022-06-26 06:00:00', 'matchType': '早盘', 'odds': 2.35, 'oddsType': '1',
              'orderNo': 'XH4tPGuL87R3', 'outcomeName': '0', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '日本乙级联赛'},
             {'awayTeamName': 'Fortuna Dusseldorf', 'betScore': None, 'homeTeamName': '1. FC Magdeburg',
              'marketName': '双重机会&两队都进球', 'matchTime': '2022-07-16 14:30:00', 'matchType': '早盘', 'odds': 4.05,
              'oddsType': '1', 'orderNo': 'XH4tPGuL87R3', 'outcomeName': '马格德堡/和局 & 不是', 'specifier': '',
              'tournamentName': '德国乙级联赛'},
             {'awayTeamName': '冈山绿雉', 'betScore': None, 'homeTeamName': 'Mito Hollyhock', 'marketName': '波胆',
              'matchTime': '2022-06-25 05:00:00', 'matchType': '早盘', 'odds': 100.95, 'oddsType': '1',
              'orderNo': 'XH4tPGuL87R3', 'outcomeName': '4:3', 'specifier': '', 'tournamentName': '日本乙级联赛'},
             {'awayTeamName': '中央西班牙人', 'betScore': None, 'homeTeamName': '普罗格雷索', 'marketName': '中央西班牙人 胜利退款',
              'matchTime': '2022-06-25 11:30:00', 'matchType': '早盘', 'odds': 1.64, 'oddsType': '1',
              'orderNo': 'XH4tPGuL87R3', 'outcomeName': '普罗格雷索', 'specifier': '', 'tournamentName': '乌拉圭乙级联赛'},
             {'awayTeamName': '瑞士', 'betScore': None, 'homeTeamName': '葡萄牙', 'marketName': '平局退款',
              'matchTime': '2022-07-09 12:00:00', 'matchType': '早盘', 'odds': 1.21, 'oddsType': '1',
              'orderNo': 'XH4tPGuL87R3', 'outcomeName': '瑞士', 'specifier': '', 'tournamentName': '国际欧洲锦标赛，女子'},
             {'awayTeamName': 'SC克里西乌马', 'betScore': None, 'homeTeamName': 'SP伊图阿诺', 'marketName': 'SP伊图阿诺 单/双',
              'matchTime': '2022-07-02 15:30:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1',
              'orderNo': 'XH4tPGuL87R3', 'outcomeName': '双', 'specifier': '', 'tournamentName': '巴西乙级联赛'},
             {'awayTeamName': '奥哈卡', 'betScore': None, 'homeTeamName': '瓜达拉哈拉大学黑狮子', 'marketName': '让球',
              'matchTime': '2022-06-25 22:05:00', 'matchType': '早盘', 'odds': 2.32, 'oddsType': '1',
              'orderNo': 'XH4tPGuL87R3', 'outcomeName': '瓜达拉哈拉大学黑狮子 ', 'specifier': 'hcp=-0.75',
              'tournamentName': '墨西哥乙级联赛，秋季赛'},
             {'awayTeamName': '哥斯达黎加', 'betScore': None, 'homeTeamName': '西班牙', 'marketName': '哥斯达黎加 胜利退款',
              'matchTime': '2022-11-23 12:00:00', 'matchType': '早盘', 'odds': 1.17, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '西班牙', 'specifier': '', 'tournamentName': '国际世界杯'},
             {'awayTeamName': '摩顿湾联(女)', 'betScore': None, 'homeTeamName': '狮子', 'marketName': '净胜球数',
              'matchTime': '2022-06-25 05:00:00', 'matchType': '早盘', 'odds': 1.27, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '狮子 3+', 'specifier': 'variant=sr:winning_margin:3+',
              'tournamentName': '澳大利亚全国超级联赛,女子'},
             {'awayTeamName': '拉贾卡萨布兰卡', 'betScore': None, 'homeTeamName': 'Hassania Union Sport Agadir',
              'marketName': '双重机会&大/小', 'matchTime': '2022-06-25 15:30:00', 'matchType': '早盘', 'odds': 4.85,
              'oddsType': '1', 'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '阿加迪尔哈萨尼亚/和局 & 大 2.5',
              'specifier': 'total=2.5', 'tournamentName': '摩洛哥足球甲级联赛'},
             {'awayTeamName': '邓迪联', 'betScore': None, 'homeTeamName': 'Kilmarnock FC', 'marketName': '上半场 - 邓迪联 不失球',
              'matchTime': '2022-07-30 10:00:00', 'matchType': '早盘', 'odds': 1.95, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '苏格兰足球超级联赛'},
             {'awayTeamName': '阿德莱德联(青年)', 'betScore': None, 'homeTeamName': '克罗伊登国王', 'marketName': '单/双',
              'matchTime': '2022-06-25 06:15:00', 'matchType': '早盘', 'odds': 1.78, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '双', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛,南澳大利亚'},
             {'awayTeamName': '布里斯班奥林匹克', 'betScore': None, 'homeTeamName': '布里斯班市FC', 'marketName': '布里斯班奥林匹克 单/双',
              'matchTime': '2022-06-25 03:30:00', 'matchType': '早盘', 'odds': 1.83, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '单', 'specifier': '', 'tournamentName': '澳大利亚全国超级联赛，昆士兰州'},
             {'awayTeamName': 'FC Gomel', 'betScore': None, 'homeTeamName': '伊斯洛奇明斯克', 'marketName': 'FC Gomel 进球数',
              'matchTime': '2022-06-25 08:00:00', 'matchType': '早盘', 'odds': 2.55, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '1', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '白俄罗斯足球超级联赛'},
             {'awayTeamName': '沙特阿拉伯', 'betScore': None, 'homeTeamName': 'Poland', 'marketName': '独赢 & 大/小',
              'matchTime': '2022-11-26 09:00:00', 'matchType': '早盘', 'odds': 3.8, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '波兰 & 小 2.5', 'specifier': 'total=2.5',
              'tournamentName': '国际世界杯'},
             {'awayTeamName': 'MG通布斯人', 'betScore': None, 'homeTeamName': 'AL巴西雷加塔斯', 'marketName': 'MG通布斯人 大/小',
              'matchTime': '2022-06-29 20:30:00', 'matchType': '早盘', 'odds': 1.53, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '巴西乙级联赛'},
             {'awayTeamName': '塞尔维亚', 'betScore': None, 'homeTeamName': '奥地利', 'marketName': '奥地利 大/小',
              'matchTime': '2022-06-25 14:00:00', 'matchType': '早盘', 'odds': 2.0, 'oddsType': '1',
              'orderNo': 'XH4tQQmJB3fz', 'outcomeName': '大1.5', 'specifier': 'total=1.5',
              'tournamentName': '国际青年U19欧洲锦标赛'},
             {'awayTeamName': 'SC Corinthians SP', 'betScore': None, 'homeTeamName': 'Fluminense FC RJ',
              'marketName': 'SC Corinthians SP 最高进球数半场', 'matchTime': '2022-07-02 15:30:00', 'matchType': '早盘',
              'odds': 2.9, 'oddsType': '1', 'orderNo': 'XHwywk2ajBF9', 'outcomeName': '下半场', 'specifier': '',
              'tournamentName': '巴西甲级联赛'},
             {'awayTeamName': '耶尔文佩', 'betScore': None, 'homeTeamName': '拉迪', 'marketName': '拉迪 不失球获胜',
              'matchTime': '2022-06-28 11:30:00', 'matchType': '早盘', 'odds': 2.1, 'oddsType': '1',
              'orderNo': 'XHwywk2ajBF9', 'outcomeName': '是', 'specifier': '', 'tournamentName': '芬兰杯'},
             {'awayTeamName': 'Busan I Park', 'betScore': None, 'homeTeamName': 'Chungnam Asan FC',
              'marketName': '独赢 & 两队都进球', 'matchTime': '2022-07-03 05:00:00', 'matchType': '早盘', 'odds': 3.0,
              'oddsType': '1', 'orderNo': 'XHwyxu7YzU9u', 'outcomeName': '牙山木槿花足球俱乐部 & 不是', 'specifier': '',
              'tournamentName': '韩国职业足球乙级联赛'},
             {'awayTeamName': 'RJ博塔弗戈', 'betScore': None, 'homeTeamName': 'Red Bull Bragantino SP',
              'marketName': 'Red Bull Bragantino SP 进球数', 'matchTime': '2022-07-04 19:00:00', 'matchType': '早盘',
              'odds': 4.55, 'oddsType': '1', 'orderNo': 'XHwyxu7YzU9u', 'outcomeName': '3+',
              'specifier': 'variant=sr:exact_goals:3+', 'tournamentName': '巴西甲级联赛'},
             {'awayTeamName': '八打灵再也城', 'betScore': None, 'homeTeamName': '柔佛', 'marketName': '八打灵再也城 单/双',
              'matchTime': '2022-06-28 09:00:00', 'matchType': '早盘', 'odds': 1.4, 'oddsType': '1',
              'orderNo': 'XHwyxu7YzU9u', 'outcomeName': '双', 'specifier': '', 'tournamentName': '马来西亚超级联赛'},
             {'awayTeamName': 'FK Ural Yekaterinburg', 'betScore': None, 'homeTeamName': 'CSKA Moscow',
              'marketName': '双重机会&两队都进球', 'matchTime': '2022-07-16 08:00:00', 'matchType': '早盘', 'odds': 2.01,
              'oddsType': '1', 'orderNo': 'XHwyyBLfvQxm', 'outcomeName': '莫斯科中央陆军/和局 & 不是', 'specifier': '',
              'tournamentName': '俄罗斯足球超级联赛'},
             {'awayTeamName': '匈牙利', 'betScore': None, 'homeTeamName': '乌克兰', 'marketName': '乌克兰 不失球',
              'matchTime': '2022-06-28 14:00:00', 'matchType': '早盘', 'odds': 1.28, 'oddsType': '1',
              'orderNo': 'XHwyyBLfvQxm', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '国际世界锦标赛欧洲区女子预选赛'},
             {'awayTeamName': '因勒乌德联', 'betScore': None, 'homeTeamName': '科克本市', 'marketName': '哪队进球',
              'matchTime': '2022-07-02 03:00:00', 'matchType': '早盘', 'odds': 5.75, 'oddsType': '1',
              'orderNo': 'XHwyyBLfvQxm', 'outcomeName': '仅 因勒乌德联', 'specifier': '',
              'tournamentName': '澳大利亚全国超级联赛,西澳大利亚'},
             {'awayTeamName': '撒马尔罕迪纳摩', 'betScore': None, 'homeTeamName': '浩罕1912', 'marketName': '上半场 - 浩罕1912 大/小',
              'matchTime': '2022-06-28 11:00:00', 'matchType': '早盘', 'odds': 0.71, 'oddsType': '2',
              'orderNo': 'XHwyzKfWDnAD', 'outcomeName': '大0.5', 'specifier': 'total=0.5',
              'tournamentName': '乌兹别克斯坦职业足球联赛'},
             {'awayTeamName': '汉坎', 'betScore': None, 'homeTeamName': 'FK Haugesund', 'marketName': '半场/全场',
              'matchTime': '2022-07-10 14:00:00', 'matchType': '早盘', 'odds': 39.95, 'oddsType': '1',
              'orderNo': 'XHwyzKfWDnAD', 'outcomeName': '海于格松/汉坎', 'specifier': '', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': 'Sarpsborg 08', 'betScore': None, 'homeTeamName': 'Bodoe/Glimt',
              'marketName': '独赢 & 两队都进球', 'matchTime': '2022-07-09 10:00:00', 'matchType': '早盘', 'odds': 3.25,
              'oddsType': '1', 'orderNo': 'XHwyzKfWDnAD', 'outcomeName': '波杜基林特 & 是', 'specifier': '',
              'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '仁川联队', 'betScore': None, 'homeTeamName': '水原三星', 'marketName': '仁川联队 不失球',
              'matchTime': '2022-07-03 06:30:00', 'matchType': '早盘', 'odds': 2.9, 'oddsType': '1',
              'orderNo': 'XHwyASEi7ptH', 'outcomeName': '是', 'specifier': '', 'tournamentName': '韩国K1联赛'},
             {'awayTeamName': '武汉', 'betScore': None, 'homeTeamName': '河北', 'marketName': '武汉 不失球获胜',
              'matchTime': '2022-06-30 07:30:00', 'matchType': '早盘', 'odds': 1.83, 'oddsType': '1',
              'orderNo': 'XHwyASEi7ptH', 'outcomeName': '是', 'specifier': '', 'tournamentName': '中国超级联赛'},
             {'awayTeamName': '奥地利', 'betScore': None, 'homeTeamName': '斯洛伐克', 'marketName': '上半场 - 总入球 ',
              'matchTime': '2022-06-28 11:00:00', 'matchType': '早盘', 'odds': 2.55, 'oddsType': '1',
              'orderNo': 'XHwyASEi7ptH', 'outcomeName': '1', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '国际青年U19欧洲锦标赛'},
             {'awayTeamName': 'Bodoe/Glimt', 'betScore': None, 'homeTeamName': 'Odds BK', 'marketName': '两队都进球',
              'matchTime': '2022-07-02 12:00:00', 'matchType': '早盘', 'odds': 2.18, 'oddsType': '1',
              'orderNo': 'XHwyASEi7ptH', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '科克城', 'betScore': None, 'homeTeamName': '布雷', 'marketName': '上半场 - 独赢 & 大/小',
              'matchTime': '2022-07-01 14:45:00', 'matchType': '早盘', 'odds': 8.55, 'oddsType': '1',
              'orderNo': 'XHwyC27GPLvT', 'outcomeName': '布雷 & 小 1.5', 'specifier': 'total=1.5',
              'tournamentName': '爱尔兰甲级联赛'},
             {'awayTeamName': 'Kashima Antlers', 'betScore': None, 'homeTeamName': 'Kashiwa Reysol',
              'marketName': 'Kashima Antlers 大/小', 'matchTime': '2022-07-02 05:30:00', 'matchType': '早盘', 'odds': 1.0,
              'oddsType': '2', 'orderNo': 'XHwyC27GPLvT', 'outcomeName': '大1.5', 'specifier': 'total=1.5',
              'tournamentName': '日本J联赛'},
             {'awayTeamName': 'Undrid FF', 'betScore': None, 'homeTeamName': '鲁纳维克II', 'marketName': 'Undrid FF 进球数',
              'matchTime': '2022-06-28 14:45:00', 'matchType': '早盘', 'odds': 2.04, 'oddsType': '1',
              'orderNo': 'XHwyC27GPLvT', 'outcomeName': '3+', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '法罗群岛乙级联赛'},
             {'awayTeamName': '山口雷法', 'betScore': None, 'homeTeamName': 'Blaublitz Akita', 'marketName': '第1个进球',
              'matchTime': '2022-07-02 01:00:00', 'matchType': '早盘', 'odds': 2.36, 'oddsType': '1',
              'orderNo': 'XHwyC27GPLvT', 'outcomeName': '山口雷法', 'specifier': 'goalnr=1', 'tournamentName': '日本乙级联赛'},
             {'awayTeamName': 'New York Red Bulls', 'betScore': None, 'homeTeamName': 'Sporting Kansas City',
              'marketName': '上半场 - 单/双', 'matchTime': '2022-07-03 20:00:00', 'matchType': '早盘', 'odds': 1.99,
              'oddsType': '1', 'orderNo': 'XHwyDiuV7U4y', 'outcomeName': '单', 'specifier': '',
              'tournamentName': '美国职业足球大联盟'},
             {'awayTeamName': 'FC Cincinnati', 'betScore': None, 'homeTeamName': 'New England Revolution',
              'marketName': '平局退款', 'matchTime': '2022-07-03 19:30:00', 'matchType': '早盘', 'odds': 3.85,
              'oddsType': '1', 'orderNo': 'XHwyDiuV7U4y', 'outcomeName': '辛辛那堤', 'specifier': '',
              'tournamentName': '美国职业足球大联盟'},
             {'awayTeamName': '班菲特', 'betScore': None, 'homeTeamName': '小保加', 'marketName': '净胜球数',
              'matchTime': '2022-07-01 20:30:00', 'matchType': '早盘', 'odds': 5.95, 'oddsType': '1',
              'orderNo': 'XHwyDiuV7U4y', 'outcomeName': '小保加 2', 'specifier': 'variant=sr:winning_margin:3+',
              'tournamentName': '阿根廷足球甲级联赛'},
             {'awayTeamName': 'KI克拉克斯维克二队', 'betScore': None, 'homeTeamName': '桑多伊', 'marketName': '独赢 & 两队都进球',
              'matchTime': '2022-06-28 14:30:00', 'matchType': '早盘', 'odds': 3.4, 'oddsType': '1',
              'orderNo': 'XHwyDiuV7U4y', 'outcomeName': '桑多伊 & 是', 'specifier': '', 'tournamentName': '法罗群岛乙级联赛'},
             {'awayTeamName': 'FK Haugesund', 'betScore': None, 'homeTeamName': 'FK Jerv', 'marketName': '上半场 - 双重机会',
              'matchTime': '2022-07-02 10:00:00', 'matchType': '早盘', 'odds': 1.35, 'oddsType': '1',
              'orderNo': 'XHwyEtjyajXh', 'outcomeName': '和局或 海于格松', 'specifier': '', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': 'Sandefjord Fotball', 'betScore': None, 'homeTeamName': 'Sarpsborg 08',
              'marketName': '上半场 - 双重机会', 'matchTime': '2022-07-03 12:00:00', 'matchType': '早盘', 'odds': 1.22,
              'oddsType': '1', 'orderNo': 'XHwyEtjyajXh', 'outcomeName': '萨尔普斯堡 或和局', 'specifier': '',
              'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '因勒乌德联', 'betScore': None, 'homeTeamName': '科克本市', 'marketName': '科克本市 进球数',
              'matchTime': '2022-07-02 03:00:00', 'matchType': '早盘', 'odds': 3.4, 'oddsType': '1',
              'orderNo': 'XHwyEtjyajXh', 'outcomeName': '2', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '澳大利亚全国超级联赛,西澳大利亚'},
             {'awayTeamName': '汉坎', 'betScore': None, 'homeTeamName': 'FK Haugesund', 'marketName': '波胆',
              'matchTime': '2022-07-10 14:00:00', 'matchType': '早盘', 'odds': 16.95, 'oddsType': '1',
              'orderNo': 'XHwyEtjyajXh', 'outcomeName': '3:1', 'specifier': '', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '江原', 'betScore': None, 'homeTeamName': '城南足球俱乐部', 'marketName': '上半场 - 城南足球俱乐部 不失球',
              'matchTime': '2022-07-02 07:00:00', 'matchType': '早盘', 'odds': 1.55, 'oddsType': '1',
              'orderNo': 'XHwyFR6MQDA7', 'outcomeName': '是', 'specifier': '', 'tournamentName': '韩国K1联赛'},
             {'awayTeamName': '洛辛堡', 'betScore': None, 'homeTeamName': 'Viking FK', 'marketName': 'Viking FK 大/小',
              'matchTime': '2022-07-03 14:00:00', 'matchType': '早盘', 'odds': 0.74, 'oddsType': '2',
              'orderNo': 'XHwyFR6MQDA7', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': '布拉迪斯拉发斯拉夫', 'betScore': None, 'homeTeamName': '皮尔森', 'marketName': '大/小 & 两队都进球',
              'matchTime': '2022-06-28 10:30:00', 'matchType': '早盘', 'odds': 1.78, 'oddsType': '1',
              'orderNo': 'XHwyFR6MQDA7', 'outcomeName': '大 2.5 & 是', 'specifier': 'total=2.5',
              'tournamentName': '国际俱乐部俱乐部友谊赛'},
             {'awayTeamName': '南墨尔本', 'betScore': None, 'homeTeamName': '东方狮子', 'marketName': '独赢 & 大/小',
              'matchTime': '2022-07-02 01:00:00', 'matchType': '早盘', 'odds': 28.95, 'oddsType': '1',
              'orderNo': 'XHwyFR6MQDA7', 'outcomeName': '东方狮子 & 小 1.5', 'specifier': 'total=1.5',
              'tournamentName': '澳大利亚全国超级联赛,维多利亚'},
             {'awayTeamName': '丹麦', 'betScore': None, 'homeTeamName': '德国', 'marketName': '上半场 - 双重机会&两队都进球',
              'matchTime': '2022-07-08 15:00:00', 'matchType': '早盘', 'odds': 1.5, 'oddsType': '1',
              'orderNo': 'XHwyFR6MQDA7', 'outcomeName': '德国/和局 & 不是', 'specifier': '', 'tournamentName': '国际欧洲锦标赛，女子'},
             {'awayTeamName': '塞尔福斯', 'betScore': None, 'homeTeamName': '格林达维克', 'marketName': '半场/全场',
              'matchTime': '2022-07-01 15:15:00', 'matchType': '早盘', 'odds': 34.95, 'oddsType': '1',
              'orderNo': 'XHwyHLmh696C', 'outcomeName': '格林达维克/塞尔福斯', 'specifier': '', 'tournamentName': '冰岛甲级联赛'},
             {'awayTeamName': '科克城', 'betScore': None, 'homeTeamName': '布雷', 'marketName': '独赢',
              'matchTime': '2022-07-01 14:45:00', 'matchType': '早盘', 'odds': 5.95, 'oddsType': '1',
              'orderNo': 'XHwyHLmh696C', 'outcomeName': '布雷', 'specifier': '', 'tournamentName': '爱尔兰甲级联赛'},
             {'awayTeamName': '戈伊亚斯GO', 'betScore': None, 'homeTeamName': 'America FC MG', 'marketName': '双重机会',
              'matchTime': '2022-07-03 17:00:00', 'matchType': '早盘', 'odds': 1.93, 'oddsType': '1',
              'orderNo': 'XHwyHLmh696C', 'outcomeName': '和局或 戈伊亚斯GO', 'specifier': '', 'tournamentName': '巴西甲级联赛'},
             {'awayTeamName': '今治足球俱乐部', 'betScore': None, 'homeTeamName': 'FC岐埠', 'marketName': '今治足球俱乐部 单/双',
              'matchTime': '2022-07-03 06:00:00', 'matchType': '早盘', 'odds': 2.02, 'oddsType': '1',
              'orderNo': 'XHwyHLmh696C', 'outcomeName': '单', 'specifier': '', 'tournamentName': '日本丙级联赛'},
             {'awayTeamName': '萨马拉苏维埃之翼足球俱乐部', 'betScore': None, 'homeTeamName': '喀山鲁宾', 'marketName': '两队都进球',
              'matchTime': '2022-06-28 08:00:00', 'matchType': '早盘', 'odds': 1.59, 'oddsType': '1',
              'orderNo': 'XHwyHLmh696C', 'outcomeName': '是', 'specifier': '', 'tournamentName': '国际俱乐部俱乐部友谊赛'},
             {'awayTeamName': '厄瓜多尔', 'betScore': None, 'homeTeamName': '玻利维亚', 'marketName': '净胜球数',
              'matchTime': '2022-07-08 17:00:00', 'matchType': '早盘', 'odds': 9.75, 'oddsType': '1',
              'orderNo': 'XHwyK7qu88G3', 'outcomeName': '玻利维亚 1', 'specifier': 'variant=sr:winning_margin:3+',
              'tournamentName': '国际Copa America, Women'},
             {'awayTeamName': 'FK Ural Yekaterinburg', 'betScore': None, 'homeTeamName': 'CSKA Moscow',
              'marketName': '上半场 - 波胆', 'matchTime': '2022-07-16 08:00:00', 'matchType': '早盘', 'odds': 24.95,
              'oddsType': '1', 'orderNo': 'XHwyK7qu88G3', 'outcomeName': '2:1', 'specifier': '',
              'tournamentName': '俄罗斯足球超级联赛'},
             {'awayTeamName': 'Sao Paulo FC SP', 'betScore': None, 'homeTeamName': 'AC Goianiense GO',
              'marketName': '上半场 - AC Goianiense GO 不失球', 'matchTime': '2022-07-03 15:00:00', 'matchType': '早盘',
              'odds': 2.2, 'oddsType': '1', 'orderNo': 'XHwyK7qu88G3', 'outcomeName': '不是', 'specifier': '',
              'tournamentName': '巴西甲级联赛'},
             {'awayTeamName': 'FC Dallas', 'betScore': None, 'homeTeamName': 'Los Angeles FC',
              'marketName': 'Los Angeles FC 进球数', 'matchTime': '2022-06-29 22:30:00', 'matchType': '早盘', 'odds': 3.3,
              'oddsType': '1', 'orderNo': 'XHwyK7qu88G3', 'outcomeName': '2', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '美国职业足球大联盟'},
             {'awayTeamName': 'Kashima Antlers', 'betScore': None, 'homeTeamName': 'Kashiwa Reysol',
              'marketName': '最高进球数半场', 'matchTime': '2022-07-02 05:30:00', 'matchType': '早盘', 'odds': 3.45,
              'oddsType': '1', 'orderNo': 'XHwyK7qu88G3', 'outcomeName': '相同', 'specifier': '',
              'tournamentName': '日本J联赛'},
             {'awayTeamName': '图库曼体育会', 'betScore': None, 'homeTeamName': '沙士菲', 'marketName': '上半场 - 独赢 & 两队都进球',
              'matchTime': '2022-07-02 17:00:00', 'matchType': '早盘', 'odds': 25.95, 'oddsType': '1',
              'orderNo': 'XHwyLh9PsvZR', 'outcomeName': '沙士菲 & 是', 'specifier': '', 'tournamentName': '阿根廷足球甲级联赛'},
             {'awayTeamName': 'Lillestrom SK', 'betScore': None, 'homeTeamName': 'Kristiansund BK',
              'marketName': 'Kristiansund BK 赢任何半场', 'matchTime': '2022-07-03 12:00:00', 'matchType': '早盘',
              'odds': 1.52, 'oddsType': '1', 'orderNo': 'XHwyLh9PsvZR', 'outcomeName': '不是', 'specifier': '',
              'tournamentName': '挪威超级联赛'},
             {'awayTeamName': 'Undrid FF', 'betScore': None, 'homeTeamName': '鲁纳维克II', 'marketName': '平局退款',
              'matchTime': '2022-06-28 14:45:00', 'matchType': '早盘', 'odds': 1.31, 'oddsType': '1',
              'orderNo': 'XHwyLh9PsvZR', 'outcomeName': 'Undrid FF', 'specifier': '', 'tournamentName': '法罗群岛乙级联赛'},
             {'awayTeamName': 'Tegevajaro Miyazaki', 'betScore': None, 'homeTeamName': 'Iwaki FC',
              'marketName': 'Tegevajaro Miyazaki 进球数', 'matchTime': '2022-07-02 03:30:00', 'matchType': '早盘',
              'odds': 4.65, 'oddsType': '1', 'orderNo': 'XHwyLh9PsvZR', 'outcomeName': '2',
              'specifier': 'variant=sr:exact_goals:3+', 'tournamentName': '日本丙级联赛'},
             {'awayTeamName': 'RJ博塔弗戈', 'betScore': None, 'homeTeamName': 'Red Bull Bragantino SP',
              'marketName': 'Red Bull Bragantino SP 胜利退款', 'matchTime': '2022-07-04 19:00:00', 'matchType': '早盘',
              'odds': 1.59, 'oddsType': '1', 'orderNo': 'XHwyLh9PsvZR', 'outcomeName': '和局', 'specifier': '',
              'tournamentName': '巴西甲级联赛'},
             {'awayTeamName': 'FK Jerv', 'betScore': None, 'homeTeamName': '洛辛堡', 'marketName': '上半场 - 平局退款',
              'matchTime': '2022-07-10 12:00:00', 'matchType': '早盘', 'odds': 3.55, 'oddsType': '1',
              'orderNo': 'XHwyMHQRuWe3', 'outcomeName': '谢夫', 'specifier': '', 'tournamentName': '挪威超级联赛'},
             {'awayTeamName': 'CA Paranaense PR', 'betScore': None, 'homeTeamName': 'SE Palmeiras SP',
              'marketName': 'SE Palmeiras SP 进球数', 'matchTime': '2022-07-02 20:00:00', 'matchType': '早盘', 'odds': 5.75,
              'oddsType': '1', 'orderNo': 'XHwyMHQRuWe3', 'outcomeName': '0', 'specifier': 'variant=sr:exact_goals:3+',
              'tournamentName': '巴西甲级联赛'},
             {'awayTeamName': '加尔斯', 'betScore': None, 'homeTeamName': '灵多姆', 'marketName': '加尔斯 最高进球数半场',
              'matchTime': '2022-06-28 13:30:00', 'matchType': '早盘', 'odds': 2.13, 'oddsType': '1',
              'orderNo': 'XHwyMHQRuWe3', 'outcomeName': '下半场', 'specifier': '', 'tournamentName': '瑞典杯'},
             {'awayTeamName': '坦佩雷联', 'betScore': None, 'homeTeamName': 'KaaPo', 'marketName': '双重机会&两队都进球',
              'matchTime': '2022-06-28 12:00:00', 'matchType': '早盘', 'odds': 3.3, 'oddsType': '1',
              'orderNo': 'XHwyMHQRuWe3', 'outcomeName': 'KaaPo/和局 & 是', 'specifier': '', 'tournamentName': '芬兰乙级联赛，B组'},
             {'awayTeamName': 'Portland Timbers', 'betScore': None, 'homeTeamName': 'Nashville SC',
              'marketName': '上半场 - 独赢', 'matchTime': '2022-07-03 20:30:00', 'matchType': '早盘', 'odds': 2.45,
              'oddsType': '1', 'orderNo': 'XHwyMHQRuWe3', 'outcomeName': '纳什维尔SC', 'specifier': '',
              'tournamentName': '美国职业足球大联盟'}]


def order_no_new(yyds_list):


    # orderNo_list=[]
    count_i = 0
    count_j = 1
    count=0
    orderNo_list=[]
    for i in range(0, len(yyds_list)):
        print("i循环:",i,count_i)
        orderNo_tuple =[]
        if i==count_i:
            orderNo_tuple.append(yyds_list[i])
            for j in range(count_j, len(yyds_list)):
                print("j循环:",j,count_j)
                if j == count_j:
                    if yyds_list[i]['orderNo']==yyds_list[j]['orderNo']:
                        # orderNo_tuple.append(yyds_list[i])
                        orderNo_tuple.append(yyds_list[j])
                        print(yyds_list[i]['orderNo'],yyds_list[j]['orderNo'])
                        count_j = count_j + 1
                        count_i = count_i + 1
                        if j==len(yyds_list) - 1:
                            orderNo_list.append(orderNo_tuple)
                            print(f"第{count}次,{count_i},{count_j}")
                        else:
                            for k in range(count_j,len(yyds_list)):
                                print(yyds_list[i]['orderNo'],yyds_list[k]['orderNo'])
                                if yyds_list[i]['orderNo'] == yyds_list[k]['orderNo']:
                                    if k == len(yyds_list) - 1:
                                        count = count + 1
                                        count_j = count_j + 1
                                        count_i = count_i + 1
                                        orderNo_list.append(orderNo_tuple)
                                        print(f"第{count}次,{count_i},{count_j}")
                                    else:
                                        orderNo_tuple.append(yyds_list[k])
                                        count_j = count_j + 1
                                        count_i = count_i + 1
                                else:
                                    orderNo_list.append(orderNo_tuple)
                                    count_j = count_j + 1
                                    count_i = count_i + 1
                                    count = count + 1
                                    print(f"第{count}次,{count_i},{count_j}")
                                    break
                    else:
                        count_i = count_i + 1
                        count_j = count_j + 1
                        count=count+1
                        break
                else:
                    break
        else:
            continue

    print(orderNo_list)
    print(len(orderNo_list))
    return orderNo_list

new_orderNo_list=[]
orderNo_list=[]
def order_no_new02(yyds_list):
    for i in yyds_list:
        orderNo_tuple =[]
        if i['orderNo'] in orderNo_list:
            index_number=orderNo_list.index(i['orderNo'])
            new_orderNo_list[index_number].append(i)
        else:
            orderNo_list.append(i['orderNo'])
            orderNo_tuple.append(i)
            new_orderNo_list.append(orderNo_tuple)
    print(new_orderNo_list)
    print(len(new_orderNo_list))
    return new_orderNo_list
yyps=order_no_new02(yyds_list=yyds_list)


dict_AA={'account': 'd0d1d2d30c/fceshi02', 'betAmount': 150.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网', 'betMix': '', 'betResult': '未结算', 'betType': 3, 'bettingTime': '2022-06-27 08:15:10', 'companyPercentage': 0.2, 'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2, 'level3CommissionRatio': 0.0, 'level3Percentage': 0.2, 'memberCommissionRatio': 0.0, 'memberName': '杜鑫test账号ac', 'options': [{'awayTeamName': 'Viking FK', 'betScore': None, 'homeTeamName': 'Lillestrom SK', 'marketName': 'Viking FK 进球数', 'matchTimeStr': '2022-07-10 12:00:00', 'matchType': '早盘', 'odds': 8.15, 'oddsType': '1', 'orderNo': 'XHwDQTqFNQT7', 'outcomeName': '3+', 'specifier': 'variant=sr:exact_goals:3+', 'tournamentName': '挪威超级联赛'}, {'awayTeamName': '浙江', 'betScore': None, 'homeTeamName': '长春亚泰', 'marketName': '上半场 - 长春亚泰 大/小', 'matchTimeStr': '2022-06-29 07:30:00', 'matchType': '早盘', 'odds': 0.97, 'oddsType': '2', 'orderNo': 'XHwDQTqFNQT7', 'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '中国超级联赛'}, {'awayTeamName': '科帕沃古', 'betScore': None, 'homeTeamName': '约尔尼', 'marketName': '约尔尼 不失球获胜', 'matchTimeStr': '2022-06-30 14:30:00', 'matchType': '早盘', 'odds': 4.55, 'oddsType': '1', 'orderNo': 'XHwDQTqFNQT7', 'outcomeName': '是', 'specifier': '', 'tournamentName': '冰岛甲级联赛'}, {'awayTeamName': 'Odds BK', 'betScore': None, 'homeTeamName': 'Stroemsgodset IF', 'marketName': 'Odds BK 最高进球数半场', 'matchTimeStr': '2022-07-09 12:00:00', 'matchType': '早盘', 'odds': 3.55, 'oddsType': '1', 'orderNo': 'XHwDQTqFNQT7', 'outcomeName': '上半场', 'specifier': '', 'tournamentName': '挪威超级联赛'}, {'awayTeamName': 'Minnesota United FC', 'betScore': None, 'homeTeamName': 'Los Angeles Galaxy', 'marketName': 'Los Angeles Galaxy 赢任何半场', 'matchTimeStr': '2022-06-29 22:30:00', 'matchType': '早盘', 'odds': 2.55, 'oddsType': '1', 'orderNo': 'XHwDQTqFNQT7', 'outcomeName': '不是', 'specifier': '', 'tournamentName': '美国职业足球大联盟'}, {'awayTeamName': '爱媛', 'betScore': None, 'homeTeamName': '藤枝MYFC', 'marketName': '哪队进球', 'matchTimeStr': '2022-07-02 04:00:00', 'matchType': '早盘', 'odds': 3.55, 'oddsType': '1', 'orderNo': 'XHwDQTqFNQT7', 'outcomeName': '仅 藤枝MYFC', 'specifier': '', 'tournamentName': '日本丙级联赛'}], 'orderNo': 'XHwDQTqFNQT7', 'sportsType': '足球', 'Total_Amount': 160.0}
list_AA=[]
for key,value in dict_AA.items():
    list_AA.append(key)
print(f"\33[34m{list_AA}\33[0m")



ppyt={'account': 'd0d1d2d38y/fceshi0224', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网', 'betResult': '输', 'betTime': '2022-06-24 08:57:04', 'betType': '单注', 'level0Commission': 0.0, 'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3CommissionRatio': 0.0, 'level3Percentage': 0.2, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'memberCommission': 0.0, 'memberCommissionRatio': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号iy', 'odds': 1.69, 'oddsType': '1', 'options': [{'awayTeamName': '芹苴', 'betScore': None, 'homeTeamName': 'QNK广南足球俱乐部', 'marketName': '独赢', 'matchTime': '2022-06-25 06:00:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1', 'orderNo': 'XH4ydmPbRncK', 'outcomeName': 'QNK广南足球俱乐部', 'specifier': '', 'tournamentName': '越南职业足球乙级联赛'}], 'orderNo': 'XH4ydmPbRncK', 'settlementTime': '2022-06-25 08:01:45', 'sportId': 'sr:sport:1', 'sportType': '足球', 'validAmount': 10.0, 'winOrLose': -10.0}
print(len((ppyt['options'][0]).keys()))






# sort_num03=(('KPV科科拉', None, '图尔库', '上半场 - KPV科科拉 大/小', "datetime.datetime(2022, 6, 18, 8, 0)", '早盘', "Decimal('1.800'), 2, 'XFBaaCfa4EEt', '大0.5', 'total=0.5', '芬兰甲级联赛'), ('里本泰德', None, 'CA Paranaense PR', '双重机会', datetime.datetime(2022, 6, 28, 20, 30), '早盘', Decimal('2.040')", 1, 'XFBaaCfa4EEt', '和局或 里本泰德', '', '国际俱乐部解放者杯'), ('卢旺达爱国军', None, '警察(卢旺达)', '卢旺达爱国军 胜利退款', "datetime.datetime(2022, 6, 16, 9, 0)", '早盘', "Decimal('3.000')", 1, 'XFBaaCfa4EEt', '警察(卢旺达)', '', '卢旺达国家足球联赛'), ('Future FC', None, 'Enppi Club', '总入球', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('1.970')", 1, 'XFBaaCfa4EEt', '2-3', 'variant=sr:goal_range:7+', '埃及足球甲级联赛'), ('罗沙里奧中央', None, '沙士菲', '上半场 - 两队都进球', "datetime.datetime(2022, 6, 20, 18, 0)", '早盘', "Decimal('4.550')", 1, 'XFMvmSzEyMM9', '是', '', '阿根廷足球甲级联赛'), ('水原三星', None, 'Jeonbuk Hyundai Motors', '独赢 & 大/小', "datetime.datetime(2022, 6, 22, 6, 0)", '早盘', "Decimal('3.950')", 1, 'XFMvmSzEyMM9', '全北现代 & 小 2.5', 'total=2.5', '韩国K1联赛'), ('卡皮拉', None, '努尔米耶尔维', '上半场 - 大/小', "datetime.datetime(2022, 6, 18, 11, 0)", '早盘', "Decimal('2.310')", 1, 'XFMvmSzEyMM9', '大1.5', 'total=1.5', '芬兰乙级联赛，A组'), ('绿色古利', None, '南墨尔本', '南墨尔本 胜利退款', "datetime.datetime(2022, 6, 24, 5, 30)", '早盘', "Decimal('1.660')", 1, 'XFMvM9hrnt25', '和局', '', '澳大利亚全国超级联赛,维多利亚'), ('Nomme Kalju FC', None, '塔林弗罗拉', '上半场 - Nomme Kalju FC 不失球', "datetime.datetime(2022, 6, 19, 10, 15)", '早盘', "Decimal('1.540')", 1, 'XFMvM9hrnt25', '不是', '', '爱沙尼亚足球甲级联赛'), ('艾尔古纳', None, '马斯里足球俱乐部', '马斯里足球俱乐部 大/小', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('2.190')", 1, 'XFMvM9hrnt25', '大1.5', 'total=1.5', '埃及足球甲级联赛'), ('Orgryte IS', None, 'Jonkopings Sodra IF', 'Jonkopings Sodra IF 最高进球数半场', "datetime.datetime(2022, 6, 28, 13, 0)", '早盘', "Decimal('3.450')", 1, 'XFMvQKQsUhG5', '上半场', '', '瑞典超甲级联赛'))
# # 遍历options里的键值对，方便写入组装数据
# aa_list = []
# sport_report_list = [
#     {'account': 'd0d1d2d38y/fceshi0224', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网',
#      'betMix': '', 'betResult': '输', 'betTime': '2022-06-24 08:57:04', 'betType': '单注', 'level0Commission': 0.0,
#      'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level0Total': 2.0, 'level0WinOrLose': 2.0,
#      'level1Commission': 0.0, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level1Total': 2.0,
#      'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2,
#      'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3CommissionRatio': 0.0,
#      'level3Percentage': 0.2, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'memberCommission': 0.0,
#      'memberCommissionRatio': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号iy', 'odds': 1.69,
#      'oddsType': '1', 'options': [
#         {'awayTeamName': '芹苴', 'betScore': None, 'homeTeamName': 'QNK广南足球俱乐部', 'marketName': '独赢',
#          'matchTime': '2022-06-25 06:00:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1',
#          'orderNo': 'XH4ydmPbRncK', 'outcomeName': 'QNK广南足球俱乐部', 'specifier': '', 'tournamentName': '越南职业足球乙级联赛'}],
#      'orderNo': 'XH4ydmPbRncK', 'settlementTime': '2022-06-25 08:01:45', 'sportId': 'sr:sport:1', 'sportType': '足球',
#      'validAmount': 10.0, 'winOrLose': -10.0}]
#
# for key, value in sport_report_list[0]['options'][0].items():
#     aa_list.append(key)
# print(aa_list)
# type_list = ["<class 'str'>", "<class 'datetime.datetime'>", "<class 'NoneType'>", "<class 'int'>"]
#
# # 单独获取options列表的数据，然后组装回去
#
# options_list=[]
# print(len(sort_num03))
# for single in sort_num03:
#     jkk_dict = {}
#     for jkk in range(0, len(single)):
#         if str(type(single[jkk])) in type_list:
#             if single[jkk] == None:
#                 new_jkk = None
#             else:
#                 new_jkk = str(single[jkk])
#         else:
#             new_jkk = float(single[jkk])
#         jkk_dict[aa_list[jkk]] = new_jkk
#     options_list.append(jkk_dict)
# print(options_list)










# excel_report=['报表-球类报表-订单查询（根据其盘口查询订单）']
#
#
#
# print(excel_report[0])
#
# if excel_report[0]=='报表-球类报表-订单查询（根据其盘口查询订单）':
#     print("saassa")
# # if excel_report[0] in ['盈亏详情-登0-登3-会员-查看订单详情-子查询', '报表-球类报表-订单查询（根据其盘口查询订单)']:
# #     print("saassa")
# # else:
# #     print("不在里面")


sport_report_list = [
    {'account': 'd0d1d2d38y/fceshi0224', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网',
     'betMix': '', 'betResult': '输', 'betTime': '2022-06-24 08:57:04', 'betType': '单注', 'level0Commission': 0.0,
     'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level0Total': 2.0, 'level0WinOrLose': 2.0,
     'level1Commission': 0.0, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level1Total': 2.0,
     'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2,
     'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3CommissionRatio': 0.0,
     'level3Percentage': 0.2, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'memberCommission': 0.0,
     'memberCommissionRatio': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号iy', 'odds': 1.69,
     'oddsType': '1', 'options': [
        {'awayTeamName': '芹苴', 'betScore': None, 'homeTeamName': 'QNK广南足球俱乐部', 'marketName': '独赢',
         'matchTime': '2022-06-25 06:00:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1',
         'orderNo': 'XH4ydmPbRncK', 'outcomeName': 'QNK广南足球俱乐部', 'specifier': '', 'tournamentName': '越南职业足球乙级联赛'}],
     'orderNo': 'XH4ydmPbRncK', 'settlementTime': '2022-06-25 08:01:45', 'sportId': 'sr:sport:1', 'sportType': '足球',
     'validAmount': 10.0, 'winOrLose': -10.0}]


yylist=['1','2']
aa_list=[]
a=0
if a==0:
    aa_list=yylist
    print(aa_list)

#取key
# for key, value in sport_report_list[0].items():
#     aa_list.append(key)
# print(aa_list)





#不带底的颜色
print("\33[30m黑色\33[0m")
print("\33[31m红色\33[0m")
print("\33[32m绿色\33[0m")
print("\33[33m黄色\33[0m")
print("\33[34m蓝色\33[0m")
print("\33[35m紫色\33[0m")
print("\33[36m蓝绿色\33[0m")
#带底的颜色
print("\33[40m黄色\33[0m")
print("\33[41m黄色\33[0m")
print("\33[42m黄色\33[0m")
print("\33[43m黄色\33[0m")

data_match = [
    ['乒乓球', '2022-06-08 05:45:00', '滚球国际TT Cup Hiiemae, Andrus vs Perv, Indrek', 0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ['乒乓球', '2022-06-08 06:00:00', '滚球捷克Czech Liga Pro Kubat, Vladimir vs Reczai, Jiri', 0.0, 0.0, 0.0, 24.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ['乒乓球', '2022-06-08 06:00:00', '滚球国际TT Cup 马克西姆丘克, 伊戈尔 vs 阿赫拉莫夫, 塞尔吉', 0.0, 0.0, 14.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0],
    ['乒乓球', '2022-06-08 06:00:00', '滚球捷克Czech Liga Pro Kubat, Vladimir vs Reczai, Jiri', 0.0, 0.0, 13.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ['乒乓球', '2022-06-08 06:00:00', '滚球捷克Czech Liga Pro Kubat, Vladimir vs Reczai, Jiri', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     13.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

data_new_match=[]
match=[]
for i in data_match:
    if i[2] in match:
        index_num = match.index(i[2])
        for k in range(3, len(i)):
            number = i[k] + data_new_match[index_num][k]
            data_new_match[index_num][k]=number
    else:
        match.append(i[2])
        data_new_match.append(i)
print(data_new_match)
print(len(data_new_match))



# list_A=['滚球捷克Czech Liga Pro Kubat, Vladimir vs Reczai, Jiri','滚球捷克Czech Liga Pro Kubat, Vladimir vs Reczai, Jiri']
# if list_A[0]== list_A[1]:
#     print("等于")
# else:
#     print(type(list_A[0]),type(list_A[1]))




# #判断j是不是最后一个，通过增加count值，来判断是否结束循环
#     if j==data_match[-1]:
#         count=count+3
#     else:
#         count = count + 2




yybs=\
    {'account': 'd0d1d2d30c/fceshi02', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网', 'betResult': '未结算', 'betType': 2, 'bettingTime': '2022-06-27 08:44:19', 'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2, 'level3CommissionRatio': 0.0, 'level3Percentage': 0.2, 'memberCommissionRatio': 0.0, 'memberName': '杜鑫test账号ac', 'mixNum': '9_1_0', 'odds': 564.84, 'oddsType': '2', 'options': [{'awayTeamName': '莫尔德', 'betScore': None, 'homeTeamName': '汉坎', 'marketName': '汉坎 大/小', 'matchTimeStr': '2022-07-03 12:00:00', 'matchType': '早盘', 'odds': 1.3, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '挪威超级联赛'}, {'awayTeamName': 'Torino FC', 'betScore': None, 'homeTeamName': 'AC Monza', 'marketName': '上半场 - 让球', 'matchTimeStr': '2022-08-14 13:00:00', 'matchType': '早盘', 'odds': 1.02, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '蒙扎 ', 'specifier': 'hcp=0', 'tournamentName': '意大利甲级联赛'}, {'awayTeamName': '奥地利', 'betScore': None, 'homeTeamName': '英格兰', 'marketName': '奥地利 大/小', 'matchTimeStr': '2022-07-06 15:00:00', 'matchType': '早盘', 'odds': 1.11, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '国际欧洲锦标赛，女子'}, {'awayTeamName': '伊斯梅利', 'betScore': None, 'homeTeamName': '马哈拉加斯', 'marketName': '伊斯梅利 大/小', 'matchTimeStr': '2022-06-28 13:00:00', 'matchType': '早盘', 'odds': 0.42, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '大0.5', 'specifier': 'total=0.5', 'tournamentName': '埃及足球甲级联赛'}, {'awayTeamName': 'Lillestrom SK', 'betScore': None, 'homeTeamName': 'Kristiansund BK', 'marketName': '大/小', 'matchTimeStr': '2022-07-03 12:00:00', 'matchType': '早盘', 'odds': 1.14, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '大3', 'specifier': 'total=3', 'tournamentName': '挪威超级联赛'}, {'awayTeamName': '丹德农迅雷', 'betScore': None, 'homeTeamName': '埃文代尔', 'marketName': '埃文代尔 大/小', 'matchTimeStr': '2022-07-02 01:00:00', 'matchType': '早盘', 'odds': 0.48, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '澳大利亚全国超级联赛,维多利亚'}, {'awayTeamName': '海德堡联', 'betScore': None, 'homeTeamName': '墨尔本港鲨鱼', 'marketName': '让球', 'matchTimeStr': '2022-07-09 03:30:00', 'matchType': '早盘', 'odds': 1.19, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '墨尔本港鲨鱼 ', 'specifier': 'hcp=-0.75', 'tournamentName': '澳大利亚全国超级联赛,维多利亚'}, {'awayTeamName': '欧克莱卡诺', 'betScore': None, 'homeTeamName': '埃文代尔', 'marketName': '欧克莱卡诺 大/小', 'matchTimeStr': '2022-07-09 01:00:00', 'matchType': '早盘', 'odds': 1.5, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '澳大利亚全国超级联赛,维多利亚'}, {'awayTeamName': 'Odds BK', 'betScore': None, 'homeTeamName': 'Stroemsgodset IF', 'marketName': 'Odds BK 大/小', 'matchTimeStr': '2022-07-09 12:00:00', 'matchType': '早盘', 'odds': 1.34, 'oddsType': '2', 'orderNo': 'XHwPNuS9cRJz', 'outcomeName': '大1.5', 'specifier': 'total=1.5', 'tournamentName': '挪威超级联赛'}], 'orderNo': 'XHwPNuS9cRJz', 'sportsType': '足球', 'Total_Amount': 10.0}
print(len(yybs))
yyts=\
    {'account': 'd0d1d2d3ip/fceshi0475', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网', 'betResult': '未结算', 'betType': 1, 'bettingTime': '2022-06-24 08:53:15', 'level0CommissionRatio': 0.0021, 'level0Percentage': 0.2, 'level1CommissionRatio': 0.0021, 'level1Percentage': 0.2, 'level2CommissionRatio': 0.0021, 'level2Percentage': 0.2, 'level3CommissionRatio': 0.0021, 'level3Percentage': 0.2, 'memberCommissionRatio': 0.0011, 'memberName': '杜鑫test账号ip', 'mixNum': '杜鑫test账号ip', 'odds': 'XH4wUnpkJnPT', 'oddsType': '足球', 'options': 10.0}
print(len(yyts))
