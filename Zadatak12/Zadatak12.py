import turtle

screen = turtle.Screen()
screen.bgcolor("White")
brush = turtle.Turtle()
brush.color("Teal")
brush.width(2)
brush.up()
brush.goto(-200, -150)
brush.down()
brush.fillcolor("Teal")
brush.begin_fill()
brush.forward(100)
brush.left(90)
brush.forward(30)
brush.left(90)
brush.forward(70)
brush.right(90)
brush.forward(50)
brush.left(90)
brush.forward(20)
brush.right(90)
brush.forward(50)
brush.right(90)
brush.forward(20)
brush.left(90)
brush.forward(50)
brush.left(90)
brush.forward(30)
brush.left(90)
brush.forward(180)
brush.end_fill()
brush.up()
brush.goto(60, -150)
brush.down()
brush.fillcolor("Teal")
brush.begin_fill()
brush.left(90)
brush.backward(100)
brush.right(90)
brush.backward(30)
brush.right(90)
brush.backward(70)
brush.left(90)
brush.backward(50)
brush.right(90)
brush.backward(20)
brush.left(90)
brush.backward(50)
brush.left(90)
brush.backward(20)
brush.right(90)
brush.backward(50)
brush.right(90)
brush.backward(30)
brush.right(90)
brush.backward(180)
brush.end_fill()
brush.up()
brush.goto(-5, 40)
brush.down()
brush.fillcolor("Teal")
brush.begin_fill()
brush.forward(70)
brush.left(90)
brush.forward(30)
brush.left(90)
brush.forward(70)
brush.left(90)
brush.forward(30)
brush.end_fill()
brush.up()
brush.goto(-135, 40)
brush.down()
brush.fillcolor("Teal")
brush.begin_fill()
brush.forward(30)
brush.left(90)
brush.forward(70)
brush.left(90)
brush.forward(30)
brush.left(90)
brush.forward(70)
brush.end_fill()
brush.up()
brush.goto(-20, -70)
brush.down()
brush.fillcolor("Teal")
brush.begin_fill()
brush.left(90)
brush.backward(100)
brush.left(90+45)
brush.backward(40)
brush.right(90+45)
brush.forward(40)
brush.left(45)
brush.forward(40)
brush.end_fill()
brush.up()
brush.goto(-20, -30)
brush.down()
brush.width(20)
brush.dot()
brush.up()
brush.goto(-120, -30)
brush.down()
brush.width(20)
brush.dot()

turtle.exitonclick()