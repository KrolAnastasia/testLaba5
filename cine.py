import pygame
import threading
import random
import time

screen_width = 1000
screen_height = 800

# Определение цветов
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (34, 145, 169)
ROSA = (260, 220, 205)
YELLOW = (255, 226, 119)

COLOR = [(204, 213, 174),(233, 237, 201),(224, 175, 160),(212, 163, 115),
         (243, 213, 181),(231, 188, 145),(212, 162, 118),(188, 138, 95),
         (164, 113, 72),(139, 94, 52),(111, 69, 24)]

def cine():
    # Инициализация Pygame
    pygame.init()

    letters = [
          ['e','h','o','l','a','e','s'],
          ['n','b','o','n','e','r','t'],
          ['t','e','b','i','d','a','p'],
          ['r','p','a','l','o','s','e'],
          ['a','d','a','d','m','a','l'],
          ['o','t','r','i','i','t','í'],
          ['r','c','e','a','l','u','c'],
    ]

    answer = [
        [(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2)],
        [(0,1),(0,2),(0,3),(0,4)],
        [(0,5),(0,6),(1,2),(1,3),(1,4),(1,5),(1,6)],
        [(1,1),(2,1),(2,2),(2,3),(2,4),(2,5)],
        [(3,1),(3,2),(3,3),(3,4),(3,5),(4,4),(4,5),(5,4),(5,5)],
        [(2,6),(3,6),(4,6),(5,6),(6,3),(6,4),(6,5),(6,6)],
        [(4,3),(5,0),(5,1),(5,2),(5,3),(6,0),(6,1),(6,2)]
    ]

    # Установка размеров окна
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cine")

    # Загрузка фонового изображения
    fon = pygame.image.load("assets/cine/cine.png")
    fon = pygame.transform.scale(fon, (screen_width, screen_height))

    # Определение размеров карточек для букв
    card_width = 90
    card_height = 90

    # Подложка под карточки с буквами
    substrate_width = 658
    substrate_height = 658

    # Правила
    rule_width = 600
    rule_height = 300

    # Словарь
    diccionario_width = 600
    diccionario_height = 600
    diccionario = pygame.image.load("assets/cine/dic.png")
    diccionario = pygame.transform.scale(diccionario, (diccionario_width, diccionario_height))
    def draw_diccionario():
        screen.blit(diccionario, ((screen_width-diccionario_width)//2, (screen_height-diccionario_height)//2))
    def draw_rule():
        # Отрисовка окна с правилами
        pygame.draw.rect(screen, WHITE, ((screen_width-rule_width)//2, (screen_height-rule_height)//2, rule_width, rule_height), border_radius=16)

        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 30)
        text = font.render("Juego Feelwords", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 80))
        screen.blit(text, text_rect)
        text = font.render("- necesitas para hacer", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 40))
        screen.blit(text, text_rect)
        text = font.render("las palabras de las letras.", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        text = font.render("Las palabras están relacionadas", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2+40))
        screen.blit(text, text_rect)
        text = font.render("con el tema CINE", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 80))
        screen.blit(text, text_rect)
        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 20)
        text = font.render("Чтобы выйти из мини игры - просто закройте окно", True, RED)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 120))
        screen.blit(text, text_rect)

    # Подсказка
    hint_width = 350
    hint_height = 400
    screen_hint = pygame.image.load("assets/cine/hint.png")
    screen_hint = pygame.transform.scale(screen_hint, (hint_width, hint_height))

    def draw_hint():  # отрисовка подсказки
        screen.blit(screen_hint, ((screen_width - hint_width) // 2, (screen_height - hint_height) // 2 - 50))

    # Определение размеров и положения кнопки подсказки
    button_width = 90
    button_height = 35
    button_x = 890
    button_y = 10

    def draw_button_hint():  # Отрисовка кнопки подсказки
        pygame.draw.rect(screen, (231, 188, 145), (button_x, button_y, button_width, button_height), border_radius=50)
        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 25)

        text = font.render("ayuda", True, WHITE)
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text, text_rect)


    # Функция для создания игрового поля
    def create_board(rows, cols):
        board = []

        for r in range(rows):
            row = []
            for c in range(cols):
                card = {
                    "image": letters[r][c],
                    "rect": pygame.Rect(c * card_width + 2 * c+179, r * card_height + 2 * r+79, card_width, card_height),
                    "opened": False,
                    "chek_color": False,
                    "color": 0,
                    "guessed": False
                }
                row.append(card)

            board.append(row)
        return board

    # Функция для отрисовки игрового поля
    def draw_board(board):
        for row in board:
            for card in row:
                if card["guessed"]:
                    if not card["chek_color"]:
                        card["color"] = COLOR[0]
                        pygame.draw.rect(screen, card["color"], card["rect"], border_radius=7)
                        card["chek_color"] = True
                    else:
                        pygame.draw.rect(screen, card["color"], card["rect"], border_radius=7)
                    font = pygame.font.Font('C:\WINDOWS\Fonts\corbell.ttf', 50)
                    text = font.render(card["image"], True, (0, 0, 0))
                    text_rect = text.get_rect()
                    text_rect.center = card["rect"].center
                    screen.blit(text, text_rect)
                elif card["opened"]:
                    pygame.draw.rect(screen, YELLOW, card["rect"], border_radius=7)
                    font = pygame.font.Font('C:\WINDOWS\Fonts\corbell.ttf', 50)
                    text = font.render(card["image"], True, (0, 0, 0))
                    text_rect = text.get_rect()
                    text_rect.center = card["rect"].center
                    screen.blit(text, text_rect)
                else:
                    pygame.draw.rect(screen, ROSA, card["rect"], border_radius=7)
                    font = pygame.font.Font('C:\WINDOWS\Fonts\corbell.ttf', 50)
                    text = font.render(card["image"], True, (0, 0, 0))
                    text_rect = text.get_rect()
                    text_rect.center = card["rect"].center
                    screen.blit(text, text_rect)


    # Функция для обработки клика на карточку
    def handle_click():
            opened_cards = []
            # Проверка
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c]["opened"] and not board[r][c]["guessed"]:
                        opened_cards.append((r, c))

            for i in range(len(answer)):
                if opened_cards == answer[i]:
                    for r in range(len(opened_cards)):
                        for c in range(len(opened_cards[r])):
                            board[opened_cards[r][0]][opened_cards[r][1]]["guessed"] = True
                else:
                    for r in range(len(opened_cards)):
                        for c in range(len(opened_cards[r])):
                            board[opened_cards[r][0]][opened_cards[r][1]]["opened"] = False

    # Создание игрового поля
    board = create_board(7, 7)

    # Основной игровой цикл
    running = True
    rule = True
    hint = False  # флаг, отвечает за окно с подсказкой
    timer = threading.Timer(100, handle_click)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif rule and event.type == pygame.MOUSEBUTTONDOWN:
                rule = False
            elif hint and event.type == pygame.MOUSEBUTTONDOWN:
                hint = False
            elif not rule and not hint and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # проверка, нажали ли на кнопку подсказки
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    hint = True
                    continue
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    for r in range(len(board)):
                        for c in range(len(board[0])):
                            if board[r][c]["rect"].collidepoint(mouse_pos):
                                timer.cancel()
                                card = board[r][c]
                                if not card["opened"] and not card["guessed"]:
                                    card["opened"] = True
                                    draw_board(board)
                                    pygame.display.update()
                                    random.shuffle(COLOR)
                                timer = threading.Timer(0.6, handle_click)
                                timer.start()


        guessed_letters = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]["guessed"]:
                    guessed_letters+=1

        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, WHITE, (171, 71, substrate_width, substrate_height), border_radius=16)
        draw_board(board)
        draw_button_hint()

        if rule:
            draw_rule()
        if hint: # если нажали на подсказку - отрисовать ее
            draw_hint()
        if guessed_letters == 49: #если все слова отгаданы
            time.sleep(1)
            draw_diccionario()

        pygame.display.flip()

    # Выход из игры
    pygame.quit()
    return 0
#cine()