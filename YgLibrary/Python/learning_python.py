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

