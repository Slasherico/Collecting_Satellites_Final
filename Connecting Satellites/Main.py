import pgzrun
from random import randint
from time import time

WIDTH = 750
HEIGHT = 550

game_over = False
s_time = 0
t_time = 0

TITLE  = ('Connecting Satellites')

Sats = []
lines = []
nexsatel = 0
satnum = 8

def CreateSatellite():
    global s_time
    for S in range(satnum):
        sateli = Actor('satellite')
        sateli.pos = randint(40,WIDTH-40), randint(40,HEIGHT-40)
        Sats.append(sateli)
    s_time = time()

def draw():
    screen.blit('space_background',(0,0))
    num = 1
    for D in Sats:
        D.draw()
        screen.draw.text(str(num),(D.pos[0],D.pos[1]+20), color=(255, 255, 255), fontsize=30)
        num = num + 1
    for line in lines:
        screen.draw.line(line[0],line[1], ('Green'))
    if nexsatel < satnum:
        t_time = time() - s_time
        screen.draw.text(str(round(t_time,1)),(10,10), fontsize=30)
    else:
        screen.draw.text(str(round(t_time,1)),(10,10), fontsize=30)
    if game_over == True:
        screen.fill('Red')
        screen.draw.text('You lost',midtop=(WIDTH//2,10) , fontsize= 70, color=('Orange'))



def update():
    global game_over
    if not game_over:
        t_time = time() - s_time
        if t_time >= 10:
            game_over = True

def on_mouse_down(pos):
    global nexsatel, lines
    if nexsatel < satnum:
        if Sats [nexsatel].collidepoint(pos):
            if nexsatel:
                lines.append((Sats[nexsatel-1].pos,Sats[nexsatel].pos))
            nexsatel=nexsatel+1
        else:
            lines=[]
            nexsatel=0
            
            


CreateSatellite()
pgzrun.go()