import pygame
from const import *

class Player(pygame.Rect):
    def __init__(self):
        self.x = int(DROW_SCREEN_SIZE[0] / 2)
        self.y = 150
        self.h = 32
        self.w = 32
        self.hp = 3