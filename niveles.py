#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from resources import *
from level_class import Level
#--Images Files:
images = None
#=======================================================================
class Level_One(Level):
    limit = (-2000,-500)
    background_color = (100,244,247)
    music_filename = "sounds/music.ogg"
    def __init__(self,imagesFiles,soundsFiles,player):
        Level.__init__(self,imagesFiles,soundsFiles,player)
        #========================
        global images
        images = imagesFiles
        #========================
		#------x inicial,rango ancho, rango alto, PLATAFORMA1 PISO1
        for i in range(0,70*3,70):
            platform = Block((i,450),images["grassMid"])
            self.platform_list.add(platform)
        platform = Block((210,450),images["grassRight"])
        self.platform_list.add(platform)

	#PLATAFORMA2 PISO3
        		#x,y
        platform = Platform((280,310),images["grassHalfLeft"])
        self.platform_list.add(platform)
	platform = Platform((350,310),images["grassHalfMid"])
        self.platform_list.add(platform)
        platform = Platform((420,310),images["grassHalfRight"])
        self.platform_list.add(platform)

        #PLATAFORMA3 PISO1
	platform = Platform((420,450),images["grassLeft"])
        self.platform_list.add(platform)
	platform = Platform((490,450),images["grassMid"])
        self.platform_list.add(platform)
        platform = Platform((560,450),images["grassRight"])
        self.platform_list.add(platform)

	#PLATAFORMA4 PISO1
	platform = Platform((910,450),images["grassLeft"])
        self.platform_list.add(platform)
	for i in range(980,1190,70):
            platform = Block((i,450),images["grassMid"])
            self.platform_list.add(platform)
	platform = Platform((1190,450),images["grassRight"])
        self.platform_list.add(platform)

	#PLATAFORMA5 PISO1
	platform = Platform((1610,450),images["grassLeft"])
        self.platform_list.add(platform)
	for i in range(1680,2520,70):
            platform = Block((i,450),images["grassMid"])
            self.platform_list.add(platform)

	#PLATAFORMA12 PISO1
	platform = Platform((2590,450),images["grassLeft"])
        self.platform_list.add(platform)
	platform = Block((2660,450),images["grassMid"])
        self.platform_list.add(platform)

	
	#PLATAFORMA6 PISO2
	platform = Platform((560,380),images["grassLeft"])
        self.platform_list.add(platform)
	for i in range(630,910,70):
		platform = Block((i,380),images["grassMid"])
        	self.platform_list.add(platform)
	platform = Platform((910,380),images["grassRight"])
        self.platform_list.add(platform)


        #PLATAFORMA7 PISO2 (movil)
        movingPlatform = MovingPlatform((1270,400),images["grassHalf"])
        movingPlatform.leftLimit = 1270
        movingPlatform.rightLimit = 1530
        movingPlatform.changeX = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)

	#PLATAFORMA8 PISO5 (movil)
        movingPlatform = MovingPlatform((280,100),images["grassHalf"])
        movingPlatform.leftLimit = 280
        movingPlatform.rightLimit = 910
        movingPlatform.changeX = 3
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)

	#PLATAFORMA9 PISO5 
        platform = Platform((1050,100),images["grassHalfLeft"])
        self.platform_list.add(platform)
	platform = Platform((1120,100),images["grassHalfMid"])
        self.platform_list.add(platform)
        platform = Platform((1190,100),images["grassHalfRight"])
        self.platform_list.add(platform)

	#PLATAFORMA10 PISO6
	platform = Platform((70,30),images["grassCliff"])
        self.platform_list.add(platform)

	#PLATAFORMA11 PISO6
        platform = Platform((2310,30),images["grassCliffAlt"])
        self.platform_list.add(platform)

	#PLATAFORMA13 PISO8
	platform = Platform((490,-110),images["grassHalfLeft"])
        self.platform_list.add(platform)
	for i in range(560,840,70):
		platform = Block((i,-110),images["grassHalfMid"])
        	self.platform_list.add(platform)
	platform = Platform((840,-110),images["grassHalfRight"])
        self.platform_list.add(platform)
	
	#PLATAFORMA14 PISO10
	platform = Platform((980,-250),images["grassHalfLeft"])
        self.platform_list.add(platform)
        platform = Platform((1050,-250),images["grassHalfRight"])
        self.platform_list.add(platform)

	#PLATAFORMA15 PISO10
	platform = Platform((1190,-250),images["grassHalfLeft"])
        self.platform_list.add(platform)
	for i in range(1260,1470,70):
		platform = Block((i,-250),images["grassHalfMid"])
        	self.platform_list.add(platform)
	platform = Platform((1470,-250),images["grassHalfRight"])
        self.platform_list.add(platform)
	
	#PLATAFORMA16 PISO10 (movil)
        movingPlatform = MovingPlatform((1560,-250),images["grassHalf"])
        movingPlatform.leftLimit = 1560
        movingPlatform.rightLimit = 2230
        movingPlatform.changeX = 4
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
	
	#PLATAFORMA117 PISO12
	platform = Platform((280,-390),images["grassHalf"])
        self.platform_list.add(platform)

	#PLATAFORMA18 PISO12
	platform = Platform((420,-390),images["grassHalf"])
        self.platform_list.add(platform)

	#PLATAFORMA19 PISO12
	platform = Platform((560,-390),images["grassHalf"])
        self.platform_list.add(platform)
	
	#PLATAFORMA20 PISO12
        platform = Platform((700,-420),images["grassCliffAlt"])
        self.platform_list.add(platform)
	

	#PLATAFORMA8 PISO5 (movil)
        movingPlatform = MovingPlatform((1120,20),images["grassHalf"])
        movingPlatform.bottomLimit = 50
        movingPlatform.topLimit = -110
        movingPlatform.changeY = 2
        movingPlatform.level = self
        movingPlatform.player = player
        self.platform_list.add(movingPlatform)
        
	#PLATAFORMA21 PISO2 A PISO9
	for i in range(-110,450,70):
		platform = Block((1800,i),images["box2"])
        	self.platform_list.add(platform)

	#PLATAFORMA22 PISO2 A PISO4
	for i in range(240,450,70):
		platform = Block((2010,i),images["box2"])
        	self.platform_list.add(platform)

	#PLATAFORMA22 PISO2 A PISO3
	for i in range(310,450,70):
		platform = Block((2220,i),images["box2"])
        	self.platform_list.add(platform)

	

	#items de vida
	heart=Block((70,-30),images["heart"])
	self.items_list.add(heart)

        
	#ENEMIGO, NOTA:AGREGAR MAS
	
	   #imagenes para las animaciones
	imagen_rana=(images["rana"],images["rana"],images["rana"],images["rana1"],images["rana1"],images["rana1"],images["rana2"],
			images["rana2"],images["rana2"],images["rana3"],images["rana3"],images["rana3"],images["rana4"],
		     	images["rana4"],images["rana4"],images["rana5"],images["rana5"],images["rana5"],images["rana7"],
			images["rana7"],images["rana7"])
	imagen_azulito=(images["azulito"],images["azulito"],images["azulito"],images["azulito"],images["azulito1"],
			images["azulito1"],images["azulito1"],images["azulito2"],images["azulito2"],images["azulito2"],
			images["azulito2"],images["azulito2"])
	imagen_oscuro=(images["oscuro"],images["oscuro"],images["oscuro"],images["oscuro1"],images["oscuro1"],images["oscuro1"],
			images["oscuro2"],images["oscuro2"],images["oscuro2"],images["oscuro3"],images["oscuro3"],images["oscuro3"])
	
	rana=AnimatedBlock((565,380),images["rana"])
	rana.imagen=imagen_rana
	rana.leftLimit = 560
	rana.rightLimit = 910
        rana.changeX = -2
        rana.level = self
        rana.player = player
        rana.dead_image = images["ranaDead"]
        self.block_list.add(rana)

	azulito=AnimatedBlock((490,-110),images["azulito"])
	azulito.imagen=imagen_azulito
	azulito.leftLimit = 490
	azulito.rightLimit = 840
        azulito.changeX = -2
        azulito.level = self
        azulito.player = player
        azulito.dead_image = images["azulitoDead"]
        self.block_list.add(azulito)
	
	oscuro=AnimatedBlock((1190,-250),images["oscuro"])
	oscuro.imagen=imagen_oscuro
	oscuro.leftLimit = 1190
	oscuro.rightLimit = 1500
        oscuro.changeX = -2
        oscuro.level = self
        oscuro.player = player
        oscuro.dead_image = images["oscuroDead"]
        self.block_list.add(oscuro)
	
        
        fly = Fly((180,-300),images["fly1"],images["fly2"])
        self.block_list.add(fly)
