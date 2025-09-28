import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 450

totaltime = 10
score = 0

titlebox = Rect((10,10), (300, 60))
questionbox = Rect((10,80), (400, 100))
timebox = Rect((420,80), (170, 100))
answerbox1 = Rect((10,200), (190, 100))
answerbox2 = Rect((220,200), (190, 100))
answerbox3 = Rect((10,310), (190,100))
answerbox4 = Rect((220,310), (190,100))
skipbox = Rect((420, 190), (170, 100))
resetscorebox = Rect((420, 310), (170,100))
questions = []
questionIndex = 0

def draw():
    global totaltime, score, current_question, titlebox, questionbox, timebox, answerbox1, answerbox2, answerbox3, answerbox4, skipbox, resetscorebox
    screen.fill("black")
    screen.draw.rect(titlebox, "black")
    screen.draw.textbox(f"Quiz Game | Score: {score}", titlebox, color="blue")
    screen.draw.filled_rect(questionbox, "white")
    screen.draw.textbox(current_question[0].strip(), questionbox, color="green")
    screen.draw.filled_rect(timebox, "green")
    screen.draw.textbox(f"{totaltime}", timebox, color="black")
    screen.draw.filled_rect(answerbox1, "purple")
    screen.draw.textbox(current_question[1].strip(), answerbox1, color="pink")
    screen.draw.filled_rect(answerbox2, "purple")
    screen.draw.textbox(current_question[2].strip(), answerbox2, color="pink")
    screen.draw.filled_rect(answerbox3, "purple")
    screen.draw.textbox(current_question[3].strip(), answerbox3, color="pink")
    screen.draw.filled_rect(answerbox4, "purple")
    screen.draw.textbox(current_question[4].strip(), answerbox4, color="pink")
    screen.draw.filled_rect(skipbox, "red")
    screen.draw.textbox("Skip", skipbox, color="white")
    screen.draw.filled_rect(resetscorebox, "orange")
    screen.draw.textbox("Reset", resetscorebox, color="white")

def update_time():
    global totaltime, current_question
    if totaltime > 0:
        totaltime -= 1
    else:
        current_question = ["Time's up! Game Over! Click Reset to play again.", "", "", "", "", "5"]
def update():
    global titlebox
    titlebox.x = titlebox.x-1
    if titlebox.right < 0: 
        titlebox.left = WIDTH
def read_file():
    global questions, questionIndex
    file = open("Python\PythonGameDeveloper\questions.txt", "r")
    for line in file:
        questions.append(line)
        questionIndex += 1
    random.shuffle(questions)
    print(questions)
    file.close()
def read_questions():
    global questionIndex,questions
    return questions.pop(0).split("|")
read_file()
current_question = read_questions()

answerBoxes = [answerbox1, answerbox2, answerbox3, answerbox4]
def on_mouse_down(pos):
    global current_question, score, totaltime, skipbox
    index = 1
    for box in answerBoxes:
        if box.collidepoint(pos):
            if index == int(current_question[5].strip()): 
                score += 1
                print(index)
                if questions:
                    current_question = read_questions()
                    totaltime = 10
            else:
                current_question = ["Incorrect. Game Over! Click Reset to play again.", "", "", "", "", "5"]
                totaltime = 0
        index += 1
        if skipbox.collidepoint(pos):
            if questions and totaltime > 0:
                    current_question = read_questions()
                    totaltime = 10
            else:
                current_question = ["Game Over! Click Reset to play again.", "", "", "", "", "5"]
                totaltime = 0
        if resetscorebox.collidepoint(pos):
            score = 0
            totaltime = 10
            questions.clear()
            read_file()
            current_question = read_questions()

clock.schedule_interval(update_time, 1)
pgzrun.go()