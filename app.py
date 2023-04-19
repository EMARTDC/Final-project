import pygame
import sys
pygame.init()

win = pygame.display.set_mode((800,600))
clock = pygame.time.Clock
pygame.display.set_caption("Survival game")

player_x = 250
player_y = 250
player_width = 25
player_height = 25

class Character:
    def _init_(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def main(self, win):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

player = Character(player_x, player_y, player_width, player_height)


class enemy:
    def _init_ (self,x,y,width,height,health,attack):
        pass
    def main(self,dispay):
        pass

class powerups:
    def _init_(self,x,y,width,color,height,modifier,name):
        pass

class projectile:
    def _init_(self,x,y,width,height,color,speed):
        pass


while True:
    win.fill((0,0,0)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT

    player.main(win)
     
    clock.tick(60)
    pygame.display.update() 
    
pygame.quit()