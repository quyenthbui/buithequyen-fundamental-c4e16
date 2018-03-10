from turtle import *
speed(-1)
shape('classic')
colors = ['red','blue','brown','yellow','gray']
for i in range(3,8):
    color(colors[i -3])
    for j in range (i):
        forward(100)
        left(180-(180*(i-2)/i))

mainloop()
