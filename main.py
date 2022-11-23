import turtle


screen = turtle.Screen()
screen.title("US States Game")



#TO ADD SHAPE AS BACKGROUND
image = "Us-States-Game-Start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# def get_mouse_click_coor(x,y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)  

# turtle.mainloop()

# User Guess
guess = screen.textinput(title="Guess the state", prompt="What's another state name").lower()
print(guess)

# Read the csv file

data = data.csv








# screen.exitonclick()