import turtle

def fibonacci(n):
    if n in (1, 2):
        return 1
    if not n:
        return 0
    return fibonacci(n-2) + fibonacci(n-1)

#print(fibonacci(8))

t = turtle.Turtle()

for i in range(14):
    f = fibonacci(i)
    for i in range(4):
        t.forward(f)
        t.left(90)
    t.circle(f, 90)

turtle.mainloop()    