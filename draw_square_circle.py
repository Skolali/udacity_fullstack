import turtle

def draw_square_circle():
    window = turtle.Screen()
    window.bgcolor("lightblue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
   # brad.size()
    brad.speed(0.5)
    count =1
    for i in range(0, 80):
        for j in range(0, 3):
            brad.forward(300)
            brad.right(120)
        brad.right(5)
      
draw_square_circle()
