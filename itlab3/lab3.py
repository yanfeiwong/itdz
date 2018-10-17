import pygame,level_map,time,numpy
import sys
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont2 = pygame.font.SysFont('Comic Sans MS', 60)
gms=0

width,height = 1200,800
mapsize=s_y,s_x=100,100
fake_way=60
block_x=width/s_x
block_y=height/s_y

rtime=60



bg = 93,161,213
blc = 80,80,80
stc = 255,0,0
etc= 255,255,0
hero_op=''

""", pygame.NOFRAME"""

screen = pygame.display.set_mode((width,height))
screen.fill(bg)
pygame.display.set_caption("Lab_3")
textsurface = myfont.render('Lab3', False, (0, 0, 0))
screen.blit(textsurface,(40,40))
textsurface = myfont.render('--A simple maze game', False, (0, 0, 0))
screen.blit(textsurface,(40,80))
textsurface = myfont.render('Instructions:', False, (0, 0, 0))
screen.blit(textsurface,(40,120))
textsurface = myfont.render('Press "R" to start or get a new map', False, (0, 0, 0))
screen.blit(textsurface,(80,160))
textsurface = myfont.render('Press "W,A,S,D" to move', False, (0, 0, 0))
screen.blit(textsurface,(80,200))
textsurface = myfont.render('Press "H" for help', False, (0, 0, 0))
screen.blit(textsurface,(80,240))
bl = pygame.Surface((block_x,block_y))
bl.fill(blc)
sbl = pygame.Surface((block_x,block_y))
sbl.fill(stc)
ebl = pygame.Surface((block_x,block_y))
ebl.fill(etc)
non = pygame.Surface((block_x,block_y))
non.fill(bg)
def draw_level():
    global herox,heroy,gms
    screen.fill(bg)
    for i in range(s_y):
        for j in range(s_x):
            if level[i,j]==0:
                screen.blit(bl,((j)*block_x,(i)*block_y))
            if level[i,j]==1:
                screen.blit(sbl,((j)*block_x,(i)*block_y))
                if gms==0:
                    herox=j
                    heroy=i
                else:
                    screen.blit(non,((j)*block_x,(i)*block_y))
            if level[i,j]==3:
                screen.blit(ebl,((j)*block_x,(i)*block_y))
    gms=1

def iswin(win):
    if win==1:
        textsurface = myfont2.render('You Win!', False, (255, 255, 255))
        screen.blit(textsurface,(1200/2-100,800/2-40))
        pygame.display.update()
    if win==0:
        textsurface = myfont2.render('You Lose!', False, (255, 255, 255))
        screen.blit(textsurface,(1200/2-100,800/2-40))
        pygame.display.update()

def help(really):
    if really==1:
        for i in range(s_y):
            for j in range(s_x):
                if level[i,j]==8:
                    screen.blit(ebl,((j)*block_x,(i)*block_y))
    if really==0:
        for i in range(s_y):
            for j in range(s_x):
                if level[i,j]==8:
                    screen.blit(non,((j)*block_x,(i)*block_y))
                    screen.blit(sbl,((herox)*block_x,(heroy)*block_y))

win=2        
em=0

while 1:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (
            event.type==pygame.KEYDOWN and (
                event.key==pygame.K_ESCAPE)):
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
            stime=time.time()
            gms=0
            win=2
            level=level_map.get_level(s_y,s_x,fake_way)
            draw_level()
            steps=0
        if event.type==pygame.KEYDOWN and event.key==pygame.K_a and gms==1:
            steps=steps+1
            if herox>=1 and level[heroy,herox-1]!=0:
                screen.blit(non,((herox)*block_x,(heroy)*block_y))
                herox=herox-1
                screen.blit(sbl,((herox)*block_x,(heroy)*block_y))
                if level[heroy,herox]==3:
                    win=1

        if event.type==pygame.KEYDOWN and event.key==pygame.K_w and gms==1:
            steps=steps+1
            if heroy>=1 and level[heroy-1,herox]!=0:
                screen.blit(non,((herox)*block_x,(heroy)*block_y))
                heroy=heroy-1
                screen.blit(sbl,((herox)*block_x,(heroy)*block_y))
                if level[heroy,herox]==3:
                    win=1

        if event.type==pygame.KEYDOWN and event.key==pygame.K_d and gms==1:
            steps=steps+1
            if herox<=s_x-2 and level[heroy,herox+1]!=0:
                screen.blit(non,((herox)*block_x,(heroy)*block_y))
                herox=herox+1
                screen.blit(sbl,((herox)*block_x,(heroy)*block_y))
                if level[heroy,herox]==3:
                    win=1

        if event.type==pygame.KEYDOWN and event.key==pygame.K_s and gms==1:
            steps=steps+1
            if heroy<=s_y-2 and level[heroy+1,herox]!=0:
                screen.blit(non,((herox)*block_x,(heroy)*block_y))
                heroy=heroy+1
                screen.blit(sbl,((herox)*block_x,(heroy)*block_y))
                if level[heroy,herox]==3:
                    win=1
        
        if event.type==pygame.KEYDOWN and event.key==pygame.K_h and gms==1:
            em=1
        if event.type==pygame.KEYUP and event.key==pygame.K_h and gms==1:
            em=0
            

                
        
    if gms==1:
            if win==2:
                ntime=time.time()
                tt=60-(ntime-stime)
            if tt<=0:
                win=0
                gms=0
            draw_level()
            help(em)
            iswin(win)
            screen.blit(sbl,((herox)*block_x,(heroy)*block_y))
            textsurface = myfont.render('Time:'+str(int(tt)), False, (0, 0, 0))
            screen.blit(textsurface,(10,10))
            textsurface = myfont.render('Steps:'+str(steps), False, (0, 0, 0))
            screen.blit(textsurface,(10,40))
    pygame.display.update()
