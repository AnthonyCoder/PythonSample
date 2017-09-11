import turtle
import math

# 实现中国国旗绘制

# 控制画笔的速度
turtle.speed(8)
# 将画笔指向到原点
turtle.goto(0,0)

bigStarLineWidth = 100
smallStarLineWidth = 50

outWith = 800
outHeight = 800 * 0.6
firstPoint = 150
starAngle=10

# 星星占的宽度
bigStarWidth = math.sin(math.radians(72)) * bigStarLineWidth
smallStarWidth = math.sin(math.radians(72)) * smallStarLineWidth
starMargin = 50;

turtle.color('red','red')
turtle.begin_fill()
for i in range(4):
    if i % 2 == 0:
        turtle.forward(outWith)
    else:
        turtle.forward(outHeight)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(firstPoint)
# ↓
turtle.right(90)
turtle.forward(firstPoint)
# →
turtle.left(90)
turtle.color('yellow','yellow')
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    turtle.forward(bigStarLineWidth)
    turtle.right(144)
turtle.end_fill()


# for i in range(4):
for j in range(4):
    turtle.penup()
    if j == 0:
        turtle.forward(smallStarWidth + starMargin)
    if j ==1:
        turtle.left(15)
        turtle.right(90)
        turtle.forward(starMargin)
    if j==2:
        turtle.left(60)
        turtle.right(90)
        turtle.forward(starMargin)
    if j==3:
        turtle.left(65)
        turtle.right(90)
        turtle.forward(starMargin)

    # ↑
    turtle.left(90)
    turtle.forward(smallStarWidth + starMargin)
    # ↓
    turtle.right(90)
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.right(20)
    turtle.pendown()
    for i in range(5):
        turtle.forward(smallStarLineWidth)
        turtle.right(144)
    turtle.end_fill()


