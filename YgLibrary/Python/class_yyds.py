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





def PrintName(name):
    print(f"The name is {name}.")
PrintName("Tom")

class Point():
    x=0.0
    y=0.0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("Point constructor")
    def ToString(self):
        return "{X:"+str(self.x)+",Y:"+str(self.y)+"}"+"\n"

class Size():
    width=0.0
    height=0.0
    def __init__(self,width,height):
        self.width=width
        self.height=height
        print("Size constructor")


    def ToString(self):
        return "{WIDTH="+str(self.width)+",HEIGHT="+str(self.height)+"}"+"\n"



#类的单继承
class Circle(Point):
    redius=0.0

    def __init__(self,x,y,redius):
        Point.__init__(self,x,y)
        self.redius=redius
        print("Circle constructor")

    def ToString(self):
        return Point.ToString(self)+ ",{RADIUS="+str(self.redius)+"}"+"\n"

#类的多继承
class Rectangle(Point,Size):
    def __init__(self,x,y,width,height):
        Point.__init__(self,x,y)
        Size.__init__(self,width,height)
    def ToString(self):
        return Point.ToString(self)+","+Size.ToString(self)



if __name__=="__main__":
    number=11
    number_one=30
    x = Comples(number,number_one)
    print(x.nn,x.nb)
    print(x.yyds())

    P = Point(10, 30)
    print(P.ToString())

    C = Circle(100, 200, 50)
    print(C.ToString())

    R = Rectangle(100, 200, 300, 400)
    print(R.ToString())