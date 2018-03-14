from turtle import *
color('blue')
speed(-1)
a = 100
for i in range(40):
    right(9)
    a -= 2
    for i in range(4):
        backward(int(a))
        right(90)
mainloop()
