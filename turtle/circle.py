import turtle

# 绘制一个圆

for i in range(360):
    turtle.setheading(i)
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
