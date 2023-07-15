import turtle

t = turtle.Turtle()
t.circle(20)
t.forward(30)

counter = 0

while counter < 5:
    t.circle(10)
    t.forward(20)
    counter += 1

turtle.mainloop()