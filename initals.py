import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("lightyellow")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(0.5)
    brad.penup()
    brad.left(180)
    brad.pendown()
    count =1
    for i in range(0, 72):
        for j in range(0, 2):
            brad.forward(100)
            brad.left(60)
            brad.forward(100)
            brad.left(120)
        brad.left(5)
    brad.left(90)
    brad.forward(300)
    
draw_flower()
