



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





















# def order_no():
#     yyds_list=(('KPV科科拉', None, '图尔库', '上半场 - KPV科科拉 大/小', "datetime.datetime(2022, 6, 18, 8, 0)", '早盘', "Decimal('1.800'), 2, 'XFBaaCfa4EEt', '大0.5', 'total=0.5', '芬兰甲级联赛'), ('里本泰德', None, 'CA Paranaense PR', '双重机会', datetime.datetime(2022, 6, 28, 20, 30), '早盘', Decimal('2.040')", 1, 'XFBaaCfa4EEt', '和局或 里本泰德', '', '国际俱乐部解放者杯'), ('卢旺达爱国军', None, '警察(卢旺达)', '卢旺达爱国军 胜利退款', "datetime.datetime(2022, 6, 16, 9, 0)", '早盘', "Decimal('3.000')", 1, 'XFBaaCfa4EEt', '警察(卢旺达)', '', '卢旺达国家足球联赛'), ('Future FC', None, 'Enppi Club', '总入球', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('1.970')", 1, 'XFBaaCfa4EEt', '2-3', 'variant=sr:goal_range:7+', '埃及足球甲级联赛'), ('罗沙里奧中央', None, '沙士菲', '上半场 - 两队都进球', "datetime.datetime(2022, 6, 20, 18, 0)", '早盘', "Decimal('4.550')", 1, 'XFMvmSzEyMM9', '是', '', '阿根廷足球甲级联赛'), ('水原三星', None, 'Jeonbuk Hyundai Motors', '独赢 & 大/小', "datetime.datetime(2022, 6, 22, 6, 0)", '早盘', "Decimal('3.950')", 1, 'XFMvmSzEyMM9', '全北现代 & 小 2.5', 'total=2.5', '韩国K1联赛'), ('卡皮拉', None, '努尔米耶尔维', '上半场 - 大/小', "datetime.datetime(2022, 6, 18, 11, 0)", '早盘', "Decimal('2.310')", 1, 'XFMvmSzEyMM9', '大1.5', 'total=1.5', '芬兰乙级联赛，A组'), ('绿色古利', None, '南墨尔本', '南墨尔本 胜利退款', "datetime.datetime(2022, 6, 24, 5, 30)", '早盘', "Decimal('1.660')", 1, 'XFMvM9hrnt25', '和局', '', '澳大利亚全国超级联赛,维多利亚'), ('Nomme Kalju FC', None, '塔林弗罗拉', '上半场 - Nomme Kalju FC 不失球', "datetime.datetime(2022, 6, 19, 10, 15)", '早盘', "Decimal('1.540')", 1, 'XFMvM9hrnt25', '不是', '', '爱沙尼亚足球甲级联赛'), ('艾尔古纳', None, '马斯里足球俱乐部', '马斯里足球俱乐部 大/小', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('2.190')", 1, 'XFMvM9hrnt25', '大1.5', 'total=1.5', '埃及足球甲级联赛'), ('Orgryte IS', None, 'Jonkopings Sodra IF', 'Jonkopings Sodra IF 最高进球数半场', "datetime.datetime(2022, 6, 28, 13, 0)", '早盘', "Decimal('3.450')", 1, 'XFMvQKQsUhG5', '上半场', '', '瑞典超甲级联赛'))
#
#     orderNo_list=[]
#     new_list=[]
#     count_i = 0
#     count_j = 1
#     count=0
#     for i in range(0, len(yyds_list)):
#         print("i循环:",i,count_i)
#         if i==count_i:
#             orderNo_list = []
#             # if i==len(yyds_list)-1:
#             new_list.append(yyds_list[i])
#             for j in range(count_j, len(yyds_list)):
#                 print("j循环:",j,count_j)
#                 if j == count_j:
#                     if yyds_list[i]['orderNo']==yyds_list[j]['orderNo']:
#                         print(yyds_list[i]['orderNo'],yyds_list[j]['orderNo'])
#                         orderNo_list.append(yyds_list[i]['outcomeList'][0])
#                         orderNo_list.append(yyds_list[j]['outcomeList'][0])
#                         count_j = count_j + 1
#                         count_i = count_i + 1
#                         if j==len(yyds_list) - 1:
#                             new_list[-1]['outcomeList'] = orderNo_list
#                             print(f"第{count}次,{count_i},{count_j}")
#                         else:
#                             for k in range(count_j,len(yyds_list)):
#                                 print(yyds_list[i]['orderNo'],yyds_list[k]['orderNo'])
#                                 if yyds_list[i]['orderNo'] == yyds_list[k]['orderNo']:
#                                     if k == len(yyds_list) - 1:
#                                         count = count + 1
#                                         count_j = count_j + 1
#                                         count_i = count_i + 1
#                                         new_list[-1]['outcomeList'] = orderNo_list
#                                         print(f"第{count}次,{count_i},{count_j}")
#                                     else:
#                                         orderNo_list.append(yyds_list[k]['outcomeList'][0])
#                                         count_j = count_j + 1
#                                         count_i = count_i + 1
#                                 else:
#                                     new_list[-1]['outcomeList']=orderNo_list
#                                     count_j = count_j + 1
#                                     count_i = count_i + 1
#                                     count = count + 1
#                                     print(f"第{count}次,{count_i},{count_j}")
#                                     break
#                     else:
#                         count_i = count_i + 1
#                         count_j = count_j + 1
#                         count=count+1
#                         break
#                 else:
#                     break
#         else:
#             continue
#
#     print(new_list)
#     print(len(new_list))





