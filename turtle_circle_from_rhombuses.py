import turtle

def draw_rhombus(turtle, size, small_angle):
    for i in range(2):
        turtle.forward(size)
        turtle.right(small_angle)
        turtle.forward(size)
        turtle.right((360-2*small_angle)//2)

def draw_flower(trtle, size, angle):
    for i in range(360//angle):
        draw_rhombus(turtle, size, 60)
        turtle.right(angle)
    turtle.right(90)
    turtle.forward(size*3)

canvas = turtle.Screen()
canvas.colormode(255)
canvas.bgcolor("lightblue")

bruce = turtle.Turtle("turtle")
bruce.color("red")
bruce.speed(5)

draw_flower(bruce, 100, 5)
