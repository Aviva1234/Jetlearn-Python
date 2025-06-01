import pgzrun
import random
WIDTH = 600
HEIGHT = 500
m = Actor("mouse")
m.x = 200
m.y = 250
c = Actor("cat")
c.x = 300
c.y = 300
score = 0
game = True
def draw():
    screen.blit("grass", (0,0))
    global score
    if game:
        m.draw()
        c.draw()
    elif not game:
        if score >= 3:
            screen.draw.text(f"Cat wins with {score} points", (100,100), color="white")
        elif score < 3:
            screen.draw.text(f"Mouse wins", (100,100), color="white")
        
def update():
    global score
    if keyboard.w:
        c.y -= 6
    elif keyboard.s:
        c.y += 6
    elif keyboard.d:
        c.x += 6
    elif keyboard.a:
        c.x -= 6
    if keyboard.up:
        m.y -= 5
    elif keyboard.down:
        m.y += 5
    elif keyboard.right:
        m.x += 5
    elif keyboard.left:
        m.x -= 5
    if c.colliderect(m):
        score += 1
        m.x = random.randint(10,290)
        m.y = random.randint(10,490)
        c.x = random.randint(10,290)
        c.y = random.randint(10,490)
def timer():
    global game
    game = False
clock.schedule(timer, 60)
pgzrun.go()