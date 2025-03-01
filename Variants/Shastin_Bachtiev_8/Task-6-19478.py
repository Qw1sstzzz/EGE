from turtle import *

m = 20
screensize(2500, 2500)
tracer(0)
lt(90)
down()

for i in range(4):
    fd(27*m)
    rt(90)
    fd(21*m)
    rt(90)
up()
fd(3*m)
rt(90)
fd(7*m)
lt(90)
down()
for i in range(4):
    fd(73*m)
    rt(90)
    fd(91*m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()
# 336