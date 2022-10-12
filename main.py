from turtle import Pen
import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800,600))

background= pygame.image.load("fire-wall.jpg")


pygame.display.set_caption("Lolz invaders")
icon = pygame.image.load('pepe.png')
pygame.display.set_icon(icon)


player_img= pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

enemy_img= pygame.image.load('wojak.png')
enemy_x = random.randint(0,800)
enemy_y = random.randint (50,150)
enemy_x_change = 0.2
enemy_y_change = 40

laser_img= pygame.image.load('laser-pen.png')
laser_x = 0
laser_y = 480
laser_x_change = 0
laser_y_change = 10
laser_state = "ready"


def player(x,y):
    screen.blit(player_img, (x, y))

def enemy(x,y):
    screen.blit(enemy_img, (x, y))

def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laser_img, (x + 16,y +10))


running = True
while running:
    
    screen.fill((0,0,0))
    screen.blit (background, (0,0))  
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_x_change = -0.4
            if event.key == pygame.K_d:
                player_x_change = 0.4

            if event.key == pygame.K_SPACE:
                if laser_state is "ready":
                    laser_x = player_x
                    fire_laser(laser_x,laser_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_x_change = 0

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736


    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.2
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change

    if laser_y <= 0:
        laser_y =  480
        laser_state = "ready"

    if laser_state is "fire":
        fire_laser (laser_x,laser_y) 
        laser_y -= laser_y_change

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    pygame.display.update()