import pygame
import pygame.mixer
from tkinter import *
from tkinter import messagebox as mb

# init pygame
pygame.init()

# create hide Tk window
Tk().wm_withdraw()


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

pygame.mixer.music.load("sound/main.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)


# images
bg = pygame.transform.scale(pygame.image.load("img/bg.png"), (width, height))
player_img = pygame.transform.scale(
    pygame.image.load("img/player.png"), (16, 32))
small_meteor1_img = pygame.transform.scale(
    pygame.image.load("img/small1.png"), (16, 16))
small_meteor2_img = pygame.transform.scale(
    pygame.image.load("img/small2.png"), (16, 16))
medium_meteor1_img = pygame.transform.scale(
    pygame.image.load("img/medium1.png"), (29, 29))
medium_meteor2_img = pygame.transform.scale(
    pygame.image.load("img/medium2.png"), (29, 27))
large_meteor1_img = pygame.transform.scale(
    pygame.image.load("img/large1.png"), (55, 57))
large_meteor2_img = pygame.transform.scale(
    pygame.image.load("img/large2.png"), (56, 56))
ufo_img = pygame.transform.scale(
    pygame.image.load("img/ufo.png"), (62, 25))
banana_img = pygame.transform.scale(
    pygame.image.load("img/banana.png"), (13, 32))
apple_img = pygame.transform.scale(
    pygame.image.load("img/apple.png"), (26, 28))
cherry_img = pygame.transform.scale(
    pygame.image.load("img/cherry.png"), (27, 30))
portal_img = pygame.transform.scale(
    pygame.image.load("img/portal.png"), (90, 90))

# groups objects
all_objects = pygame.sprite.Group()
meteors = pygame.sprite.Group()
ufos = pygame.sprite.Group()
fruits = pygame.sprite.Group()
portals = pygame.sprite.Group()

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

# fruits
banana_x = 400
banana_y = 110
banana = Object(banana_img, banana_x, banana_y, 0)

apple_x = 130
apple_y = 285
apple = Object(apple_img, apple_x, apple_y, 0)

cherry_x = 225
cherry_y = 420
cherry = Object(cherry_img, cherry_x, cherry_y, 0)

# portals
portal_x = 110
portal_y = 140
portal = Object(portal_img, portal_x, portal_y, 0)

# meteors
meteor1 = Object(small_meteor2_img, 630, 420, 0)
meteor2 = Object(medium_meteor2_img, 630, 435, 0)
meteor3 = Object(medium_meteor1_img, 620, 385, 0)
meteor4 = Object(large_meteor1_img, 610, 315, 0)
meteor5 = Object(medium_meteor2_img, 600, 285, 0)
meteor6 = Object(large_meteor2_img, 540, 270, 0)
meteor7 = Object(medium_meteor1_img, 515, 278, 0)
meteor8 = Object(large_meteor1_img, 500, 215, 0)
meteor9 = Object(medium_meteor2_img, 465, 215, 0)
meteor10 = Object(large_meteor2_img, 565, 445, 0)
meteor11 = Object(small_meteor1_img, 556, 443, 0)
meteor12 = Object(large_meteor1_img, 510, 390, 0)
meteor13 = Object(medium_meteor1_img, 480, 390, 0)
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

# outside
meteor43 = Object(small_meteor2_img, 708, 227, 0)
meteor44 = Object(small_meteor2_img, 611, 533, 0)
meteor45 = Object(small_meteor2_img, 674, 469, 0)
meteor46 = Object(small_meteor2_img, 625, 34, 0)
meteor47 = Object(small_meteor2_img, 606, 178, 0)
meteor48 = Object(small_meteor2_img, 670, 146, 0)
meteor49 = Object(small_meteor2_img, 657, 195, 0)
meteor50 = Object(small_meteor2_img, 660, 172, 0)
meteor51 = Object(small_meteor2_img, 722, 196, 0)
meteor52 = Object(small_meteor2_img, 627, 369, 0)
meteor53 = Object(small_meteor2_img, 679, 24, 0)
meteor54 = Object(small_meteor2_img, 635, 479, 0)
meteor55 = Object(small_meteor2_img, 739, 419, 0)
meteor56 = Object(small_meteor2_img, 664, 103, 0)
meteor57 = Object(small_meteor2_img, 668, 400, 0)
meteor58 = Object(small_meteor2_img, 688, 159, 0)
meteor59 = Object(small_meteor2_img, 689, 138, 0)
meteor60 = Object(small_meteor2_img, 651, 241, 0)
meteor61 = Object(small_meteor2_img, 747, 402, 0)
meteor62 = Object(small_meteor2_img, 672, 124, 0)
meteor63 = Object(small_meteor2_img, 613, 546, 0)
meteor64 = Object(small_meteor2_img, 652, 326, 0)
meteor65 = Object(small_meteor2_img, 741, 521, 0)
meteor66 = Object(small_meteor2_img, 720, 379, 0)
meteor67 = Object(small_meteor2_img, 739, 109, 0)
meteor68 = Object(small_meteor2_img, 669, 93, 0)
meteor69 = Object(small_meteor2_img, 640, 59, 0)
meteor70 = Object(small_meteor2_img, 619, 142, 0)
meteor71 = Object(small_meteor2_img, 670, 500, 0)
meteor72 = Object(small_meteor2_img, 739, 109, 0)
meteor73 = Object(small_meteor2_img, 641, 361, 0)
meteor74 = Object(small_meteor2_img, 606, 114, 0)
meteor75 = Object(small_meteor2_img, 607, 363, 0)
meteor76 = Object(small_meteor2_img, 25, 486, 0)
meteor77 = Object(small_meteor2_img, 21, 82, 0)
meteor78 = Object(small_meteor2_img, 28, 391, 0)
meteor79 = Object(small_meteor2_img, 14, 492, 0)
meteor80 = Object(small_meteor2_img, 27, 209, 0)
meteor81 = Object(small_meteor2_img, 18, 237, 0)
meteor82 = Object(small_meteor2_img, 14, 306, 0)
meteor83 = Object(small_meteor2_img, 2, 18, 0)
meteor84 = Object(small_meteor2_img, 3, 24, 0)
meteor85 = Object(small_meteor2_img, 10, 385, 0)
meteor86 = Object(small_meteor2_img, 39, 496, 0)
meteor87 = Object(small_meteor2_img, 29, 391, 0)
meteor88 = Object(small_meteor2_img, 35, 359, 0)
meteor89 = Object(small_meteor2_img, 17, 246, 0)
meteor90 = Object(small_meteor2_img, 10, 223, 0)
meteor91 = Object(small_meteor2_img, 29, 316, 0)
meteor92 = Object(small_meteor2_img, 22, 20, 0)
meteor93 = Object(small_meteor2_img, 7, 199, 0)
meteor94 = Object(small_meteor2_img, 29, 114, 0)
meteor95 = Object(small_meteor2_img, 27, 115, 0)
meteor96 = Object(small_meteor2_img, 36, 454, 0)
meteor97 = Object(small_meteor2_img, 34, 51, 0)
meteor98 = Object(small_meteor2_img, 36, 329, 0)
meteor99 = Object(small_meteor2_img, 8, 485, 0)
meteor100 = Object(small_meteor2_img, 18, 534, 0)


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
meteors.add(meteor43)
meteors.add(meteor44)
meteors.add(meteor45)
meteors.add(meteor46)
meteors.add(meteor47)
meteors.add(meteor48)
meteors.add(meteor49)
meteors.add(meteor50)
meteors.add(meteor51)
meteors.add(meteor52)
meteors.add(meteor53)
meteors.add(meteor54)
meteors.add(meteor55)
meteors.add(meteor56)
meteors.add(meteor57)
meteors.add(meteor58)
meteors.add(meteor59)
meteors.add(meteor60)
meteors.add(meteor61)
meteors.add(meteor62)
meteors.add(meteor63)
meteors.add(meteor64)
meteors.add(meteor65)
meteors.add(meteor66)
meteors.add(meteor67)
meteors.add(meteor68)
meteors.add(meteor69)
meteors.add(meteor70)
meteors.add(meteor71)
meteors.add(meteor72)
meteors.add(meteor73)
meteors.add(meteor74)
meteors.add(meteor75)
meteors.add(meteor76)
meteors.add(meteor77)
meteors.add(meteor78)
meteors.add(meteor79)
meteors.add(meteor80)
meteors.add(meteor81)
meteors.add(meteor82)
meteors.add(meteor83)
meteors.add(meteor84)
meteors.add(meteor85)
meteors.add(meteor86)
meteors.add(meteor87)
meteors.add(meteor88)
meteors.add(meteor89)
meteors.add(meteor90)
meteors.add(meteor91)
meteors.add(meteor92)
meteors.add(meteor93)
meteors.add(meteor94)
meteors.add(meteor95)
meteors.add(meteor96)
meteors.add(meteor97)
meteors.add(meteor98)
meteors.add(meteor99)
meteors.add(meteor100)

# adds fruits
fruits.add(banana)
fruits.add(apple)
fruits.add(cherry)

# adds ufos
ufos.add(ufo1)
ufos.add(ufo2)
ufos.add(ufo3)

# adds all_objects
all_objects.add(rocket)
all_objects.add(banana)
all_objects.add(apple)
all_objects.add(cherry)
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
all_objects.add(meteor43)
all_objects.add(meteor44)
all_objects.add(meteor45)
all_objects.add(meteor46)
all_objects.add(meteor47)
all_objects.add(meteor48)
all_objects.add(meteor49)
all_objects.add(meteor50)
all_objects.add(meteor51)
all_objects.add(meteor52)
all_objects.add(meteor53)
all_objects.add(meteor54)
all_objects.add(meteor55)
all_objects.add(meteor56)
all_objects.add(meteor57)
all_objects.add(meteor58)
all_objects.add(meteor59)
all_objects.add(meteor60)
all_objects.add(meteor61)
all_objects.add(meteor62)
all_objects.add(meteor63)
all_objects.add(meteor64)
all_objects.add(meteor65)
all_objects.add(meteor66)
all_objects.add(meteor67)
all_objects.add(meteor68)
all_objects.add(meteor69)
all_objects.add(meteor70)
all_objects.add(meteor71)
all_objects.add(meteor72)
all_objects.add(meteor73)
all_objects.add(meteor74)
all_objects.add(meteor75)
all_objects.add(meteor76)
all_objects.add(meteor77)
all_objects.add(meteor78)
all_objects.add(meteor79)
all_objects.add(meteor80)
all_objects.add(meteor81)
all_objects.add(meteor82)
all_objects.add(meteor83)
all_objects.add(meteor84)
all_objects.add(meteor85)
all_objects.add(meteor86)
all_objects.add(meteor87)
all_objects.add(meteor88)
all_objects.add(meteor89)
all_objects.add(meteor90)
all_objects.add(meteor91)
all_objects.add(meteor92)
all_objects.add(meteor93)
all_objects.add(meteor94)
all_objects.add(meteor95)
all_objects.add(meteor96)
all_objects.add(meteor97)
all_objects.add(meteor98)
all_objects.add(meteor99)
all_objects.add(meteor100)

# text
fruits_font = pygame.font.Font(None, 35)
fruits_text = fruits_font.render("Фрукты: 0", True, pygame.Color("white"))

run = True
points = 0

mb.showinfo("Ракета", "Ваша задача собрать все фрукты на просторах космоса и переместиться в портал.\n\nУдачи!")
while run:

    # draw background
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

    # rocket goto start
    if len(pygame.sprite.pygame.sprite.spritecollide(rocket, meteors, False)) > 0:
        rocket.rect.x = start_x
        rocket.rect.y = start_y
    if len(pygame.sprite.pygame.sprite.spritecollide(rocket, ufos, False)) > 0:
        rocket.rect.x = start_x
        rocket.rect.y = start_y

    # get points
    if len(pygame.sprite.pygame.sprite.spritecollide(rocket, fruits, True)) > 0:
        points += 1
        fruits_text = fruits_font.render(
            ("Фрукты: " + str(points)), True, pygame.Color("white"))
        if points == 3:
            rocket.rect.x = start_x
            rocket.rect.y = start_y
            portals.add(portal)
            all_objects.add(portal)
            mb.showinfo("Ракета", "НЛО телепортируют Вас в начало!")

    # player touch the portal
    if len(pygame.sprite.pygame.sprite.spritecollide(rocket, portals, False)) > 0:
        mb.showinfo("Ракета", "Вы победили!")
        run = False

    # draw objects in window
    all_objects.update()
    all_objects.draw(window)
    window.blit(fruits_text, (370, 480))
    pygame.display.update()
