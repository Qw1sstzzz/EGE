from turtle import *

screensize(2500, 2500)
m = 20
tracer(0)
lt(90)
down()

for i in range(3):
    fd(2*m)
    rt(90)
    fd(3*m)
    lt(90)

rt(180)
fd(6*m)
rt(90)
fd(9*m)

up()
bk(3*m)
rt(90)
down()

for i in range(2):
    fd(1*m)
    rt(90)
    fd(2*m)
    lt(90)

rt(180)
fd(3*m)
rt(90)
fd(4*m)
rt(90)
fd(1*m)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()