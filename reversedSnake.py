import pygame
import time
import random,sys
from pygame.locals import *


WINDOWWIDTH = 600
WINDOWHEIGHT = 480
color_CYAN = (0, 255, 255)
color_BLACK = (0, 0, 0)

CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

move_direction = {
  "UP" : 0,
  "DOWN" : 1,
  "LEFT" : 2,
  "RIGHT" : 3
}
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    index = 0
    @classmethod
    def load_images(cls):
        cls.images = [
            pygame.image.load('snakeHead.png').convert_alpha(),
            pygame.image.load('snakeBody.png').convert_alpha(),
            pygame.image.load('snakeTail.png').convert_alpha()]
    
    def __init__(self, texture, x, y, width = 1, height = 1):
        super(Snake, self).__init__()
        
        self.x = x
        self.y = y        
        self.rect = self.images[0].get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.rect=Rect(self.x, self.y, self.width,self.height)
        self.direction = move_direction["UP"]
        self.offsetX=0
        self.offsetY=0
        

    def update(self):
        if self.isAnimating:            
            self.animate()

    def move(self,direction):
        if direction == move_direction["LEFT"]:
            self.x -= 5
            
        if direction == move_direction["RIGHT"]:
            self.x += 5
            
        if direction == move_direction["UP"]:
            self.y -= 5
            
        if direction == move_direction["DOWN"]:
            self.y += 5
                 

    def draw(self, surface):
        surface.blit(self.images[2],(self.x+(self.offsetX*2), self.y+(self.offsetY*2)))
        surface.blit(self.images[1],(self.x+(self.offsetX), self.y+self.offsetY))
        surface.blit(self.images[0],(self.x, self.y))
        

    def startAnimation(self):
        self.isAnimating = True

    def animate(self):        
        self.images[2]= pygame.transform.flip(self.images[2], True, False)       
        time.sleep(0.2)

    def stopAnimation(self):
        self.isAnimating=False
        

class Snake(pygame.sprite.Sprite):
    index = 0
    @classmethod
    def load_images(cls):
        cls.images = [
            pygame.image.load('snakeHead.png').convert_alpha(),
            pygame.image.load('snakeBody.png').convert_alpha(),
            pygame.image.load('snakeTail.png').convert_alpha()]
    
    def __init__(self, texture, x, y, width = 1, height = 1):
        super(Snake, self).__init__()        
        self.x = x
        self.y = y        
        self.rect = self.images[0].get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.rect=Rect(self.x, self.y, self.width,self.height)
        self.direction = move_direction["LEFT"]
        self.offsetX = 0
        self.offsetY = 0
        self.prev_direction = -1        
        
    def isTurned(self):
        if self.prev_direction == self.direction:
            return True
        else:
            return False
        
    def update(self):
        if self.isAnimating:
            self.move(self.direction)
            self.animate(self.direction)

    def move(self,direction):
        if direction == move_direction["LEFT"]:
            self.x -= 5
            self.offsetX = +self.width
            self.offsetY = 0
        if direction == move_direction["RIGHT"]:
            self.x += 5
            self.offsetX = -self.width
            self.offsetY = 0
        if direction == move_direction["UP"]:
            self.y -= 5
            self.offsetX = 0
            self.offsetY = +self.height
        if direction == move_direction["DOWN"]:
            self.y += 5
            self.offsetX = 0
            self.offsetY = -self.height     

    def draw(self, surface):
        surface.blit(self.images[2],(self.x+(self.offsetX*2), self.y+(self.offsetY*2)))
        surface.blit(self.images[1],(self.x+(self.offsetX), self.y+self.offsetY))
        surface.blit(self.images[0],(self.x, self.y))
        

    def startAnimation(self):
        self.isAnimating = True

    def animate(self,direction):
        if self.isTurned() == False:
            if direction == move_direction["LEFT"]:
                self.images[2]= pygame.transform.rotate(self.images[2], 90)
            elif direction == move_direction["RIGHT"]:
                self.images[2]= pygame.transform.rotate(self.images[2], -90)
            elif direction == move_direction["UP"]:
                self.images[2]= pygame.transform.rotate(self.images[2], 0)
            elif direction == move_direction["DOWN"]:
                self.images[2]= pygame.transform.rotate(self.images[2], -90)
        self.prev_direction = self.direction
        if direction == move_direction["LEFT"] or direction == move_direction["RIGHT"]:
            self.images[2]= pygame.transform.flip(self.images[2], False, True)
        elif direction == move_direction["UP"] or direction == move_direction["DOWN"]:
            self.images[2]= pygame.transform.flip(self.images[2], True, False)    
        #self.images[2]= pygame.transform.rotate(self.images[2], -90)
        time.sleep(0.2)

    def stopAnimation(self):
        self.isAnimating=False
            


if __name__ == "__main__":
    pygame.init()
    caption = "snake reversed"
    pygame.display.set_caption(caption)
    Game_Window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    Game_Window.fill(color_CYAN)
    
    sheadPng = pygame.image.load("snakeHead.png").convert_alpha()
    sbodyPng = pygame.image.load("snakeBody.png").convert_alpha()
    stailPng = pygame.image.load("snakeTail.png").convert_alpha()
    pygame.display.set_icon(sheadPng)   

    Snake.load_images()
    snake = Snake(sheadPng, WINDOWWIDTH*0.45, WINDOWHEIGHT*0.75)
    snake.startAnimation()
    y = WINDOWHEIGHT*0.7
    
    while True:#the game loop
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        snake.update()
        Game_Window.fill(color_CYAN)
        #Game_Window.blit(bkg_texture, (0, 0))
        i = 0
       
        snake.draw(Game_Window)
        clock.tick(60)
        pygame.display.flip()        
