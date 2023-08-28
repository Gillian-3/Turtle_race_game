from turtle import Turtle, Screen
import random
is_race_on=False
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple","violet","black"]
y=145
all_turtles=[]
for color in colors:
    dummy=Turtle(shape="turtle")
    dummy.penup()
    dummy.color(color)
    dummy.goto(-230,y)
    y-=35
    all_turtles.append(dummy)
if user_bet:
    is_race_on=True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>220:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color.lower()==user_bet.lower():
                print(f"you've won! the {winning_color} is the winner")
            else:
                print(f"you've Lost! the {winning_color} is the winner")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()