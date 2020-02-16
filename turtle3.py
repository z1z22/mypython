import turtle
from datetime import *

def skip(step):
    '''抬起画笔运动'''
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()



def mkHand(handname,length):
    '''注册Turtle形状，建立表针'''
    turtle.reset()
    skip(-length * 0.1)

    turtle.begin_poly()
    turtle.forward(length * 1.1)
    turtle.end_poly()
    handForm = turtle.get_poly()
    turtle.register_shape(handname,handForm)

def Init():
    global secHand, minHand, hourHand,printer

    turtle.mode('logo')

    mkHand('secHand',135)
    mkHand('minHand',125)
    mkHand('hourHand',90)
    secHand = turtle.Turtle()
    secHand.shape('secHand')
    minHand = turtle.Turtle()
    minHand.shape('minHand')
    hourHand = turtle.Turtle()
    hourHand.shape('hourHand')

    for hand in secHand,minHand,hourHand:
        hand.shapesize(1,1,3)
        hand.speed(0)

    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()

def SetupClock(radius):
    '''建立表的外框'''
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            skip(-radius - 20)

            skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align='center',font=('Courier', 14, 'bold'))
            elif i == 30:
                skip(25)
                turtle.write(int(i/5), align='center',font=('Courier', 14, 'bold'))
                skip(-25)
            elif (i == 25 or i == 35):
                skip(20)
                turtle.write(int(i/5), align='center',font=('Courier', 14, 'bold'))
                skip(-20) 
            else:
                turtle.write(int(i/5), align='center',font=('Courier', 14, 'bold'))
            skip(-radius - 20)
        else:
            turtle.dot(5)
            skip(-radius)
        turtle.right(6)
def Week(t):
    week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    return week[t.weekday()]          

def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" %(y,m,d)

def Tick():
    '''绘制表针动态显示'''
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute /60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hourHand.setheading(30*hour)

    turtle.tracer(False)
    printer.forward(65)
    printer.write(Week(t),align = 'center',font=('Courier',14))
    printer.back(130)
    printer.write(Date(t),align = 'center',font =('Courier',14))
    printer.home()
    turtle.tracer(True)

    #100ms后继续调用tick
    turtle.ontimer(Tick, 100)

def main():
    '''绘制时钟'''
    turtle.tracer(False)
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()





if __name__ == '__main__':
    main()