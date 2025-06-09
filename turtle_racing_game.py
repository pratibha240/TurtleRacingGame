from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title = "Make your bet" , prompt = "Which turtle will win the race ? Enter a color.")
colors = ["red", "orange", "yellow", "green" , "purple","pink"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []


for t in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t])
    new_turtle.goto(x= -230, y=y_position[t])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won!")
            else:
                print("You have lost")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()