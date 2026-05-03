import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

sattelites = []
lines = []
next_sattelite = 0

start_time = 0
total_time = 0
end_time = 0

number_of_satellites = 0

def create_satellites():
    global sattelites
    global start_time
    for count in range(0, number_of_satellites):
        sattelites = actor('sattelite')
        sattelites.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        sattelites.append(sattelites)
    start_time = time()


def draw():
    global sattelites
    global total_time

    screen.blit('background', (0,0))

    for sattelites in sattelites:
        screen.draw.text(str(number), (sattelites.pos[0], sattelites.pos[1]+20))
        sattelites.draw()
        number = number + 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))
    
    if next_sattelite < number_of_satellites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)\
    
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

create_satellites()
draw()