



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


class Circle(Point):
    redius=0.0

    def __init__(self,x,y,redius):
        Point.__init__(self,x,y)
        self.redius=redius
        print("Circle constructor")

    def ToString(self):
        return Point.ToString(self)+ ",{RADIUS="+str(self.redius)+"}"+"\n"

class Size():
    width=0.0
    height=0.0
    def __init__(self,width,height):
        self.width=width
        self.height=height
        print("Size constructor")


    def ToString(self):
        return "{WIDTH="+str(self.width)+",HEIGHT="+str(self.height)+"}"+"\n"


class Rectangle(Point,Size):
    def __init__(self,x,y,width,height):
        Point.__init__(self,x,y)
        Size.__init__(self,width,height)
    def ToString(self):
        return Point.ToString(self)+","+Size.ToString(self)




if __name__=="__main__":
    P = Point(10, 30)
    print(P.ToString())

    C = Circle(100, 200, 50)
    print(C.ToString())

    R=Rectangle(100,200,300,400)
    print(R.ToString())



