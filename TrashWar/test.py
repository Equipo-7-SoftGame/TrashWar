import random, pygame, sys
from pygame.locals import *

color=(255,255,255)
fondo=pygame.image.load('images/stages/stage1.png')
chara=pygame.image.load('images/characters/sub.png')
bote=pygame.image.load('images/characters/bote1.png')



def main():
    fondo = pygame.image.load('images/stages/stage1.png')
    chara = pygame.image.load('images/characters/sub.png')
    bote = pygame.image.load('images/characters/bote1.png')

    chara_x=10
    chara_y=400
    botx=5
    boty=128
    pygame.init()
    pygame.display.set_caption("Trash War")
    screen = pygame.display.set_mode((1024,576))
    reloj= pygame.time.Clock()

    while True:
       screen.blit(fondo,(0,0))
       screen.blit(chara,((chara_x,chara_y)))
       screen.blit(bote,((botx,boty)))
       botx=botx+5
       for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit(0)

       if event.type == KEYDOWN:
           if event.key == K_LEFT:
               chara_x -= 8
           if event.key == K_RIGHT:
               chara_x += 8
           if event.key == K_UP:
               chara_y -= 8
           if event.key == K_DOWN:
               chara_y += 8

       if chara_x < -10:
           chara_x = -10
       if chara_y < -10:
           chara_y = -10
       if chara_x > 1020:
           chara_x = 1020
       if chara_y > 1020:
           chara_y = 1020
       pygame.display.update()
main()
