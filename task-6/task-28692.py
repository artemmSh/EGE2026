from turtle import *

screensize(4000, 4000)
m = 30
tracer(False)

for i in range(3):
    fd(5 * m)
    lt(270)
    bk(8 * m)
    lt(270)
up()
fd(2 * m)
rt(90)
bk(3 * m)
lt(90)
down()
for i in range(3):
    fd(4 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(4 * m)
rt(180)
bk(2 * m)
down()
for i in range(2):
    fd(5 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(10, 'white')
print(4 * 6 + 5 * 7 + 5 * 8 - 3 * 3)
update()
done()
