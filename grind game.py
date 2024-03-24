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

spritesheet31 = get_sprite_bigger(sprite31,0.565,0.825)

class Zombie:
    def __init__(self,speed,attack,posx,posy,hit_range):
        self.speed = speed
        self.attack = attack
        self.change_time = 0
        self.posx = posx
        self.posy = posy
        self.hit_range = hit_range
        self.direction = 0
        
    def draw(self,window):
        SCALE = 1.75
        #zombie attack going left 
        
        self.sprite_zombie_attack_going_left = pygame.image.load("zombie_attack_going_left.png")
        
        self.sprite_zombie_attack_going_left_big =  pygame.transform.scale(self.sprite_zombie_attack_going_left,
        (self.sprite_zombie_attack_going_left.get_width()*SCALE,self.sprite_zombie_attack_going_left.get_height()*SCALE))
        
        
        
        
        #zombie attack going right
        
        self.sprite_zombie_attack_going_right = pygame.image.load("zombie_attack_going_right.png")
        
        self.sprite_zombie_attack_going_right_big =  pygame.transform.scale(self.sprite_zombie_attack_going_right,
        (self.sprite_zombie_attack_going_right.get_width()*SCALE,self.sprite_zombie_attack_going_right.get_height()*SCALE))
        
        
        
        #left foot first going left
        
        self.sprite_zombie_left_going_left = pygame.image.load("zombie_left _going_left.png")
        
        self.sprite_zombie_left_big_going_left = pygame.transform.scale(self.sprite_zombie_left_going_left,
        (self.sprite_zombie_left_going_left.get_width()*SCALE,self.sprite_zombie_left_going_left.get_height()*SCALE))
        
        
        #right foot first going left
        
        self.sprite_zombie_right_going_left = pygame.image.load("zombie_right _going_left.png")
        
        self.sprite_zombie_right_big_going_left = pygame.transform.scale(self.sprite_zombie_right_going_left,
        (self.sprite_zombie_right_going_left.get_width()*SCALE,self.sprite_zombie_right_going_left.get_height()*SCALE))
        
        
        #left foot first going right
        
        self.sprite_zombie_left = pygame.image.load("zombie_left.png")
        
        self.sprite_zombie_left_big = pygame.transform.scale(self.sprite_zombie_left,
        (self.sprite_zombie_left.get_width()*SCALE,self.sprite_zombie_left.get_height()*SCALE))
        
        #right foot first going right
        
        self.sprite_zombie_right = pygame.image.load("zombie_right.png")
        
        self.sprite_zombie_right_big = pygame.transform.scale(self.sprite_zombie_right,
        (self.sprite_zombie_right.get_width()*SCALE,self.sprite_zombie_right.get_height()*SCALE))
        
        
        if self.direction == 0:
            if self.change_time > 0 and self.change_time <= 15:
                window.blit(self.sprite_zombie_left_big_going_left,(self.posx,self.posy))
                
            if self.change_time >= 16 and self.change_time <= 30:
                window.blit(self.sprite_zombie_right_big_going_left,(self.posx,self.posy))
                
            if self.attack == 1:
                window.blit(self.sprite_zombie_attack_going_right_big,(self.posx,self.posy))
                
                    
        
        
        if self.direction == 1:
            
            if self.attack == 2:
                window.blit(self.sprite_zombie_attack_going_left_big,(self.posx,self.posy))
            
            if self.attack == 0:
                if self.change_time < 0 and self.change_time >= 15:
                    window.blit(self.sprite_zombie_left_big,(self.posx,self.posy))
                    
                if self.change_time >= 16 and self.change_time <= 30:
                    window.blit(self.sprite_zombie_right_big,(self.posx,self.posy))
                


        self.change_time += 1
        
        if self.change_time == 31:
            self.change_time = 0
            
        
    def move(self,p1x,p1y):
        
        self.attack = 0
        
        self.sprite_zombie_left = pygame.image.load("zombie_left.png")
        # directhion = 0 je ide desno, a levo vice-versa
        
        
        if self.posx > p1x:
            self.direction = 0
        if self.posx< p1x:
            self.direction = 1
            
        if self.direction == 1:
            self.posx += self.speed
        if self.direction == 0:
            self.posx -= self.speed
            
        if self.posx + self.hit_range + self.sprite_zombie_left.get_width()*4 < p1x:
            if self.direction == 0:
                self.attack = 2
                
        if self.posx - self.hit_range < p1x:
            if self.direction == 1:
                self.attack = 1
        


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
    def __init__(self,spritesheete_pos,speed):
        self.speed = speed
        self.movement = [0,0]
        self.change_time = 0
        self.spritesheete_pos = spritesheete_pos
        self.spritesheete_pos = [1,590]
        self.movefix = 0
        self.knight_lane = 3
        self.ff = 0
        self.clicked = 0
        self.cooldown = 0
        SCALE = 4
        
        #Left foot first
        
        self.spriteshee1 = pygame.image.load('run.knight1.png')
        
        self.spritesheet1 = pygame.transform.scale(self.spriteshee1,(self.spriteshee1.get_width()*SCALE,
        self.spriteshee1.get_height()*SCALE))

        
        #Right foot first
        
        self.spriteshee2 = pygame.image.load('run.knight2.png')
        
        self.spritesheet2 = pygame.transform.scale(self.spriteshee2,(self.spriteshee2.get_width()*SCALE,
        self.spriteshee2.get_height()*SCALE))

        #mid

        self.spriteshee3 = pygame.image.load('run.knight3.png')
        
        self.spritesheet3 = pygame.transform.scale(self.spriteshee3,(self.spriteshee3.get_width()*SCALE,
        self.spriteshee3.get_height()*SCALE))

        #attack
        
        self.sprite_attack = pygame.image.load("attack1knight.png")
        
        self.sprite_attack_big = pygame.transform.scale(self.sprite_attack,(self.sprite_attack.get_width()*SCALE,
        self.sprite_attack.get_height()*SCALE))


    def draw(self,window):
        
        self.mouseState = pygame.mouse.get_pressed()
        
        if self.change_time >= 31:
            window.blit(self.sprite_attack_big,(self.spritesheete_pos[0],self.spritesheete_pos[1]))
            
        if self.cooldown <= 0:
            if mouseState[0] == True:
                self.clicked = 1
                self.change_time = 31
                self.cooldown = 4
        
        if self.change_time <= 15:
            window.blit(self.spritesheet1,(self.spritesheete_pos[0],self.spritesheete_pos[1]))
            
        if self.change_time >= 16 and self.change_time < 31:
            window.blit(self.spritesheet3,(self.spritesheete_pos[0],self.spritesheete_pos[1]))
            
        
        if self.change_time >= 31:
            window.blit(self.sprite_attack_big,(self.spritesheete_pos[0],self.spritesheete_pos[1]))
            
        if self.change_time == 30:
            self.change_time = 0
            
        if self.change_time == 45:
            self.change_time = 0
            
        self.change_time += 1
        self.cooldown -= 1
        
    def move(self,keys):
        if self.ff <= 0:
            if keys[pygame.K_SPACE]:
                self.ff = 60 
                
        if self.ff <= 60 and self.ff >= 31:
            self.spritesheete_pos[1] -= 4
            
        if self.ff <= 30 and self.ff >= 1:
                self.spritesheete_pos[1] += 4
                
        if self.spritesheete_pos[0] > 20:
            if keys[pygame.K_a]:
                self.spritesheete_pos[0] -= self.speed
            
        if self.spritesheete_pos[0] + self.spriteshee2.get_width()*4 < 980:
            if keys[pygame.K_d]:
                self.spritesheete_pos[0] += self.speed

        self.ff -= 1      
        
        
        
        

