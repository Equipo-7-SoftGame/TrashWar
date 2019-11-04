import pygame
import sys
from pygame.locals import *


color = (255, 255, 255)
fondo = pygame.image.load('images/stages/fondo.jpg')
jugar = pygame.image.load('images/button/jugar.png')
jugar1 = pygame.image.load('images/button/jugar1.png')
ajustes = pygame.image.load('images/button/ajustes.png')
ajustes1 = pygame.image.load('images/button/ajustes1.png')
salir = pygame.image.load('images/button/salir.png')
salir1 = pygame.image.load('images/button/salir1.png')


def main():
    pygame.init()
    pygame.display.set_caption("Trash War")
    screen = pygame.display.set_mode((500, 500))

    boton1 = Boton(jugar, jugar1, 150, 200)
    boton2 = Boton(ajustes, ajustes1, 150, 300)
    boton3 = Boton(salir, salir1, 150, 400)
    cursor1 = Cursor()
    reloj1 = pygame.time.Clock()

    while True:
        screen.blit(fondo, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    Juego()
                if cursor1.colliderect(boton2.rect):
                    Ajustes()
                if cursor1.colliderect(boton3.rect):
                    pygame.quit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        reloj1.tick(20)

        cursor1.update()
        boton1.update(screen, cursor1)
        boton2.update(screen, cursor1)
        boton3.update(screen, cursor1)
        pygame.display.update()


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, (0, 0, 1, 1))

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()


class Boton(pygame.sprite.Sprite):
    def __init__(self, jugar, jugar1, x=150, y=200):
        self.imagen_normal = jugar
        self.imagen_seleccion = jugar1
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)

    def update(self, screen, Cursor):
        if Cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        screen.blit(self.imagen_actual, self.rect)


