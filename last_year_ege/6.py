from turtle import *

screensize(4000, 4000)
m = 20
tracer(False)

for i in range(2):
    fd(20 * m)
    lt(270)
    fd(12 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for i in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(4, 'dark green')
print(7 * 14 + 21 * 13 - 6 * 12)
update()
done()
