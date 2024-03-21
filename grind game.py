import pygame
import math
import random
from PIL import Image

flag = True


#for x in range(w):
#    for y in range(h):
#        if pixels[x,y][-1] != 0 and pixels[x,y][-1] != 255:
#            a = 5







pygame.init()

def button_colision(width,height,x,y,mousePos,mouseState):
    if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height and mouseState[0] == True:
        return True
    else:
        return False

def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist > r1 + r2:
        return False
    else:
        return True
    
def colision1(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False


WIDTH,HEIGHT = 1000,800

window = pygame.display.set_mode((WIDTH,HEIGHT))

def get_sprite_bigger(sprite,times_bigger_widht,times_bigger_height):
    
    spritesheet = pygame.transform.scale(sprite,(sprite.get_width()*times_bigger_widht,
    sprite32.get_height()*times_bigger_height))

    return spritesheet



def blit( spritesheet, x, y, window ):
    
    window.blit(spritesheet,(x,y))
    

sprite32 = pygame.image.load('hill.png')


sprite31 = pygame.image.load('haunt.png')

sprite_attack = pygame.image.load("attack1knight.png")
spritesheet31 = get_sprite_bigger(sprite31,0.565,0.825)


class Target:
    def __init__(self,x,y,speed,width,height,direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction
        self.size = 30
        
        
    def draw_going_Right(self,window):
        pygame.draw.rect(window, pygame.Color("Black"), 
        pygame.Rect(self.x, self.y, self.width,self.height)) # Draws a rectangle
        pygame.draw.circle(window, pygame.Color(40,40,40), (self.x+15,self.y + self.height), self.size)
        pygame.draw.circle(window, pygame.Color("Gray"), (self.x+15,self.y + self.height), self.size - 15)
        pygame.draw.rect(window, pygame.Color("blue"),
        pygame.Rect(self.x + 50, self.y+5,70,50))
        pygame.draw.circle(window, pygame.Color(40,40,40), (self.x + self.width-15,self.y + self.height), self.size)
        pygame.draw.circle(window, pygame.Color("Gray"), (self.x + self.width-15,self.y + self.height),self.size - 15)
        
    def draw_going_left(self,window):
        pygame.draw.rect(window, pygame.Color("Black"), 
        pygame.Rect(self.x, self.y-5, self.width,self.height)) # Draws a rectangle
        pygame.draw.circle(window, pygame.Color(40,40,40), (self.x+15,self.y + self.height), self.size)
        pygame.draw.circle(window, pygame.Color("Gray"), (self.x+15,self.y + self.height), self.size - 15)
        pygame.draw.rect(window, pygame.Color("blue"),
        pygame.Rect(self.x + 5, self.y+5,70,50))
        pygame.draw.circle(window, pygame.Color(40,40,40), (self.x + self.width-15,self.y + self.height), self.size)
        pygame.draw.circle(window, pygame.Color("Gray"), (self.x + self.width-15,self.y + self.height),self.size - 15)
        
        
    def move(self):
        if self.direction == 0:
            self.x += self.speed
        else:
            self.x -= self.speed
FPS = 60
class Player:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.movement = [0,0]
        self.change_time = 0
        self.spritesheete_pos = [1,590]
        self.movefix = 0
        self.knight_lane = 3
        self.ff = 0
        
        #Left foot first
        
        self.spriteshee1 = pygame.image.load('run.knight1.png')
        self.spritesheet1 = pygame.transform.scale(self.spriteshee1,(self.spriteshee1.get_width()*4,self.spriteshee1.get_height()*4))

        
        #Right foot first
        
        self.spriteshee2 = pygame.image.load('run.knight2.png')
        self.spritesheet2 = pygame.transform.scale(self.spriteshee2,(self.spriteshee2.get_width()*4,self.spriteshee2.get_height()*4))

        #mid

        self.spriteshee3 = pygame.image.load('run.knight3.png')
        self.spritesheet3 = pygame.transform.scale(self.spriteshee3,(self.spriteshee3.get_width()*4,self.spriteshee3.get_height()*4))




    def draw(self,window):
        
        if self.change_time <= 15:
            window.blit(self.spritesheet1,(self.spritesheete_pos[0],self.spritesheete_pos[1]))
            
        if self.change_time >= 16:
            window.blit(self.spritesheet3,(self.spritesheete_pos[0],self.spritesheete_pos[1]))
            
            
        if self.change_time == 30:
            self.change_time = 0
            
            
        self.change_time += 1
        
        
    def move(self,keys):
        if self.ff <= 0:
            if keys[pygame.K_SPACE]:
                self.ff = 60 
                
        if self.ff <= 60 and self.ff >= 31:
            self.spritesheete_pos[1] -= 4
            
        if self.ff <= 30 and self.ff >= 1:
                self.spritesheete_pos[1] += 4
                
        if self.spritesheete_pos[0] > 20:
            if keys[pygame.K_LEFT]:
                self.spritesheete_pos[0] -= self.speed
            
        if self.spritesheete_pos[0] + self.spriteshee2.get_width()*4 < 980:
            if keys[pygame.K_RIGHT]:
                self.spritesheete_pos[0] += self.speed

        self.ff -= 1      
        
        
        
s = random.randint(0,1000)

l_targets = []
target = Target(400,600,2,125,100,1)
l_targets.append(target)

if target.direction == 0:
    target.x = -150
if target.direction == 1:
    target.x = 950



sprite_offset_x = 19


sprites = pygame.image.load("KnightSpritesheet.png")
i = 0
import time
SCALE = 4
sprites = pygame.transform.scale(sprites,(sprites.get_width()*4,sprites.get_height()*4))
#hile True:
#   if i>3:
#       i = 0
#   window.fill("black")
#   window.blit(sprites,(0,0),(56*i*4,1*4,37*4,54*4))
#   pygame.display.update()
#   i+=1
#   time.sleep(0.45)
    
    
p = Player(0,0,3)

clock = pygame.time.Clock()


hauntstage = 1
hillstage = 0


while True:
    
    
    window.fill("White")
    
    blit(spritesheet31,0,0,window)
    keys = pygame.key.get_pressed()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()   
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_ESCAPE]:
        exit()
        

        
        
        
    p.move(keys)
    #pygame.draw.rect(window, pygame.Color("Gray"), pygame.Rect((0,650, 1000,100)))
    
    p.draw(window)

            
    pygame.display.update()
    
    clock.tick(FPS)
    