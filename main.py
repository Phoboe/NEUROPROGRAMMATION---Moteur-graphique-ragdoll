'''DOCSTRING :
Ce programme cherche à simuler réalistiquement les collision et la gestions des forces d'un objet simple : un segment, assimilé à un point,
une rotation propre et les vitesses associées.
'''



import pygame                        # Importation de pygame
from pygame.locals import *          # Obligatoire pour la récupération des évennements de pygame (exemple : appui sur une touche du clavier)
from random import random, randrange # module sur l'aléatoire
from math import *                   # On se sert des fonctions de la trigo


from Neuron import Perceptron, Neuron # module perso non utilisé pour le moment
neuron = Neuron()                     # Voir module Neuron
from Perso import *                   # module perso sur les infos du personnage
import constructor as constr          # Module perso pour construire des objets comme des points et des vecteurs simplement



pygame.init() # Obligatoire, lancement du processus pygame et appel de certaines fonctions

width, height = 1280, 720 # définition prématurée des variables pour créer la fenêtre

window = pygame.display.set_mode((width, height))             # création de la fenêtre pygame du jeu
#window = pygame.display.set_mode((width, height), FULLSCREEN) # si nécessité de lancer la fenêtre en plein écran (il y a FULLSCREEN, RESIZABLE... voir la doc pygame)

pygame.key.set_repeat(400, 30) # choix des intervalles de répétition des touches du clavier si on reste appuyés dessus
pygame.mouse.set_visible(True) # choix de la visibilité de la souris dans la fenêtre
clock = pygame.time.Clock()    # création de l'objet clock : sert notament à définir les fps de la boucle
window.fill((0,0,0))           # remplissage de l'écran d'une couleur codée en RGB (ici noir)

continuer = True # variable définissant si la boucle principale tourne ou non
grav = 9.81 / 60 # variable de gravité à l'échelle 1:60


class Bat():
    ''' Objet qui collisionnera '''
    def __init__(self):
        self.pos = (width/2, height/2) # Position (linéaire) du segment
        self.lenght = 50               # Longueur du segment
        self.alpha = 0                 # position angulaire du segment
        self.speed = (2, 1.5)          # vitesse linéaire du segment
        self.omega = 0.1               # vitesse angulaire du segment
        return None

    def collide(self, side):
        ''' Fonction s'occupant de modifier les vitesses du segment lorsqu'il collisionne. '''
        if side == 'down': # Collision avec le sol
            ''' # Cette condition prennait en compte la vitesse angulaire du segment à l'impact
            if self.omega < 0:
                x = (   self.speed[0] * 0.8) + (cos(bat.alpha + (pi/2)) * (bat.lenght/2) * bat.omega)
                y = ( - self.speed[1] * 0.8) + (sin(bat.alpha + (pi/2)) * (bat.lenght/2) * bat.omega)
            else:
                x = (   self.speed[0] * 0.8) + (cos(bat.alpha - (pi/2)) * (bat.lenght/2) * bat.omega)
                y = ( - self.speed[1] * 0.8) + (sin(bat.alpha - (pi/2)) * (bat.lenght/2) * bat.omega)
                pass'''
            x =   self.speed[0] * 0.8    # coordonée horizontale du vecteur accéleration dû à la collision
            y = - self.speed[1] * 0.8    # coordonée verticale   du vecteur accéleration dû à la collision
            vector = constr.Vector(x, y) # on construit le vecteur en fonctions des coordonnées décrites précedemment
            angle = vector.angle()       # on calcule l'angle de ce vecteur par rapport à l'horizontale
            longi = vector.norm() * cos(angle - self.alpha) #composante longitudinale
            tang  = vector.norm() - longi                   #composante tangentielle
            self.speed = (vector.x * (longi/tang) / 60, vector.y * (longi/tang) / 60) # on définit la vitesse linéaire du segment en appliquant le vecteur accéleration précedemment calculé
            if angle - self.alpha > pi:  # cette condition vise à fournir une vitesse tangentielle positive ou négative selon l'orientation du vecteur accéleration par rapport au segment
                self.omega = - (tang * (self.lenght/2)) / 60
            else:
                self.omega = (tang * (self.lenght/2)) / 60
            pass
        pass

