import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
my_gif = "blank_states_img.gif"
screen.addshape(my_gif)
turtle.shape(my_gif)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)}/50 Guessed states",
                                    prompt="What's another states name?").title()

    if answer_state == "Exit":
        unknown_states = []
        for state in all_states:
            if state not in guessed_states:
                unknown_states.append(state)
        new_data = pandas.DataFrame(unknown_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        location = data[data.state == answer_state]
        t.goto(int(location.x), int(location.y))
        t.write(answer_state)


# states to learn



def get_mouse_coordinates(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_coordinates)
# screen.exitonclick()
turtle.mainloop()
