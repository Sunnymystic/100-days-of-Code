import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_df= pandas.read_csv('50_states.csv')
states_list = states_df.state.to_list()
correctly_guess_states = []
total = 50
while len(correctly_guess_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(correctly_guess_states)}/{total} States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()
    df_match = states_df[states_df.state == answer_state]
    try:
        state_name = df_match.state.item()
    except ValueError:
        continue

    if state_name == answer_state:
        correctly_guess_states.append(answer_state)
        x_coord = float(df_match.x.item())
        y_coord = float(df_match.y.item())
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x_coord, y_coord)
        t.color("black")
        t.write(df_match.state.values[0], align="center", font=("Arial", 8, "normal"))

remaining_states = [x for x in states_list if x not in correctly_guess_states]
df = pandas.DataFrame(remaining_states)
df.to_csv('states you missed in 50_states quiz')

screen.bye()