bat = Bat() # on crée l'objet qui collisionnera


def add(prime, second):
    ''' Additionne deux tuples doubles. (le 1er avec le 2eme) '''
    prime = (prime[0] + second[0], prime[1] + second[1])
    return prime

def integ(prime):
    ''' Retourne le tuple double en valeurs int '''
    return (int(prime[0]), int(prime[1]))





while continuer == True: # boucle principale du jeu

    bat.speed = add(bat.speed, (0, grav)) # on fait marcher la gravité
    bat.alpha += bat.omega                # on fait varier la position angulaire selon la vitesse angulaire
    bat.alpha = bat.alpha % (2*pi)        # on ramène la position angulaire à une valeur modulo (2*pi)
    bat.pos = add(bat.pos, bat.speed)     #  # on fait varier la position linéaire selon la vitesse linéaire

    ### Gestion de la collision
    A = (bat.pos[0] + (cos(bat.alpha   )*bat.lenght/2), bat.pos[1] + (sin(bat.alpha   )*bat.lenght/2)) # calcul de la positin du point A (extrémité du baton)
    B = (bat.pos[0] + (cos(bat.alpha+pi)*bat.lenght/2), bat.pos[1] + (sin(bat.alpha+pi)*bat.lenght/2)) # du point B (autre extrémité du bâton)
    ''' REMARQUE : Les coordonées de pygame sont inversés en ordonées. Le vecteur directeur de la droite des ordonées est orienté
    vers le bas. Déscendre d'un pixel c'est donc diminuer la valeur de 1 de la position en ordonnées.
    Mais ce n'est pas le cas pour ves abscisses. Le point de coordonées (0,0) est situé en haut à gauche de la fenêtre.'''
    if A[1] > height-35: # gestion de la collision du segment si les coordonées du point A sont en dessous d'une valeur de hauteur
        bat.pos = (bat.pos[0], (height-35.01) - (sin(bat.alpha   )*(bat.lenght/2))) # on replace le segment un peu plus haut pour qu'il ne collisionne pas à l'infini
        bat.collide('down')                                                         # On lance la fonction collide de l'objet "bat"
    if B[1] > height-35: # pareil mais pour le point B
        bat.pos = (bat.pos[0], (height-35.01) - (sin(bat.alpha+pi)*(bat.lenght/2)))
        bat.collide('down')
        pass
    ### Fin Gestion collision





    print('--------------------')  # Débogage :
    print('speed   :', bat.speed)  # vitesse linéaire
    print('angular : ', bat.omega) # vitesse angulaire

    window.fill((0,0,0)) # déja commenté plus haut
    pygame.draw.line(window, (255, 255, 255), (0,height-30), (width, height-30)) # on trace une ligne qui sera le sol
    pygame.draw.line(window, (255, 150, 150), integ(A), integ(B), 2)             # on trace le segment AB
    pygame.draw.circle(window, (255, 0, 0), integ(A), 3, 1)                      # on trace un petit cercle au point A
    pygame.draw.circle(window, (255, 0, 0), integ(B), 3, 1)                      # on trace un petit cercle au point B
    pygame.display.flip()                                                        # On actualise la fenêtre pygame
    clock.tick(60)                                                               # on définit les FPS à 60 ou moins







    for event in pygame.event.get():  # gestion des évenements Pygame
        if event.type == KEYDOWN:     # Si une touche est enfoncée
            if event.key == K_ESCAPE: # si cette touche est ECHAP
                continuer = False     # on arrete le programe
        if event.type == QUIT:        # si on clique sur FERMER
            continuer = False         # on arrete le programme
        souris_x, souris_y = pygame.mouse.get_pos() # On get les positions de la souis sur l'écran (positions relatives à la fenêtre)
        pass # Fin de la gestion des évennements

    continue



































'''END'''
