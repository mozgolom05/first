import turtle 

colors = ['red', 'purple', 'blue', 'green', 'orange','grey']
        
t = turtle.Pen()
             
turtle.bgcolor('black')

for x in range(400):
    t.pencolor(colors[x%2])
    t.width(x/10+1)
    t.forward(x)
    t.left(42)
