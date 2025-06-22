import pgzrun
import random
import time
WIDTH = 500
HEIGHT = 500
#screen.draw.text(f'Score: {count}',(10,10),color="white")

satellites = []
lines = []
next = 0
total = 0
start = time.time()

num = int(input("How many satellites do you want?"))
for i in range(0,num):
    s = Actor("satellite")
    s.x = random.randint(50,450)
    s.y = random.randint(50,450)
    satellites.append((s,i))

def draw():
    screen.blit("space", (0,0))
    screen.draw.text(f"Time: {int(total)}",(20,20),color="red")
    for sa in satellites:
        sa[0].draw()
        screen.draw.text(f"{sa[1]+1}", (sa[0].x, sa[0].y+20), color="red")
    for line in lines:
        screen.draw.line(line[0],line[1],"red")
    if next>=num:
        screen.blit("space", (0,0))
        screen.draw.text(f"You completed the game in {int(total)} seconds!",(100,100),color="red")
        screen.draw.text(f"Normal time: {num*2} seconds",(120,120),color="red")
def on_mouse_down(pos):
    global lines, next,  total
    if next<num:
        total = time.time()-start
        if satellites[next][0].collidepoint(pos):
            if next:
                lines.append((satellites[next-1][0].pos,satellites[next][0].pos))
            next+=1
            print(lines)
        else:
            lines = []
            next = 0
pgzrun.go()
