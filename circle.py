import pgzrun
WIDTH = 800
HEIGHT = 800
radius = 160
r = 180
g = 20
b = 170
def draw():
    global radius, r, g, b
    screen.fill("black")
    for i in range (0,15):
        screen.draw.filled_circle((400, 400), radius, (r,g,b))
        radius-=10
        r-=10
        g+=10
#def update():
    #pass    
pgzrun.go()