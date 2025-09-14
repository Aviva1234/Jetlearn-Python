import pgzrun
import random
#.wav & .ogg files can be used for sound effects and music
WIDTH = 600
HEIGHT = 500
game = True
score = 0
level = 1
wasps = []
m = Actor("starshooter")
m.x = 300
m.y = 400
bullets = []
def draw():
    screen.blit("space", (0,0))
    global score
    screen.draw.text(f"Score: {score}", (10,10), color="white")
    if game:
        m.draw()
        for b in bullets:
            b.draw()
        for w in wasps:
            w.draw()
def update():
    global game
    global score
    global level
    if keyboard.right:
        m.x += 5
    elif keyboard.left:
        m.x -= 5
    if m.x >= 550:
        m.x = 550
    elif m.x <= 40:
        m.x = 40
    for b in bullets:
        b.y -= 10
        if b.y < 0:
            bullets.remove(b)
    for w in wasps:
        w.y+=0.2
        if w.y > 550:
            game = False
    for b in bullets:
        for w in wasps:
            if b.colliderect(w):
                bullets.remove(b)
                wasps.remove(w)
                score+=10
            if len(wasps) == 0:
                level+=1
                spawn_wasps()
def on_key_down(key):
    if key == keys.SPACE:
        b = Actor("bullet")
        b.x = m.x
        b.y = m.y - 30
        bullets.append(b)
        sounds.eep.play()
def spawn_wasps():
    global level
    for o in range(level):
        for i in range(0,6):
            w = Actor("wasp")
            w.x = 50+i*100
            w.y = 50+o*70
            wasps.append(w)
spawn_wasps()
pgzrun.go()