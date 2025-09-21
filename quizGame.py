import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 450

totaltime = 10
score = 0

titlebox = Rect((10,10), (580, 60))
questionbox = Rect((10,80), (400, 100))
timebox = Rect((420,80), (170, 100))
answerbox1 = Rect((10,200), (190, 100))
answerbox2 = Rect((220,200), (190, 100))
answerbox3 = Rect((10,310), (190,100))
answerbox4 = Rect((220,310), (190,100))
skipbox = Rect((420, 190), (170, 100))
resetscorebox = Rect((420, 310), (170,100))

def draw():
    global totaltime, score
    screen.fill("black")
    screen.draw.rect(titlebox, "black")
    screen.draw.textbox("Quiz Game", titlebox, color="blue")
    screen.draw.filled_rect(questionbox, "white")
    if totaltime < 0:
        screen.draw.textbox(f"Time's up! Game Over! Score: {score}", questionbox, color="red")
    screen.draw.filled_rect(timebox, "green")
    screen.draw.textbox(f"{totaltime}", timebox, color="black")
    screen.draw.filled_rect(answerbox1, "purple")
    screen.draw.filled_rect(answerbox2, "purple")
    screen.draw.filled_rect(answerbox3, "purple")
    screen.draw.filled_rect(answerbox4, "purple")
    screen.draw.filled_rect(skipbox, "red")
    screen.draw.textbox("Skip", skipbox, color="white")
    screen.draw.filled_rect(resetscorebox, "orange")
    screen.draw.textbox("Reset", resetscorebox, color="white")

def update_time():
    global totaltime
    if totaltime >= 0:
        totaltime -= 1
def update():
    pass

clock.schedule_interval(update_time, 1)
pgzrun.go()