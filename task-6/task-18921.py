from turtle import *

screensize(4000, 4000)
m = 30
tracer(False)

for i in range(13):
    fd(13 * m)
    rt(90)
    fd(5 * m)

up()
rt(90)
fd(7 * m)
lt(90)
fd(10 * m)

down()

for i in range(23):
    fd(8 * m)
    lt(90)
    fd(11 * m)
    lt(90)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(10, 'white')

print(18*18+8*11-3*7)

update()
done()
