import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("lightblue")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()
    
def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(0.5)
    sides=1
    while(sides<= 4):
        brad.forward(100)
        brad.right(90)
        sides+=1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(50)

def draw_triangle():
    sophie = turtle.Turtle()
    sophie.shape("arrow")
    sophie.color("black")
    sides=1
    sophie.left(180)
    while(sides<= 3):
        sophie.forward(100)
        sophie.left(120)
        sides+=1

    
draw_shapes()
