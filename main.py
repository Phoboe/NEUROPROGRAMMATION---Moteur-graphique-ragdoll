import pygame
from pygame.locals import *
from random import random, randrange
from math import *
import os


from Neuron import Perceptron, Neuron
neuron = Neuron()
from Perso import *



pygame.init()

width, height = 1280, 720

window = pygame.display.set_mode((width, height), FULLSCREEN)

pygame.key.set_repeat(400, 30)
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
window.fill((0,0,0))

continuer = True
grav = 0.060
pressed = False



class Bat():
    def __init__(self):
        self.A = (width/2, height/2)
        self.B = (self.A[0] + 100, self.A[1] + 100)
        self.lenght = sqrt((self.A[0]-self.B[0])**2+(self.A[1]-self.B[1])**2)
        self.speedA = (random()*10-5, -random()*10)
        self.speedB = (random()*10-5, -random()*10)
        return None

    def constrain(self):
        dx = self.A[0] - self.B[0]
        dy = self.A[1] - self.B[1]
        lenght = sqrt((dx*dx) + (dy*dy))
        percent = ((lenght - self.lenght)/lenght)/2
        offx = dx * percent
        offy = dy * percent

        self.A = add(self.A, (-offx,-offy))
        self.B = add(self.B, ( offx, offy))
    pass
bat = Bat()


def add(prime, second):
    ''' Additionne deux tuples doubles. (le 1er avec le 2eme) '''
    prime = (prime[0] + second[0], prime[1] + second[1])
    return prime

def integ(prime):
    ''' Retourne le tuple double en valeurs int '''
    return (int(prime[0]), int(prime[1]))


while continuer == True:

    window.fill((0,0,0))

    #bat.speedA = (bat.speedA[0], bat.speedA[1] + grav) #la ligne du dessous le fait tout aussi bien
    bat.speedA = add(bat.speedA, (0, grav)) # on fait marcher la gravité
    bat.speedB = add(bat.speedB, (0, grav))
    #bat.A = (bat.A[0] + bat.speedA[1], bat.A[1] + bat.speedA[1]) # la ligne du dessous le fait tout aussi bien (pareil pour B)
    bat.A = add(bat.A, bat.speedA)
    bat.B = add(bat.B, bat.speedB)

    ### Gestion de la collision
    if bat.A[1] > height-10:
        bat.A = (bat.A[0], height - 10.1)
        bat.speedA = (0.2 * bat.speedA[0], -0.5 * bat.speedA[1])
    if bat.B[1] > height-10:
        bat.B = (bat.B[0], height - 10.1)
        bat.speedB = (0.2 * bat.speedB[0], -0.5 * bat.speedB[1])

    if bat.A[0] > width:
        bat.A = (width - 0.05, bat.A[1])
        bat.speedA = (-0.6 * bat.speedA[0], bat.speedA[1])
    if bat.B[0] > width:
        bat.B = (width - 0.05, bat.B[1])
        bat.speedB = (-0.6 * bat.speedB[0], bat.speedB[1])
    if bat.A[0] < 0:
        bat.A = (0.05, bat.A[1])
        bat.speedA = (-0.6 * bat.speedA[0], bat.speedA[1])
    if bat.B[0] < 0:
        bat.B = (0.05, bat.B[1])
        bat.speedB = (-0.6 * bat.speedB[0], bat.speedB[1])
    ### Fin Gestion collision





    ### Contraintes
    bat.constrain()
    ### Fin Contraintes




    window.fill((0,0,0))
    pygame.draw.line(window, (255, 150, 150), integ(bat.A), integ(bat.B), 2)
    pygame.draw.circle(window, (255, 0, 0), integ(bat.A), 3)
    pygame.draw.circle(window, (255, 0, 0), integ(bat.B), 3)
    pygame.display.flip()
    clock.tick(60)







    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
        if event.type == QUIT:
            continuer = False
        pressed = pygame.mouse.get_pressed()[0]
        souris_x, souris_y = pygame.mouse.get_pos()
        pass

    continue



































''' os.system("timeout /t 3") '''
