import random, pygame, sys
from pygame.locals import *


color=(255,255,255)
fondo=pygame.image.load('images/stages/fondo2.png')
nivel1=pygame.image.load('images/extras/1E.png')
nivel11=pygame.image.load('images/extras/11E.png')
nivel2=pygame.image.load('images/extras/2E.png')
nivel21=pygame.image.load('images/extras/21E.png')
nivel3=pygame.image.load('images/extras/3E.png')
nivel31=pygame.image.load('images/extras/31E.png')
atras=pygame.image.load('images/extras/atras.png')
atras1=pygame.image.load('images/extras/atras1.png')


class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,(0,0,1,1))
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self, nivel1,nivel11,x=100,y=200):
        self.imagen_normal=nivel1
        self.imagen_seleccion=nivel11
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        screen.blit(self.imagen_actual, self.rect)


def main():
    pygame.init()
    pygame.display.set_caption("Trash War")
    screen = pygame.display.set_mode((500,500))

    boton1 = Boton(nivel1,nivel11,130,10)
    boton2 = Boton(nivel2,nivel21,130,170)
    boton3 = Boton(nivel3,nivel31,130,330)
    boton4 = Boton(atras,atras1,10,460)
    cursor1 = cursor()
    reloj1 = pygame.time.Clock()

    while True:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton4.rect):
                    pygame.quit()

            if event.type==QUIT:
                pygame.quit()
                sys.exit(0)
        reloj1.tick(20)

        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        boton4.update(screen,cursor1)
        pygame.display.update()

main()
