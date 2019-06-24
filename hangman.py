import turtle
#draw stand
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(250)
turtle.pu()
turtle.goto(0,-60)
turtle.pd()
#head
turtle.circle(30)
#body
turtle.right(90)
turtle.forward(150)

#left arm
turtle.goto(0, -125)
turtle.right(135)
turtle.forward(55)
#right arm
turtle.goto(0, -125)
turtle.right(90)
turtle.forward(55)
#left foot
turtle.pu()
turtle.goto(0, -210)
turtle.pd()
turtle.right(175)
turtle.forward(65)
#right foot
turtle.goto(0, -210)
turtle.left(80)
turtle.forward(65)
print("GAME OVER!")
#face details
#eyes
turtle.pu()
turtle.goto(-5, -15)
turtle.pd()
turtle.right(75)
turtle.forward(10)
turtle.pu()
turtle.goto(-10, -15)
turtle.pd()
turtle.left(55)
turtle.forward(10)
#turtle.circle(4)

turtle.pu()
turtle.goto(15, -20)
turtle.pd()
turtle.pd()
turtle.right(60)
turtle.forward(10)
turtle.pu()
turtle.goto(10, -20)
turtle.pd()
turtle.left(55)
turtle.forward(10)
#turtle.circle(4)

#mouth
turtle.pu()
turtle.goto(-15, -35)
turtle.pd()
turtle.left(55)
turtle.forward(20)
#turtle.backward(8)
turtle.pu()
turtle.goto(-15, -35)
turtle.pd()
turtle.forward(40)
turtle.backward(20)
turtle.right(90)
turtle.forward(10)
turtle.circle(5, 180)
turtle.forward(10)
turtle.left(90)
turtle.forward(4)
turtle.left(90)
turtle.pu()
turtle.forward(2)
turtle.pd()
turtle.forward(7)
turtle.pu()
turtle.home()


print(turtle.position())








