import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed


width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ракета")
pygame.display.set_icon(pygame.image.load("icon.ico"))
run = True

bg = pygame.transform.scale(pygame.image.load("img/bg.png"), (width, height))
player_img = pygame.transform.scale(pygame.image.load("img/player.png"), (32, 32))

all_objects = pygame.sprite.Group()


start_x = 150
start_y = 250
rocket = Object(player_img, start_x, start_y, 1)


all_objects.add(rocket)

while run:
    # pygame.time.delay(30)
    window.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and rocket.rect.x > 0:
            rocket.rect.x -= rocket.speed
            rocket.image = pygame.transform.rotate(player_img, 90)
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and rocket.rect.x < width-32:
            rocket.rect.x += rocket.speed
            rocket.image = pygame.transform.rotate(player_img, -90)
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and rocket.rect.y >0:
            rocket.rect.y -= rocket.speed
            rocket.image = pygame.transform.rotate(player_img, 0)
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and rocket.rect.y < height-32:
            rocket.image = pygame.transform.rotate(player_img, 180)
            rocket.rect.y += rocket.speed

    all_objects.update()
    all_objects.draw(window)
    pygame.display.update()