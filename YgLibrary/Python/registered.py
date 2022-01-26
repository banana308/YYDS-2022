from selenium import webdriver
import time
import random
import datetime
import win32api
import win32con
from selenium.webdriver.common.keys import Keys




driver = webdriver.Chrome()
driver.implicitly_wait(10)




# 浏览器初始化
def stat01(driver):
    base_url = "http://192.168.10.120:2000/"
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    return

#代理登录
def login01(driver):
    username = "DuDuDuxin0005"
    password01 = "Bfty123456"
    password02 = "Bfty123456"
    name = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div[2]/div/div[1]/input")#输入账号
    name.send_keys(username)
    pw01 = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div[3]/div/div[1]/input")#输入密码
    pw01.send_keys(password01)
    pw02 = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/form/div[4]/div/div/input")#输入安全码
    pw02.send_keys(password02)
    Bottner = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/form/button")#点击登录
    Bottner.click()
    bbt = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/div")  # 点击用户管理
    bbt.click()
    print("登入成功"+"\n")
    yyt = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li")  # 点击会员管理
    yyt.click()
    time.sleep(1)
    return

#新增会员
def register(driver):
    global username,yy
    rtt = driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div[1]/div/button[2]")#点击新增会员
    rtt.click()
    Bottner = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/form/div[1]/div/div/div/input")#点击盘口类别
    Bottner.click()

    #选择盘口
    #num0=0
    #print(num0)
    if num0==0:
        opop01=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]")#选择A盘口
        opop01.click()
        yy="a"+"Du"
        time.sleep(1)
    if num0==1:
        opop02=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[2]/span")#选择B盘口
        opop02.click()
        yy="b"+"Du"
        time.sleep(1)
    if num0==2:
        opop03 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[3]")#选择C盘口
        opop03.click()
        yy="c"+"Du"
        time.sleep(1)
    if num0==3:
        opop04= driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[4]")#选择D盘口
        opop04.click()
        yy="d"+"Du"
        time.sleep(1)


    #选择账号和密码
    username ="FCeshi0"+str(i)
    designation="杜鑫余额浮动测试账号0"+str(i)
    password="Bfty123456"
    name=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/form/div[2]/div/div[1]/input")
    name.send_keys(username)
    name02=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/form/div[3]/div/div[1]/input")
    name02.send_keys(designation)
    pwd=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/form/div[4]/div/div[1]/input")
    pwd.send_keys(password)
    time.sleep(1)
    print("正在注册用户："+str(yy)+str(username))



    #选择占城数
    Account=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/div/div/input")
    Account.click()
    time.sleep(1)
    #根据自己的占成比定位
    num1 = random.randint(0,7)
    if num1==0:
        Account01=driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[1]")#5%占成
        Account01.click()
    if num1 == 1:
        Account02 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[2]")  # 6%占成
        Account02.click()
    if num1 == 2:
        Account03 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[3]")  # 7%占成
        Account03.click()
    if num1 == 3:
        Account04 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[4]")  # 8%占成
        Account04.click()
    if num1 == 4:
        Account05 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[5]")  # 9%占成
        Account05.click()
    if num1 == 5:
        Account06 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[6]")  # 10%占成
        Account06.click()
    if num1 == 6:
        Account07 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[7]")  # 11%占成
        Account07.click()
    if num1 == 7:
        Account08 = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[8]")  # 12%占成
        Account08.click()
    time.sleep(1)

    #输入RMB
    RMB=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/form/div[3]/div/div/div[2]/div/div/div/input")  # 输入RMB
    RMB.send_keys(money)
    return num0


