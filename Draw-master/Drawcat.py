#Drawcat 画多啦一梦
import turtle  as tt


# 无轨迹跳跃
def my_goto(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

# # 眼睛

def eyes():
    my_goto(-45,190 )
    tt.tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            tt.lt(3)
            tt.fd(a)
        else:
            a += 0.05
            tt.lt(3)
            tt.fd(a)
    tt.tracer(True)

# 胡须
def beard():
    my_goto(-37, 135)
    tt.seth(165)
    tt.fd(60)

    my_goto(-37, 125)
    tt.seth(180)
    tt.fd(60)

    my_goto(-37, 115)
    tt.seth(193)
    tt.fd(60)

    my_goto(37, 135)
    tt.seth(15)
    tt.fd(60)

    my_goto(37, 125)
    tt.seth(0)
    tt.fd(60)

    my_goto(37, 115)
    tt.seth(-13)
    tt.fd(60)

# 嘴巴
def mouth():
    my_goto(5, 148)
    tt.seth(270)
    tt.fd(100)
    tt.seth(0)
    tt.circle(120, 50)
    tt.seth(230)
    tt.circle(-120, 100)

# 围巾
def scarf():
    tt.fillcolor('#e70010')
    tt.begin_fill()
    tt.seth(0)
    tt.fd(200)
    tt.circle(-5, 90)
    tt.fd(10)
    tt.circle(-5, 90)
    tt.fd(207)
    tt.circle(-5, 90)
    tt.fd(10)
    tt.circle(-5, 90)
    tt.end_fill()

# 鼻子
def nose():
    my_goto(-10, 158)
    tt.fillcolor('#e70010')
    tt.begin_fill()
    tt.circle(20)
    tt.end_fill()

# 黑眼睛
def black_eyes():
    tt.seth(0)
    my_goto(-20, 195)
    tt.fillcolor('#000000')
    tt.begin_fill()
    tt.circle(13)
    tt.end_fill()

    tt.pensize(6)
    my_goto(20, 205)
    tt.seth(75)
    tt.circle(-10, 150)
    tt.pensize(3)

    my_goto(-17, 200)
    tt.seth(0)
    tt.fillcolor('#ffffff')
    tt.begin_fill()
    tt.circle(5)
    tt.end_fill()
    my_goto(0, 0)



# 脸
def face():
    tt.fd(183)
    tt.fillcolor('#ffffff')
    tt.begin_fill()
    tt.lt(45)
    tt.circle(120, 100)

    tt.seth(90)
    # tt.eyes()
    tt.seth(180)
    tt.penup()
    tt.fd(60)
    tt.pendown()
    tt.seth(90)
    # tt.eyes()
    tt.penup()
    tt.seth(180)
    tt.fd(64)
    tt.pendown()
    tt.seth(215)
    tt.circle(120, 100)
    tt.end_fill()

# 头型
def head():
    tt.penup()
    tt.circle(150, 40)
    tt.pendown()
    tt.fillcolor('#00a0de')
    # tt.fillcolor('#ffffff')
    tt.begin_fill()
    tt.circle(150, 280)
    tt.end_fill()

# 画哆啦A梦
def Doraemon():
    # 头部
    head()

    # 围脖
    scarf()

    # 脸
    face()

    # 眼睛
    eyes()

    # 红鼻子
    nose()

    # 嘴巴
    mouth()

    # 胡须
    beard()

    # 身体
    my_goto(0, 0)
    tt.seth(0)
    tt.penup()
    tt.circle(150, 50)
    tt.pendown()
    tt.seth(30)
    tt.fd(40)
    tt.seth(70)
    tt.circle(-30, 270)


    tt.fillcolor('#00a0de')
    tt.begin_fill()

    tt.seth(230)
    tt.fd(80)
    tt.seth(90)
    tt.circle(1000, 1)
    tt.seth(-89)
    tt.circle(-1000, 10)

    # print(pos())

    tt.seth(180)
    tt.fd(70)
    tt.seth(90)
    tt.circle(30, 180)
    tt.seth(180)
    tt.fd(70)

    # print(pos())
    tt.seth(100)
    tt.circle(-1000, 9)

    tt.seth(-86)
    tt.circle(1000, 2)
    tt.seth(230)
    tt.fd(40)

    # print(pos())


    tt.circle(-30, 230)
    tt.seth(45)
    tt.fd(81)
    tt.seth(0)
    tt.fd(203)
    tt.circle(5, 90)
    tt.fd(10)
    tt.circle(5, 90)
    tt.fd(7)
    tt.seth(40)
    tt.circle(150, 10)
    tt.seth(30)
    tt.fd(40)
    tt.end_fill()

    # 左手
    tt.seth(70)
    tt.fillcolor('#ffffff')
    tt.begin_fill()
    tt.circle(-30)
    tt.end_fill()
    # 画眼睛
    black_eyes()

    # 脚
    my_goto(103.74, -182.59)
    tt.seth(0)
    tt.fillcolor('#ffffff')
    tt.begin_fill()
    tt.fd(15)
    tt.circle(-15, 180)
    tt.fd(90)
    tt.circle(-15, 180)
    tt.fd(10)
    tt.end_fill()

    my_goto(-96.26, -182.59)
    tt.seth(180)
    tt.fillcolor('#ffffff')
    tt.begin_fill()
    tt.fd(15)
    tt.circle(15, 180)
    tt.fd(90)
    tt.circle(15, 180)
    tt.fd(10)
    tt.end_fill()

    # 右手
    my_goto(-133.97, -91.81)
    tt.seth(50)
    tt.fillcolor('#ffffff')
    tt.begin_fill()
    tt.circle(30)
    tt.end_fill()

    # 口袋
    my_goto(-103.42, 15.09)
    tt.seth(0)
    tt.fd(38)
    tt.seth(230)
    tt.begin_fill()
    tt.circle(90, 260)
    tt.end_fill()

    my_goto(5, -40)
    tt.seth(0)
    tt.fd(70)
    tt.seth(-90)
    tt.circle(-70, 180)
    tt.seth(0)
    tt.fd(70)

    #铃铛
    my_goto(-103.42, 15.09)
    tt.fd(90)
    tt.seth(70)
    tt.fillcolor('#ffd200')
    # print(pos())
    tt.begin_fill()
    tt.circle(-20)
    tt.end_fill()
    tt.seth(170)
    tt.fillcolor('#ffd200')
    tt.begin_fill()
    tt.circle(-2, 180)
    tt.seth(10)
    tt.circle(-100, 22)
    tt.circle(-2, 180)
    tt.seth(180-10)
    tt.circle(100, 22)
    tt.end_fill()
    tt.goto(-13.42, 15.09)
    tt.seth(250)
    tt.circle(20, 110)
    tt.seth(90)
    tt.fd(15)
    tt.dot(10)
    my_goto(0, -150)


if __name__ == '__main__':
    tt.screensize(800,600, "#f0f0f0")
    tt.pensize(3)  # 画笔宽度
    tt.speed(14)    # 画笔速度
    Doraemon()
    my_goto(500, -310)
    tt.write('ks1941', font=("Bradley Hand ITC", 14, "bold"))
    tt.mainloop()

