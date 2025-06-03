from turtle import *

m = 15
screensize(2500, 2500)
tracer(0)
lt(90)

for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(1*m)
lt(90)
down()

for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(5, 'white')

update()
done()

print((15+21)*2)