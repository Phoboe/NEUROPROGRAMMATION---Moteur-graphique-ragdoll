
import pymunk
from pymunk.vec2d import Vec2d
import pymunk.pygame_util


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

run = True
grav = 9.81






while run == True:



    window.fill((0,0,0))
    pygame.draw.line(window, (0, 255, 0), (0, height-30), (width, height-30), 1)
    pygame.display.flip()
    clock.tick(60)







    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
        if event.type == QUIT:
            run = False
        souris_x, souris_y = pygame.mouse.get_pos()
        pass

    continue



































''' os.system("timeout /t 3") '''
