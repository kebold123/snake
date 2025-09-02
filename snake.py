import pygame
from config import *
import random

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [CENTER]
        self.color = SNAKE_COLOR
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None
        self.last = None
        self.speed = 10
    
    def draw(self, screen):
        head_x, head_y = self.positions[0]
        head = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, head)
        eye = pygame.Rect((head_x + 5, head_y + 5), (3, 3))
        pygame.draw.rect(screen, (0, 0, 0), eye)
        eye = pygame.Rect((head_x + 13, head_y + 5), (3, 3))
        pygame.draw.rect(screen, (0, 0, 0), eye)

        for position in self.positions[1:]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.color, rect)
        if self.last:
            rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BACKGROUND_COLOR, rect)

    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self, is_apple=False):
        if is_apple:
            self.positions.insert(0, self.get_next_head())
            self.length += 1
        else:
            self.positions.insert(0, self.get_next_head())
            self.last = self.positions.pop()

    def get_next_head(self):
        head_x, head_y = self.positions[0]
        if self.direction == UP:
            return head_x, head_y - GRID_SIZE
        elif self.direction == DOWN:
            return head_x, head_y + GRID_SIZE
        elif self.direction == LEFT:
            return head_x - GRID_SIZE, head_y
        else:
            return head_x + GRID_SIZE, head_y