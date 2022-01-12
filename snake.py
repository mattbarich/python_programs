import pygame
import time
import random

pygame.init()

# Game Colors
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
yellow = (255, 255, 102)

# initialize game window
window_size_width = 750
window_size_height = 500
game_window = pygame.display.set_mode((window_size_width, window_size_height))
pygame.display.set_caption("Simple Snake")
game_clock = pygame.time.Clock()

snake_speed = 10
snake_block = 10

font_style = pygame.font.SysFont("Times New Roman", 50)


def player_score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow)
    game_window.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mes = font_style.render(msg, True, color)
    game_window.blit(mes, [window_size_width / 2, window_size_height / 2])


def game_loop():
    game_over = False
    game_close = False

    start_posX = window_size_width / 2
    start_posY = window_size_height / 2

    y_change = 0
    x_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, window_size_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_size_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            game_window.fill(blue)
            message("You Lost! Press C to play again or Q to Quit", red)
            player_score(length_of_snake - 1)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
        if start_posX > window_size_width or start_posX < 0 or start_posY >= window_size_height or start_posY < 0:
            game_over = True

        start_posX += x_change
        start_posY += y_change
        game_window.fill(blue)
        pygame.draw.rect(game_window, green, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(start_posX)
        snake_head.append(start_posY)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        player_score(length_of_snake - 1)

        pygame.display.update()

        if start_posX == foodx and start_posY == foody:
            foodx = round(random.randrange(0, window_size_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_size_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

    pygame.quit()
    quit()


game_loop()
