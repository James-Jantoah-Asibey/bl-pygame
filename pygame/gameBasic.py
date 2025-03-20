import pygame
import random


pygame.init()


height = 600
width = 800
player_width, player_height = 50, 50
object_width, object_height = 50, 50
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((width,height))


pygame.display.set_caption("Avoid the falling objects")


clock = pygame.time.Clock()
FPS = 60


class Player:
    def __init__(self):
        self.x = width // 2
        self.y = height - player_height - 10
        self.width = player_width
        self.height = player_height
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < width - self.width:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, blue, (self.x, self.y, self.width, self.height))

class FallingObject:
    def __init__(self):
        self.x = random.randint(0, width - object_width)
        self.y = -object_height
        self.width = object_width
        self.height = object_height
        self.speed = random.randint(3, 7)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.y > height


player = Player()
falling_objects = []
score = 0
lives = 3
running = True

while running:
    clock.tick(FPS)
    screen.fill('WHITE')  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw()
    
    if keys[pygame.K_LEFT]:
        player
    if keys[pygame.K_RIGHT]:
        player
    if keys[pygame.K_UP]:
        player 
    if keys[pygame.K_DOWN]:
        player
     
    if random.randint(1, 30) == 1:  
        falling_objects.append(FallingObject())

    
    for obj in falling_objects[:]:
        obj.move()
        obj.draw()

        
        if (obj.x < player.x + player.width and
            obj.x + obj.width > player.x and
            obj.y < player.y + player.height and
            obj.y + obj.height > player.y):
            lives -= 1
            falling_objects.remove(obj)  

        
        elif obj.off_screen():
            falling_objects.remove(obj)
            score += 1  


 
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))


 
    if lives <= 0:
        game_over_text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over_text, (width // 2 - 50, height // 2))
        pygame.display.update()
        pygame.time.delay(2000)  
        running = False

    pygame.display.update()  

pygame.quit()