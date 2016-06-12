#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

def loadImages():
    images = {}
    #-------------------------------------------------------------------
    images["background"] = pygame.image.load("imagenes/bosque2.jpg").convert()
    images["intro"] = pygame.image.load("imagenes/intro.jpg").convert()
    images["Margery_Run Right_0"] = pygame.image.load("imagenes/Margery_Run Right_0.png").convert_alpha()
    images["Margery_Run Right_1"] = pygame.image.load("imagenes/Margery_Run Right_1.png").convert_alpha()
    images["Margery_Run Right_2"] = pygame.image.load("imagenes/Margery_Run Right_2.png").convert_alpha()
    images["Margery_Run Right_3"] = pygame.image.load("imagenes/Margery_Run Right_3.png").convert_alpha()
    images["Margery_Run Left_0"] = pygame.image.load("imagenes/Margery_Run Left_0.png").convert_alpha()
    images["Margery_Run Left_1"] = pygame.image.load("imagenes/Margery_Run Left_1.png").convert_alpha()
    images["Margery_Run Left_2"] = pygame.image.load("imagenes/Margery_Run Left_2.png").convert_alpha()
    images["Margery_Run Left_3"] = pygame.image.load("imagenes/Margery_Run Left_3.png").convert_alpha()
    images["playerJumpIzquierda"] = pygame.image.load("imagenes/Margery_Jump Left_0.png").convert_alpha()
    images["playerJumpDerecha"] = pygame.image.load("imagenes/Margery_Jump Right_0.png").convert_alpha()
    images["grassCliff"] = pygame.image.load("imagenes/grassCliff.png").convert_alpha()
    images["grassCliffAlt"] = pygame.image.load("imagenes/grassCliffAlt.png").convert_alpha()
    images["grassLeft"] = pygame.image.load("imagenes/grassLeft.png").convert_alpha()
    images["grassMid"] = pygame.image.load("imagenes/grassMid.png").convert_alpha()
    images["grassRight"] = pygame.image.load("imagenes/grassRight.png").convert_alpha()
    images["heart"] = pygame.image.load("imagenes/heart.png").convert_alpha()
    
    images["liquidWater"] = pygame.image.load("imagenes/liquidWater.png").convert_alpha()
    images["liquidWaterTop_mid"] = pygame.image.load("imagenes/liquidWaterTop_mid.png").convert_alpha()
    
    images["grassHalfLeft"] = pygame.image.load("imagenes/grassHalfLeft.png").convert_alpha()
    images["grassHalfMid"] = pygame.image.load("imagenes/grassHalfMid.png").convert_alpha()
    images["grassHalfRight"] = pygame.image.load("imagenes/grassHalfRight.png").convert_alpha()
    
    images["grassHalf"] = pygame.image.load("imagenes/grassHalf.png").convert_alpha()
    
    #--CAJAS-----------------------------------------------------------------------------------------------------
    images["box2"] = pygame.image.load("imagenes/box2.png").convert_alpha()
    
    #---ENEMIGOS---------------------------------------------------------------
    images["rana"] = pygame.image.load("imagenes/rana7.png").convert_alpha()
    images["rana1"] = pygame.image.load("imagenes/rana6.png").convert_alpha()
    images["rana2"] = pygame.image.load("imagenes/rana5.png").convert_alpha()
    images["rana3"] = pygame.image.load("imagenes/rana4.png").convert_alpha()
    images["rana4"] = pygame.image.load("imagenes/rana3.png").convert_alpha()
    images["rana5"] = pygame.image.load("imagenes/rana2.png").convert_alpha()
    images["rana6"] = pygame.image.load("imagenes/rana1.png").convert_alpha()
    images["rana7"] = pygame.image.load("imagenes/rana0.png").convert_alpha()
    images["ranaDead"] = pygame.image.load("imagenes/rana5.png").convert_alpha()
    
    images["azulito"] = pygame.image.load("imagenes/azulito0.png").convert_alpha()
    images["azulito1"] = pygame.image.load("imagenes/azulito1.png").convert_alpha()
    images["azulito2"] = pygame.image.load("imagenes/azulito2.png").convert_alpha()
    images["azulitoDead"] = pygame.image.load("imagenes/azulitoDead.png").convert_alpha()

    images["oscuro"] = pygame.image.load("imagenes/oscuro.png").convert_alpha()
    images["oscuro1"] = pygame.image.load("imagenes/oscuro1.png").convert_alpha()
    images["oscuro2"] = pygame.image.load("imagenes/oscuro2.png").convert_alpha()
    images["oscuro3"] = pygame.image.load("imagenes/oscuro3.png").convert_alpha()
    images["oscuroDead"] = pygame.image.load("imagenes/oscuroDead.png").convert_alpha()
	
    images["fly1"] = pygame.image.load("imagenes/pajaro1.png").convert_alpha()
    images["fly2"] = pygame.image.load("imagenes/pajaro2.png").convert_alpha()
    images["flyDead"] = pygame.image.load("imagenes/pajaroDead.png").convert_alpha()
    
    
    images["hud_0"] = pygame.image.load("imagenes/hud_0.png").convert_alpha()
    images["hud_1"] = pygame.image.load("imagenes/hud_1.png").convert_alpha()
    images["hud_2"] = pygame.image.load("imagenes/hud_2.png").convert_alpha()
    images["hud_3"] = pygame.image.load("imagenes/hud_3.png").convert_alpha()
    images["hud_4"] = pygame.image.load("imagenes/hud_4.png").convert_alpha()
    images["hud_5"] = pygame.image.load("imagenes/hud_5.png").convert_alpha()
    images["hud_6"] = pygame.image.load("imagenes/hud_6.png").convert_alpha()
    images["hud_7"] = pygame.image.load("imagenes/hud_7.png").convert_alpha()
    images["hud_8"] = pygame.image.load("imagenes/hud_8.png").convert_alpha()
    images["hud_9"] = pygame.image.load("imagenes/hud_9.png").convert_alpha()
    
    images["hud_p3Alt"] = pygame.image.load("imagenes/hud_heartFull.png").convert_alpha()
    images["hud_x"] = pygame.image.load("imagenes/hud_x.png").convert_alpha()
	#moneda
    images["hud_coin"] = pygame.image.load("imagenes/moneda1.png").convert_alpha()
  
    images["SpringDown"] = pygame.image.load("imagenes/springboardDown.png").convert_alpha()
    images["SpringUp"] = pygame.image.load("imagenes/springboardUp.png").convert_alpha()
    
    images["signExit"] = pygame.image.load("imagenes/signExit.png").convert_alpha()
    
    return images
    
def loadSounds():
    sounds = {}
    #-------------------------------------------------------------------
    sounds["coin"] = pygame.mixer.Sound("sounds/coin_sound.ogg")
    sounds["box"] = pygame.mixer.Sound("sounds/complete.ogg")
    sounds["spring"] = pygame.mixer.Sound("sounds/spring.ogg")
    sounds["weight"] = pygame.mixer.Sound("sounds/weight_sound.ogg")
    sounds["slime"] = pygame.mixer.Sound("sounds/fail.ogg")
    sounds["jump"] = pygame.mixer.Sound("sounds/Jump17.ogg")
    sounds["waterSplash"] = pygame.mixer.Sound("sounds/watersplash.ogg")
    sounds["button"] = pygame.mixer.Sound("sounds/button.ogg")
    #-------------------------------------------------------------------
    return sounds
