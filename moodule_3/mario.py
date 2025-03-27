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
    def __init__(self, x, y):
        size = (40,60)
        self.rect = pygame.Rect((x,y), size)
        position =(100, h-150)
        vel =[0, 0]
        speed = 5
        lumpPower = -15
        gravity = 1
        on_ground = False

    def input(self, keys):
        if keys[pygame.K_LEFT]:
            self.vel[0] =-self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel[0] = self.speed
        else:
            self.vel[0] = 0

        if keys[pygame.K_SPACE] and self.onGround:
            self.vel[1] = self.jump
        
        def apply_gravity(self, platforms):
            self.vel[1]=self.gravity
            self.rect.x +=self.gravity

scroll_x = 0

platform = [
    pygame.Rect(0, h-100, 2000, 40),
    pygame.Rect(300, h-200, 200, 40),
    pygame.Rect(600, h-300, 200, 40),
    pygame.Rect(900, h-400, 200, 40),
]

running = True
# screen color
while running:
    clock.tick(60)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            sys.exit()
    pygame.display.flip()        