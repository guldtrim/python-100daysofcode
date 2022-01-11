from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_pos = [80, 50, 20, -10, -40, -70]
turtle_list = []
winner = ""

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=start_pos[i])
    turtle_list.append(new_turtle)

print(turtle_list)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        color = turtle.color()
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if round(turtle.xcor()) > 200:
            is_race_on = False
            print(f"Turtle: {color[0]} won the race!")
            winner = color[0] 

if user_bet == winner:
    print("You win the bet.")
else:
    print("You lose the bet.")



screen.exitonclick()