import pygame
import random

# initilalize game- telles computer that the following 
# code should be interpretted as a game.
pygame.init()

# step 1. set up display
height = 600
width = 800

# THIS IS REUSABLE code that represents our game screen
screen = pygame.display.set_mode((width,height))

# thuis will allow us to show the title of the game when a 
# user opens our game
pygame.display.set_caption("Avoid the falling objects")

# set frame rate
clock = pygame.time.Clock() # games run on frame
FPS = 60 # Game updates 60 times per second

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Step 2. Create player object
#object -
pointGauge = [shooting, playmaking, offfense, speed, height]