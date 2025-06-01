import pgzrun
import random
import time
WIDTH = 500
HEIGHT = 500
a = Actor("pink-alien")
a.x = 200
a.y = 200
count = 0
game = True
def draw():
    if game:
        screen.fill("black")
        a.draw()
        screen.draw.text(f'Score: {count}',(10,10),color="white")
    elif not game:
        screen.fill("red")
        screen.draw.text(f'Game Over! Your score was: {count}',(100,100),color="white")
def timer():
    global game
    game= False

def on_mouse_down(pos):
    global count
    print(a.collidepoint(pos))
    if a.collidepoint(pos):
        a.x = random.randint(50,350)
        a.y = random.randint(50,350)
        count += 1
clock.schedule(timer,60)
pgzrun.go()