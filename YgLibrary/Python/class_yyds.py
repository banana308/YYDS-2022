"""
@:class 的学习
#面向对象
"""


'''
class MyClass:
    """一个简单的类实例"""
    i =1213456

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
'''

class Comples:
    def __init__(self,number,number_one):
        self.nn=number
        self.nb=number_one

    def yyds(self):
        for i in range(0,int(number+1)):
                if i % 2 != 0:
                    print(f"\033[31m{i}是奇数\033[0m")
                else:
                    print(f"\033[32m{i}是偶数\033[0m")

if __name__=="__main__":
    number=11
    number_one=30
    x = Comples(number,number_one)
    print(x.nn,x.nb)
    print(x.yyds())