import pygame
import math
from pygame.locals import *

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#keys mapping (use W,A,S,D in keyboard)
keys = {
    "top" : False,
    "down":False,
    "right":False,
    "left" :False
}

running = True 

playerpos = [100, 100]

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

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
    sudut = math.atan2(mouse[1] - (playerpos[1]+32), mouse[0] -(playerpos[0]+26))
    player_rotation = pygame.transform.rotate(player, 360 - sudut * 57.29)
    new_playerpos = (playerpos[0] - player_rotation.get_rect().width/2, playerpos[1] - player_rotation.get_rect().height/2)
    screen.blit(player_rotation, new_playerpos)

    pygame.display.flip()

    for event in pygame.event.get() :
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
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
        #end logic 

        #move player 
        if keys["top"]:
            playerpos[1] -= 10
        elif keys["down"]:
            playerpos[1] += 10 
        elif keys["right"]:
            playerpos[0] -= 10
        elif keys["left"]:
            playerpos[0] += 10
