import turtle
# 控制画笔的速度
turtle.speed(5)
# 将画笔定位到原点
turtle.goto(0,0)
# 从原点开始，画出一个边长为100的正方形
for i in range(4):
    # 正向运动 100 的距离
    turtle.forward(100)
    # 向右偏 90 度
    turtle.right(90)