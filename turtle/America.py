import turtle
import math

# 实现美国国旗绘制

# 控制画笔的速度
turtle.speed(10)
# 将画笔指向到原点
turtle.goto(0,0)
# 星星线长度
starLineWidth = 20

# 星星占的宽度
starWidth = math.sin(math.radians(72)) * starLineWidth
# 第一颗星星和最后一颗上下左右边距
starMargin = 10
# 星星行数
starRow = 11

outWidth = 600
outHeight = outWidth * 0.6
inWidth = starRow * starWidth + starMargin * 2
inHeight = starWidth * 9 + starMargin*2
h = 8

turtle.color('black','black')
for i in range(4):
    if i % 2 == 1:
        turtle.forward(outHeight)
        turtle.right(90)
    else:
        turtle.forward(outWidth)
        turtle.right(90)


turtle.home()
#蓝色矩形背景
turtle.color('blue','blue')
turtle.begin_fill()
for i in range(4):
    if i % 2 == 1:
        turtle.forward(inHeight)
        turtle.right(90)
    else:
        turtle.forward(inWidth)
        turtle.right(90)
turtle.end_fill()


turtle.home()
#白色五角星
turtle.color('white','white')
print("高度："+str(math.sin(math.radians(72))*starLineWidth))
for k in range(starRow):
    turtle.penup()
    turtle.home()
    # →
    print("向右前进："+str(starMargin + starWidth * k))
    turtle.forward(starMargin + starWidth * k)
    if k % 2 == 0:
        for j in range(5):
            turtle.penup()
            # ↓
            turtle.right(90)
            if j == 0:
                turtle.forward(starMargin+h)
            else:
                turtle.forward(starWidth * 2)
            # →
            turtle.left(90)
            turtle.pendown()
            turtle.begin_fill()
            # 画星星
            for i in range(5):
                turtle.forward(starLineWidth)
                turtle.right(144)
            turtle.end_fill()
    else:
        # ↓
        turtle.right(90)
        turtle.forward(starWidth)
        # →
        turtle.left(90)
        for j in range(4):
            turtle.penup()
            # ↓
            turtle.right(90)
            if j == 0:
                turtle.forward(starMargin+h)
            else:
                turtle.forward(starWidth * 2)
            # →
            turtle.left(90)
            turtle.pendown()
            turtle.begin_fill()
            # 画星星
            for i in range(5):
                turtle.forward(starLineWidth)
                turtle.right(144)
            turtle.end_fill()
#
# # 画上半部的条纹
turtle.penup()
turtle.home()
turtle.forward(inWidth)
turtle.pendown()
for j in range(7):
    if j % 2 == 0:
        turtle.color('red', 'red')
    else:
        turtle.color('white', 'white')
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(outWidth - inWidth)
        else:
            turtle.forward(inHeight/7)

        turtle.right(90)
    turtle.end_fill()
    # ↓
    turtle.right(90)
    turtle.forward(inHeight/7)
    # →
    turtle.left(90)

# 画下半部分条纹
turtle.penup()
turtle.home()
# ↓
turtle.right(90)
turtle.forward(inHeight)
turtle.left(90)
turtle.pendown()
for j in range(6):
    if j % 2 == 1:
        turtle.color('red', 'red')
    else:
        turtle.color('white', 'white')
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(outWidth)
        else:
            turtle.forward((outHeight-inHeight)/6)

        turtle.right(90)
    turtle.end_fill()
    # ↓
    turtle.right(90)
    turtle.forward((outHeight-inHeight)/6)
    # →
    turtle.left(90)





