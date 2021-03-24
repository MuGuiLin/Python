'''
在用Python编写绘图程序时，我们会用到turtle海龟绘图库 import turtle 和 from turtle import * 两个语句，但在PyCharm2017编写程序时，会发现后者无法使用，接下来我会讲解我使用的解决办法。
'''


# 利用海龟绘图画一个倒立的等边三角形

# 海龟绘图库turtle的导入、调用方式1
from turtle import *
'''
pensize(10) # 设置画笔宽度为2像素
color('red', 'blue') # 设置画笔颜色,背景色

begin_fill()  # 开始绘制
speed(8) # 绘制速度秒

i = 1
while i <= 3: # 绘制边数
    forward(100)  # 图形大小
    right(120)  # 角度
    i = i + 1

end_fill() # 绘制结束
done() # 画布悬停 (不然会闪退)
'''

# turtle的导入、调用方式2
import turtle
'''
turtle.color('red', 'yellow')

turtle.begin_fill()
turtle.speed(8)

i = 1
while i <= 3:
    turtle.forward(100)
    turtle.right(120)
    i = i + 1

turtle.end_fill()
turtle.done()
'''

# 利用海龟绘图画一个正立的等边三角形

'''
pensize(10) 
color('red', 'blue')

begin_fill()
speed(8)

i = 1
while i <= 3:
    forward(100)
    left(120)
    i = i + 1

end_fill()
done()
'''

# 利用海龟绘图画一个正立的等边三角形

'''
color('red', 'yellow')
begin_fill()
speed(1)

i = 1
while i <= 5:
    forward(200)
    right(144) # 五角星内角为36度
    i = i + 1

end_fill()
done()
'''

#　利用海龟绘图画一个半径为100的实心圆，画笔颜色为黑色，填充颜色为蓝色
color('black', 'blue')

hideturtle()
begin_fill()

speed(2)
circle(100)

end_fill()
done()