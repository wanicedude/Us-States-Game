import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")


# TO ADD SHAPE AS BACKGROUND
image = "Us States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x,y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

guessed_states = []

while len(guessed_states) < 50:
    # User Guess
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                            prompt="What's another state's name?").title()

    # Read the csv file
    data = pandas.read_csv("../../Documents/GITHUB/US States Game/50_states.csv")
    all_states = data.state.to_list()

    # Check if guess is among the 50 states

    if guess == "Exit":
        not_state = []
        for state in all_states:
            if state not in guessed_states:
                not_state.append(state)
        print(not_state)
    if guess in all_states:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# states to learn.csv

        
not_state_dict = {
    "State": not_state
}

print(not_state_dict)
        



# screen.exitonclick()
