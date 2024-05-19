import pygame
import time

screen_width = 2000
screen_height = 800

# Определение цветов
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (34, 145, 169)


def restorante():

    pygame.mixer.pre_init(44100, -16, 1, 512)

    # Инициализация Pygame
    pygame.init()

    si = pygame.mixer.Sound("assets/si.ogg") #звуковой эффект "правильный ответ"
    no = pygame.mixer.Sound("assets/no.ogg") #звуковой эффект "неправильный ответ"

    # Установка размеров окна
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Restorante")

    # Загрузка фонового изображения, диалог 1 - приветствие
    hola = pygame.image.load("assets/restorante/hola.png")
    hola = pygame.transform.scale(hola, (screen_width, screen_height))

    # Загрузка фонового изображения, диалог 2 - меню
    menu = pygame.image.load("assets/restorante/menu.png")
    menu = pygame.transform.scale(menu, (screen_width, screen_height))

    # Загрузка фонового изображения, диалог 3 - сок
    sok = pygame.image.load("assets/restorante/sok.png")
    sok = pygame.transform.scale(sok, (screen_width, screen_height))

    # Загрузка фонового изображения, диалог 4 - рагу
    carne = pygame.image.load("assets/restorante/carne.png")
    carne = pygame.transform.scale(carne, (screen_width, screen_height))

    # Загрузка фонового изображения, диалог 5 - финал
    fin = pygame.image.load("assets/restorante/fin.png")
    fin = pygame.transform.scale(fin, (screen_width, screen_height))

    # Определение размеров и положения кнопки
    button_width = 500
    button_height = 80
    button_x = 250
    button_y = 400

    # Определение размеров и положения 2 кнопки
    button2_x = 250
    button2_y = 500

    # Определение размеров и положения 3 кнопки
    button3_x = 250
    button3_y = 600

    def draw_dialog_ofic(string,str2): # отрисовка диалогов официанта
        x = 250
        y = 50
        width = 730
        height = 100
        # Отрисовка окна с текстом
        pygame.draw.rect(screen, (255,255,255), (x, y, width, height), border_radius=50)
        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 34)

        if str2 == "":
            text = font.render(string, True, RED)
            text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
            screen.blit(text, text_rect)
        else: #Если текст длинный и занимает две строки
            text = font.render(string, True, RED)
            text_rect = text.get_rect(center=(x + width // 2, y + height // 2-20))
            screen.blit(text, text_rect)

            text = font.render(str2, True, RED)
            text_rect = text.get_rect(center=(x + width // 2, y + height // 2+20))
            screen.blit(text, text_rect)

    def draw_dialog_character(string, str2, x, y, color_button, color_words): # отрисовка диалогов девочки

        pygame.draw.rect(screen, color_button, (x, y, button_width, button_height), border_radius=50)
        font = pygame.font.Font('C:\WINDOWS\Fonts\\consola.ttf', 30)

        if str2 == "":
            text = font.render(string, True, color_words)
            text_rect = text.get_rect(center=(x + button_width // 2, y + button_height // 2))
            screen.blit(text, text_rect)
        else: #Если текст длинный и занимает две строки
            text = font.render(string, True, color_words)
            text_rect = text.get_rect(center=(x + button_width//2, y + button_height//2-20))
            screen.blit(text, text_rect)

            text = font.render(str2, True, color_words)
            text_rect = text.get_rect(center=(x + button_width // 2, y + button_height // 2+20))
            screen.blit(text, text_rect)

    def handle_click(mouse_x,  mouse_y, respuestaCorrecto): #проверка нажатия кнопок
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
            if respuestaCorrecto == 1:
                draw_dialog_character("Si!!", "", button_x, button_y, GREEN, WHITE)
                si.play()
                return True
            else:
                draw_dialog_character("Inténtalo de nuevo)", "", button_x, button_y, RED, WHITE)
                no.play()
                return False
        elif button2_x <= mouse_x <= button2_x + button_width and button2_y <= mouse_y <= button2_y + button_height:
            if respuestaCorrecto == 2:
                si.play()
                draw_dialog_character("Correcto!", "", button2_x, button2_y, GREEN, WHITE)
                return True
            else:
                draw_dialog_character("Piensa más:)", "", button2_x, button2_y, RED, WHITE)
                no.play()
                return False
        elif button3_x <= mouse_x <= button3_x + button_width and button3_y <= mouse_y <= button3_y + button_height:
            if respuestaCorrecto == 3:
                si.play()
                draw_dialog_character("Genial!", "", button3_x, button3_y, GREEN, WHITE)
                return True
            else:
                draw_dialog_character("Oops..", "", button3_x, button3_y, RED, WHITE)
                no.play()
                return False


    # Основной игровой цикл
    active_dialog = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if active_dialog == 1:
                    if handle_click(mouse_x, mouse_y, 2):
                        pygame.display.update()
                        time.sleep(0.8)
                        active_dialog+=1
                    else:
                        pygame.display.update()
                        time.sleep(0.8)
                elif active_dialog == 2:
                    if handle_click(mouse_x, mouse_y, 1):
                        pygame.display.update()
                        time.sleep(0.8)
                        active_dialog += 1
                    else:
                        pygame.display.update()
                        time.sleep(0.8)
                elif active_dialog == 3:
                    if handle_click(mouse_x, mouse_y, 2):
                        pygame.display.update()
                        time.sleep(0.8)
                        active_dialog += 1
                    else:
                        pygame.display.update()
                        time.sleep(0.8)
                elif active_dialog == 4:
                    if handle_click(mouse_x, mouse_y, 1):
                        pygame.display.update()
                        time.sleep(0.8)
                        active_dialog += 1
                    else:
                        pygame.display.update()
                        time.sleep(0.8)
                elif active_dialog == 5:
                    if handle_click(mouse_x, mouse_y, 3):
                        pygame.display.update()
                        time.sleep(0.8)
                        active_dialog += 1
                    else:
                        pygame.display.update()
                        time.sleep(0.8)

        if active_dialog == 1:
            # Отрисовка
            screen.blit(hola, (0, 0))
            draw_dialog_ofic("¡Hola, ¡buenos días!", "")
            draw_dialog_character("¡Buenas tardes!", "", button_x, button_y, WHITE, BLUE)
            draw_dialog_character("¡Hola! Tengo una reserva.", "", button2_x, button2_y, WHITE, BLUE)
            draw_dialog_character("Buenas, ¿me traes", "la cuenta, por favor?", button3_x, button3_y, WHITE, BLUE)
        elif active_dialog == 2:
            # Отрисовка
            screen.blit(hola, (0, 0))
            draw_dialog_ofic("¡Genial! A qué nombre?", "")
            draw_dialog_character("A nombre de Lucía Perez.", "", button_x, button_y, WHITE, BLUE)
            draw_dialog_character("Para 3 personas.", "", button2_x, button2_y, WHITE, BLUE)
            draw_dialog_character("A las 8 de la tarde.", "", button3_x, button3_y, WHITE, BLUE)
        elif active_dialog == 3:
            # Отрисовка
            screen.blit(menu, (0, 0))
            draw_dialog_ofic("Pase por favor. Aquí está la carta.",
                             "¿Qué le gustaría beber?")
            draw_dialog_character("La carne asada, por favor.", "", button_x, button_y, WHITE, BLUE)
            draw_dialog_character("Un zumo de naranja.", "", button2_x, button2_y, WHITE, BLUE)
            draw_dialog_character("Necesito un tenedor.", "", button3_x, button3_y, WHITE, BLUE)
        elif active_dialog == 4:
            # Отрисовка
            screen.blit(sok, (0, 0))
            draw_dialog_ofic("Ahora mismo le pongo.",
                             "¿Y para comer?")
            draw_dialog_character("La carne asada, por favor.", "", button_x, button_y, WHITE, BLUE)
            draw_dialog_character("No tengo sed, gracias.", "", button2_x, button2_y, WHITE, BLUE)
            draw_dialog_character("La cuenta por favor.", "", button3_x, button3_y, WHITE,BLUE)
        elif active_dialog == 5:
            # Отрисовка
            screen.blit(carne, (0, 0))
            draw_dialog_ofic("Le ha gustado todo?",
                             "En qué puedo ayudarle más?")
            draw_dialog_character("Quiero reservar la mesa.", "", button_x, button_y, WHITE, BLUE)
            draw_dialog_character("Hasta luego.", "", button2_x, button2_y, WHITE, BLUE)
            draw_dialog_character("Me trae la cuenta por favor.", "", button3_x, button3_y, WHITE, BLUE)
        elif active_dialog == 6:
            # Отрисовка
            screen.blit(fin, (0, 0))

        pygame.display.flip()

    pygame.quit()
    return 0
#restorante()