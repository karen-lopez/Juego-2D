#!/usr/bin/env python

import pygame,math

#--Images and Sounds Files:
images = None
sounds = None
#--------------------------
# Screen dimensions:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
#=======================================================================
class Block(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def actualizar(self,img):
	self.rect = self.img.get_rect()
#=======================================================================
class Shell(Block):
    done = False
    countdown = 150
    leftLimit = 0
    rightLimit = 0
    changeX = 0
    previous_snail_pos = None
    def __init__(self,pos,img):
        Block.__init__(self,pos,img)
        self.is_shell = True
        
    def update(self):
        if self.countdown == 0:
            self.done = True
        else:
            self.countdown -= 1
#======================================================================= 
class AnimatedItem(Block):
    firstImage = True
    countdown = 9
    def __init__(self,pos,img1,img2):
        Block.__init__(self,pos,img1)
        self.image1 = img1
        self.image2 = img2
        
    def update(self):
        if self.countdown == 0:
            if self.firstImage:
                self.image = self.image2
                self.firstImage = False
            else:
                self.image = self.image1
                self.firstImage = True
            self.countdown = 9
        else:
            self.countdown -= 1
#======================================================================= 
class Animacion(Block):
    imagen= None
    img= None
    def __init__(self,pos,imagen,n,width,height):
        Block.__init__(self,pos,imagen)
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.current_frame = 0
        self.frames = n
        self.frame_width = width
        self.frame_height = height
        
    def update(self):
        if self.current_frame >=  self.frames - 1:
            self.current_frame = 0
        else:
            self.current_frame += 1
        new_area = pygame.Rect((self.current_frame * self.frame_width, 0, self.frame_width, self.frame_height))
        imag=self.imagen.subsurface(new_area)
	self.image=img
	self.actualizar(img)
#=======================================================================
class DeadSprite(Block):
    def __init__(self,pos,img):
        Block.__init__(self,pos,img)
    def update(self):
        self.rect.y -= 10
#=======================================================================
class Fly(AnimatedItem): ##aplicar algoritmo raro
    dead = False
    angle = 0
    def __init__(self,pos,img1,img2):
        AnimatedItem.__init__(self,pos,img1,img2)
        
    def update(self):
        if self.dead:
            self.rect.y += 10
        else:
            if self.countdown == 0:
                if self.firstImage:
                    self.image = self.image2
                    self.firstImage = False
                else:
                    self.image = self.image1
                    self.firstImage = True
                self.countdown = 7
            else:
                self.countdown -= 1
            
            self.rect.x += int(3 * math.sin(math.radians(self.angle)))    
            self.rect.y += int(3 * math.cos(math.radians(self.angle)))
            
            if self.angle >= 360:
                self.angle = 0
            
            self.angle += 1
        
#=======================================================================
class MovableBlock(Block):
    level = None
    def __init__(self,pos,img1,img2,player):
        Block.__init__(self,pos,img1)
        self.drawing = pygame.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height) 
        self.player = player
        self.touched = False
        self.scored = False
        self.img2 = img2
        
    def update(self):
        if pygame.sprite.collide_rect(self,self.player):
            if self.level.world_shift[0] < 0 and self.player.rect.x <= 60:
                self.drawing.bottom = self.player.rect.top
                self.drawing.x += self.player.changeX *-1
            elif not self.level.limit_left() and self.player.rect.x >= SCREEN_WIDTH -142:
                self.drawing.bottom = self.player.rect.top
                self.drawing.x += self.player.changeX *-1
            else:
                self.drawing.bottom = self.player.rect.top
            self.touched = True
            if not self.scored:
                sounds["coin"].play()
                self.scored = True
                self.level.score_list.add(ScoreBlock(self.rect.center,images["hud_1"]))
                self.image = self.img2
                self.player.coins += 1
            self.player.changeY += 2
        else:
            self.drawing.topleft = self.rect.topleft 
            self.touched = False
