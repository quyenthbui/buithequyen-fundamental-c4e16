from turtle import *
shape('classic')
speed(1)
colors = ['red','blue','brown','yellow','gray']
count = 0
for i in range(5):
    color(colors[i])
    begin_fill()
    if i != 0:
        forward(100)
    for i in range(2):
        forward(100)
        right(90)
        forward(200)
        right(90)
    end_fill()




mainloop()
