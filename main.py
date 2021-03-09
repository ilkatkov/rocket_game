import pygame

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ракета")
pygame.display.set_icon(pygame.image.load("icon.ico"))
run = True

bg = pygame.transform.scale(pygame.image.load("img/bg.png"), (width, height))


while run:
    window.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()