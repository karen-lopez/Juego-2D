#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from resources import *
#--------------------------
# Screen dimensions:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
#--------------------------
#--Images and Sounds Files:
images = None
sounds = None
#--------------------------

class Level(object):
    """This is a super-class used to define a class"""
    def __init__(self,imagesFiles,soundsFiles,player):
        global images
        global sounds
        images = imagesFiles
        sounds = soundsFiles
        # Pass images and sounds to resources.py module.
        load_images_sounds(images,sounds)
        #----Create the sprite.Groups ----------------------------------
        self.platform_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.hud_list = pygame.sprite.Group()
        self.score_list = pygame.sprite.Group()
        self.items_list = pygame.sprite.Group()
        self.dead_sprites_list = pygame.sprite.Group()
        # Pass player object -------------------------------------------
        self.player = player
        self.background = images["background"] # set the background image.
        # Hasta qué punto este mundo ha sido desplazado izquierda / derecha / arriba / abajo.
        self.world_shift = [0,SCREEN_HEIGHT *-1]
    #===================================================================  
    def update(self):
        if not self.player.terminate:
            # Update all the sprite.Groups: ----------------------------
            self.player.update() # update player...
            self.platform_list.update()
            self.block_list.update()
            self.score_list.update()
            self.items_list.update()
            self.dead_sprites_list.update()
            # delete score blocks:
            for score in self.score_list:
                if score.check():
                    self.score_list.remove(score)
            # check limits:
            if self.player.rect.x > SCREEN_WIDTH -142 and not self.limit_left():
                self.player.rect.x = SCREEN_WIDTH -142
                self.shift_world((-3,0))
            elif self.player.rect.x < 60 and self.world_shift[0] < 0:
                self.player.rect.x = 60
                self.shift_world((3,0))
            #check for shell convertion to snail    
            for item in self.items_list:
                if isinstance(item,Shell):
                    if item.done:
                        snail = AnimatedBlock(item.rect.bottomleft,images["snailWalk1"])
                        snail.image1 = images["snailWalk1"]
                        snail.image2 = images["snailWalk2"]
                        snail.leftLimit = item.leftLimit
                        snail.rightLimit = item.rightLimit
                        snail.changeX = -2
                        snail.level = self
                        snail.player = self.player
                        snail.is_snail = True
                        snail.dead_image = images["snailShell"]
                        self.block_list.add(snail)
                        self.items_list.remove(item)
            # check if one the blocks is out of the screen:
            for dead in self.dead_sprites_list:
                if dead.rect.top > SCREEN_HEIGHT:
                    self.dead_sprites_list.remove(dead)
        else:
            self.player.terminate_game()
            pygame.mixer.music.stop()
    #===================================================================    
    def draw(self,screen):
        """draw everything on the screen"""
        screen.fill(self.background_color)
        # Draw all the platforms into the screen:
        self.platform_list.draw(screen)
        # Draw all the items objects:
        self.items_list.draw(screen)
        # Draw all the blocks:
        for block in self.block_list:
            if isinstance(block,MovableBlock):
                screen.blit(block.image,block.drawing)
            else:
                screen.blit(block.image,block.rect)
        # Draw dead sprites into the screen:
        self.dead_sprites_list.draw(screen)
        # Draw all the hud object into the screen:
        self.hud_list.draw(screen)
        # Draw score items into the screen: ----------------------------
        self.score_list.draw(screen)
    #===================================================================
    def shift_world(self,shift):
        """When the user moves left/right and we need to scroll everything:"""
        #keep track on the shift amount.
        for i, v in enumerate(shift):
            self.world_shift[i] += v
        # Go through all the sprites and shift.
        for platform in self.platform_list:
            if isinstance(platform,MovingPlatform):
                platform.topLimit += shift[1]
                platform.bottomLimit += shift[1]
            platform.rect.x += shift[0]
            platform.rect.y += shift[1]
        #------------------------------------------
        for block in self.block_list:
            if isinstance(block,Weight):
                block.initial_position[0] += shift[0]
                block.initial_position[1] += shift[1]
            block.rect.x += shift[0]
            block.rect.y += shift[1]
        #-------------------------------------------
        for score in self.score_list:
            score.rect.x += shift[0]
            score.rect.y += shift[1]
        #-------------------------------------------
        for hud in self.hud_list:
            hud.rect.x += shift[0]
            hud.rect.y += shift[1]
        #-------------------------------------------
        for item in self.items_list:
            item.rect.x += shift[0]
            item.rect.y += shift[1]
        #-------------------------------------------
        for dead in self.dead_sprites_list:
            dead.rect.x += shift[0]
            dead.rect.y += shift[1]
    #===================================================================
    def limit_left(self):
        if self.limit[0] >= self.world_shift[0]:
            return True
        else:
            return False

    def limit_bottom(self):
        if self.limit[1] >= self.world_shift[1]:
            return True
        else:
            return False
    #===================================================================      
    def scroll_world(self,player):
        previousPosition = self.world_shift[1]
        self.world_shift[1] += player.changeY * -1
        if player.jumped:
            if player.changeY < 0:
                if player.rect.y < 40 and self.world_shift[1] < 0:
                    self.world_shift[1] = previousPosition
                    player.rect.y = 40
                    self.shift_world((0,player.changeY * -1))
                else:
                    self.world_shift[1] = previousPosition
                
            elif player.rect.bottom > SCREEN_HEIGHT - 30 and not self.limit_bottom():
                    player.rect.bottom = SCREEN_HEIGHT - 30
                    self.world_shift[1] = previousPosition
                    self.shift_world((0,player.changeY * -1))
            else:
                self.world_shift[1] = previousPosition
        else:
            self.world_shift[1] = previousPosition
    
    def load_music(self):
        pygame.mixer.music.load(self.music_filename)
