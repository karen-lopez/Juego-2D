#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Menu(object):
    state = 0
    def __init__(self,screen,items,bg_color=(0,0,0),font_color=(255,255,255),
                            select_color=(255,0,0),ttf_font=None,font_size=25,bg_image=None):
        self.screen = screen
        self.scr_width = self.screen.get_width()
        self.scr_height = self.screen.get_height()
        self.bg_color = bg_color
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        self.bg_image = bg_image
        
    def display_frame(self):
        if self.bg_image != None:
            self.screen.blit(self.bg_image,(0,0))
            
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,(12, 109, 141))
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (self.scr_width /3) - (width /2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (self.scr_height /2)  + (index * height)
            
            self.screen.blit(label,(posX,posY))
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1

