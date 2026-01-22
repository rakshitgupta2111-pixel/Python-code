import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

num_sides=int(input("Enter the number of sides of polygon"))
side_length=70
angle=360.0/num_sides
for i in range(num_sides):
   polygon.forward(side_length)
   polygon.right(angle)

turtle.done()

