from turtle import *

screensize(4000, 4000)
m = 1
tracer(False)

rt(45)
for i in range(10):
    rt(45)
    fd(203 * m)
    rt(45)

up()

bk(40 * m)
rt(45)

down()

for i in range(5):
    fd(20 * m)
    lt(90)

up()

# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*m, y*m)
#         dot(4, 'red')

print(202*202+20*20)

update()
done()
