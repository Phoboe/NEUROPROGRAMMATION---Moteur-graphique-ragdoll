
import pygame
from pygame.locals import *
from random import random, randrange
from math import *
import os


from Neuron import Perceptron, Neuron
neuron = Neuron()




pygame.init()

width, height = 1280, 720

window = pygame.display.set_mode((width, height), FULLSCREEN)

pygame.key.set_repeat(400, 30)
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
window.fill((0,0,0))

continuer = True
grav = 0.068



class Bat():
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.alpha = random()*pi*2
        self.lenght = 50
        self.speedAlpha = random()*pi/30
        self.speed = (0, 0)

bat = Bat()



while continuer == True:

    bat.alpha += bat.speedAlpha
    bat.speed = (bat.speed[0], bat.speed[1] + grav)        #gestion de la gravité (tuple)
    bat.x += bat.speed[0]
    bat.y += bat.speed[1]

    A = (bat.x + (cos(bat.alpha   )*bat.lenght/2), bat.y + (sin(bat.alpha   )*bat.lenght/2))
    B = (bat.x + (cos(bat.alpha+pi)*bat.lenght/2), bat.y + (sin(bat.alpha+pi)*bat.lenght/2))

    window.fill((0,0,0))
    pygame.draw.line(window, (0, 255, 0), A, B)
    pygame.display.flip()
    clock.tick(60)







    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
        if event.type == QUIT:
            continuer = False
        souris_x, souris_y = pygame.mouse.get_pos()
        pass

    continue



































''' os.system("timeout /t 3") '''
