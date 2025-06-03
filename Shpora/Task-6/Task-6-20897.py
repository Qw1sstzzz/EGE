from turtle import *

lt(90)
down()

screensize(2500, 2500)
m = 25
tracer(0)

for i in range(9):
    fd(27*m)
    rt(90)
    fd(30*m)
    rt(90)

up()
fd(3 * m)
rt(90)
fd(6 * m)
lt(90)
down()

for i in range(9):
    fd(77*m)
    rt(90)
    fd(66*m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()