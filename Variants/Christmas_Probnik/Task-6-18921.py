from turtle import *

screensize(2000, 2000)
m = 20
tracer(0)
lt(90)

for _ in range(13):
    fd(13*m)
    rt(90)
    fd(5*m)

up()
rt(90)
fd(7*m)
lt(90)
fd(10*m)
down()

for i in range(23):
    fd(8*m)
    lt(90)
    fd(11*m)
    lt(90)

up()

for x in range(-20, 30):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()

# 391