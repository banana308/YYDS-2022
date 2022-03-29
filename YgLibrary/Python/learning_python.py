#下载pycham地址：
# https://www.jetbrains.com/zh-cn/pycharm/download/#section=windows

#下载python地址：
# Python官网：https://www.python.org/
# Python文档下载地址：https://www.python.org/doc/


#下载Git地址：
# https://git-scm.com/downloads

#Pygame地址:
#http://www.pygame.org/download.shtml
#pip install -U pygame

# #Git配置指令
# 一、Git的user name和email设置
# git config --global user.name "xxxx"
# git config --global user.email "xxxx@163.com"
#
# 二、生成密钥
# 使用你注册github的邮箱生成秘钥
#
# ssh-keygen -t rsa -C "xxxx@163.com"
# 中间连续3次Enter键
# .ssh目录会生成id_rsa和id_rsa.pub两个文件，
# id_rsa是私钥，不能泄露出去，
# id_rsa.pub是公钥，可以放心地告诉任何人（关于RSA加密，可以自行百度，这里不详细展开）
#
# 如果之前此电脑已经生成过密钥，根据提示在overwrite的时候选择 y 覆盖即可。
#
# 三、添加SSH key到github账户
# 在GitHub的账户添加SSH
# Key，GitHub才能根据此进行加密解密，从而判断此提交是由你本人操作。
#
# 带pub的公钥复制到上面
#
# 四、测试SSH key是否设置成功
# ssh -T git@github.com
#
# The authenticity of host 'github.com (192.30.253.113)' can't be established.
# RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
# Are you sure you want to continue connecting (yes/no)? yes
#
# 是否继续连接？输入 yes
#
# 输出如下，则表示通过
#
# Hi xxxx! You've successfully authenticated, but GitHub does not provide shell        access
#
# 五、设置项目连接方式
#
# git remote set-url git@github.com:oDevilo/Java-Base
# 这里修改的是项目中.git （隐藏）文件夹下的config文件
# 原来如下：
#
# [remote "origin"]
# url = https: // github.com / oDevilo / Java - Base
# fetch = +refs / heads / *:refs / remotes / origin / *
#
# 修改后：
#
# [remote "origin"]
# url = git @ github.com:oDevilo / Java - Base
# fetch = +refs / heads / *:refs / remotes / origin / *
# 之后我们的提交都会变为ssh连接



# #终端提交代码
# git add .
# git commit -m "XXX提交"
# git push origin main  or  git push
# or git push -u origin main





#自动化Allure生成测试报告
# 1、下载地址：https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
# 目前最新版本为2.13.6
# 2、解压allure后，打开bin目录下的allure.bat安装
# 3、下载完成后，在系统环境变量，配置path的bin目录下
# 4、安装allure-pytest插件
# pip install allure-pytest

# allure常用特性
# 希望在报告中看到测试功能，子功能或场景，测试步骤，包括测试附加信息可以使用@feature,@story,@step,@attach
#
# 步骤：
#
# import allure
# 功能上加@allure.feature("功能名称")
# 子功能上加@allure.story("子功能名称")
# 步骤上加@allure.step("步骤细节")
# @allure.attach("具体文本信息")，需要附加的信息，可以是数据，文本，图片，视频，网页
# 如果只测试部分功能运行的时候可以加限制过滤：
# pytest 文件名 --allure-features "需要运行的功能名称"
# allure特性—feature/story
#
# @allure.feature与@allure.store的关系
#
# feature相当于一个功能，一个大的模块，将case分类到某个feature中，报告中在behaviore中显示，相当于testsuite
# story相当于对应这个功能或者模块下的不同场景，分支功能，属于feature之下的结构，报告在features中显示，相当于testcase
# feature与story类似于父与子关系
# step特性
#
# 测试过程中每个步骤，一般放在具体逻辑方法中
# 可以放在关键步骤中，在报告中显示
# 在app,web自动化测试中，建议每切换到一个新的页面当做一个step
# 用法：
# @allure.step() 只能以装饰器的形式放在类或方法上面
# with allure.step():  可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
# 运行：
#
# 　　在测试执行期间收集结果
#
# 　　pytest [测试文件] -s -q --alluredir=./result --clean-alluredir
#
# --alluredir这个选项，用于指定存储测试结果的路径
# --clean-alluredir 这个选项用来清除之前生成的结果
# 查看测试报告：
#
# 　　方法一：测试完成后查看实际报告，在线看报告，会直接打开默认浏览器展示当前报告
#
# 　　　　　　allure serve ./result
#
# 　　方法二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤
#
# 　　　　　　生成报告：
#
# 　　　　　　　　　　allure generate ./result -o ./report --clean   (注意：--clean用来清除之前已生成的报告)
#
# 　　　　　　打开报告：
#
# 　　　　　　　　　　allure open -h 127.0.0.1 -p 8883 ./report   （该方法直接生成一个tomcat服务，可远程访问）


