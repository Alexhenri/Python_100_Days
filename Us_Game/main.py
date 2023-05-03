import turtle
import pandas
from state import State

screen = turtle.Screen()

screen.title("Us Game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_dict = states_data.to_dict()
name = states_dict["state"]
x = states_dict["x"]
y = states_dict["y"]

states = []

for i in range(0, 50):
    add_state = State(name[i], (x[i], y[i]), screen)
    states.append(add_state)

screen.mainloop()