def order_no_new(yyds_list):
    yyds_list=(('KPV科科拉', None, '图尔库', '上半场 - KPV科科拉 大/小', "datetime.datetime(2022, 6, 18, 8, 0)", '早盘', "Decimal('1.800'), 2, 'XFBaaCfa4EEt', '大0.5', 'total=0.5', '芬兰甲级联赛'), ('里本泰德', None, 'CA Paranaense PR', '双重机会', datetime.datetime(2022, 6, 28, 20, 30), '早盘', Decimal('2.040')", 1, 'XFBaaCfa4EEt', '和局或 里本泰德', '', '国际俱乐部解放者杯'), ('卢旺达爱国军', None, '警察(卢旺达)', '卢旺达爱国军 胜利退款', "datetime.datetime(2022, 6, 16, 9, 0)", '早盘', "Decimal('3.000')", 1, 'XFBaaCfa4EEt', '警察(卢旺达)', '', '卢旺达国家足球联赛'), ('Future FC', None, 'Enppi Club', '总入球', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('1.970')", 1, 'XFBaaCfa4EEt', '2-3', 'variant=sr:goal_range:7+', '埃及足球甲级联赛'), ('罗沙里奧中央', None, '沙士菲', '上半场 - 两队都进球', "datetime.datetime(2022, 6, 20, 18, 0)", '早盘', "Decimal('4.550')", 1, 'XFMvmSzEyMM9', '是', '', '阿根廷足球甲级联赛'), ('水原三星', None, 'Jeonbuk Hyundai Motors', '独赢 & 大/小', "datetime.datetime(2022, 6, 22, 6, 0)", '早盘', "Decimal('3.950')", 1, 'XFMvmSzEyMM9', '全北现代 & 小 2.5', 'total=2.5', '韩国K1联赛'), ('卡皮拉', None, '努尔米耶尔维', '上半场 - 大/小', "datetime.datetime(2022, 6, 18, 11, 0)", '早盘', "Decimal('2.310')", 1, 'XFMvmSzEyMM9', '大1.5', 'total=1.5', '芬兰乙级联赛，A组'), ('绿色古利', None, '南墨尔本', '南墨尔本 胜利退款', "datetime.datetime(2022, 6, 24, 5, 30)", '早盘', "Decimal('1.660')", 1, 'XFMvM9hrnt25', '和局', '', '澳大利亚全国超级联赛,维多利亚'), ('Nomme Kalju FC', None, '塔林弗罗拉', '上半场 - Nomme Kalju FC 不失球', "datetime.datetime(2022, 6, 19, 10, 15)", '早盘', "Decimal('1.540')", 1, 'XFMvM9hrnt25', '不是', '', '爱沙尼亚足球甲级联赛'), ('艾尔古纳', None, '马斯里足球俱乐部', '马斯里足球俱乐部 大/小', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('2.190')", 1, 'XFMvM9hrnt25', '大1.5', 'total=1.5', '埃及足球甲级联赛'), ('Orgryte IS', None, 'Jonkopings Sodra IF', 'Jonkopings Sodra IF 最高进球数半场', "datetime.datetime(2022, 6, 28, 13, 0)", '早盘', "Decimal('3.450')", 1, 'XFMvQKQsUhG5', '上半场', '', '瑞典超甲级联赛'))

    orderNo_list=[]
    new_list=[]
    count_i = 0
    count_j = 1
    count=0
    for i in range(0, len(yyds_list)):
        print("i循环:",i,count_i)
        orderNo_tuple = ()
        if i==count_i:
            # new_list.append(yyds_list[i])
            for j in range(count_j, len(yyds_list)):
                print("j循环:",j,count_j)
                if j == count_j:
                    # print(yyds_list[i][8],yyds_list[j][8])
                    if yyds_list[i][8]==yyds_list[j][8]:
                        orderNo_tuple = yyds_list[i]+ yyds_list[j]
                        print(yyds_list[i][8],yyds_list[j][8])
                        count_j = count_j + 1
                        count_i = count_i + 1
                        if j==len(yyds_list) - 1:
                            orderNo_list.append(orderNo_tuple)
                            print(f"第{count}次,{count_i},{count_j}")
                        else:
                            for k in range(count_j,len(yyds_list)):
                                print(yyds_list[i][8],yyds_list[k][8])
                                if yyds_list[i][8] == yyds_list[k][8]:
                                    if k == len(yyds_list) - 1:
                                        count = count + 1
                                        count_j = count_j + 1
                                        count_i = count_i + 1
                                        orderNo_list.append(orderNo_tuple)
                                        print(f"第{count}次,{count_i},{count_j}")
                                    else:
                                        orderNo_tuple=orderNo_tuple+yyds_list[k]
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


