import pygame
import sys
 #screen set up
pygame.init()

w = 800
h = 600

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

pygame.display.set_caption('Fario')
# charater
class player:
    def __init__(self):
        size = (40,60)
        position =(100, h-150)
        vel =[0, 0]
        speed = 5
        lumpPower = -15
        gravity = 1
        on_ground = False


running = True
# screen color
while running:
    clock.tick(60)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            sys.exit()
    pygame.dislpay.flip()        