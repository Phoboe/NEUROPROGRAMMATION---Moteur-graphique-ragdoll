from math import sqrt, pi
from random import random


'''
Tout ce qui est relatif au personnage
 - position des membres
 - Unification du corps (forces anti-disloquantes)
'''


dict = {
'tete':((67,21), 25),
'cou ':((64,62),(64,111)),
'rachis':((64,111),(64,293)),
'cuisse':((64,293),(64,422)),
'jambe':((64,422),(64,571)),
'pied':((64,571),(571,82)),
'bras':((64,111),(20,218)),
'avant bras':((20,218),(20,307)),
'main':((20,307),(20,360))
}









class Bras1():
    def __init__(self):
        attach = dict['rachis'][0]
        self.x1 = dict['bras'][0][0]
        self.y1 = dict['bras'][0][1]
        self.x2 = dict['bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = dict['bras'][1][1] + (random() - 0.5) # + ou - 0.5
        self.alpha = 3*pi/4 # = -90 --> horizontal vers le bas
        self.lenght = sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2) # distance entre les deux points
        self.speedAlpha = 0
        self.speed = 0

    def center(self):
        ''' Calcule le centre de masse du segment. '''
        ''' Renvoie un tuple double.               '''
        return ( (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2 )

    def replace(self, pos):
        ''' Replace le mambre par rapport à un point de réference. '''
        ''' Prend un tuple double en entrée.                       '''
        self.x1 = pos[0] + dict['bras'][0][0]
        self.y1 = pos[1] + dict['bras'][0][1]
        self.x2 = pos[0] + dict['bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = pos[1] + dict['bras'][1][1] + (random() - 0.5) # + ou - 0.5
        return None
    pass

class Bras2():
    def __init__(self):
        attach = dict['rachis'][0]
        self.x1 = dict['bras'][0][0]
        self.y1 = dict['bras'][0][1]
        self.x2 = dict['bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = dict['bras'][1][1] + (random() - 0.5) # + ou - 0.5
        self.alpha = 3*pi/4 # = -90 --> horizontal vers le bas
        self.lenght = sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2) # distance entre les deux points
        self.speedAlpha = 0
        self.speed = 0

    def center(self):
        ''' Calcule le centre de masse du segment. '''
        ''' Renvoie un tuple double.               '''
        return ( (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2 )

    def replace(self, pos):
        ''' Replace le mambre par rapport à un point de réference. '''
        ''' Prend un tuple double en entrée.                       '''
        self.x1 = pos[0] + dict['bras'][0][0]
        self.y1 = pos[1] + dict['bras'][0][1]
        self.x2 = pos[0] + dict['bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = pos[1] + dict['bras'][1][1] + (random() - 0.5) # + ou - 0.5
        return None
    pass

class AvantBras1():
    def __init__(self):
        attach = dict['bras'][1]
        self.x1 = dict['avant bras'][0][0]
        self.y1 = dict['avant bras'][0][1]
        self.x2 = dict['avant bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = dict['avant bras'][1][1] + (random() - 0.5) # + ou - 0.5
        self.alpha = 3*pi/4 # = -90 --> horizontal vers le bas
        self.lenght = sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2) # distance entre les deux points
        self.speedAlpha = 0
        self.speed = 0

    def center(self):
        ''' Calcule le centre de masse du segment. '''
        ''' Renvoie un tuple double.               '''
        return ( (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2 )

    def replace(self, pos):
        ''' Replace le mambre par rapport à un point de réference. '''
        ''' Prend un tuple double en entrée.                       '''
        self.x1 = pos[0] + dict['avant bras'][0][0]
        self.y1 = pos[1] + dict['avant bras'][0][1]
        self.x2 = pos[0] + dict['avant bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = pos[1] + dict['avant bras'][1][1] + (random() - 0.5) # + ou - 0.5
        return None
    pass

class AvantBras2():
    def __init__(self):
        attach = dict['bras'][1]
        self.x1 = dict['avant bras'][0][0]
        self.y1 = dict['avant bras'][0][1]
        self.x2 = dict['avant bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = dict['avant bras'][1][1] + (random() - 0.5) # + ou - 0.5
        self.alpha = 3*pi/4 # = -90 --> horizontal vers le bas
        self.lenght = sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2) # distance entre les deux points
        self.speedAlpha = 0
        self.speed = 0

    def center(self):
        ''' Calcule le centre de masse du segment. '''
        ''' Renvoie un tuple double.               '''
        return ( (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2 )

    def replace(self, pos):
        ''' Replace le mambre par rapport à un point de réference. '''
        ''' Prend un tuple double en entrée.                       '''
        self.x1 = pos[0] + dict['avant bras'][0][0]
        self.y1 = pos[1] + dict['avant bras'][0][1]
        self.x2 = pos[0] + dict['avant bras'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = pos[1] + dict['avant bras'][1][1] + (random() - 0.5) # + ou - 0.5
        return None
    pass









class rachis():
    def __init__(self):
        attach = None
        self.x1 = dict['rachis'][0][0]
        self.y1 = dict['rachis'][0][1]
        self.x2 = dict['rachis'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = dict['rachis'][1][1] + (random() - 0.5) # + ou - 0.5
        self.alpha = 3*pi/4 # = -90 --> horizontal vers le bas
        self.lenght = sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2) # distance entre les deux points
        self.speedAlpha = 0
        self.speed = 0

    def center(self):
        ''' Calcule le centre de masse du segment. '''
        ''' Renvoie un tuple double.               '''
        return ( (self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2 )

    def replace(self, pos):
        ''' Replace le mambre par rapport à un point de réference. '''
        ''' Prend un tuple double en entrée.                       '''
        self.x1 = pos[0] + dict['rachis'][0][0]
        self.y1 = pos[1] + dict['rachis'][0][1]
        self.x2 = pos[0] + dict['rachis'][1][0] + (random() - 0.5) # + ou - 0.5
        self.y2 = pos[1] + dict['rachis'][1][1] + (random() - 0.5) # + ou - 0.5
        return None
    pass













pass
