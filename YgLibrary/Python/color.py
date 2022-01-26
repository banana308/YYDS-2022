'''
@#语法：
@\033[显示方式; 前景色; 背景色m******\033[0m
'''

class color():
    def number01(self):
        # 基本属性
        print("\033[0;<这是默认>\033[0m")  # 默认0
        print("\033[1;<这是高亮>\033[0m")  # 高亮1
        print("\033[4;这是下划线>\033[0m")  # 下划线4
        print("\033[5;<这是闪烁>\033[0m")  # 闪烁5
        print("\033[7;<这是反显>\033[0m")  # 反显7
        print("\033[8;<这是不可见>\033[0m")  # 不可见8

    def number02(self):
        #前景色
        print("\033[30m<这是黑色前景色>30\033[0m")  # 黑色30
        print("\033[31m<这是红色前景色>31\033[0m")  # 红色31
        print("\033[32m<这是绿色前景色>32\033[0m")  # 绿色32
        print("\033[33m<这是黄色前景色>33\033[0m")  # 黄色33
        print("\033[34m<这是蓝色前景色>34\033[0m")  # 蓝色34
        print("\033[35m<这是紫红色前景色>35\033[0m")  # 紫红色35
        print("\033[36m<这是青蓝色前景色>36\033[0m")  # 青蓝色36
        print("\033[37m<这是白色前景色>37\033[0m")  # 白色37


    def number03(self):
        #这是背景色
        print("\033[37;40m<这是黑色背景色>40m\033[0m")  # 黑色40
        print("\033[30;41m<这是红色背景色>41m\033[0m")  # 红色41
        print("\033[30;42m<这是绿色背景色>42m\033[0m")  # 绿色42
        print("\033[30;43m<这是黄色背景色>43m\033[0m")  # 黄色43
        print("\033[30;44m<这是蓝色背景色>44m\033[0m")  # 蓝色44
        print("\033[30;45m<这是紫红色背景色>45m\033[0m")  # 紫红色45
        print("\033[30;46m<这是青蓝色背景色>46m\033[0m")  # 青蓝色46
        print("\033[30;47m<这是白色背景色>47m\033[0m")  # 白色47

    def number04(self):
        print("\033[0;31;40m<这是默认显示方式，红色字体，黑色背景色>40m\033[0m")
        print("\033[1;32;41m<这是高亮显示方式，绿色字体，红色背景色>40m\033[0m")
        print("\033[4;33;42m<这是下划线显示方式，黄色字体，绿色背景色>40m\033[0m")
        print("\033[5;34;43m<这是闪烁显示方式，蓝色字体，黄色背景色>40m\033[0m")
        print("\033[7;35;47m<这是反显显示方式，紫红色字体，白色背景色>40m\033[0m")
        print("\033[8;36;45m<这是不可见显示方式，青蓝色字体，紫红色背景色>40m\033[0m")


if __name__=="__main__":
    x=color()
    print(x.number01())
    print(x.number02())
    print(x.number03())
    print(x.number04())

