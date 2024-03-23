import time
import random
from turtle import Screen, Turtle

class Food(Turtle):

    def __init__(self, color='cyan'):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(color)
        self.speed('slowest')
        self.change_position()

    def change_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(0,270)
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def update_score(self):
        current_score = f'Score: {self.score}'
        self.clear()
        self.write(arg=current_score, align=ALIGNMENT, font=FONT)
        self.score += 1

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, color='white'):
        self.color = color
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.color('yellow')

    def create_snake(self):
        for i in range(3):
            pos = (-20*i, 0)
            self.add_part(pos)

    def add_part(self, position):
        snake_part = Turtle(shape='square')
        snake_part.color(self.color)
        snake_part.penup()
        snake_part.goto(position)
        self.snake_body.append(snake_part)

    def extend_snake(self):
        self.add_part(self.snake_body[-1].position())

    def move(self):
        for part_num in range(len(self.snake_body)-1, 0, -1):
            new_position = self.snake_body[part_num-1].position()
            self.snake_body[part_num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("SNAKE GAME")
window.tracer(0)

allowed_colors = ['red','violet','pink','white','yellow','green','blue','brown','orange']
food_color = window.textinput('Food Color', 'Enter The Color Of Food: ').lower()
snake_color = window.textinput('Snake Color', 'Enter The Color Of Snake: ').lower()

if food_color not in allowed_colors or snake_color not in allowed_colors:
    window.textinput('Wrong Input', 'Press Enter To Continue')
    food_color = 'cyan'
    snake_color = 'white'

snake = Snake(snake_color)
food = Food(food_color)
scoreboard = Scoreboard()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

game_over = False
while not game_over:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.change_position()
        snake.extend_snake()
        scoreboard.update_score()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_over = True
        scoreboard.game_over()

    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            game_over = True
            scoreboard.game_over()

window.exitonclick()

