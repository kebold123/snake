import pygame
import sys

from config import *
from apple import Apple
from snake import Snake

def handle_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT
            elif event.key == pygame.K_q:
                if snake.speed > 5:
                    snake.speed -= 5
            elif event.key == pygame.K_e:
                if snake.speed < 30:
                    snake.speed += 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption(f'Snake. Score: 1. Speed: 10')
clock = pygame.time.Clock()

apple = Apple()
snake = Snake()
pygame.init()
while True:
    clock.tick(snake.speed)
    handle_keys()

    snake.update_direction()

    if snake.get_next_head() in snake.positions:
        screen.fill(BACKGROUND_COLOR)
        apple = Apple()
        snake = Snake()

    if snake.get_next_head() == apple.position:
        apple = Apple()
        snake.move(is_apple=True)
        pygame.display.set_caption(f'Snake. Score: {snake.length}')
    else:
        snake.move()

    apple.draw(screen)
    snake.draw(screen)

    pygame.display.flip()