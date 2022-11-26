import turtle
from game import Game
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "Us States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game = Game()


# while 
game.correct_guess()
# User Guess
# guess = screen.textinput(title="Guess the state",
#                          prompt="What's another state name").capitalize()
# print(guess)

# Read the csv file
# data = pandas.read_csv("../../Documents/GITHUB/US States Game/50_states.csv")


# # Step 2
# for state in data.state:
#     if state == guess:
#         print("Correct guess")
#         game.correct_guess(guess)



















screen.exitonclick()