#=======================================================================
class Platform(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        rect = self.image.get_rect()
        self.rect = pygame.Rect(rect.left,rect.top,rect.width,10)
        self.rect.topleft = pos
#=======================================================================   
class MovingPlatform(Platform):
    changeX = 0
    changeY = 0
    bottomLimit = 0
    topLimit = 0
    leftLimit = 0
    rightLimit = 0
    level = None
    player = None
    def update(self):
        self.rect.x += self.changeX
        self.rect.y += self.changeY
        # check if the player is on the platform:-----------------------
        self.player.rect.y += 5
        if pygame.sprite.collide_rect(self,self.player.innerSprite):
            if self.player.rect.x >= SCREEN_WIDTH -142 and self.changeX > 0:
                self.player.rect.x = SCREEN_WIDTH -142
                self.level.shift_world(((self.changeX + self.player.changeX)*-1,0))
            elif self.player.rect.x <= 60 and self.changeX < 0:
                self.player.rect.x = 60
                self.level.shift_world(((self.changeX + self.player.changeX)*-1,0))
            else:
                self.player.rect.x += self.changeX
            #self.player.changeY = 4
            if self.player.rect.top < 40 and self.changeY < 0:
                self.level.shift_world((0,self.changeY *-1))
        self.player.rect.y -= 5
        #---------------------------------------------------------------
        
        if self.rect.bottom > self.bottomLimit or self.rect.top < self.topLimit:
            self.changeY *= -1
        cur_pos = self.rect.x - self.level.world_shift[0]
        if cur_pos < self.leftLimit or cur_pos > self.rightLimit:
            self.changeX *= -1
#=======================================================================
class AnimatedBlock(Block):
    changeX = 0
    changeY = 0
    bottomLimit = 0
    topLimit = 0
    leftLimit = 0
    rightLimit = 0
    level = None
    player = None
    imagen = None
    image1= None
    dead_image = None
    firstImage = True
    count = 0
    is_snail = False #True if this AnimatedBlock represent a snail.
    is_shell = False #True if this AnimatedBlock represent a shell
    def __init__(self,pos,img):
        Block.__init__(self,pos,img)
        self.rect.bottomleft = pos
    def update(self):
        #------------------------------
        self.rect.x += self.changeX
        self.rect.y += self.changeY
        #---------------------------------------------------------------
	self.image1 = self.imagen[self.count]      
        if self.rect.bottom > self.bottomLimit or self.rect.top < self.topLimit:
            self.changeY *= -1
        cur_pos = self.rect.x - self.level.world_shift[0]
        if cur_pos < self.leftLimit or cur_pos > self.rightLimit:
            self.changeX *= -1
	if self.changeX > 0:
            self.image1 = pygame.transform.flip(self.imagen[self.count],True,False)
            self.dead_image = pygame.transform.flip(self.dead_image,True,False)

	if self.count == len(self.imagen)-1:
		self.count=0
        self.image= self.image1
	self.count += 1
#=======================================================================
class Spring(Block):
    countdown = 150
    def __init__(self,pos,img,player):
        Block.__init__(self,pos,img)
        self.rect.bottomleft = pos
        self.shrunken = False
        self.player = player
		
    def update(self):
        if self.countdown == 0:
            self.shrunken = False
            self.image = images["SpringDown"]
            self.countdown = 150
        else:
            self.countdown -= 1
        #------------------------------------    
        if pygame.sprite.collide_rect(self,self.player):
            self.player.changeX = 0
            if not self.shrunken:
                self.image = images["SpringUp"]
                self.player.changeY = -30
                self.shrunken = True
                sounds["spring"].play()
#=======================================================================
class Weight(Block):
    countdown = 120
    change = True
    changeY = 0
    def __init__(self,pos,img,player,group,items_list):
        Block.__init__(self,pos,img)
        self.player = player
        self.group = group
        self.initial_position = list(pos)
        items_list.add(Block((self.rect.left,self.rect.top -70),images["chain"]))
        items_list.add(Block((self.rect.left,self.rect.top -140),images["box2"]))
    def update(self):
        if self.countdown == 0:
            if self.change:
                self.image = images["weight"]
                self.rect.y += self.changeY
                self.changeY += 1
                if pygame.sprite.collide_rect(self,self.player):
                    self.player.terminate = True
                    sounds["weight"].play()
                hit_list = pygame.sprite.spritecollide(self,self.group,False)
                for block in hit_list:
                    self.rect.bottom = block.rect.top
                    self.countdown = 120
                    sounds["weight"].play()
                    self.change = False
            else:
                self.countdown = 120
                self.changeY = 0
                self.rect.topleft = self.initial_position
                self.image = images["weightChained"]
                self.change = True
                if pygame.sprite.collide_rect(self,self.player):
                    self.player.rect.bottom = self.rect.top
        elif self.rect.x < SCREEN_WIDTH +70 and self.rect.x > 0:
            self.countdown -= 1
        else:
            self.countdown = 120
#=======================================================================
class ScoreBlock(Block):
    countdown = 60
    def __init__(self,pos,img):
        # Call the parent class (Block) constructor:
        Block.__init__(self,pos,img)
        self.rect.center = pos

    def update(self):
        self.rect.y -= 2
        self.countdown -= 1
    
    def check(self):
        if self.countdown == 0:
            return True
        else:
            return False
#=======================================================================
def load_images_sounds(imagesFiles,soundsFiles):
    global images
    global sounds
    #------------
    images = imagesFiles
    sounds = soundsFiles
    
