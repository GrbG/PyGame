import pygame
import time
import random


pygame.init()

# reso pantalla
display_width = 800
display_height = 600

# rgb colors :D
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

car_width = 297

# reso pantalla
gameDisplay = pygame.display.set_mode((display_width, display_height))
# titulo ventana
pygame.display.set_caption('Ventana QL')
clock = pygame.time.Clock()

# cargo una imagen
carImage = pygame.image.load('vochito.png')


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):  # muestro el auto en la ventana
    gameDisplay.blit(carImage, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()  # actualiza la ventana completa

    time.sleep(2)
    game_loop()


def crash():
    message_display('You CRASHED!')


def game_loop():
    x = (display_width * 0.1)
    y = (display_height * 0.5)
    x_change = 0

    thing_starx = random.randrange(0, display_width)
    thing_stary = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():    # eventos por segundo
            if event.type == pygame.QUIT:   # evento para salir de la ventana
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x = x + x_change
        gameDisplay.fill(green)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_starx, thing_stary, thing_width, thing_height, red)
        thing_stary = thing_stary + thing_speed

        car(x, y)

        if x < 0 or x > (display_width - car_width):
            crash()

        if thing_stary > display_height:
            thing_stary = 0 - thing_height
            thing_starx = random.randrange(0, display_width)

        pygame.display.update()  # actualiza la ventana completa
        clock.tick(30)  # FPS


game_loop()
pygame.quit()
quit()
