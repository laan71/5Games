import turtle
import random

screen = turtle.Screen()
screen.title("Dropping Hearts by Laila")
screen.bgpic("img/bg.gif")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

# Add the shapes
girl = "img/girl.gif"
heart = "img/heart.gif"

screen.register_shape(girl)
screen.register_shape(heart)


class Targets(turtle.Turtle):
    def __init__(self):
        super().__init__(shape=heart)
        self.up()


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__(shape=girl)
        self.penup()
        self.goto(0, -230)
        self.up()

    def move_right(self):
        if self.xcor() < 350:
            self.goto(self.xcor() + 30, self.ycor())

    def move_left(self):
        if self.xcor() > -350:
            self.goto(self.xcor() - 30, self.ycor())


player = Player()
targets = []
target_number = 3
score = 0
drops = 3

game_over = False

screen.onkey(player.move_right, 'Right')
screen.onkey(player.move_left, 'Left')

while not game_over:

    delay = random.random()
    if len(targets) < target_number and delay < 0.05:
        target = Targets()
        target.goto(random.randint(-370, 355), 280)
        target.dy = random.randint(1, 5)*-0.5
        targets.append(target)

    for i in targets:
        # Move down
        i.goto(i.xcor(), i.ycor() + i.dy)

        # Game point
        if i.distance(player) <= 40:
            score += 1
            i.goto(1000, 1000)
            targets.remove(i)

        # Remove from list if below screen, and count drops
        if i.ycor() < -320:
            i.goto(1000, 1000)
            targets.remove(i)
            drops -= 1

    if drops <= 0:
        game_over = True

    screen.update()
