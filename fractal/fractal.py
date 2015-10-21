import random
import turtle 

def tree(size, myTurtle, c1, c2):
	myTurtle.pensize(size / 10)
	# if size < 10:
	# 	myTurtle.color(c1)
	# else: 
	myTurtle.color(c2)
	if size > 3:
		myTurtle.forward(size)
		myTurtle.left(25)
		tree(size - random.randint(5, 20), myTurtle, c1, c2)
		myTurtle.right(50)
		tree(size - random.randint(5, 20), myTurtle, c1, c2)
		myTurtle.left(25)
		myTurtle.penup()
		myTurtle.backward(size)
		myTurtle.pendown()

def tree1(size, myTurtle, c1, c2):
	myTurtle.pensize(size / 5)
	myTurtle.color(c2)
	if size > 1:
		myTurtle.forward(size)
		myTurtle.left(25)
		tree(size - random.randint(1, 3), myTurtle, c1, c2)
		myTurtle.right(50)
		tree(size - random.randint(1, 3), myTurtle, c1, c2)
		myTurtle.left(25)
		myTurtle.penup()
		myTurtle.backward(size)
		myTurtle.pendown()

def star(size, pen):
	p.begin_fill()
	for i in range(4):
		pen.forward(size)
		pen.right(150)
	p.end_fill()

def fence(p, n):
	if n == 0: 
		p.forward(10)
		return 
	p.forward(40)
	p.left(90)
	p.forward(20)
	p.backward(20)
	p.right(180)
	p.forward(50)
	p.backward(50)
	p.left(90)
	fence(p, n-1)

turtle.setup(width=1500, height=1000)
window = turtle.Screen()
window.bgcolor("#06073B")

p = turtle.Pen()
p.up()
p.color("#EBD300")

for i in range(10):
	p.goto(random.randint(-700, 600), random.randint(200, 300))
	p.down()
	star(5, p)
	p.up()
p.hideturtle()

myTurtle = turtle.Turtle()
col1 = ["#D0F67B", "#D0F67B", "#D0F67B"]
col2 = ["#6F1672", "#420044", "#29002A"]
myTurtle.left(90)
myTurtle.speed(9)
myTurtle.penup()
myTurtle.setpos(-250, -250)
for i in range(6):
	myTurtle.goto(-500+i*60+i, 100)
	myTurtle.pendown()
	tree1(50, myTurtle, None, "#060019")
	myTurtle.penup()
myTurtle.hideturtle()

p = turtle.Pen()
p.up()
p.goto(-550, 140)
p.down()
p.color("#110B1B")
p.pensize(10)
fence(p, 9)
p.up()
p.goto(-530, 100)
p.down()
fence(p, 9)
p.up()
p.hideturtle()

myTurtle.color("#1C1035")
for i in range(6):
	myTurtle.goto(-460+i*60+i, 50)
	myTurtle.pendown()
	tree1(50, myTurtle, None, "#320370")
	myTurtle.penup()
myTurtle.hideturtle()

for i in range(2, -1, -1):
	myTurtle.goto(250-i*70, -380+140*i)
	myTurtle.pendown()
	tree(100-i*3, myTurtle, col1[i], col2[i])
	myTurtle.penup()
myTurtle.pendown()

window.exitonclick()