#选择A盘口后的  返水和限额设置
def K_water_A(driver):
    #足球选择退水和限额
    bbp=driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[1]/div/div/div/div[3]")#点击退水和限额
    bbp.click()

    #A盘口-足球
    # 让球，大/小，单/双点击返水设定
    A_football01= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football01.click()
    #选择返水比例
    num2 = random.randint(0, 7)
    if num2==0:
        f_water01=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[1]")#选择比例18%
        f_water01.click()
    if num2 == 1:
        f_water02 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[2]")#选择比例17%
        f_water02.click()
    if num2 == 2:
        f_water03 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[3]")#选择比例16%
        f_water03.click()
    if num2 == 3:
        f_water04 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[4]")#选择比例14%
        f_water04.click()
    if num2 == 4:
        f_water05= driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[5]")#选择比例13%
        f_water05.click()
    if num2 == 5:
        f_water06 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[6]")#选择比例12%
        f_water06.click()
    if num2 == 6:
        f_water07 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[7]")#选择比例10%
        f_water07.click()
    if num2 == 7:
        f_water08 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[8]")#选择比例7%
        f_water08.click()
    time.sleep(1)

    # 让球，大/小，单/双 单场最高投注限额
    A_football02 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football02.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_football03= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football03.send_keys(money01)

    # 滚球让球，滚球大/小，单/双点击返水设定下拉框
    A_football001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football001.click()
    # 选择返水比例
    num3 = random.randint(0, 7)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[1]")#选择比例18%
        f_water001.click()
    if num3 == 1:
        f_water002 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[2]")#选择比例17%
        f_water002.click()
    if num3 == 2:
        f_water003 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[3]")#选择比例16%
        f_water003.click()
    if num3 == 3:
        f_water004 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[4]")#选择比例14%
        f_water004.click()
    if num3 == 4:
        f_water005 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[5]")#选择比例13%
        f_water005.click()
    if num3 == 5:
        f_water006 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[6]")#选择比例12%
        f_water006.click()
    if num3 == 6:
        f_water007 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[7]")#选择比例10%
        f_water007.click()
    if num3 == 7:
        f_water008 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[8]")#选择比例7%
        f_water008.click()
    time.sleep(1)
    #滚球让球，滚球大/小，单/双 单场最高投注限额
    A_football002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football002.send_keys(money01)
    #滚球让球，滚球大/小，单/双 单注最高投注限额
    A_football003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football003.send_keys(money01)

    # 独赢，滚球独赢 单场最高投注限额
    A_football0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_football0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_football00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_football00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football00003.send_keys(money01)

    # A盘口-篮球
    # 点击篮球模块
    A_basketball001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]")
    A_basketball001.click()


    #点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 7)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[1]")#选择比例18%
        f_water01.click()
    if num2 == 1:
        f_water02 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[2]")#选择比例17%
        f_water02.click()
    if num2 == 2:
        f_water03 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[3]")#选择比例16%
        f_water03.click()
    if num2 == 3:
        f_water04 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[4]")#选择比例14%
        f_water04.click()
    if num2 == 4:
        f_water05 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[5]")#选择比例13%
        f_water05.click()
    if num2 == 5:
        f_water06 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[6]")#选择比例12%
        f_water06.click()
    if num2 == 6:
        f_water07 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[7]")#选择比例10%
        f_water07.click()
    if num2 == 7:
        f_water08 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[8]")#选择比例7%
        f_water08.click()
    time.sleep(1)
    # 让球，大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath( "/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    ##点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_basketball0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0001.click()
    # 选择返水比例
    num3 = random.randint(0, 7)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[1]")#选择比例18%
        f_water001.click()
    if num3 == 1:
        f_water002 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[2]")#选择比例17%
        f_water002.click()
    if num3 == 2:
        f_water003 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[3]")#选择比例16%
        f_water003.click()
    if num3 == 3:
        f_water004 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[4]")#选择比例14%
        f_water004.click()
    if num3 == 4:
        f_water005 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[5]")#选择比例13%
        f_water005.click()
    if num3 == 5:
        f_water006 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[6]")#选择比例12%
        f_water006.click()
    if num3 == 6:
        f_water007 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[7]")#选择比例10%
        f_water007.click()
    if num3 == 7:
        f_water008 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[8]")#选择比例7%
        f_water008.click()
    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    #独赢，滚球独赢 单场最高投注限额
    A_basketball0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_basketball0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_basketball00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_basketball00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00003.send_keys(money01)

    # A盘口-其他
    # 点击其他模块
    A_other001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[3]")
    A_other001.click()

    # 点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 7)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[1]")#选择比例18%
        f_water01.click()
    if num2 == 1:
        f_water02 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[2]")#选择比例17%
        f_water02.click()
    if num2 == 2:
        f_water03 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[3]")#选择比例16%
        f_water03.click()
    if num2 == 3:
        f_water04 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[4]")#选择比例14%
        f_water04.click()
    if num2 == 4:
        f_water05 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[5]")#选择比例13%
        f_water05.click()
    if num2 == 5:
        f_water06 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[6]")#选择比例12%
        f_water06.click()
    if num2 == 6:
        f_water07 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[7]")#选择比例10%
        f_water07.click()
    if num2 == 7:
        f_water08 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[8]")#选择比例7%
        f_water08.click()
    time.sleep(1)
    #让球，大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    #让球，大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)

    #点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_other0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_other0001.click()
    # 选择返水比例
    num3 = random.randint(0, 7)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[1]")#选择比例18%
        f_water001.click()
    if num3 == 1:
        f_water002 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[2]")#选择比例17%
        f_water002.click()
    if num3 == 2:
        f_water003 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[3]")#选择比例16%
        f_water003.click()
    if num3 == 3:
        f_water004 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[4]")#选择比例14%
        f_water004.click()
    if num3 == 4:
        f_water005 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[5]")#选择比例13%
        f_water005.click()
    if num3 == 5:
        f_water006 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[6]")#选择比例12%
        f_water006.click()
    if num3 == 6:
        f_water007 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[7]")#选择比例10%
        f_water007.click()
    if num3 == 7:
        f_water008 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[8]")#选择比例7%
        f_water008.click()
    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)
    # 独赢，滚球独赢 单场最高投注限额
    A_other0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_other0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_other00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_other00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other00003.send_keys(money01)

    #点击确定
    yytt=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[1]/button[2]")
    yytt.click()
    aa = '注册成功'
    print("注册用户：" + str(yy) + str(username) + "  " + str(aa))
    time.sleep(5)

    # 写入text
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    path = "C:\\test\\registered.txt"
    f = open(path, mode="a")
    f.write(yy + username + "\n")
    time.sleep(1)
    return