# dict_AA=\
#     {'account': 'd0d1d2d38y/fceshi0224', 'betAmount': 10.0, 'betIp': '192.168.10.120', 'betIpAddress': '局域网', 'betMix': '', 'betResult': '输', 'betTime': '2022-06-24 08:57:04', 'betType': '单注', 'level0Commission': 0.0, 'level0CommissionRatio': 0.0, 'level0Percentage': 0.2, 'level0Total': 2.0, 'level0WinOrLose': 2.0, 'level1Commission': 0.0, 'level1CommissionRatio': 0.0, 'level1Percentage': 0.2, 'level1Total': 2.0, 'level1WinOrLose': 2.0, 'level2Commission': 0.0, 'level2CommissionRatio': 0.0, 'level2Percentage': 0.2, 'level2Total': 2.0, 'level2WinOrLose': 2.0, 'level3Commission': 0.0, 'level3CommissionRatio': 0.0, 'level3Percentage': 0.2, 'level3Total': 2.0, 'level3WinOrLose': 2.0, 'memberCommission': 0.0, 'memberCommissionRatio': 0.0, 'memberTotal': -10.0, 'memberWinOrLose': -10.0, 'name': '杜鑫test账号iy', 'odds': 1.69, 'oddsType': '1', 'options': [{'awayTeamName': '芹苴', 'betScore': None, 'homeTeamName': 'QNK广南足球俱乐部', 'marketName': '独赢', 'matchTime': '2022-06-25 06:00:00', 'matchType': '早盘', 'odds': 1.69, 'oddsType': '1', 'orderNo': 'XH4ydmPbRncK', 'outcomeName': 'QNK广南足球俱乐部', 'specifier': '', 'tournamentName': '越南职业足球乙级联赛'}], 'orderNo': 'XH4ydmPbRncK', 'settlementTime': '2022-06-25 08:01:45', 'sportId': 'sr:sport:1', 'sportType': '足球', 'validAmount': 10.0, 'winOrLose': -10.0}
# list_AA=[]
# for key,value in dict_AA.items():
#     list_AA.append(key)
# print(list_AA)







