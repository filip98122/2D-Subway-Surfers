import pygame
import math
import random
from PIL import Image

flag = True

image = Image.open("KnightSpritesheet.png")
pixels = image.load()
print(pixels[2,35])
w,h = image.size
#top and bottom
y_levels = [[0,54],[57,135],[136,136 + 59]]

#for x in range(w):
#    for y in range(h):
#        if pixels[x,y][-1] != 0 and pixels[x,y][-1] != 255:
#            a = 5

a = 0
next_px = "full"
xlist =[]
for i in range(len(y_levels)):
    start = -1
    end = -1
    for x in range(214):
        
        
        flag = True
        for y in range(y_levels[i][0],y_levels[i][1]):
            transparency = pixels[x,y][-1]
            if transparency > 10:
                flag = False
                if start==-1:
                    start = x
                
                
                
        if flag == True:
            a += 1
            if end==-1 and start!=-1:
                end = x
                xlist.append([start,end])
                start = -1
                end = -1
            
            
print(xlist)            
print(a)

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


WIDTH,HEIGHT = 800,800

window = pygame.display.set_mode((WIDTH,HEIGHT))


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
    def __init__(self,x,y,speed,):
        self.x = x
        self.y = y
        self.speed = speed
        self.spritesheet = pygame.image.load('KnightSpritesheet.png')
        self.spritesheet =pygame.transform.scale(self.spritesheet,(self.spritesheet.get_width()*4,self.spritesheet.get_height()*4))
        self.width = self.spritesheet.get_width()*0.15
        self.render_frame = 0
        self.size = 4
        self.frame_count = 0
        self.frame_flip = 15
        self.state = 2
        self.info = [
            
            #x offset,y ofset,width,height, number of frames
            [56,0,37,54,2],
            [56,61,45,54,7],
            [0,140,41,52,7]
            ]
    def draw(self,window):

        if self.render_frame >self.info[self.state][4]:
            self.render_frame = 0
        window.blit(self.spritesheet,(0,0),(self.info[self.state][0]*self.render_frame*self.size,self.info[self.state][1]*self.size,self.info[self.state][2]*self.size,self.info[self.state][3]*self.size))
        if self.frame_count == self.frame_flip:
            self.render_frame+=1
            self.frame_count = 0
        self.frame_count+=1
        
        
            
            
            
        
        
s = random.randint(0,1000)
target = Target(400,600,2,125,100,1)

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
    
    
p = Player(0,0,4)

clock = pygame.time.Clock()

while True:
    
    window.fill("White")
    keys = pygame.key.get_pressed()
    mouseState = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()   
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if keys[pygame.K_ESCAPE]:
        exit()
        
    target.move()
    p.draw(window)
    pygame.draw.rect(window, pygame.Color("Gray"), pygame.Rect((0,650, 800,100)))
    if target.direction == 0:
        target.draw_going_Right(window)
    else:
        target.draw_going_left(window)
    pygame.display.update()
    clock.tick(FPS)
    