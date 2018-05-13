'''
import turtle
turtle.reset()

for i in range(4):
	turtle.forward(100)
	turtle.left(90)

'''


'''from turtle import *

def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)

f(500, 4)'''

from turtle import *

reset()   # 把画布清空，小海龟回到初始点
speed(9)  # 最快速度为9，最慢速度为1

for i in range(255) :
    colormode(255)    # 颜色分量值不超过255
    pencolor(i, i, i) # 画笔颜色会越来越淡
    forward(50 + i)
    left(99)





'''import turtle

from turtle import *



def part( total, length, breadth, col ):

    angleInc = 360/total

    width( breadth )

    color( col )

    for i in range(total):

        forward( length )

        left( angleInc )



def rosette( total, length, width, color, angleInc ):

    for i in range( int(360/angleInc) ):

        part( total, length, width, color )

        left( angleInc )



turtle.setup( 300, 300, 20, 20 )

turtle.speed(9)



rosette(10,40,1,"blue",36)

rosette(5,80,1,"red",36)

turtle.exitonclick()'''