#-----------------HASTA AQUI LOS ENEMIGOS!! -------------------------------------------------------------
        
	#monedas
        for i in range(565,910,50):
            hud = Block((i,350),images["hud_coin"])
            self.hud_list.add(hud)
	for i in range(490,840,50):
            hud = Block((i,-140),images["hud_coin"])
            self.hud_list.add(hud)
	for i in range(1190,1500,50):
            hud = Block((i,-290),images["hud_coin"])
            self.hud_list.add(hud)


        exit_sign = Block((2590,360),images["signExit"])
        self.items_list.add(exit_sign)
        
        spring = Spring((350,315),images["SpringDown"],player)
        self.block_list.add(spring)
        
           
        for i in range(630,910,70):
            water = AnimatedItem((i,430),images["liquidWaterTop_mid"],
                                pygame.transform.flip(images["liquidWaterTop_mid"],True,False))
            self.items_list.add(water)
        
#=======================================================================            
class Level_Two(Level_One):
    background_color = (222,222,130)
    music_filename = "game_files/Mushroom Theme_0.ogg"
    def __init__(self,imagesFiles,soundsFiles,player):
        Level.__init__(self,imagesFiles,soundsFiles,player)
        #========================
        global images
        images = imagesFiles
        #========================
       
        exit_sign = Block((2590,360),images["signExit"])
        self.items_list.add(exit_sign)