#选择B盘口后的  返水和限额设置
def K_water_B(driver):
    #足球选择退水和限额
    bbp=driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[1]/div/div/div/div[3]")#点击退水和限额
    bbp.click()
    #A盘口-足球
    # 让球，大/小，单/双点击返水设定
    A_football01= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football01.click()
    #选择返水比例
    num2 = random.randint(0, 4)
    time.sleep(1)
    if num2==0:
        f_water01=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[1]")#选择比例14%
        f_water01.click()
    if num2 == 1:
        f_water02 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[2]")#选择比例13%
        f_water02.click()
    if num2 == 2:
        f_water03 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[3]")#选择比例12%
        f_water03.click()
    if num2 == 3:
        f_water04 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[4]")#选择比例10%
        f_water04.click()
    if num2 == 4:
        f_water05= driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[5]")#选择比例7%
        f_water05.click()
    time.sleep(1)

    # 让球，大/小，单/双 单场最高投注限额
    A_football02 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football02.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_football03= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football03.send_keys(money01)

    # 滚球让球，滚球大/小，单/双点击返水设定下拉框
    A_football001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football001.click()
    # 选择返水比例
    num3 = random.randint(0, 4)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[1]")#选择比例14%
        f_water001.click()
    if num3 == 1:
        f_water002 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[2]")#选择比例13%
        f_water002.click()
    if num3 == 2:
        f_water003 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[3]")#选择比例12%
        f_water003.click()
    if num3 == 3:
        f_water004 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[4]")#选择比例10%
        f_water004.click()
    if num3 == 4:
        f_water005 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[5]")#选择比例7%
        f_water005.click()
    time.sleep(1)
    #滚球让球，滚球大/小，单/双 单场最高投注限额
    A_football002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football002.send_keys(money01)
    #滚球让球，滚球大/小，单/双 单注最高投注限额
    A_football003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football003.send_keys(money01)

    # 独赢，滚球独赢 单场最高投注限额
    A_football0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_football0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_football00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_football00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football00003.send_keys(money01)

    # A盘口-篮球
    # 点击篮球模块
    A_basketball001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]")
    A_basketball001.click()


    #点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 4)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[1]")#选择比例14%
        f_water01.click()
    if num2 == 1:
        f_water02 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[2]")#选择比例13%
        f_water02.click()
    if num2 == 2:
        f_water03 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[3]")#选择比例12%
        f_water03.click()
    if num2 == 3:
        f_water04 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[4]")#选择比例10%
        f_water04.click()
    if num2 == 4:
        f_water05 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[5]")#选择比例7%
        f_water05.click()
    time.sleep(1)
    # 让球，大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath( "/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    ##点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_basketball0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0001.click()
    # 选择返水比例
    num3 = random.randint(0, 4)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[1]")#选择比例14%
        f_water001.click()
    if num3 == 1:
        f_water002 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[2]")#选择比例13%
        f_water002.click()
    if num3 == 2:
        f_water003 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[3]")#选择比例12%
        f_water003.click()
    if num3 == 3:
        f_water004 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[4]")#选择比例10%
        f_water004.click()
    if num3 == 4:
        f_water005 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[5]")#选择比例7%
        f_water005.click()
    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    #独赢，滚球独赢 单场最高投注限额
    A_basketball0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_basketball0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_basketball00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_basketball00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00003.send_keys(money01)

    # A盘口-其他
    # 点击其他模块
    A_other001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[3]")
    A_other001.click()

    # 点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 4)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[1]")#选择比例14%
        f_water01.click()
    if num2 == 1:
        f_water02 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[2]")#选择比例13%
        f_water02.click()
    if num2 == 2:
        f_water03 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[3]")#选择比例12%
        f_water03.click()
    if num2 == 3:
        f_water04 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[4]")#选择比例10%
        f_water04.click()
    if num2 == 4:
        f_water05 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[5]")#选择比例7%
        f_water05.click()
    time.sleep(1)
    #让球，大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    #让球，大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)

    #点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_other0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_other0001.click()
    # 选择返水比例
    num3 = random.randint(0, 4)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[1]")#选择比例14%
        f_water001.click()
    if num3 == 1:
        f_water002 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[2]")#选择比例13%
        f_water002.click()
    if num3 == 2:
        f_water003 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[3]")#选择比例12%
        f_water003.click()
    if num3 == 3:
        f_water004 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[4]")#选择比例10%
        f_water004.click()
    if num3 == 4:
        f_water005 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[5]")#选择比例7%
        f_water005.click()
    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)
    # 独赢，滚球独赢 单场最高投注限额
    A_other0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_other0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_other00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_other00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other00003.send_keys(money01)

    #点击确定
    yytt=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[1]/button[2]")
    yytt.click()
    aa = '注册成功'
    print("注册用户：" + str(yy) + str(username) + "  " + str(aa))
    time.sleep(5)

    # 写入text
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    path = "C:\\test\\registered.txt"
    f = open(path, mode="a")
    f.write(yy + username + "\n")
    time.sleep(1)
    return

