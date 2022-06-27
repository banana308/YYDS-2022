



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

sportId_sql_list=[]
sport_num_sql_list=[]
sort_num=[(('1531516017847869442', '0'),), (('1531517033355976705', '1'),), (('1531517351158390786', '2'),), (('1531517760300163074', '3'),)]

for sportId in sort_num:
    sportId_sql_list.append(sportId[0][0])
    sport_num_sql_list.append(sportId[0][1])
print(sportId_sql_list)
print(sport_num_sql_list)



del sportId_sql_list[0:2]
print(sportId_sql_list)





























def order_no():
    yyds_list=[{ 'betTime': '2022-06-16 23: 26: 42', 'orderNo': 'XFTztEQGVk9k', 'sportName': '足球', 'outcomeList': [
            { 'tournamentName': '模拟现实联盟K-League 1 SRL', 'TeamName': 'Gimcheon Sangmu (Srl)VsSuwon FC (Srl)', 'betScore': '(1: 0) ', 'marketName': '大/小', 'outcomeName': '大2.5/3', 'oddsType': 1, 'odds': 2.35, 'outcomeWinOrLoseName': '输'
            }
        ], 'betAmount': 100.0, 'profitAmount': -100.0, 'backwaterAmount': 0.0, 'resultAmount': 0.0
    },
    { 'betTime': '2022-06-16 23: 26: 42', 'orderNo': 'XFTztEQGVk9k', 'sportName': '足球', 'outcomeList': [
            { 'tournamentName': '模拟现实联盟K-League 1 SRL', 'TeamName': 'Pohang Steelers SRLVsGangwon FC SRL', 'betScore': '(4: 0) ', 'marketName': '大/小', 'outcomeName': '小2', 'oddsType': 1, 'odds': 2.42, 'outcomeWinOrLoseName': '赢'
            }
        ], 'betAmount': 100.0, 'profitAmount': -100.0, 'backwaterAmount': 0.0, 'resultAmount': 0.0
    },
               {'betTime': '2022-06-16 23: 26: 42', 'orderNo': 'XFTztEQGVk9k', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '模拟现实联盟K-League 1 SRL', 'TeamName': 'Pohang Steelers SRLVsGangwon FC SRL',
                    'betScore': '(4: 0) ', 'marketName': '大/小', 'outcomeName': '小2', 'oddsType': 1, 'odds': 2.42,
                    'outcomeWinOrLoseName': '赢'
                    }
               ], 'betAmount': 100.0, 'profitAmount': -100.0, 'backwaterAmount': 0.0, 'resultAmount': 0.0
                },
    { 'betTime': '2022-06-15 22: 26: 20', 'orderNo': 'YYYYYYYYSSSSS', 'sportName': '足球', 'outcomeList': [
            { 'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚', 'TeamName': 'Olympia Warriors HobartVs河岸奥林匹克', 'betScore': None, 'marketName': '双重机会&大/小', 'outcomeName': 'Olympia Warriors Hobart/河岸奥林匹克 & 大 3.5', 'oddsType': 1, 'odds': 2.06, 'outcomeWinOrLoseName': '输'
            }
        ], 'betAmount': 154.0, 'profitAmount': -154.0, 'backwaterAmount': 0.03, 'resultAmount': 0.03
    },
               {'betTime': '2022-06-16 23: 26: 42', 'orderNo': 'bbkkkkk', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '模拟现实联盟K-League 1 SRL', 'TeamName': 'Gimcheon Sangmu (Srl)VsSuwon FC (Srl)',
                    'betScore': '(1: 0) ', 'marketName': '大/小', 'outcomeName': '大2.5/3', 'oddsType': 1, 'odds': 2.35,
                    'outcomeWinOrLoseName': '输'
                    }
               ], 'betAmount': 100.0, 'profitAmount': -100.0, 'backwaterAmount': 0.0, 'resultAmount': 0.0
                },

               {'betTime': '2022-06-16 23: 26: 42', 'orderNo': 'bbkkkkk', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '模拟现实联盟K-League 1 SRL', 'TeamName': 'Pohang Steelers SRLVsGangwon FC SRL',
                    'betScore': '(4: 0) ', 'marketName': '大/小', 'outcomeName': '小2', 'oddsType': 1, 'odds': 2.42,
                    'outcomeWinOrLoseName': '赢'
                    }
               ], 'betAmount': 100.0, 'profitAmount': -100.0, 'backwaterAmount': 0.0, 'resultAmount': 0.0
                },

               {'betTime': '2022-06-16 23: 26: 42', 'orderNo': 'bbkkkkk', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '模拟现实联盟K-League 1 SRL', 'TeamName': 'Pohang Steelers SRLVsGangwon FC SRL',
                    'betScore': '(4: 0) ', 'marketName': '大/小', 'outcomeName': '小2', 'oddsType': 1, 'odds': 2.42,
                    'outcomeWinOrLoseName': '赢'
                    }
               ], 'betAmount': 100.0, 'profitAmount': -100.0, 'backwaterAmount': 0.0, 'resultAmount': 0.0
                },
               {'betTime': '2022-06-15 22: 26: 20', 'orderNo': '666666666666666', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚', 'TeamName': 'Olympia Warriors HobartVs河岸奥林匹克',
                    'betScore': None, 'marketName': '双重机会&大/小', 'outcomeName': 'Olympia Warriors Hobart/河岸奥林匹克 & 大 3.5',
                    'oddsType': 1, 'odds': 2.06, 'outcomeWinOrLoseName': '输'}], 'betAmount': 154.0,
                'profitAmount': -154.0, 'backwaterAmount': 0.03, 'resultAmount': 0.03},
               {'betTime': '2022-06-15 22: 26: 20', 'orderNo': '7777777777', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚', 'TeamName': 'Olympia Warriors HobartVs河岸奥林匹克',
                    'betScore': None, 'marketName': '双重机会&大/小', 'outcomeName': 'Olympia Warriors Hobart/河岸奥林匹克 & 大 3.5',
                    'oddsType': 1, 'odds': 2.06, 'outcomeWinOrLoseName': '输'}], 'betAmount': 154.0,
                'profitAmount': -154.0, 'backwaterAmount': 0.03, 'resultAmount': 0.03},
               {'betTime': '2022-06-15 22: 26: 20', 'orderNo': '9999', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚', 'TeamName': 'Olympia Warriors HobartVs河岸奥林匹克',
                    'betScore': None, 'marketName': '双重机会&大/小', 'outcomeName': 'Olympia Warriors Hobart/河岸奥林匹克 & 大 3.5',
                    'oddsType': 1, 'odds': 2.06, 'outcomeWinOrLoseName': '输'}], 'betAmount': 154.0,
                'profitAmount': -154.0, 'backwaterAmount': 0.03, 'resultAmount': 0.03},
               {'betTime': '2022-06-15 22: 26: 20', 'orderNo': '9999', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚', 'TeamName': 'Olympia Warriors HobartVs河岸奥林匹克',
                    'betScore': None, 'marketName': '双重机会&大/小', 'outcomeName': 'Olympia Warriors Hobart/河岸奥林匹克 & 大 3.5',
                    'oddsType': 1, 'odds': 2.06, 'outcomeWinOrLoseName': '输'}], 'betAmount': 154.0,
                'profitAmount': -154.0, 'backwaterAmount': 0.03, 'resultAmount': 0.03},
               {'betTime': '2022-06-15 22: 26: 20', 'orderNo': '1010', 'sportName': '足球', 'outcomeList': [
                   {'tournamentName': '澳大利亚全国超级联赛,塔斯马尼亚', 'TeamName': 'Olympia Warriors HobartVs河岸奥林匹克',
                    'betScore': None, 'marketName': '双重机会&大/小', 'outcomeName': 'Olympia Warriors Hobart/河岸奥林匹克 & 大 3.5',
                    'oddsType': 1, 'odds': 2.06, 'outcomeWinOrLoseName': '输'}], 'betAmount': 154.0,
                'profitAmount': -154.0, 'backwaterAmount': 0.03, 'resultAmount': 0.03}
               ]

    orderNo_list=[]
    new_list=[]
    count_i = 0
    count_j = 1
    count=0
    for i in range(0, len(yyds_list)):
        print("i循环:",i,count_i)
        if i==count_i:
            orderNo_list = []
            # if i==len(yyds_list)-1:
            new_list.append(yyds_list[i])
            for j in range(count_j, len(yyds_list)):
                print("j循环:",j,count_j)
                if j == count_j:
                    if yyds_list[i]['orderNo']==yyds_list[j]['orderNo']:
                        print(yyds_list[i]['orderNo'],yyds_list[j]['orderNo'])
                        orderNo_list.append(yyds_list[i]['outcomeList'][0])
                        orderNo_list.append(yyds_list[j]['outcomeList'][0])
                        count_j = count_j + 1
                        count_i = count_i + 1
                        if j==len(yyds_list) - 1:
                            new_list[-1]['outcomeList'] = orderNo_list
                            print(f"第{count}次,{count_i},{count_j}")
                        else:
                            for k in range(count_j,len(yyds_list)):
                                print(yyds_list[i]['orderNo'],yyds_list[k]['orderNo'])
                                if yyds_list[i]['orderNo'] == yyds_list[k]['orderNo']:
                                    if k == len(yyds_list) - 1:
                                        count = count + 1
                                        count_j = count_j + 1
                                        count_i = count_i + 1
                                        new_list[-1]['outcomeList'] = orderNo_list
                                        print(f"第{count}次,{count_i},{count_j}")
                                    else:
                                        orderNo_list.append(yyds_list[k]['outcomeList'][0])
                                        count_j = count_j + 1
                                        count_i = count_i + 1
                                else:
                                    new_list[-1]['outcomeList']=orderNo_list
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

    print(new_list)
    print(len(new_list))


















