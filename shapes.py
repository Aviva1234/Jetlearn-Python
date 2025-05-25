import pgzrun
WIDTH = 800
HEIGHT = 800
width = 100
height = 700
r = 180
g = 20
b = 170
def draw():
    global width, height, r, g, b
    screen.fill("black")
    for i in range (0,20):
        r1 = Rect((0,0),(width, height))
        r1.center = 300,300
        screen.draw.rect(r1, (r,g,b))
        width+=20
        height-=20
        r-=5
        g+=5
#def update():
    #pass    
pgzrun.go()