#选择C盘口后的  返水和限额设置
def K_water_C(driver):
    #足球选择退水和限额
    bbp=driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[1]/div/div/div/div[3]")#点击退水和限额
    bbp.click()

    #A盘口-足球
    # 让球，大/小，单/双点击返水设定
    A_football01= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football01.click()
    #选择返水比例
    num2 = random.randint(0, 0)
    time.sleep(1)
    if num2==0:
        f_water01=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li")#选择比例7%
        f_water01.click()
    '''
    if num2 == 1:
        f_water02 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li")#选择比例17%
        f_water02.click()
    if num2 == 2:
        f_water03 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[3]")#选择比例16%
        f_water03.click()
    if num2 == 3:
        f_water04 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[4]")#选择比例14%
        f_water04.click()
    if num2 == 4:
        f_water05= driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[5]")#选择比例13%
        f_water05.click()
    if num2 == 5:
        f_water06 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[6]")#选择比例12%
        f_water06.click()
    if num2 == 6:
        f_water07 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[7]")#选择比例10%
        f_water07.click()
    if num2 == 7:
        f_water08 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[8]")#选择比例7%
        f_water08.click()
    '''
    time.sleep(1)

    # 让球，大/小，单/双 单场最高投注限额
    A_football02 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football02.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_football03= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football03.send_keys(money01)

    # 滚球让球，滚球大/小，单/双点击返水设定下拉框
    A_football001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football001.click()
    # time.sleep(3)
    # 选择返水比例
    num3 = random.randint(0, 0)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li")#选择比例7%
        f_water001.click()

    # if num3 == 1:
    #     f_water002 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water002.click()
    # if num3 == 2:
    #     f_water003 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water003.click()
    # if num3 == 3:
    #     f_water004 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water004.click()
    # if num3 == 4:
    #     f_water005 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water005.click()
    # if num3 == 5:
    #     f_water006 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water006.click()
    # if num3 == 6:
    #     f_water007 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water007.click()
    # if num3 == 7:
    #     f_water008 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water008.click()

    time.sleep(1)
    #滚球让球，滚球大/小，单/双 单场最高投注限额
    A_football002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football002.send_keys(money01)
    #滚球让球，滚球大/小，单/双 单注最高投注限额
    A_football003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football003.send_keys(money01)

    # 独赢，滚球独赢 单场最高投注限额
    A_football0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_football0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_football00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_football00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football00003.send_keys(money01)

    # A盘口-篮球
    # 点击篮球模块
    A_basketball001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]")
    A_basketball001.click()


    #点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 0)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li")#选择比例18%
        f_water01.click()

    # if num2 == 1:
    #     f_water02 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water02.click()
    # if num2 == 2:
    #     f_water03 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water03.click()
    # if num2 == 3:
    #     f_water04 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water04.click()
    # if num2 == 4:
    #     f_water05 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water05.click()
    # if num2 == 5:
    #     f_water06 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water06.click()
    # if num2 == 6:
    #     f_water07 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water07.click()
    # if num2 == 7:
    #     f_water08 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water08.click()

    time.sleep(1)
    # 让球，大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath( "/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    ##点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_basketball0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0001.click()
    # 选择返水比例
    num3 = random.randint(0, 0)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li")#选择比例18%
        f_water001.click()

    # if num3 == 1:
    #     f_water002 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water002.click()
    # if num3 == 2:
    #     f_water003 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water003.click()
    # if num3 == 3:
    #     f_water004 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water004.click()
    # if num3 == 4:
    #     f_water005 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water005.click()
    # if num3 == 5:
    #     f_water006 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water006.click()
    # if num3 == 6:
    #     f_water007 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water007.click()
    # if num3 == 7:
    #     f_water008 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water008.click()

    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    #独赢，滚球独赢 单场最高投注限额
    A_basketball0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_basketball0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_basketball00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_basketball00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00003.send_keys(money01)

    # A盘口-其他
    # 点击其他模块
    A_other001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[3]")
    A_other001.click()

    # 点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 0)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li")#选择比例18%
        f_water01.click()

    # if num2 == 1:
    #     f_water02 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water02.click()
    # if num2 == 2:
    #     f_water03 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water03.click()
    # if num2 == 3:
    #     f_water04 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water04.click()
    # if num2 == 4:
    #     f_water05 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water05.click()
    # if num2 == 5:
    #     f_water06 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water06.click()
    # if num2 == 6:
    #     f_water07 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water07.click()
    # if num2 == 7:
    #     f_water08 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water08.click()

    time.sleep(1)
    #让球，大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    #让球，大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)

    #点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_other0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_other0001.click()
    # 选择返水比例
    num3 = random.randint(0, 0)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li")#选择比例18%
        f_water001.click()

    # if num3 == 1:
    #     f_water002 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water002.click()
    # if num3 == 2:
    #     f_water003 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water003.click()
    # if num3 == 3:
    #     f_water004 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water004.click()
    # if num3 == 4:
    #     f_water005 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water005.click()
    # if num3 == 5:
    #     f_water006 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water006.click()
    # if num3 == 6:
    #     f_water007 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water007.click()
    # if num3 == 7:
    #     f_water008 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water008.click()

    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)
    # 独赢，滚球独赢 单场最高投注限额
    A_other0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_other0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_other00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_other00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other00003.send_keys(money01)

    #点击确定
    yytt=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[1]/button[2]")
    yytt.click()
    aa = '注册成功'
    print("注册用户：" + str(yy) + str(username) + "  " + str(aa))
    time.sleep(5)

    # 写入text
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    path = "C:\\test\\registered.txt"
    f = open(path, mode="a")
    f.write(yy + username + "\n")
    time.sleep(1)
    return

