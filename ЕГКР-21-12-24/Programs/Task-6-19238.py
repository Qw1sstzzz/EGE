from turtle import *

m = 20
lt(90)
screensize(2000,2000)
tracer(0)

for i in range(8):
    fd(16*m)
    rt(90)
    fd(22*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(8):
    fd(52*m)
    rt(90)
    fd(77*m)
    rt(90)
up()

for x in range(-30, 30):
    for y in range(-30,30):
        goto(x*m, y*m)
        dot(6, 'white')

update()
done()

print(17*11)