def Juego():
    fondo = pygame.image.load('images/stages/fondo2.png')
    nivel1 = pygame.image.load('images/extras/1E.png')
    nivel1A = pygame.image.load('images/extras/11E.png')
    nivel2 = pygame.image.load('images/extras/2E.png')
    nivel2A = pygame.image.load('images/extras/21E.png')
    nivel3 = pygame.image.load('images/extras/3E.png')
    nivel3A = pygame.image.load('images/extras/31E.png')
    atras = pygame.image.load('images/extras/atras.png')
    atras1 = pygame.image.load('images/extras/atras1.png')

    pygame.init()
    pygame.display.set_caption("Trash War")
    screen = pygame.display.set_mode((500, 500))

    boton1 = Boton(nivel1, nivel1A, 130, 10)
    boton2 = Boton(nivel2, nivel2A, 130, 170)
    boton3 = Boton(nivel3, nivel3A, 130, 330)
    boton4 = Boton(atras, atras1, 10, 460)
    cursor1 = Cursor()
    reloj1 = pygame.time.Clock()

    while True:
        screen.blit(fondo, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    Nivel1()
                if cursor1.colliderect(boton4.rect):
                    main()

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        reloj1.tick(20)

        cursor1.update()
        boton1.update(screen, cursor1)
        boton2.update(screen, cursor1)
        boton3.update(screen, cursor1)
        boton4.update(screen, cursor1)
        pygame.display.update()


def Ajustes():
    fondo = pygame.image.load('images/stages/fondo2.png')
    cursor1 = Cursor()

    atras = pygame.image.load('images/extras/atras.png')
    atras1 = pygame.image.load('images/extras/atras1.png')
    boton1 = pygame.image.load('images/extras/image3.png')
    boton2 = pygame.image.load('images/extras/image4.png')
    boton3 = pygame.image.load('images/extras/image5.png')
    derecha1 = pygame.image.load('images/extras/derecha1.png')
    derecha2 = pygame.image.load('images/extras/derecha2.png')
    flechas = pygame.image.load('images/extras/flechas.png')
    flechas1 = pygame.image.load('images/extras/flechas1.png')
    flechasG = pygame.image.load('images/extras/flechasG.png')
    izquierda1 = pygame.image.load('images/extras/izquierda1.png')
    izquierda2 = pygame.image.load('images/extras/izquierda2.png')
    s1 = pygame.image.load('images/extras/s1.png')
    s2 = pygame.image.load('images/extras/s2.png')
    s3 = pygame.image.load('images/extras/s3.png')
    s4 = pygame.image.load('images/extras/s4.png')
    sg = pygame.image.load('images/extras/SG1.png')
    sg1 = pygame.image.load('images/extras/SG.png')
    wasd = pygame.image.load('images/extras/wasd.png')
    wasd1 = pygame.image.load('images/extras/wasd1.png')
    wasdG = pygame.image.load('images/extras/wasdG.png')


    pygame.init()
    pygame.display.set_caption("Trash War")
    screen = pygame.display.set_mode((500, 500))

    reloj = pygame.time.Clock()
    boton4 = Boton(atras, atras1, 10, 460)
    botons = Boton(s1, s2, 200, 100)
    botons2 = Boton(sg1, sg1, 260, 100)
    botons3 = Boton(s1, s2, 200, 230)
    botons4 = Boton(sg1, sg1, 260, 230)
    botonder = Boton(derecha1, derecha2, 300, 385)
    botonizq = Boton(izquierda1,izquierda2,160,385)
    #Guapo ;)
    botonF = Boton(flechas, flechas1, 230, 385)
    botonW = Boton(wasdG, wasdG, 230, 385)

    while True:
        screen.blit(fondo, (0, 0))
        screen.blit(boton1, (160, 30))
        screen.blit(boton2, (160, 160))
        screen.blit(boton3, (160, 290))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botons):
                    botons = Boton(sg, sg, 200, 100)
                    botons2 = Boton(s3, s4, 260, 100)
                if cursor1.colliderect(botons2):
                    botons2 = Boton(sg1, sg1, 260, 100)
                    botons = Boton(s1, s2, 200, 100)
                if cursor1.colliderect(botons3):
                    botons3 = Boton(sg, sg, 200, 230)
                    botons4 = Boton(s3, s4, 260, 230)
                if cursor1.colliderect(botons4):
                    botons4 = Boton(sg1, sg1, 260, 230)
                    botons3 = Boton(s1, s2, 200, 230)

                if cursor1.colliderect(botonF):
                    botonF = Boton(flechasG, flechasG, 200, 365)
                    botonW = Boton(wasd, wasd1, 260, 365)
                if cursor1.colliderect(botonW):
                    botonF = Boton(flechas, flechas1, 200, 365)
                    botonW = Boton(wasdG, wasdG, 260, 365)
                if cursor1.colliderect(boton4):
                    main()

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        reloj.tick(20)

        cursor1.update()
        boton4.update(screen, cursor1)
        botons.update(screen, cursor1)
        botons2.update(screen, cursor1)
        botons3.update(screen, cursor1)
        botons4.update(screen, cursor1)
        botonF.update(screen, cursor1)
        botonW.update(screen, cursor1)
        botonizq.update(screen, cursor1)
        botonder.update(screen, cursor1)
        pygame.display.update()


def Nivel1():
    fondo = pygame.image.load('images/stages/stage1.png')
    chara = pygame.image.load('images/characters/sub.png')
    bote = pygame.image.load('images/characters/barco1.png')

    chara_x = 10
    chara_y = 400
    botx = 5
    boty = 80
    pygame.init()
    pygame.display.set_caption("Trash War")
    screen = pygame.display.set_mode((1024,576))
    reloj= pygame.time.Clock()

    while True:
        screen.blit(fondo, (0, 0))
        screen.blit(chara, ((chara_x, chara_y)))
        screen.blit(bote, ((botx, boty)))
        botx = botx+8
        for event in pygame.event.get():
            if event.type == QUIT:
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
        if chara_y < 175:
            chara_y = 175
        if chara_x > 1020:
            chara_x = 1020
        if chara_y > 1020:
            chara_y = 1020
        pygame.display.update()


main()
