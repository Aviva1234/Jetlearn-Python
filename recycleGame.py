import pgzrun
import random

WIDTH = 1210
HEIGHT = 908

final_level = 5
current_level = 1
items = ["bottle", "plastic-bag", "plastic-bottle", "potato-chips", "paper-bag"]
game = True
gameComplete = False
actors = []
animations = []

def draw():
    screen.blit("recycle-diagram", (0, 0))
    if gameComplete:
        screen.draw.text("You Win!", (WIDTH/2, HEIGHT/2), background="green", color="black")
    elif not game:
        screen.draw.text("Game Over", (WIDTH/2, HEIGHT/2), background="red", color="black")
    else:
        for actor in actors:
            actor.draw()
    
def handle_game_over():
    global game
    game = False
def update():
    global current_level, final_level, actors, animations, items
    if len(actors) == 0:
        make_actors()
        for actor in actors:
            duration = 10-current_level
            actor.anchor = ("center", "bottom")
            animation = animate(actor, y=HEIGHT, duration=duration, on_finished=handle_game_over)
            animations.append(animation)
def on_mouse_down(pos):
    global actors, current_level, final_level, animations, gameComplete
    for actor in actors:
        if actor.image == "paper-bag":
            if actor.y > HEIGHT - 100:
                actors.remove(actor)
        if actor.collidepoint(pos):
            if actor.image == "paper-bag":
                handle_game_over()
            else:
                actors.remove(actor)
                if current_level == final_level and not actors:
                    gameComplete = True
                else:
                    if not actors:
                        for animation in animations:
                            if animation.running:
                                animation.stop()
                        current_level += 1
                        actors = []
                        animations = []

def make_actors():
    global actors, current_level, items
    pb = Actor("paper-bag", (random.randint(50, WIDTH-50), 0))
    actors.append(pb)
    for i in range(current_level):
        img = random.choice(items)
        gap = WIDTH // (current_level + 1)
        item = Actor(img)
        item.x = (i + 1) * gap
        item.y = 0
        actors.append(item)
    

pgzrun.go()