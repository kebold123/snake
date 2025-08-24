import random
import pygame
from config import *

class Apple:
    def __init__(self):
        self.position = self.get_position()
        self.color = APPLE_COLOR   

    @staticmethod
    def get_position():
        x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE
        y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE
        return x, y
    
    def draw(self, screen):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, rect)