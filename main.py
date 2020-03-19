import pygame
from pygame.locals import *
from random import random, randrange
from math import *
import os


from Neuron import Perceptron, Neuron
neuron = Neuron()
from Perso import *
import constructor as constr



pygame.init()

width, height = 1280, 720

window = pygame.display.set_mode((width, height), FULLSCREEN)

pygame.key.set_repeat(400, 30)
pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
window.fill((0,0,0))

continuer = True
grav = 1 / 60 * 9.81
pressed = False



class Bat():
    def __init__(self):
        self.pos = (width/2, height/2)
        self.lenght = 50
        self.alpha = 0
        self.speed = (random()*10-5, -random()*7)
        self.speedAlpha = 0.1
        return None

    def collide(self, side):
        if side == 'down':
            if self.speedAlpha > 0:
                x = (   self.speed[0] * 0.8 / 60) + (cos(bat.alpha + (pi/2)) * (bat.lenght/2) * bat.speedAlpha)
                y = ( - self.speed[1] * 0.8 / 60) + (sin(bat.alpha + (pi/2)) * (bat.lenght/2) * bat.speedAlpha)
            else:
                x = (   self.speed[0] * 0.8 / 60) + (cos(bat.alpha - (pi/2)) * (bat.lenght/2) * bat.speedAlpha)
                y = ( - self.speed[1] * 0.8 / 60) + (sin(bat.alpha - (pi/2)) * (bat.lenght/2) * bat.speedAlpha)
                pass
            vector = constr.Vector(x, y)
            angle = vector.angle()
            longi = vector.norm() * cos(angle - self.alpha) #composante longitudinale
            tang  = vector.norm() - longi      #composante tangentielle
            self.speed = (vector.x * (longi/tang) / 60, vector.y * (longi/tang) / 60)
            if angle - self.alpha > pi:
                self.speedAlpha += tang/longi * vector.norm() * (self.lenght/2) / 60
            else:
                self.speedAlpha -= tang/longi * vector.norm() * (self.lenght/2) / 60
            pass
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

    bat.speed = add(bat.speed, (0, grav)) # on fait marcher la gravité
    bat.alpha += bat.speedAlpha
    bat.alpha = bat.alpha % (2*pi)
    bat.pos = add(bat.pos, bat.speed)

    ### Gestion de la collision
    A = (bat.pos[0] + (cos(bat.alpha   )*bat.lenght/2), bat.pos[1] + (sin(bat.alpha   )*bat.lenght/2))
    B = (bat.pos[0] + (cos(bat.alpha+pi)*bat.lenght/2), bat.pos[1] + (sin(bat.alpha+pi)*bat.lenght/2))
    if A[1] > height-35:
        bat.pos = (bat.pos[0], (height-35.01) - (sin(bat.alpha   )*(bat.lenght/2)))
        bat.collide('down')
    if B[1] > height-35:
        bat.pos = (bat.pos[0], (height-35.01) - (sin(bat.alpha+pi)*(bat.lenght/2)))
        bat.collide('down')
        pass
    ### Fin Gestion collision





    ### Contraintes
     # bat.constrain()
    ### Fin Contraintes



    if bat.speed[0] > 15 or bat.speed[1] > 15:
        print('--------------------')
        print('speed   :', bat.speed)
        print('angular : ', bat.speedAlpha)

    window.fill((0,0,0))
    pygame.draw.line(window, (255, 255, 255), (0,height-30), (width, height-30))
    pygame.draw.line(window, (255, 150, 150), integ(A), integ(B), 2)
    pygame.draw.circle(window, (255, 0, 0), integ(A), 3, 1)
    pygame.draw.circle(window, (255, 0, 0), integ(B), 3, 1)
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
