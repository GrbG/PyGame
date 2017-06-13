import pygame


pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))   # reso pantalla
pygame.display.set_caption('Ventana QL')   # titulo ventana
clock = pygame.time.Clock()

crashed = False
while not crashed:
    for event in pygame.event.get():    # eventos por segundo
        if event.type == pygame.QUIT:   # evento para salir de la ventana
            crashed = True
        print(event)
    pygame.display.update()  # actualiza la ventana completa
    clock.tick(30)  # FPS

pygame.quit()
quit()