l_targets = []
target = Target(400,600,2,125,100,1)
l_targets.append(target)

if target.direction == 0:
    target.x = -150
if target.direction == 1:
    target.x = 950

l_zombies = []



sprite_zombie_right = pygame.image.load("zombie_right.png")
q = sprite_zombie_right.get_width()*4

spriteshee2 = pygame.image.load('run.knight2.png')
aa = spriteshee2.get_height()*4



zom = Zombie(1.5,0,random.randint(10,990 - q),520,50)
l_zombies.append(zom)


sprite_offset_x = 19


sprites = pygame.image.load("KnightSpritesheet.png")
i = 0
import time

sprites = pygame.transform.scale(sprites,(sprites.get_width()*4,sprites.get_height()*4))
#hile True:
#   if i>3:
#       i = 0
#   window.fill("black")
#   window.blit(sprites,(0,0),(56*i*4,1*4,37*4,54*4))
#   pygame.display.update()
#   i+=1
#   time.sleep(0.45)
    
    
p = Player([1,590],3)

clock = pygame.time.Clock()


hauntstage = 1
hillstage = 0


while True:
    
    
    window.fill("White")
    
    spawn_zombies = random.randint(0,10000)
    if len(l_zombies) <= 2:
        if spawn_zombies <= 10:
            zom = Zombie(1.5,0,random.randint(10,990 - q),520,50)
            l_zombies.append(zom)
    
    
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
        

        
        
    zom.move(p.spritesheete_pos[0],p.spritesheete_pos[1])
    zom.draw(window)
    
    p.move(keys)
    #pygame.draw.rect(window, pygame.Color("Gray"), pygame.Rect((0,650, 1000,100)))
    
    p.draw(window)

            
    pygame.display.update()
    
    clock.tick(FPS)
    