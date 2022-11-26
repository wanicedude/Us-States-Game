import turtle
# from turtle import Turtle
import pandas
IMAGE = "Us States Game/blank_states_img.gif"
screen = turtle.Screen()



class Game:
    def __init__(self):
        self.score = 0
        self.guessed_states = []
        self.data = pandas.read_csv("../../Documents/GITHUB/US States Game/50_states.csv")
        self.all_states = self.data.state.to_list()
        self.states_to_learn = []
        self.guess = screen.textinput(title="Guess the state", prompt="What's another state name").capitalize()
        
    def correct_guess(self):
        # for state in self.data.state:
        if self.data[self.data.state == self.guess]:
                print(self.data.state)
                # self.write(f"SCORE: {self.score} High Score: {self.high_score}",
                #    True, align='center', font=('candara', 24, 'bold'))
        #         self.guessed_states.append(self.guess)
        # guess_loc = self.data[self.data.state == self.guess]
        # guess_loc.to_dict()
        # print(guess_loc)
        # self.write_guess()
                
    def write_guess(self):
        pass
                
                
                
                # self.score += 1
                # self.guessed_states.append(self.guess)
                # print(self.guessed_states)
                # print(self.score)
                # self.write_state()
                # self.check_if_game_over()
        
    def correct_score(self):
        self.score += 1
        print(self.score)


        