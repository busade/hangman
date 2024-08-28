# from turtle import Turtle, Screen
import time, random



# screen = Screen()
# screen.setup(width = 600, height=600)
# screen.bgcolor("black")
# screen.title("Snake game")


# body_part_1 = Turtle("square")
# body_part_1.color("white")

# body_part_2 = Turtle("square")
# body_part_2.color("white")
# body_part_2.goto(-20,0)

# body_part_3= Turtle("square")
# body_part_3.color("white")
# body_part_3.goto(-40,0)

# or use for loop
# positions = [(0,0),(-20,0),(-40,0)]
# screen.tracer(0)
# segments = []
# for p in positions:
#     body = Turtle("square")
#     body.color("white")
#     body.penup()
#     body.goto(p)
#     segments.append(body)

# game_is_on = True

# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     # for s in segments:
#     #     s.forward(20)


#     for seg in range(len(segments)-1,0,-1):
#         new_x=segments[seg - 1].xcor()
#         new_y = segments[seg - 1].ycor()
#         segments[seg].goto(new_x,new_y)


easy_words = ["Apple", "Book", "Cat", "Dog", "Fish", "Tree", "Sun", "Ball", "Milk", "Star"]
medium_words = ["Planet", "Laptop", "Python", "Garden", "Wizard", "Butter", "Secret", "Castle", "Travel", "Rocket"]
hard_words = ["Chrysanthemum", "Unbelievable", "Quarantine", "Phenomenon", "Subterranean", "Hypothesis", "Kaleidoscope", "Synecdoche", "Constellation", "Acknowledgment"]


chosen_word = random.choice(easy_words).lower()

guess = input ("guess a letter").lower()

for l in chosen_word:
    if l == guess:
        print("right")
    else:
        print("wrong")
# screen.exitonclick()