from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
driver.implicitly_wait(10)


num=['bDuFCeshi01', 'aDuFCeshi02', 'bDuFCeshi03', 'cDuFCeshi04', 'dDuFCeshi05', 'cDuFCeshi06', 'aDuFCeshi07', 'cDuFCeshi08', 'bDuFCeshi09', 'bDuFCeshi010', 'cDuFCeshi011', 'dDuFCeshi012', 'cDuFCeshi013', 'dDuFCeshi014', 'bDuFCeshi015', 'dDuFCeshi016', 'cDuFCeshi017', 'bDuFCeshi018', 'aDuFCeshi019', 'bDuFCeshi020', 'aDuFCeshi021', 'bDuFCeshi022', 'dDuFCeshi023', 'dDuFCeshi024', 'aDuFCeshi025', 'aDuFCeshi026', 'bDuFCeshi027', 'cDuFCeshi028', 'cDuFCeshi029', 'dDuFCeshi030', 'bDuFCeshi031', 'aDuFCeshi032', 'aDuFCeshi033', 'aDuFCeshi034', 'dDuFCeshi035', 'dDuFCeshi036', 'cDuFCeshi037', 'aDuFCeshi038', 'dDuFCeshi039', 'cDuFCeshi040', 'aDuFCeshi041', 'cDuFCeshi042', 'aDuFCeshi043', 'dDuFCeshi044', 'cDuFCeshi045', 'bDuFCeshi046', 'cDuFCeshi047', 'cDuFCeshi048', 'bDuFCeshi049', 'bDuFCeshi050', 'aDuFCeshi051', 'aDuFCeshi052', 'cDuFCeshi053', 'bDuFCeshi054', 'dDuFCeshi055', 'cDuFCeshi056', 'cDuFCeshi057', 'dDuFCeshi058', 'dDuFCeshi059', 'bDuFCeshi060', 'cDuFCeshi061', 'cDuFCeshi062', 'bDuFCeshi063', 'bDuFCeshi064', 'aDuFCeshi065', 'bDuFCeshi066', 'dDuFCeshi067', 'cDuFCeshi068', 'aDuFCeshi069', 'aDuFCeshi070', 'aDuFCeshi071', 'cDuFCeshi072', 'cDuFCeshi073', 'dDuFCeshi074', 'dDuFCeshi075', 'dDuFCeshi076', 'dDuFCeshi077', 'bDuFCeshi078', 'cDuFCeshi079', 'dDuFCeshi080', 'cDuFCeshi081', 'cDuFCeshi082', 'dDuFCeshi083', 'aDuFCeshi084', 'dDuFCeshi085', 'bDuFCeshi086', 'aDuFCeshi087', 'aDuFCeshi088', 'dDuFCeshi089', 'aDuFCeshi090', 'cDuFCeshi091', 'bDuFCeshi092', 'dDuFCeshi093', 'dDuFCeshi094', 'cDuFCeshi095', 'cDuFCeshi096', 'aDuFCeshi097', 'dDuFCeshi098', 'bDuFCeshi099', 'bDuFCeshi0100']

list = []
# 写入text
path = "C:\\test\\registered.txt"
f = open(path, mode="r")
lines = f.readlines()
for lines in lines:
    list.append(lines.strip('\n'))


# 浏览器初始化
def stat(driver):
    base_url = "http://192.168.10.120:96/"
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    return

# 登录
def login(driver):
    global username01,watera
    # i转化为字符串，方便变量叠加
    username01 =num[i]
    # time.sleep(2)
    print("取值成功："+str(username01))
    password01 ="Bfty123456"
    name = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form[1]/div[1]/div/div/input")#输入账号
    #name.clear()
    name.send_keys(username01)
    time.sleep(1)
    pw01 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form[1]/div[2]/div/div/input")#输入密码
    pw01.clear()
    time.sleep(1)
    pw01.send_keys(password01)
    Bottner = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form[1]/div[3]/div/div/button")#点击登录
    Bottner.click()
    time.sleep(7)
    print(username01+"登入成功")
    return username01

def alter01_name(driver):
    # i转化为字符串，方便变量叠加
    username = "FCeshi0" + str(i+1)
    name = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form/div[1]/div/div[1]/input")  # 输入账号
    name.send_keys(username)
    Bottner = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form/div[2]/div/div/button[2]")  # 点击提交
    Bottner.click()
    time.sleep(3)
    print(username01+"输入新登账号:" +username+"成功")

def alter01_password(driver):
    password = "Bfty123456"
    password01 = "Bfty123456"
    password02 = "Bfty123456"
    pwd = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/input")#当前密码
    pwd.send_keys(password)
    pwd01 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form/div[4]/div/div[1]/input")#新密码
    pwd01.send_keys(password01)
    pwd02 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form/div[6]/div/div[1]/input")#确认密码
    pwd02.send_keys(password02)
    Bottner = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/form/div[7]/div/div/button[2]")  #点击提交
    Bottner.click()
    time.sleep(5)
    print(username01+"修改密码成功" + "\n")


if __name__=='__main__':
    try:
        global i
        # i 注册账号数字变量
        for i in range(60,len(num)):
            print(i)
            if i==60:
                stat(driver)
                login(driver)
                alter01_name(driver)
                alter01_password(driver)
            else:
                login(driver)
                alter01_name(driver)
                alter01_password(driver)
                if i==len(num):
                    driver.quit()
                    exit()
    except():
        driver.quit()
        exit()




