# import colorgram as col
#
# rgb_colors_in_image = []
# colors = col.extract('image.jpg', 30)
# for item in colors:
#     red = item.rgb.r
#     green = item.rgb.g
#     blue = item.rgb.b
#     rgb_colors_in_image.append((red, green, blue))
# print(rgb_colors_in_image)

import turtle as tu
import random as rnd

LIST_COLORS = [(224, 156, 75), (30, 105, 150), (14, 53, 90), (163, 17, 43), (228, 209, 96), (170, 92, 30),
               (124, 182, 210), (204, 164, 18), (182, 42, 87), (36, 140, 35), (124, 197, 146), (48, 55, 109),
               (223, 76, 54), (204, 130, 164), (102, 9, 54), (81, 24, 16), (209, 91, 107), (39, 188, 154),
               (147, 213, 172), (1, 82, 120), (143, 207, 223), (83, 72, 39), (229, 181, 157), (95, 101, 166),
               (226, 171, 184), (36, 160, 173)]
# create cursor
cursor = tu.Turtle()
window = tu.Screen()
window.colormode(255)
window.screensize(600, 600)
window.bgcolor((234, 233, 232))
cursor.penup()
cursor.setheading(225)
cursor.forward(225)
first_pos = cursor.pos()
for y in range(1, 11):
    # set heading to East, 0
    cursor.setheading(0)
    if y == 1:
        y_pos = 0 + first_pos[1]
    else:
        y_pos = y * (20 + 30) + first_pos[1]
    x_pos = first_pos[0]
    cursor.setpos((x_pos, y_pos))
    for x in range(1, 11):
        # paint circle of 20
        cursor.pendown()
        next_color = rnd.choice(LIST_COLORS)
        cursor.pencolor(next_color)
        cursor.fillcolor(next_color)
        cursor.dot(20, next_color)
        cursor.penup()
        # move forward 50
        cursor.forward(50)
# wait for user to click in screen
window.exitonclick()
