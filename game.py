import pygame
import math
from pygame.locals import *
from random import randint

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

score = 0
arrows = []

enemy_timer = 100  # Waktu generate Musuh
enemies = [[width, 100]]

# keys mapping (use W,A,S,D in keyboard)
keys = {
    "top": False,
    "down": False,
    "right": False,
    "left": False
}

running = True

playerpos = [100, 100]

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
enemy_img = pygame.image.load("resources/images/badguy.png")


while(running):
    screen.fill(0)

    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass, (x*100, y*100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    #screen.blit(player, playerpos)
    mouse = pygame.mouse.get_pos()
    sudut = math.atan2(mouse[1] - (playerpos[1]+32),
                       mouse[0] - (playerpos[0]+26))
    player_rotation = pygame.transform.rotate(player, 360 - sudut * 57.29)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width/2,
                     playerpos[1] - player_rotation.get_rect().height/2)
    screen.blit(player_rotation, new_playerpos)

    for bullet in arrows:
        arrow_index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > width or bullet[2] < -64 or bullet[2] > height:
            arrows.pop(arrow_index)
        arrow_index += 1
        for projectile in arrows:
            new_arrow = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(new_arrow, (projectile[1], projectile[2]))
    
    enemy_timer -= 1
    if enemy_timer == 0:
        enemies.append([width, randint(50, height-32)])
        enemy_timer = randint(1, 100)

    index = 0 
    for enemy in enemies:
        enemy[0] -= 5
        if enemy[0] < -64:
            enemies.pop(index)

    enemy_react = pygame.Rect(enemy_img.get_rect())
    enemy_react.top = enemy[1]
    enemy_react.left = enemy[0]

    if enemy_react.left < 64:
        enemies.pop(index)
        print("WOI KESERANG DONG WOIIIIIIIIIIIII!!! ")

    index_arrow = 0
    for bullet in arrows:
        bullet_rect = pygame.Rect(arrow.get_rect())
        bullet_rect.left = bullet[1]
        bullet_rect.top = bullet[2]
        #crash bullet with enemies
        if enemy_react.colliderect(bullet_rect):
            score += 1
            enemies.pop(index)
            arrows.pop(index_arrow)
            print("HaHAHA Mati!!!")
            print("score:{}".format(score))
        index_arrow += 1
    index += 1
    
    for enemy in enemies: 
        screen.blit(enemy_img, enemy) #create enemy from left screen 

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # logic mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            arrows.append([sudut, new_playerpos[0]+32, new_playerpos[1]+32])

        #logic in keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys["top"] = True
            elif event.key == K_s:
                keys["down"] = True
            elif event.key == K_a:
                keys["right"] = True
            elif event.key == K_d:
                keys["left"] = True

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys["top"] = False
            elif event.key == K_s:
                keys["down"] = False
            elif event.key == K_a:
                keys["right"] = False
            elif event.key == K_d:
                keys["left"] = False
        # end logic

        # move player
        if keys["top"]:
            playerpos[1] -= 10
        elif keys["down"]:
            playerpos[1] += 10
        elif keys["right"]:
            playerpos[0] -= 10
        elif keys["left"]:
            playerpos[0] += 10
