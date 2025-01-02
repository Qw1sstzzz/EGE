from turtle import *

lt(90)
m = 15
screensize(2000, 2000)
tracer(0)

for i in range(2):
    fd(10*m)
    rt(90)
    fd(20*m)
    rt(90)

up()
bk(4*m)
rt(90)
fd(7*m)
lt(90)
down()

for i in range(4):
    fd(8*m)
    lt(90)
    fd(12*m)
    lt(90)

up()
fd(10*m)
down()

for i in range(4):
    fd(12*m)
    rt(90)
up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5,'darkred')

update()
done()

print(21*11 + 13*13 - 5*13)
# 335