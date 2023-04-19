import pygame
import sys
import math

pygame.init()

win = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("Survival game")

x = 50
y = 50
width = 40
height = 60
speed = 5

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw_player(self, win):
        pygame.draw.rect(win,(255,0,0),(self.x,self.y,self.width,self.height))

class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 10
        self.angle = math.atan2(self.y-self.mouse_y, self.x-self.mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self, win):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(win, (0,0,0), (self.x, self.y), 5)
    def delete_bullet(self):
        return self.x < 10 or x > 1280 or self.y < 0 or self.y > 720

player_bullets = []

while True:
    win.fill((192,192,192)) 

    mouse_x, mouse_y = pygame.mouse.get_pos()

    player = Player(x,y,width,height)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        if event.type == pygame.MOUSEBUTTONDOWN:
            player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x -= speed

    if keys[pygame.K_d]:
        x += speed

    if keys[pygame.K_w]:
        y -= speed

    if keys[pygame.K_s]:
        y += speed
    
    player.draw_player(win)   

    for bullet in player_bullets:
        bullet.main(win)
        if bullet.delete_bullet():
           player_bullets.remove(bullet)

    clock.tick(60)
    pygame.display.update() 
    
pygame.quit()