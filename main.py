import pygame

# class for player and meteors


class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed


# window settings
width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ракета")
pygame.display.set_icon(pygame.image.load("icon.ico"))
run = True

# images
bg = pygame.transform.scale(pygame.image.load("img/bg.png"), (width, height))
player_img = pygame.transform.scale(
    pygame.image.load("img/player.png"), (32, 32))
small_meteor1_img = pygame.transform.scale(
    pygame.image.load("img/small1.png"), (16, 16))
small_meteor2_img = pygame.transform.scale(
    pygame.image.load("img/small2.png"), (16, 16))
medium_meteor1_img = pygame.transform.scale(
    pygame.image.load("img/medium1.png"), (32, 32))
medium_meteor2_img = pygame.transform.scale(
    pygame.image.load("img/medium2.png"), (32, 32))
large_meteor1_img = pygame.transform.scale(
    pygame.image.load("img/large1.png"), (64, 64))
large_meteor2_img = pygame.transform.scale(
    pygame.image.load("img/large2.png"), (64, 64))
ufo_img = pygame.transform.scale(
    pygame.image.load("img/ufo.png"), (64, 32))

# groups objects
all_objects = pygame.sprite.Group()
meteors = pygame.sprite.Group()
ufos = pygame.sprite.Group()

# player object
start_x = 590
start_y = 400
rocket = Object(player_img, start_x, start_y, 2)

# ufos

ufo_x1 = 375
ufo_y1 = 110
ufo1 = Object(ufo_img, ufo_x1, ufo_y1, 2)

ufo_x2 = 130
ufo_y2 = 285
ufo2 = Object(ufo_img, ufo_x2, ufo_y2, 3)

ufo_x3 = 207
ufo_y3 = 470
ufo3 = Object(ufo_img, ufo_x3, ufo_y3, 0)

# meteors
meteor1 = Object(small_meteor2_img, 630, 420, 0)
meteor2 = Object(medium_meteor2_img, 630, 435, 0)
meteor3 = Object(medium_meteor1_img, 620, 385, 0)
meteor4 = Object(large_meteor1_img, 610, 315, 0)
meteor5 = Object(medium_meteor2_img, 580, 325, 0)
meteor6 = Object(large_meteor2_img, 540, 270, 0)
meteor7 = Object(medium_meteor1_img, 515, 278, 0)
meteor8 = Object(large_meteor1_img, 500, 215, 0)
meteor9 = Object(medium_meteor2_img, 465, 215, 0)
meteor10 = Object(large_meteor2_img, 565, 445, 0)
meteor11 = Object(small_meteor1_img, 565, 443, 0)
meteor12 = Object(large_meteor1_img, 510, 390, 0)
meteor13 = Object(medium_meteor1_img, 485, 390, 0)
meteor14 = Object(large_meteor2_img, 420, 385, 0)
meteor15 = Object(medium_meteor1_img, 390, 385, 0)
meteor16 = Object(medium_meteor2_img, 355, 365, 0)
meteor17 = Object(medium_meteor1_img, 320, 375, 0)
meteor18 = Object(large_meteor2_img, 290, 405, 0)
meteor19 = Object(large_meteor1_img, 270, 470, 0)
meteor20 = Object(medium_meteor1_img, 245, 515, 0)
meteor21 = Object(medium_meteor2_img, 210, 505, 0)
meteor22 = Object(small_meteor2_img, 190, 500, 0)
meteor23 = Object(large_meteor2_img, 150, 440, 0)
meteor24 = Object(medium_meteor1_img, 140, 420, 0)
meteor25 = Object(medium_meteor2_img, 110, 400, 0)
meteor26 = Object(large_meteor2_img, 90, 370, 0)
meteor27 = Object(medium_meteor1_img, 90, 340, 0)
meteor28 = Object(large_meteor1_img, 60, 270, 0)
meteor29 = Object(medium_meteor1_img, 60, 235, 0)
meteor30 = Object(large_meteor2_img, 50, 165, 0)
meteor31 = Object(small_meteor1_img, 80, 145, 0)
meteor32 = Object(medium_meteor2_img, 80, 105, 0)
meteor33 = Object(large_meteor2_img, 105, 65, 0)
meteor34 = Object(medium_meteor2_img, 160, 105, 0)
meteor35 = Object(medium_meteor1_img, 190, 125, 0)
meteor36 = Object(large_meteor2_img, 220, 105, 0)
meteor37 = Object(large_meteor1_img, 270, 65, 0)
meteor38 = Object(medium_meteor1_img, 335, 105, 0)
meteor39 = Object(large_meteor2_img, 355, 45, 0)
meteor40 = Object(large_meteor1_img, 420, 45, 0)
meteor41 = Object(medium_meteor1_img, 440, 115, 0)
meteor42 = Object(large_meteor2_img, 440, 145, 0)

