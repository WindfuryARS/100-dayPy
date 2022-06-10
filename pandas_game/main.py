import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
game_is_on = True
data = pandas.read_csv("50_states.csv")
list_of_state = data['state'].to_list()
#    print(list_of_state)

while game_is_on:
    answer_state = screen.textinput(title=str(score) + "/50 Guess the States",
                                    prompt="What's another stat's name?").capitalize()
    #    print(answer_state)

    if answer_state in list_of_state:
        print("You're right!")
        list_of_state.remove(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        #        print(list_of_state)

        if not list_of_state:
            break
    else:
        #        print(list_of_state)
        pass

screen.exitonclick()

# get x,y where you click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
