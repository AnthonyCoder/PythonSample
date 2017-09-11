import turtle
import math


print("欢迎来到英雄联盟，敌军还有三秒钟到达战场，碾碎他们。")
hp = 100
mp = 100
name = input("请输入您的英雄名字:")
if not name:
    name = "玩家_赤壁喧嚣"

heroType = input("请输入您的英雄类型 [1:人族][2:魔族][3:神族]")
print("你可以通过键盘控制你的英雄方向 [A;向左][D:向右][W:向上][S:向下]")
turtle.speed(5)
turtle.goto(0,0)


