from turtle import Turtle, Screen
from timeboard import TimeBoard
import pandas as pd

writer = Turtle()
screen = Screen()
game_over = False
score = 0

timeboard = TimeBoard(screen, game_over)

writer.hideturtle()
writer.penup()

with open("50_states.csv") as file:
    data = pd.read_csv(file)

print(sum(data["state"] == "Hawaii"))
all_states = data["state"].to_list()

image = "blank_states_img.gif"

screen.setup(900, 900)
screen.addshape(image)
screen.bgpic(image)

guessed_states = []

while not game_over:
    guess = screen.textinput(title=f"US States (50) / {score}", prompt="Guess the state: ")
    guess = guess.strip()

    if guess == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pd.DataFrame(missing_states)
        df.to_csv("States To Learn")
        break

    elif guess not in all_states:
        print("There is no state with this name !")

    if guess is None:
        print("X")

    elif guess in all_states and guess not in guessed_states:
        new_row = data[data["state"] == guess].iloc[0]
        writer.goto(new_row.x, new_row.y)
        writer.write(new_row.state)
        score += 1
        guessed_states.append(guess)

screen.exitonclick()
screen.mainloop()



