# Set up the window and its attributes
import turtle 
A1 = turtle.Screen()             
A1.bgcolor("lightgreen")
Ayo = turtle.Turtle()          
Ayo.pensize(3)
Ayo.color("#071733")
Ayo.right(90)
Ayo.speed(100)
def Birb(Turt,Size):
    for spider in range(1):
        Turt.begin_fill()
        Turt.circle(Size)
        Turt.end_fill()
    for legs in range(1):
        Turt.color("#EEB211")
        Turt.begin_fill()
        Turt.right(45)
        Turt.forward(110)
        Turt.left(135)
        Turt.forward(115)
        Turt.end_fill()
 
Amina = Birb(Ayo,100)
A1.exitonclick()