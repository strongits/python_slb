from turtle import *

reset()
speed(9)
colormode(255)
bgcolor(136,177,221)

shape("turtle")
for i in range(365):
	forward(1.01 ** i) #how long forward 
	left(9) # ture left 9'C
	if(i % 7 == 0):
		stamp()

'''
for i in range(265):
	pencolor(255-i,0,i) # decrease red,increase blue
	pensize(1.01 ** i)
	forward(1.01 ** i) #how long forward 
	left(6) # ture left 9'C
'''