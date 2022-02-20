from turtle import Turtle, Screen

screen = Screen()
# ---- Developed By iChampignon ----
# 2. Taking colors from the list

turtle = Turtle("turtle")
turtle.hideturtle()
color = ['brown',
         'brown',
         'brown',
         'brown',
         'brown',

         'blue',
         'blue',
         'blue',
         'blue',
         'blue',
         'yellow',
         'yellow',
         'yellow',
         'yellow',
         'yellow',
         'red',
         'red',
         'red',
         'red',
         'red',
         ]

# 3. Taking 20 circles and Radius

CIRCLES = [
    ((0, -5), 5,),
    ((0, -10), 10),
    ((0, -15), 15),
    ((0, -20), 20),
    ((0, -25), 25),

    ((0, -30), 30),
    ((0, -35), 35),
    ((0, -40), 40),
    ((0, -45), 45),
    ((0, -50), 50),

    ((0, -55), 55),
    ((0, -60), 60),
    ((0, -65), 65),
    ((0, -70), 70),
    ((0, -75), 75),

    ((0, -80), 80),
    ((0, -85), 85),
    ((0, -90), 90),
    ((0, -95), 95),
    ((0, -100), 100),
]
index = 0

# 4. Including "for loop" for circulating circles in starting position (x, y)

for position, radius in CIRCLES:
    turtle.penup()
    turtle.pencolor(color[index])
    turtle.setposition(position)
    turtle.pendown()
    turtle.circle(radius)
    index = index + 1

# 5. Hiding the turtle prompt

turtle.hideturtle()