#选择D盘口后的  返水和限额设置
def K_water_D(driver):
    #足球选择退水和限额
    bbp=driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[1]/div/div/div/div[3]")#点击退水和限额
    bbp.click()

    #A盘口-足球
    # 让球，大/小，单/双点击返水设定
    A_football01= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football01.click()
    time.sleep(1)
    #选择返水比例
    time.sleep(1)
    num2 = random.randint(0, 0)
    if num2==0:
        f_water01=driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li")#选择比例7%
        f_water01.click()

    # if num2 == 1:
    #     f_water02 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li")#选择比例17%
    #     f_water02.click()
    # if num2 == 2:
    #     f_water03 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water03.click()
    # if num2 == 3:
    #     f_water04 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water04.click()
    # if num2 == 4:
    #     f_water05= driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water05.click()
    # if num2 == 5:
    #     f_water06 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water06.click()
    # if num2 == 6:
    #     f_water07 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water07.click()
    # if num2 == 7:
    #     f_water08 = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water08.click()

    time.sleep(1)

    # 让球，大/小，单/双 单场最高投注限额
    A_football02 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football02.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_football03= driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football03.send_keys(money01)

    # 滚球让球，滚球大/小，单/双点击返水设定下拉框
    A_football001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_football001.click()
    # 选择返水比例
    num3 = random.randint(0, 0)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li")#选择比例7%
        f_water001.click()

    # if num3 == 1:
    #     f_water002 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water002.click()
    # if num3 == 2:
    #     f_water003 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water003.click()
    # if num3 == 3:
    #     f_water004 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water004.click()
    # if num3 == 4:
    #     f_water005 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water005.click()
    # if num3 == 5:
    #     f_water006 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water006.click()
    # if num3 == 6:
    #     f_water007 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water007.click()
    # if num3 == 7:
    #     f_water008 = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water008.click()

    time.sleep(1)
    #滚球让球，滚球大/小，单/双 单场最高投注限额
    A_football002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football002.send_keys(money01)
    #滚球让球，滚球大/小，单/双 单注最高投注限额
    A_football003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_football003.send_keys(money01)

    # 独赢，滚球独赢 单场最高投注限额
    A_football0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_football0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_football00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_football00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_football00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_football00003.send_keys(money01)

    # A盘口-篮球
    # 点击篮球模块
    A_basketball001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]")
    A_basketball001.click()


    #点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 0)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li")#选择比例18%
        f_water01.click()

    # if num2 == 1:
    #     f_water02 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water02.click()
    # if num2 == 2:
    #     f_water03 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water03.click()
    # if num2 == 3:
    #     f_water04 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water04.click()
    # if num2 == 4:
    #     f_water05 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water05.click()
    # if num2 == 5:
    #     f_water06 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water06.click()
    # if num2 == 6:
    #     f_water07 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water07.click()
    # if num2 == 7:
    #     f_water08 = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water08.click()

    time.sleep(1)
    # 让球，大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath( "/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 让球，大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    ##点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_basketball0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0001.click()
    # 选择返水比例
    num3 = random.randint(0, 0)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li")#选择比例18%
        f_water001.click()

    # if num3 == 1:
    #     f_water002 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water002.click()
    # if num3 == 2:
    #     f_water003 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water003.click()
    # if num3 == 3:
    #     f_water004 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water004.click()
    # if num3 == 4:
    #     f_water005 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water005.click()
    # if num3 == 5:
    #     f_water006 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water006.click()
    # if num3 == 6:
    #     f_water007 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water007.click()
    # if num3 == 7:
    #     f_water008 = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water008.click()

    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_basketball002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_basketball003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_basketball003.send_keys(money01)

    #独赢，滚球独赢 单场最高投注限额
    A_basketball0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_basketball0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_basketball00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_basketball00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_basketball00003.send_keys(money01)

    # A盘口-其他
    # 点击其他模块
    A_other001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[3]")
    A_other001.click()

    # 点击让球，大/小，单/双 返水设定下拉框
    A_basketball0021 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_basketball0021.click()
    # 选择返水比例
    num2 = random.randint(0, 0)
    if num2 == 0:
        f_water01 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li")#选择比例18%
        f_water01.click()

    # if num2 == 1:
    #     f_water02 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water02.click()
    # if num2 == 2:
    #     f_water03 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water03.click()
    # if num2 == 3:
    #     f_water04 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water04.click()
    # if num2 == 4:
    #     f_water05 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water05.click()
    # if num2 == 5:
    #     f_water06 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water06.click()
    # if num2 == 6:
    #     f_water07 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water07.click()
    # if num2 == 7:
    #     f_water08 = driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water08.click()

    time.sleep(1)
    #让球，大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    #让球，大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[1]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)

    #点击滚球让球，滚球大/小，单/双 返水设定下拉框
    A_other0001 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div/div/input")
    A_other0001.click()
    # 选择返水比例
    num3 = random.randint(0, 0)
    if num3 == 0:
        f_water001 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li")#选择比例18%
        f_water001.click()

    # if num3 == 1:
    #     f_water002 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[2]")#选择比例17%
    #     f_water002.click()
    # if num3 == 2:
    #     f_water003 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[3]")#选择比例16%
    #     f_water003.click()
    # if num3 == 3:
    #     f_water004 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[4]")#选择比例14%
    #     f_water004.click()
    # if num3 == 4:
    #     f_water005 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[5]")#选择比例13%
    #     f_water005.click()
    # if num3 == 5:
    #     f_water006 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[6]")#选择比例12%
    #     f_water006.click()
    # if num3 == 6:
    #     f_water007 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[7]")#选择比例10%
    #     f_water007.click()
    # if num3 == 7:
    #     f_water008 = driver.find_element_by_xpath("/html/body/div[9]/div[1]/div[1]/ul/li[8]")#选择比例7%
    #     f_water008.click()

    time.sleep(1)
    # 滚球让球，滚球大/小，单/双 单场最高投注限额
    A_other002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other002.send_keys(money01)
    # 滚球让球，滚球大/小，单/双 单注最高投注限额
    A_other003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[1]/div[2]/div/form/div[3]/div/div/div[2]/div/div/div[1]/input")
    A_other003.send_keys(money01)
    # 独赢，滚球独赢 单场最高投注限额
    A_other0002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other0002.send_keys(money01)
    # 独赢，滚球独赢 单注最高投注限额
    A_other0003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other0003.send_keys(money01)

    # 其他玩法 单场最高投注限额
    A_other00002 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[1]/div/div/div[2]/div/div/div[1]/input")
    A_other00002.send_keys(money01)
    # 其他玩法 单注最高投注限额
    A_other00003 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[2]/div/div/div[2]/div/div/div[1]/input")
    A_other00003.send_keys(money01)

    #点击确定
    yytt=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/div[1]/button[2]")
    yytt.click()

    aa = '注册成功'
    print("注册用户：" + str(yy) + str(username) + "  " + str(aa))
    time.sleep(5)

    # 写入text
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    path = "C:\\test\\registered.txt"
    f = open(path, mode="a")
    f.write(yy + username + "\n")
    time.sleep(1)

    return

if __name__=='__main__':
    try:
        # i 注册账号数字变量
        for i in range(89,101):
            #选择盘口变量，来决定使用那个盘口的Ui框架
            num0 = random.randint(0, 3)

            # 通用信用额度设定
            money = "1000"
            # 通用投注限额设定
            money01 = "20000"

            if i==89:
                stat01(driver)
                login01(driver)
                register(driver)
                if num0 == 0:
                    K_water_A(driver)
                if num0 == 1:
                    K_water_B(driver)
                if num0 == 2:
                    K_water_C(driver)
                if num0 == 3:
                    K_water_D(driver)
            else:
                register(driver)
                if num0 == 0:
                    K_water_A(driver)
                if num0 == 1:
                    K_water_B(driver)
                if num0 == 2:
                    K_water_C(driver)
                if num0 == 3:
                    K_water_D(driver)
                if i==100:
                    driver.quit()
                    exit()
    except():
        driver.quit()
        exit()




