from turtle import *

screensize(3000, 3000)
m = 30
tracer(False)

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(20 * m)
    rt(90)
up()
bk(4 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for i in range(4):
    fd(8 * m)
    lt(90)
    fd(12 * m)
    lt(90)
up()
fd(10 * m)
down()
for i in range(4):
    fd(12 * m)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(4, 'dark blue')

print(max(11 * 21 + 9 * 13 - 5 * 8, 11 * 21 + 13 * 13 - 5 * 13))

update()
done()