# adds objects in groups

# adds meteors
meteors.add(meteor1)
meteors.add(meteor2)
meteors.add(meteor3)
meteors.add(meteor4)
meteors.add(meteor5)
meteors.add(meteor6)
meteors.add(meteor7)
meteors.add(meteor8)
meteors.add(meteor9)
meteors.add(meteor10)
meteors.add(meteor11)
meteors.add(meteor12)
meteors.add(meteor13)
meteors.add(meteor14)
meteors.add(meteor15)
meteors.add(meteor16)
meteors.add(meteor17)
meteors.add(meteor18)
meteors.add(meteor19)
meteors.add(meteor20)
meteors.add(meteor21)
meteors.add(meteor22)
meteors.add(meteor23)
meteors.add(meteor24)
meteors.add(meteor25)
meteors.add(meteor26)
meteors.add(meteor27)
meteors.add(meteor28)
meteors.add(meteor29)
meteors.add(meteor30)
meteors.add(meteor31)
meteors.add(meteor32)
meteors.add(meteor33)
meteors.add(meteor34)
meteors.add(meteor35)
meteors.add(meteor36)
meteors.add(meteor37)
meteors.add(meteor38)
meteors.add(meteor39)
meteors.add(meteor40)
meteors.add(meteor41)
meteors.add(meteor42)

# adds all_objects
all_objects.add(rocket)
all_objects.add(ufo1)
all_objects.add(ufo2)
all_objects.add(ufo3)
all_objects.add(meteor1)
all_objects.add(meteor2)
all_objects.add(meteor3)
all_objects.add(meteor4)
all_objects.add(meteor5)
all_objects.add(meteor6)
all_objects.add(meteor7)
all_objects.add(meteor8)
all_objects.add(meteor9)
all_objects.add(meteor10)
all_objects.add(meteor11)
all_objects.add(meteor12)
all_objects.add(meteor13)
all_objects.add(meteor14)
all_objects.add(meteor15)
all_objects.add(meteor16)
all_objects.add(meteor17)
all_objects.add(meteor18)
all_objects.add(meteor19)
all_objects.add(meteor20)
all_objects.add(meteor21)
all_objects.add(meteor22)
all_objects.add(meteor23)
all_objects.add(meteor24)
all_objects.add(meteor25)
all_objects.add(meteor26)
all_objects.add(meteor27)
all_objects.add(meteor28)
all_objects.add(meteor29)
all_objects.add(meteor30)
all_objects.add(meteor31)
all_objects.add(meteor32)
all_objects.add(meteor33)
all_objects.add(meteor34)
all_objects.add(meteor35)
all_objects.add(meteor36)
all_objects.add(meteor37)
all_objects.add(meteor38)
all_objects.add(meteor39)
all_objects.add(meteor40)
all_objects.add(meteor41)
all_objects.add(meteor42)

while run:

    window.blit(bg, (0, 0))

    # exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # keys events
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and rocket.rect.x > 0:
            rocket.rect.x -= rocket.speed
            rocket.image = pygame.transform.rotate(player_img, 90)
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and rocket.rect.x < width-32:
            rocket.rect.x += rocket.speed
            rocket.image = pygame.transform.rotate(player_img, -90)
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and rocket.rect.y > 0:
            rocket.rect.y -= rocket.speed
            rocket.image = pygame.transform.rotate(player_img, 0)
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and rocket.rect.y < height-32:
            rocket.image = pygame.transform.rotate(player_img, 180)
            rocket.rect.y += rocket.speed

    # ufos direction
    ufo1.rect.y += ufo1.speed
    ufo2.rect.x += ufo2.speed
    if len(pygame.sprite.pygame.sprite.spritecollide(ufo1, meteors, False)) > 0:
        ufo1.speed *= -1
    if len(pygame.sprite.pygame.sprite.spritecollide(ufo2, meteors, False)) > 0:
        ufo2.speed *= -1

    # draw objects in window
    all_objects.update()
    all_objects.draw(window)
    pygame.display.update()
