'''main.py'''
import turtle as trtl

# wn.setup(900, 1100, 0, 0)
print("hi! welcome in to Zyack's Donuts!")
print("please be specific when you tell me what you want.")
print("i'm hard of hearing.")
bread_color = input("do you want a cake or whole wheat donut?")

wn = trtl.Screen()
wn.tracer(False)

shadow = trtl.Turtle()
shadow.ht()
shadow.speed(0)
shadow.pencolor("#5F6565")
shadow.fillcolor("#5F6565")
shadow.penup()
shadow.goto(0, -185)
shadow.pendown()
shadow.begin_fill()
shadow.circle(350, 360, 4)
shadow.end_fill()
shadow.penup()

plate = trtl.Turtle()
plate.ht()
plate.speed(0)
plate.pencolor("#c1cdcd")
plate.fillcolor("#c1cdcd")
plate.penup()
plate.goto(0, -175)
plate.pendown()
plate.begin_fill()
plate.circle(350, 360, 4)
plate.end_fill()
plate.penup()

bread = trtl.Turtle()
bread.ht()
bread.speed(0)
if bread_color == "cake":
    bread.pencolor("#F2AC45")
    bread.fillcolor("#F2AC45")
elif bread_color == "whole wheat":
    bread.pencolor("#9A702B")
    bread.fillcolor("#9A702B")
else:
    print("you think you can be smart with me?")
    print("get lost chump.")
    print("we sell cake or whole wheat.")
    print("come back later after you've cooled down.")
    exit()
print("i like that one!")
shadow.begin_fill()
shadow.goto(0, -40)
shadow.pendown()
shadow.circle(200)
shadow.end_fill()
shadow.penup()
shadow.ht()
bread.penup()
bread.goto(0, -20)
bread.pendown()
bread.begin_fill()
bread.circle(200)
bread.end_fill()
bread.ht()

icing = trtl.Turtle()
icing.speed(0)
icing_color = input("do you want chocolate, vanilla, or pink icing?")
if icing_color == "pink":
    icing.pencolor("#EE82EE")
    icing.fillcolor("#EE82EE")
    print("pink it is!")
elif icing_color == "chocolate":
    icing.pencolor("#4C2100")
    icing.fillcolor("#4C2100")
    print("chocolate it is!")
elif icing_color == "vanilla":
    icing.pencolor("#F7EDE6")
    icing.fillcolor("#F7EDE6")
    print("vanilla it it!")
else:
    print("that isn't an option. you're gonna get pink, buster.")
    icing.pencolor("#EE82EE")
    icing.fillcolor("#EE82EE")
print("icing...")
icing.penup()
icing.begin_fill()
icing.goto(0, 15)
icing.circle(162)
icing.end_fill()
icing.penup()
icing_bump_size = [14, 16, 14, 18, 24, 30, 14, 14]
for bump in range(50):
    icing.begin_fill()
    icing.goto(0, 180)
    icing.pendown()
    icing.right(380)
    icing.forward(158)
    icing.circle(icing_bump_size.pop())
    icing.end_fill()
    if len(icing_bump_size) == 0:
        icing_bump_size = [12, 16, 18, 24, 30]
    if bump == 30:
        print("icing's done.")

bread.penup()
bread.goto(0, 125)
bread.pendown()
bread.begin_fill()
bread.circle(60)
bread.end_fill()
bread.ht()

shadow.st()
shadow.begin_fill()
shadow.goto(0, 130)
shadow.circle(50)
shadow.end_fill()
shadow.ht()

sprinkle = trtl.Turtle()
sprinkle.speed(0)
sprinkle_yes = input("do you want sprinkles?")
if sprinkle_yes == "yes":
    SPRINKLE_TYPE = input("chocolate or rainbow?")
elif sprinkle_yes == "no":
    sprinkle.ht()
    print("enjoy the donut and thanks for coming in!")
    wn = trtl.Screen()
    wn.mainloop()
else:
    print("huh!? i can't hear ya! here have some sprinkles")
    SPRINKLE_TYPE = "rainbow"
if SPRINKLE_TYPE == "rainbow":
    sprinkle_color = ["red", "yellow", "#EE82EE",
                      "blue", "green", "purple", "white"]
    print("rainbow sprinkles it it!")
elif SPRINKLE_TYPE == "chocolate":
    sprinkle_color = ["#210E00"]
    print("chocolate sprinkles it is!")
else:
    print("huh!? i can't hear ya! here have some sprinkles")
    sprinkle_color = ["red", "yellow", "#EE82EE",
                      "blue", "green", "purple", "white"]
DIRECTION = 90
print("sprinkling...")
for color in range(60):
    new_color = sprinkle_color.pop()
    sprinkle.pencolor(new_color)
    sprinkle.fillcolor(new_color)
    sprinkle.penup()
    sprinkle.goto(0, 190)
    SPRINKLE_X = 0
    SPRINKLE_Y = 75
    sprinkle.right(SPRINKLE_X + color*1.5)
    sprinkle.forward(SPRINKLE_Y + color*1.5)
    SPRINKLE_X = sprinkle.xcor()
    SPRINKLE_Y = sprinkle.ycor()
    sprinkle.setheading(DIRECTION)
    sprinkle.pendown()
    sprinkle.begin_fill()
    sprinkle.right(90)
    for circle in range(2):
        sprinkle.forward(4)
        sprinkle.left(90)
        sprinkle.forward(8)
        sprinkle.left(90)
    sprinkle.end_fill()
    DIRECTION += 65
    if SPRINKLE_TYPE == "rainbow":
        if len(sprinkle_color) == 0:
            sprinkle_color = ["red", "yellow", "#EE82EE",
                              "blue", "green", "purple", "white"]
    elif SPRINKLE_TYPE == "chocolate":
        if len(sprinkle_color) == 0:
            sprinkle_color = ["#210E00"]
sprinkle.ht()

print("bon appetit!")
print()
print("you can exit the store by pressing the red x button btw")

wn.mainloop()
