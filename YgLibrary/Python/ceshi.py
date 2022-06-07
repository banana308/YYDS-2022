import datetime
import time



# list_A=['8','7','101','10','9','11','100']

# list_y=[]
# list01=[]
# #写入text
# path = "C:\\test\\michid.txt"
# f = open(path, mode="r")
# lines=f.readlines()
# for lines in lines:
#     list_y.append(lines.strip('\n'))
#     for k in range(0,len(list_y)):
#         if  list_y[k] in list01:
#             pass
#         else:
#             list01.append(list_y[k])
# print(len(list01))
# print(list01)


# for i in range(0,len(order_no02)):
#     if order_no02[i] in order_no01:
#         order_no01.remove(order_no02[i])
#     else:
#         pass
# print(len(order_no01))
# print(order_no01)
# ['XgPLKTrmDbMh', 'XgPLMKw4QUg5', 'XgPLNg4MK3Gu', 'XgPLNgsJtu4V', 'XgPLPetGNzSP']



# list=[]
# for i in range(1,1001):
#     name = "fceshi0" + str(i)
#     # name="sr:match:27885276"
#     # name="6210"
#     # path01 = "C:\\test\\test_jmeter\\matchId.txt"
#     path01 = "C:\\test\正式版\\user.txt"
#     f = open(path01, 'a')
#     f.write( name+ "\n")
#     list.append(name)
#     if i==1000:
#         print(len(list))
#     else:
#         pass



# lsit = [2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0, len(lsit) - 1):
#     a = sum(lsit[0:i])
#     b = sum(lsit[0:(i + 1)])
#
#     print(a, b, " ", str(lsit[i]), "串1")



# def get_time(number):
#     for number in range(number, 0, -1):
#         time.sleep(1)
#         print(number,"秒",end=" end")
#
#
# get_time(15)


all_user_old=[{},{},{},{}]

userName_list=['yy01','yy02','yy03','yy04',]
psd_list=['yy01','yy02','yy03','yy04',]

for i in range(0,4):
    all_user_old[i][f'登{i}的账号']=userName_list[i]
    all_user_old[i][f'登{i}的密码'] = psd_list[i]
    print(all_user_old[i])

print(all_user_old)











# list=['XfL2iMdzsph8', 'XfL2j2Ydpbwe', 'XfL2jgUUqwdX', 'XfL2jvN4GaeV', 'XfL2jKeJPJjD', 'XfL2jWW4g645', 'XfL2keq5S3B9', 'XfL2ks57jXAQ', 'XfL2kF9c7zQd', 'XfL2mCpAFQjE', 'XfL2mRsS6tWp', 'XfL2n6x9Mewd', 'XfL2nhZi6J5F', 'XfL2nxtUhLxV', 'XfL2nKrYQmr7', 'XfL2nVB26kAz', 'XfL2p8YMWThh', 'XfL2pidqLuZ8', 'XfL2pvRaSGpZ', 'XfL2pHJbakrY', 'XfL2pUJSnP2i', 'XfL2qaJbZM8Z', 'XfL2qkhdkGWB', 'XfL2qybJeSYL', 'XfL2qL48Y99D', 'XfL2qWqKbeqh', 'XfL2r7rjY5m7', 'XfL2rfAiNatf', 'XfL2rsmacZ5c', 'XfL2rCTXVB8H', 'XfL2rN7KjPzS', 'XfL2sMVs2BhQ', 'XfL2tkujJXcM', 'XfL2tCkG42Ge', 'XfL2tSitdfBi', 'XfL2u3MATvjS', 'XfL2ucMntxUv', 'XfL2umfnyBug', 'XfL2uwDrmgnr', 'XfL2uEYSZs37', 'XfL2uX86cw7Q', 'XfL2v7MxrjBG', 'XfL2vq9dZubz', 'XfL2vBJBnMYz', 'XfL2vNryBAjz', 'XfL2w22Wm8pV', 'XfL2wjap4UAz', 'XfL2wwijcP2J', 'XfL2wLvtVjSq', 'XfL2wVjPGNGc', 'XfL2x7ySJjaK', 'XfL2xjkvWFbY', 'XfL2xuk4wvaq', 'XfL2xGSUwPmj', 'XfL2xXiuw2k7', 'XfL2ybTvQxvu', 'XfL2yqaPjGrD', 'XfL2yBZyfn4a', 'XfL2yP9tb7Q7', 'XfL2yYqTPNKc', 'XfL2z99GA6Bf', 'XfL2zhSAjcUM', 'XfL2zt4evFkD', 'XfL2zDFNcjwY', 'XfL2zNvYjyn6', 'XfL2A2aMQGKq', 'XfL2Ad3HHiQC', 'XfL2AqxSurL7', 'XfL2ABKzemCT', 'XfL2AQMKhNga', 'XfL2B4QqZLpG', 'XfL2BgCRWCvD', 'XfL2Bup7rpzi', 'XfL2BJatHLgF', 'XfL2BVYn7mGY', 'XfL2C8TazyPr', 'XfL2CjJbY88d', 'XfL2CxhnNxHL', 'XfL2CKbiVNSg', 'XfL2CVDDJVk3', 'XfL2D7tAU6wM', 'XfL2Dj5LbtCP', 'XfL2DwpRhchK', 'XfL2DGvhfBE3', 'XfL2DSpZaJgU', 'XfL2E53qTkML', 'XfL2EgT9sWkL', 'XfL2EuJ5t66Z', 'XfL2EFncpqRc', 'XfL2ESztAzxL', 'XfL2F4yK37YG', 'XfL2FefEfSej', 'XfL2FpneCV9r', 'XfL2FxsM7eVa', 'XfL2FFW5a2dE', 'XfL2FQRfgxX5', 'XfL2FZnmFqfs', 'XfL2G9KzGiLn', 'XfL2GhddR2Zu', 'XfL2GrmB6NrU']
# lsit01=['XfL2iMdzsph8', 'XfL2j2Ydpbwe', 'XfL2jgUUqwdX', 'XfL2jvN4GaeV', 'XfL2jKeJPJjD', 'XfL2jWW4g645', 'XfL2keq5S3B9', 'XfL2ks57jXAQ', 'XfL2kF9c7zQd', 'XfL2mCpAFQjE', 'XfL2mRsS6tWp', 'XfL2n6x9Mewd', 'XfL2nhZi6J5F', 'XfL2nxtUhLxV', 'XfL2nKrYQmr7', 'XfL2nVB26kAz', 'XfL2p8YMWThh', 'XfL2pidqLuZ8', 'XfL2pvRaSGpZ', 'XfL2pHJbakrY', 'XfL2pUJSnP2i', 'XfL2qaJbZM8Z', 'XfL2qkhdkGWB', 'XfL2qybJeSYL', 'XfL2qL48Y99D', 'XfL2qWqKbeqh', 'XfL2r7rjY5m7', 'XfL2rfAiNatf', 'XfL2rsmacZ5c']
#
# for i in range(0,len(lsit01)):
#     if lsit01[i] in list:
#         list.remove(lsit01[i])
#     else:
#         pass
# print(len(list))
# print(list)





