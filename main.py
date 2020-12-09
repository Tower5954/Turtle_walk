import turtle as t
import random

mike = t.Turtle()

######Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
mike.pensize(15)
mike.speed("fastest")

for _ in range(200):
    mike.color(random.choice(colours))
    mike.forward(30)
    mike.setheading(random.choice(directions))