sort_num03=(('KPV科科拉', None, '图尔库', '上半场 - KPV科科拉 大/小', "datetime.datetime(2022, 6, 18, 8, 0)", '早盘', "Decimal('1.800'), 2, 'XFBaaCfa4EEt', '大0.5', 'total=0.5', '芬兰甲级联赛'), ('里本泰德', None, 'CA Paranaense PR', '双重机会', datetime.datetime(2022, 6, 28, 20, 30), '早盘', Decimal('2.040')", 1, 'XFBaaCfa4EEt', '和局或 里本泰德', '', '国际俱乐部解放者杯'), ('卢旺达爱国军', None, '警察(卢旺达)', '卢旺达爱国军 胜利退款', "datetime.datetime(2022, 6, 16, 9, 0)", '早盘', "Decimal('3.000')", 1, 'XFBaaCfa4EEt', '警察(卢旺达)', '', '卢旺达国家足球联赛'), ('Future FC', None, 'Enppi Club', '总入球', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('1.970')", 1, 'XFBaaCfa4EEt', '2-3', 'variant=sr:goal_range:7+', '埃及足球甲级联赛'), ('罗沙里奧中央', None, '沙士菲', '上半场 - 两队都进球', "datetime.datetime(2022, 6, 20, 18, 0)", '早盘', "Decimal('4.550')", 1, 'XFMvmSzEyMM9', '是', '', '阿根廷足球甲级联赛'), ('水原三星', None, 'Jeonbuk Hyundai Motors', '独赢 & 大/小', "datetime.datetime(2022, 6, 22, 6, 0)", '早盘', "Decimal('3.950')", 1, 'XFMvmSzEyMM9', '全北现代 & 小 2.5', 'total=2.5', '韩国K1联赛'), ('卡皮拉', None, '努尔米耶尔维', '上半场 - 大/小', "datetime.datetime(2022, 6, 18, 11, 0)", '早盘', "Decimal('2.310')", 1, 'XFMvmSzEyMM9', '大1.5', 'total=1.5', '芬兰乙级联赛，A组'), ('绿色古利', None, '南墨尔本', '南墨尔本 胜利退款', "datetime.datetime(2022, 6, 24, 5, 30)", '早盘', "Decimal('1.660')", 1, 'XFMvM9hrnt25', '和局', '', '澳大利亚全国超级联赛,维多利亚'), ('Nomme Kalju FC', None, '塔林弗罗拉', '上半场 - Nomme Kalju FC 不失球', "datetime.datetime(2022, 6, 19, 10, 15)", '早盘', "Decimal('1.540')", 1, 'XFMvM9hrnt25', '不是', '', '爱沙尼亚足球甲级联赛'), ('艾尔古纳', None, '马斯里足球俱乐部', '马斯里足球俱乐部 大/小', "datetime.datetime(2022, 6, 18, 13, 0)", '早盘', "Decimal('2.190')", 1, 'XFMvM9hrnt25', '大1.5', 'total=1.5', '埃及足球甲级联赛'), ('Orgryte IS', None, 'Jonkopings Sodra IF', 'Jonkopings Sodra IF 最高进球数半场', "datetime.datetime(2022, 6, 28, 13, 0)", '早盘', "Decimal('3.450')", 1, 'XFMvQKQsUhG5', '上半场', '', '瑞典超甲级联赛'))


# 遍历options里的键值对，方便写入组装数据
aa_list = []
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

for key, value in sport_report_list[0]['options'][0].items():
    aa_list.append(key)
print(aa_list)
type_list = ["<class 'str'>", "<class 'datetime.datetime'>", "<class 'NoneType'>", "<class 'int'>"]

# 单独获取options列表的数据，然后组装回去
jkk_list = []
jkk_dict = {}
options_list=[]
print(len(sort_num03))
for single in sort_num03:
    for jkk in range(0, len(single)):
        if str(type(single[jkk])) in type_list:
            if single[jkk] == None:
                new_jkk = None
            else:
                new_jkk = str(single[jkk])
        else:
            new_jkk = float(single[jkk])
        jkk_dict[aa_list[jkk]] = new_jkk
    jkk_list.append(jkk_dict)
    options_list.append(jkk_list)
print(options_list)










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




















