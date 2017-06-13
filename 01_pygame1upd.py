import pygame


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

# reso pantalla
gameDisplay = pygame.display.set_mode((display_width, display_height))
# titulo ventana
pygame.display.set_caption('Ventana QL')
clock = pygame.time.Clock()

# cargo una imagen
carImage = pygame.image.load('vochito.png')


def car(x, y):  # muestro el auto en la ventana
    gameDisplay.blit(carImage, (x, y))


x = (display_width * 0.1)
y = (display_height * 0.5)

crashed = False
while not crashed:
    for event in pygame.event.get():    # eventos por segundo
        if event.type == pygame.QUIT:   # evento para salir de la ventana
            crashed = True
    gameDisplay.fill(green)
    car(x, y)
    pygame.display.update()  # actualiza la ventana completa
    clock.tick(30)  # FPS

pygame.quit()
quit()
