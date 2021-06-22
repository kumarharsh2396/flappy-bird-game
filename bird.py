import math
import os
from random import randint
from collections import deque
import pygame
from pygame.locals import *

#base variables
FPS = 60
ANIMATION_SPEED = 0.18 #pixels per milisec
WIN_WIDTH = 284 * 2 #Background image sie: 284 * 512; tilled twice
WIN_HEIGHT = 512

def main():
    #main workflow
    pygame.init()
    pygame_surface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()