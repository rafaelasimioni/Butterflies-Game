#COLOR
import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT

cinzaClaro = (240, 240, 240)
verdeOliva = (173, 204, 96)
white = (255, 255, 255)

MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

MENU_TEXT = (
    'use the up, down, left and right keys to play'

)

WIN_WIDTH = 714
WIN_HEIGHT = 327

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED ={
    'Level1Bg0' : 1,
    'Level1Bg1': 0,
    'Player1' : 5,
    'Enemy1': 8,
    'Enemy2': 8

}


#S
SPAWN_TIME = 2000


# WIN_WIDTH = 1201
# WIN_HEIGHT = 604



