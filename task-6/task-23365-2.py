from turtle import *

screensize(4000, 4000)
m = 40
tracer(False)

for i in range(3):
    fd(39 * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()
fd(27 * m)
rt(90)
fd(24 * m)
lt(90)
down()
for i in range(3):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(10, 'white')
print(39 * 48 + 29 * 18 - 12 * 18)
update()
done()