# list=["1","2","3","4","5","6",]




from concurrent.futures import ThreadPoolExecutor
import time

# def spider(page):
#     time.sleep(page)
#     print(f"crawl task{page} finished")
#     return page
#
# with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大容纳数量为5的线程池
#         task1 = t.submit(spider, 1)
#         task2 = t.submit(spider, 2)  # 通过submit提交执行的函数到线程池中
#         task3 = t.submit(spider, 3)
#
#         print(f"task1: {task1.done()}")  # 通过done来判断线程是否完成
#         print(f"task2: {task2.done()}")
#         print(f"task3: {task3.done()}")
#
#         time.sleep(5)
#         print(f"task1: {task1.done()}")
#         print(f"task2: {task2.done()}")
#         print(f"task3: {task3.done()}")
#         print(task1.result())  # 通过result来获取返回值

# # num_lsit = ["复式3串4": [2_3, 3_4],"复式4串11": {[2_6, 3_4, 4_11]},"复式5串26": {[2_10, 3_10, 4_5, 5_26]},"复式6串57": {[2_15, 3_20, 4_15,5_6,6_57]}]
num_lsit = [{"复式3串4":["2_3_0","3_4_1"]},{"复式4串11":["2_6_0","3_4_0","4_11_1"]},{"复式5串25": ["2_10_0", "3_10_0", "4_5_0", "5_26_1"]},{"复式6串57": ["2_15_0", "3_20_0", "4_15_0","5_6_0","6_57_1"]}]




# # a=(num_lsit[0])['复式'][0]
#
# # print(list((num_lsit[0])['复式'][0]))
# print(list(list((num_lsit[1]).values())[0][2])[2])
# print(list(list((num_lsit[1]).values())[0][2])[3])
# a=f"{(str((list(list((num_lsit[1]).values())[0][2])[2])))}{str((list(list((num_lsit[1]).values())[0][2])[3]))}"
# print(str((list(list((num_lsit[1]).values())[0][2])[2]))+str((list(list((num_lsit[1]).values())[0][2])[3])))
# print(a)



# kk_lsit=[('sr:match:33294097_236_quarternr=1|total=51.5_12',), ('sr:match:33703537_757_quarternr=1|total=20.5_12',)]
# outcomeId = kk_lsit[1][0]
# print(outcomeId)


# print(len(num_lsit))