from turtle import *
speed(1)
shape('classic')
for i in range(3,7):
    if i == 3 or i == 5:
        color('blue')
    else:
        color('red')
    for j in range (i):
        forward(100)
        left(180 - (180*(i-2)/i))

mainloop()
