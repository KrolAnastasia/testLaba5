import pygame
import random
import time
import sys
from escuela import escuela
from library import library
from restorante import restorante
from cine import cine
from tienda import tienda

# Размеры экрана игры
screen_width = 1000
screen_height = 700
map_height = 600 # высота карты в игре

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (34, 145, 169)
ROSA = (224, 175, 160)
YELLOW = (255, 226, 119)

# number_task_run - номер рабочего задания в начале игры
# character_x, character_y - координаты местоположения персонажа в начале игры
def main_game(number_task_run, character_x, character_y):

    pygame.mixer.pre_init(44100, -16, 1, 512)

    # Инициализация Pygame
    pygame.init()

    pygame.mixer.music.load("assets/music.mp3") # загрузка музыки на фон
    pygame.mixer.music.play(-1)  # включение музыки на фоне
    s = pygame.mixer.Sound("assets/si.ogg") # звуковой эффект "успешного выполнения задания"

    # Установка размеров окна
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Paseo por la ciudad")

    # Загрузка изображения карты города и персонажа
    city_map = pygame.image.load("assets/city_map.png")
    city_map = pygame.transform.scale(city_map, (screen_width, map_height))
    character = pygame.image.load("assets/character.png")
    # Размер и местоположение перснажа
    character_width = character.get_width() // 6
    character_height = character.get_height() // 6
    character = pygame.transform.scale(character, (character_width, character_height))
    character_rect = character.get_rect()
    character_rect.x = character_x
    character_rect.y = character_y

    # Подсказки
    hint_width = 600
    hint_height = 400
    screen_hint = pygame.image.load("assets/hint.png")
    screen_hint = pygame.transform.scale(screen_hint, (hint_width, hint_height))

    def draw_hint(): # отрисовка подсказки
        screen.blit(screen_hint, ((screen_width - hint_width) // 2 , (screen_height - hint_height) // 2 - 50))

    # Определение размеров и положения кнопки подсказки
    button_width = 90
    button_height = 35
    button_x = 890
    button_y = 10

    def draw_button_hint(): # Отрисовка кнопки подсказки
        pygame.draw.rect(screen, ROSA, (button_x, button_y, button_width, button_height), border_radius=50)
        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 25)

        text = font.render("ayuda", True, WHITE)
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text, text_rect)

    def draw_task(string): # Отрисовка окна с заданиями
        pygame.draw.rect(screen, (238, 207, 207), (0, map_height, screen_width, screen_height - map_height))
        pygame.draw.rect(screen, WHITE, (0, map_height, screen_width, screen_height - map_height), border_radius=50)
        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 32)
        text = font.render(string, True, (255, 145, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height - ((screen_height - map_height) // 2)))
        screen.blit(text, text_rect)


    # Основной игровой цикл
    running = True
    final = False # флаг, отвечает за конец игры
    hint = False # флаг, отвечает за окно с подсказкой
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif not final and hint and event.type == pygame.MOUSEBUTTONDOWN:
                hint = False
            elif not final and event.type == pygame.MOUSEBUTTONDOWN: # проверка, нажали ли на кнопку подсказки
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    hint = True


        # Движение персонажа через стрелки
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_rect.x -= 1
            if character_rect.x<0:
                character_rect.x += 1
        if keys[pygame.K_RIGHT]:
            character_rect.x += 1
            if character_rect.x>=screen_width-character_width:
                character_rect.x -= 1
        if keys[pygame.K_UP]:
            character_rect.y -= 1
            if character_rect.y<0:
                character_rect.y += 1
        if keys[pygame.K_DOWN]:
            character_rect.y += 1
            if character_rect.y>map_height-character_height:
                character_rect.y -= 1

        # Отрисовка карты и персонажа
        screen.blit(city_map, (0, 0))
        screen.blit(character, character_rect)
        draw_button_hint()

        if hint: # если нажали на подсказку - отрисовать ее
            draw_hint()

        # Проверка, достиг ли персонаж нужного места на карте
        if number_task_run==1:
            draw_task("1. Ir(←↑↓→) al cine hacia arriba y hacia la izquierda.") # текущее задание
            if character_rect.x > 0 and character_rect.y > 0 and character_rect.x < 100 and character_rect.y <150:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Genial!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, map_height // 2))
                screen.blit(text, text_rect)
                s.play() # включить эффект, если персонаж достиг нужной точки на карте
                pygame.display.update()
                time.sleep(0.6)

                if cine() == 0: # включить игру "Кино"
                    main_game(2, character_rect.x, character_rect.y) # вновь запустить основную игру, задав текущее задание 2
                    # и оставив персонажа на том же месте, где игра прервалась

        elif number_task_run==2:
            draw_task("2. Ir a la escuela derecha y abajo.")
            if character_rect.x > 750 and character_rect.y >160 and character_rect.x < 900 and character_rect.y <250:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Excelente!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, map_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                if escuela()==0: # включить игру "Школа"
                    main_game(3, character_rect.x, character_rect.y)

        elif number_task_run==3:
            draw_task("3. Ir a la biblioteca a la izquierda y hacia abajo.")
            if character_rect.x > 200 and character_rect.y > 350 and character_rect.x < 300 and character_rect.y <450:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Bien hecho!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, map_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                if library() == 0: # включить игру "Библиотека"
                    main_game(4, character_rect.x, character_rect.y)

        elif number_task_run==4:
            draw_task("4. Ir al restaurante hacia arriba y hacia la derecha.")
            if character_rect.x > 430 and character_rect.y > 90 and character_rect.x < 550 and character_rect.y <130:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Correcto!!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, map_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                if restorante() == 0: # включить игру "Ресторан"
                    main_game(5, character_rect.x, character_rect.y)

        elif number_task_run==5:
            draw_task("5. Ir a la tienda hacia abajo y hacia la derecha.")
            if character_rect.x > 800 and character_rect.y > 400 and character_rect.x < 900 and character_rect.y <600:
                font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 36)
                text = font.render("¡Genial!", True, (0, 0, 0))
                text_rect = text.get_rect(center=(screen_width // 2, map_height // 2))
                screen.blit(text, text_rect)
                s.play()
                pygame.display.update()
                time.sleep(0.6)

                pygame.mixer.music.stop() # выключить музыку для следующей игры
                if tienda() == 0: # включить игру "Магазин"
                    main_game(6, character_rect.x, character_rect.y)
        elif number_task_run == 6:
            draw_task("¡Bien hecho!")
            final = True
            pygame.draw.rect(screen, ROSA, (screen_width // 2 - 275, map_height // 2 - 75, 550, 150),
                             border_radius=50)
            font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 45)
            text = font.render("¡Pasaste el juego!", True, WHITE)
            text_rect = text.get_rect(center=(screen_width // 2, map_height // 2 - 30))
            screen.blit(text, text_rect)
            text = font.render("¡Ven otra vez!", True, WHITE)
            text_rect = text.get_rect(center=(screen_width // 2, map_height // 2 + 30))
            screen.blit(text, text_rect)


        pygame.display.flip()

    pygame.quit()
    sys.exit()

main_game(1, screen_width // 2, map_height // 2) # запустить игру с текущим 1 заданием, персонажа поставить в центр экрана