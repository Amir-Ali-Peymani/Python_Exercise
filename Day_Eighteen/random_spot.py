#import colorgram
import turtle as t
import random

#rgb_colors = []
#colors = colorgram.extract('D:\\Projects\\Python\\Python_Exercise\\Day_Eighteen\\787682.jpg', 30)

#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#print(rgb_colors)
t.colormode(255)
colors = [(5, 7, 11), (37, 9, 8), (43, 13, 16), (114, 36, 31), (130, 69, 62), (164, 149, 131),
            (13, 17, 16), (110, 35, 38), 
          (121, 63, 67), (74, 78, 85), (195, 90, 77), (162, 133, 88),
           (157, 168, 156), (208, 225, 210), (204, 81, 86), (61, 62, 69), (219, 213, 191), 
           (229, 202, 88), (67, 65, 56), (86, 94, 88), (212, 116, 120), (137, 162, 170), 
           (182, 200, 184), (200, 230, 235), (251, 156, 144), (251, 214, 1), (60, 65, 63), 
           (122, 131, 122), (55, 67, 70), (242, 149, 153)]

max = t.Turtle()
t.penup()
t.speed(0)
t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100
for a in range(1, number_of_dots+1):
    t.dot(20, random.choice(colors))
    t.forward(50)
    if a % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)       


screen = t.Screen()
screen.exitonclick()




