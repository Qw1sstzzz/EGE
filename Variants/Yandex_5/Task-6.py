from turtle import *

lt(90)
m = 25
tracer(0)

for i in range(7):
    rt(90)
    fd(7*m)
    rt(90)
    fd(6*m)
up()
rt(90)
fd(3*m)
rt(90)
fd(1*m)
down()
for i in range(4):
    rt(90)
    fd(6*m)
    rt(90)
    fd(11*m)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'darkred')

done()

# 74