#!/usr/bin/env python

import pygame
from resources import *

#--Images and Sounds Files:
images = None
sounds = None
#--------------------------
# Screen dimensions:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
#=======================================================================
class Sprite(pygame.sprite.Sprite):
    """"This class represent a little piece of the player bottom """
    def __init__(self,left,top,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(left,top,width,height)

class Player(pygame.sprite.Sprite):
    """This class represents the player."""
    #these variables will track the speed of the player...
    changeX = 0 
    changeY = 0
    orientacion =2
    #-----------
    walkPos = 0 # this will hold the current image of the walkImages sequence.
    jumped = False # this is will be true when the player is on the air.
    terminate = False # will be true when the game have to finish
    level = None # a reference to the level
    coins = 0 # the number of coins collected
    game_over = False # true when the game is over
    vida = False
    def __init__(self,pos,imagesFiles,soundsFiles):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        #===============
        global images  
        global sounds
        #===============
        images = imagesFiles 
        sounds = soundsFiles
        #===============
        #Create a tuple that contain all the images needed for the walking animation in order:
        self.walkDerecha = (images["Margery_Run Right_0"],images["Margery_Run Right_0"],
                            images["Margery_Run Right_0"],images["Margery_Run Right_1"],images["Margery_Run Right_1"],
                            images["Margery_Run Right_1"],images["Margery_Run Right_2"],images["Margery_Run Right_2"],                       				    images["Margery_Run Right_2"],images["Margery_Run Right_3"],images["Margery_Run Right_3"],
			    images["Margery_Run Right_3"])
	self.walkIzquierda =(images["Margery_Run Left_0"],images["Margery_Run Left_0"],images["Margery_Run Left_0"],
				images["Margery_Run Left_1"],images["Margery_Run Left_1"],images["Margery_Run Left_1"],
				images["Margery_Run Left_2"],images["Margery_Run Left_2"],images["Margery_Run Left_2"],
				images["Margery_Run Left_3"],images["Margery_Run Left_3"],images["Margery_Run Left_3"])
        
        if self.orientacion==1:
                self.image = self.walkIzquierda[0]
	elif self.orientacion==2:
		self.image = self.walkDerecha[0]
        self.rect = self.image.get_rect()
        
        
        #Create a custom sprite that represent the base of the player.
        self.innerSprite = Sprite(self.rect.left,self.rect.bottom -10,self.rect.width,10)

        self.rect.center = pos
        self.terminate = False

    def update(self):
        # Check the boundaries of the screen:
        if self.rect.x < 5 and self.changeX < 0:
            self.changeX = 0
        elif self.rect.x > SCREEN_WIDTH - 70 and self.changeX > 0:
            self.changeX = 0
            
        #Update innerSprite coordinates:
        self.innerSprite.rect.bottomleft = self.rect.bottomleft

        #Gravity:
        self.gravity()
        
        #Move left/right
        self.rect.x += self.changeX
        #See if we hit a block:
        hit_list = pygame.sprite.spritecollide(self,self.level.block_list,False)
        for block in hit_list:
            if isinstance(block,MovableBlock):
                if self.changeX > 0 and not block.touched:
                    self.rect.right = block.rect.left
                elif self.changeX < 0 and not block.touched:
                    self.rect.left = block.rect.right
            elif isinstance(block,AnimatedBlock):
                self.terminate = True
                sounds["slime"].play()
            elif isinstance(block,Fly):
                pass
            elif isinstance(block,Shell):
                pass
            else:
                if self.changeX > 0:
                    self.rect.right = block.rect.left
                elif self.changeX < 0:
                    self.rect.left = block.rect.right
                    
        #This will check if we are on the top of the world...
        if self.changeY < self.level.world_shift[1] and self.level.world_shift[1] < 0:
            self.level.shift_world((0,self.level.world_shift[1] * -1))
        #This will scroll the world up and down...
        self.level.scroll_world(self)
        #===============================================================
        #Move up/down
        self.rect.y += self.changeY
        self.innerSprite.rect.bottom = self.rect.bottom
        #===============================================================
        #See if we hit a block:
        hit_list = pygame.sprite.spritecollide(self,self.level.block_list,False)
        for block in hit_list:
            if isinstance(block,MovableBlock):
                if self.changeY > 0 and not block.touched:
                    self.rect.bottom = block.rect.top
                    self.jumped = False
		    if self.orientacion==1:
                	self.image = self.walkIzquierda[0]
		    elif self.orientacion==2:
			self.image = self.walkDerecha[0]
                    self.changeY = 0
                    if self.rect.bottom >= SCREEN_HEIGHT -30:
                        self.level.shift_world((0,(SCREEN_HEIGHT -30) - self.rect.bottom))
                        self.rect.bottom = SCREEN_HEIGHT -30
            elif isinstance(block,Spring):
                if self.changeY > 0:
                    if block.shrunken:
                        self.rect.bottom = block.rect.top
                        self.jumped = False
                        if self.orientacion==1:
                		self.image = self.walkIzquierda[0]
		        elif self.orientacion==2:
				self.image = self.walkDerecha[0]
                        self.changeY = 0
                else:
                    self.rect.top = block.rect.bottom
                    self.changeY = 0
            elif isinstance(block,Weight):
                if self.changeY > 0:
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                    if self.orientacion==1:
                	self.image = self.walkIzquierda[0]
		    elif self.orientacion==2:
			self.image = self.walkDerecha[0]
                    self.changeY = 0
                else:
                    self.rect.top = block.rect.bottom
                    self.changeY = 0
            elif isinstance(block,AnimatedBlock):
                if block.is_snail and self.changeY > 0:
                    self.level.block_list.remove(block)
                    shell = Shell(block.rect.topleft,images["snailShell"])
                    shell.leftLimit = block.leftLimit
                    shell.rightLimit = block.rightLimit
                    shell.changeX = block.changeX
                    shell.previous_snail_pos = block.rect.topleft
                    self.level.items_list.add(shell)
                    
                elif not self.terminate and self.changeY > 0:
                    self.level.block_list.remove(block)
                    #self.level.score_list.add(ScoreBlock(self.rect.center,images["hud_5"]))
                    self.level.dead_sprites_list.add(DeadSprite(block.rect.topleft,block.dead_image))
                elif self.changeY < 0:
                    self.rect.top = block.rect.bottom
                    self.changeY = 0
            elif isinstance(block,Fly):
                if self.changeY > 0 and self.jumped:
                    #self.level.score_list.add(ScoreBlock(self.rect.center,images["hud_4"]))
                    self.level.dead_sprites_list.add(DeadSprite(block.rect.topleft,images["flyDead"]))
                    self.level.block_list.remove(block)
                elif not self.terminate:
                    self.terminate = True
                    sounds["slime"].play()
            else:
                if self.changeY > 0:
                    self.rect.bottom = block.rect.top
                    self.jumped = False
                    if self.orientacion==1:
                	self.image = self.walkIzquierda[0]
		    elif self.orientacion==2:
			self.image = self.walkDerecha[0]
                    self.changeY = 0
                    if self.rect.bottom >= SCREEN_HEIGHT -30:
                        self.level.shift_world((0,(SCREEN_HEIGHT -30) - self.rect.bottom))
                        self.rect.bottom = SCREEN_HEIGHT -30
                else:
                    self.rect.top = block.rect.bottom
                    self.changeY = 0
        #===============================================================        
        #See if we hit a platform:
        hit_list = pygame.sprite.spritecollide(self.innerSprite,self.level.platform_list,False)
        for platform in hit_list:
            if self.changeY > 0:
                self.rect.bottom = platform.rect.top
                self.jumped = False
                if self.orientacion==1:
                	self.image = self.walkIzquierda[0]
		elif self.orientacion==2:
			self.image = self.walkDerecha[0]
                self.changeY = 0
                if self.rect.bottom >= SCREEN_HEIGHT -30:
                    self.level.shift_world((0,(SCREEN_HEIGHT -30) - self.rect.bottom))
                    self.rect.bottom = SCREEN_HEIGHT -30
        #===============================================================
        #See if we hit a hud object:
        hit_list = pygame.sprite.spritecollide(self,self.level.hud_list,True)
        for block in hit_list:
            #self.level.score_list.add(ScoreBlock(block.rect.center,images["hud_1"]))
            sounds["coin"].play()
            self.coins += 1
        #===============================================================
	#See if we hit a items object:
        hit_list = pygame.sprite.spritecollide(self,self.level.items_list,True)
        for block in hit_list:
            self.vida = True
        #===============================================================
        #see if we are in the air:
        if self.changeY > 0 and not self.jumped:
            self.jumped = True
	    if self.orientacion==1:
            	self.image = images["playerJumpIzquierda"]
	    elif self.orientacion==2:
            	self.image = images["playerJumpDerecha"]
        #===============================================================
        # change the image of the player while it's walking...    
        if not self.jumped:
            if self.changeX != 0:
		if self.orientacion==1:
                	self.image = self.walkIzquierda[self.walkPos]
		elif self.orientacion==2:
			self.image = self.walkDerecha[self.walkPos]
                if self.walkPos == len(self.walkIzquierda) -1:
                    self.walkPos = 1
                else:
                    self.walkPos += 1
            elif self.walkPos != 0:
                self.walkPos = 0
                if self.orientacion==1:
                	self.image = self.walkIzquierda[0]
		elif self.orientacion==2:
			self.image = self.walkDerecha[0]
        #===============================================================
        
    def gravity(self):
        """calculate the effect of the gravity."""
        if self.changeY == 0:
            self.changeY = 3
        elif self.changeY < 15:
            self.changeY += 1
        if self.rect.bottom > SCREEN_HEIGHT:
            self.terminate = True

    def jump(self):
        """Call when the user press the 'jump' button."""
        if not self.jumped:
            # Move down a bit and see if there is a platform below us.
            self.rect.y += 3
            hit_list1 = pygame.sprite.spritecollide(self,self.level.block_list,False)
            hit_list2 = pygame.sprite.spritecollide(self,self.level.platform_list,False)
            self.rect.y -= 3
            
            if self.rect.bottom == SCREEN_HEIGHT or len(hit_list1) > 0 or len(hit_list2) > 0:
                self.changeY = -20
                if self.orientacion==1:
            		self.image = images["playerJumpIzquierda"]
	    	elif self.orientacion==2:
            		self.image = images["playerJumpDerecha"]
                self.jumped = True
                self.walkPos = 1
                sounds["jump"].play()

    def down(self):
        """Call when the user press the 'down button'."""
        # Move two pixels down to test if we are on a platform or a block:
        self.innerSprite.rect.y += 5
        hit_list = pygame.sprite.spritecollide(self.innerSprite,self.level.platform_list,False)
        self.innerSprite.rect.y -= 5 # Move two pixels up to restore the original setting.
        for block in hit_list:
            if isinstance(block,Platform):
                if len(hit_list) > 0 and self.rect.bottom >= SCREEN_HEIGHT -30:
                    self.level.shift_world((0,-20))
                else:
                    for platform in hit_list:
                        self.innerSprite.rect.top = platform.rect.bottom
                        self.rect.bottom = self.innerSprite.rect.bottom
                        if self.orientacion==1:
            			self.image = images["playerJumpIzquierda"]
	    		elif self.orientacion==2:
            			self.image = images["playerJumpDerecha"]
                        self.jumped = True
                    if self.rect.bottom >= SCREEN_HEIGHT -30:
                        self.level.shift_world((0,-20))
    #===================================================================
    def move_left(self):
        self.changeX = -3
	self.orientacion=1
    def move_right(self):
        self.changeX = 3
	self.orientacion=2;
    def stop(self):
        self.changeX = 0
	
    #===================================================================    
    def terminate_game(self):
        if self.rect.top > SCREEN_HEIGHT:
            self.game_over = True
        else:
            self.rect.y += 3
        if self.orientacion==1:
                self.image = self.walkIzquierda[0]
	elif self.orientacion==2:
		self.image = self.walkDerecha[0]
