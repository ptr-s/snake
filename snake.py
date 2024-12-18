import pygame
import random
from config import *

# Инициализация Pygame
pygame.init()

# Определение цветов
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (169, 169, 169)  # Цвет камней

# Установка размеров окна
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Установка параметров игры
snake_block = 20
snake_speed = 15

# Установка шрифта
font_style = pygame.font.Font("assets/bahnschrift.ttf", 25)
score_font = pygame.font.Font("assets/Comic Sans MS.ttf", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def draw_stones(stones):
    for stone in stones:
        pygame.draw.rect(screen, gray, [stone[0], stone[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():  # основной игровой цикл
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    food_count = 0  # Счётчик еды
    stones = []  # Список камней

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("Ты проиграл! Нажми C для продолжения или Q для выхода", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

        # Добавление камней после 5 кусочков пищи
        if food_count >= 5 and len(stones) < 5:  # Максимум 5 камней
            stone_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            stone_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            stones.append((stone_x, stone_y))

        draw_stones(stones)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        # Проверка на столкновение со стенами
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            food_count += 1  # Увеличиваем счётчик еды

        # Проверка на столкновение с камнями
        for stone in stones:
            if snake_Head[0] == stone:
                game_close = True

        pygame.display.update()

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()