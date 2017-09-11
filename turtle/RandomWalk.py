import random
import turtle

x = -80
#纵坐标的线绘制

for y in range(-80,80+1,10):
    turtle.penup()

    turtle.goto(x, y)

    turtle.pendown()

    turtle.forward(160)

    # 横坐标线绘制

    y = 80

    turtle.right(90)

for x in range(-80,80+1,10):
    turtle.penup()

    turtle.goto(x, y)

    turtle.pendown()

    turtle.forward(160)

    turtle.pensize(3)

    turtle.color("red")

    # 模拟走动(是个方向等概率）

    turtle.penup()

    turtle.goto(0, 0)

    turtle.pendown()

    x = y = 0

#设置移动范围

while abs(x) < 80 and abs(y) < 80:
    r = random.randint(0, 3)  # 产生随机数，0，1，2，3表示是个方向

if r == 0:

    x += 10  # right

    turtle.setheading(0)

    turtle.forward(10)

elif r == 1:

    y -= 10

    turtle.setheading(270)

    turtle.forward(10)

elif r == 2:

    x -= 10

    turtle.setheading(180)

    turtle.forward(10)

elif r == 3:

    y += 10

    turtle.setheading(90)

    turtle.forward(10)

    turtle.done()