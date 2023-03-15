import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pandas.read_csv("50_states.csv")

all_states = df.state.to_list()
guessed_states = 0
list_of_states = []
while guessed_states < 50:
    if guessed_states ==0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{guessed_states}/50 States correct.", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in df.values:
        guessed_row = df[df["state"] ==answer_state]
        lijstje = guessed_row.values.tolist()
        xcor = lijstje[0][1]
        ycor = lijstje[0][2]
        timmy = turtle.Turtle(visible=False)
        timmy.penup()
        timmy.goto(xcor,ycor)
        timmy.write(answer_state, align="left",  font=("Arial", 8, "normal"))
        guessed_states += 1 
        list_of_states.append(answer_state)

    
for state in list_of_states:
    all_states.remove(state)

my_dict = {'state': all_states}
pandas.DataFrame(my_dict).to_csv('out.csv', index=False)















