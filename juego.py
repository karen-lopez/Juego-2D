#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame,niveles
from jugador import Player
from FilesLoader import *
from menu import Menu
#--Images and Sounds Files:
images = None
sounds = None
#--------------------------
# Screen dimensions:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
#=======================================================================
#.............................Main Class................................
class Game(object):
    running = False
    quitGame = False
    win_message = False
    lives = 2
    
    opciones_menu = False
    ayuda_menu = False
    continuar_menuPausa = False
    menu_menuPausa =False
    game_over = False
    menu1 = True
    pausa = False 
    
    def __init__(self,screen):
        # Load images
        global images
        images = loadImages()
        #Load sounds Effects
        global sounds
        sounds = loadSounds()
        # Ojbects
        self.player = Player((93,324),images,sounds)
        self.playerSprite = pygame.sprite.Group()
        self.playerSprite.add(self.player)
        # -------------------
        self.levelList = []
        self.levelList.append(niveles.Level_One(images,sounds,self.player))
        self.levelList.append(niveles.Level_Two(images,sounds,self.player))
        self.currentLevel = 0
        self.level = self.levelList[self.currentLevel]
        self.level.load_music()
        self.player.level = self.level
        #--------------------------------------------------------------
        self.text_font = pygame.font.Font("fuentes/FreeSansBold.ttf",38)
        #Create menu object:

        self.menu = Menu(screen,("INICIO","OPCIONES","AYUDA","SALIR"),ttf_font="fuentes/dejavu.ttf",
                                font_color=(0,0,0),bg_image=images["intro"],font_size=34)
	self.menuPausa = Menu(screen,("Continuar Juego","Menu prinsipal"),ttf_font="fuentes/dejavu.ttf",
                                font_color=(0,0,0),bg_image=images["background"],font_size=34)

        self.screen = screen
    def run_logic(self):
        if self.running:
            if not self.player.game_over:
                self.level.update()
                # See if we have to shift the levels   
                limit_left =  self.level.limit_left()
                x = self.player.rect.x
                if  limit_left and x > SCREEN_WIDTH - 105:
                    if self.currentLevel < len(self.levelList) -1:
                        pygame.mixer.music.stop()
                        self.player.rect.center = (93,324)
                        self.currentLevel += 1
                        self.level = self.levelList[self.currentLevel]
                        self.level.load_music()
                        self.player.level = self.level
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
                        if self.orientacion==1:
                		self.image = self.walkIzquierda[0]
		    	elif self.orientacion==2:
				self.image = self.walkDerecha[0]
                        self.win_message = True

	        if self.player.vida:
			self.lives +=1
			self.player.vida = False
            else:
                if self.lives == 0:
                    self.running = False
                    self.game_over = True
                else:
                    self.lives -= 1
                    self.__init__(self.screen)
                    pygame.mixer.music.play(-1)
	    
    #-------------------------------------------------------------------
    def displayFrame(self,screen):
        if self.running:
            self.level.draw(screen)
            self.playerSprite.draw(screen)
            
            screen.blit(images["hud_p3Alt"],(5,5))
            screen.blit(images["hud_x"],(60,15))
            if self.lives == 3:
                screen.blit(images["hud_3"],(110,10))
            elif self.lives == 2:
                screen.blit(images["hud_2"],(110,10))
            elif self.lives == 1:
                screen.blit(images["hud_1"],(110,10))
            else:
                screen.blit(images["hud_0"],(110,10))
                
            screen.blit(images["hud_coin"],((SCREEN_WIDTH / 2) -60,10))
            screen.blit(images["hud_x"],(SCREEN_WIDTH /2,20))
            
            # draw the number of coins collected: ----------------------
            coins = str(self.player.coins)
            if len(coins) < 2:
                coins = "0" + coins
            i = 50
            for n in coins:
                screen.blit(self.number_image(int(n)),((SCREEN_WIDTH / 2)+i,10))
                i += 35
            # ----------------------------------------------------------
            
            if self.win_message:
                text = self.text_font.render("GANASTE!!",True,(128,128,255))
                screen.blit(text,(30,300))
                pygame.display.flip() 
                pygame.time.wait(3000)
                self.running = False
                self.win_message = False
        elif self.opciones_menu:
            self.screen.blit(images["intro"],(0,0))
	elif self.ayuda_menu:
            self.screen.blit(images["intro"],(0,0))
	    text = self.text_font.render("La respuesta esta en tu corazon",True,(128,128,255))
            screen.blit(text,(30,300))
	elif self.continuar_menuPausa:
            self.pausa = False
	    self.running = True
	elif self.menu_menuPausa:
            self.menu.display_frame()
	    self.menu1 = True
	    self.pausa = False
        elif self.game_over:
            self.screen.blit(images["intro"],(0,0))
            text = self.text_font.render("GAME OVER",True,(128,128,255))
            screen.blit(text,(250,125))
            text = self.text_font.render("presiona ESC para ir menu",True,(128,128,255))
            screen.blit(text,(30,300)) 
        else:
	    if self.menu1:
            	self.menu.display_frame()
	    if self.pausa:
		self.menuPausa.display_frame()
    #-------------------------------------------------------------------
    def number_image(self,n):
        """ return a image with the number given in it. """
        if n == 1:
            return images["hud_1"]
        elif n == 2:
            return images["hud_2"]
        elif n == 3:
            return images["hud_3"]
        elif n == 4:
            return images["hud_4"]
        elif n == 5:
            return images["hud_5"]
        elif n == 6:
            return images["hud_6"]
        elif n == 7:
            return images["hud_7"]
        elif n == 8:
            return images["hud_8"]
        elif n == 9:
            return images["hud_9"]
        else:
            return images["hud_0"]
    #-------------------------------------------------------------------
    def eventHandler(self):
        flag = False
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                flag = True # Flag that we are done so we exit this loop
                pygame.mixer.music.stop()
            #---------KEY DOWN EVENTS-----------------------------------
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif event.key == pygame.K_UP:
                    if self.running:
                        self.player.jump()
                elif event.key == pygame.K_DOWN:
                    if self.running:
                        self.player.down()
                elif event.key == pygame.K_ESCAPE:
                    if self.running:
			self.pausa = True
                        self.running = False
			self.menu_menuPausa = False
			self.continuar_menuPausa = False
			self.menu1 = False
                        pygame.mixer.music.stop()
		    elif self.menu1:
		            self.lives = 2
		            self.ayuda_menu = False
		            self.opciones_menu = False
		            self.game_over = False

                elif event.key == pygame.K_RETURN and not self.running:
			if self.menu1 :
		            if not self.opciones_menu and not self.ayuda_menu and not self.game_over:
		                if self.menu.state == 0:
		                    self.__init__(self.screen)
		                    self.lives = 2
		                    self.running = True
		                    pygame.mixer.music.play(-1)
		                elif self.menu.state == 1:
		                    self.opciones_menu = True
				    self.running = False
				elif self.menu.state == 2:
		                    self.ayuda_menu = True
		                else:
		                    self.quitGame = True
				#self.menu = False

			if self.pausa :
		            if not self.menu_menuPausa and not self.game_over:
		                if self.menuPausa.state == 0:
		                   # self.__init__(self.screen)
		                    #self.lives = 2
		                    self.running = True
		                    pygame.mixer.music.play(-1)
		                elif self.menuPausa.state == 1:
		                    self.menu_menuPausa = True
				#self.menuPausa = False

                        
                if not self.running:
		    if self.menu1:
                    	self.menu.event_handler(event)
		    if self.pausa:
			self.menuPausa.event_handler(event)
            #---------KEY UP EVENTS-------------------------------------
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT:
                    self.player.stop()
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (self.player.rect.left + abs(self.level.world_shift[0]),
                        self.player.rect.top - (500 - abs(self.level.world_shift[1])))
            if self.quitGame:
                flag = True

        return flag
