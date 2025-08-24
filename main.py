import pygame
import sys

from config import *
from apple import Apple

def handle_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

apple = Apple()
pygame.init()
while True:
    clock.tick(SPEED)
    handle_keys()
    apple.draw(screen)

    pygame.display.flip()