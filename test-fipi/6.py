from turtle import *

screensize(4000, 4000)
m = 50
tracer(False)

rt(45)
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
rt(315)
fd(10 * m)
rt(90)
fd(20 * m)
rt(90)
for i in range(2):
    fd(10 * m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(4, 'dark blue')
print(9 * 19 + 10 * 9)
update()
done()
