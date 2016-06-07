import pygame
from pygame.locals import *
import sys
from libplano import *
import os
import random

def circunferenciaPuntoMedio2(centro,r):
	l=[]
	l2=[]
	l3=[]
	l4=[]
	l5=[]
	l6=[]
	l7=[]
	l8=[]
	x=0
	y=r
	d=5/4-r
	punto=translacion(centro,(x,y))
	l.append(punto)
	punto=translacion(centro,(x,-y))
	l2.append(punto)
	punto=translacion(centro,(-x,y))
	l3.append(punto)
	punto=translacion(centro,(-x,-y))
	l4.append(punto)
	punto=translacion(centro,(y,x))
	l5.append(punto)
	punto=translacion(centro,(y,-x))
	l6.append(punto)
	punto=translacion(centro,(-y,x))
	l7.append(punto)
	punto=translacion(centro,(-y,-x))
	l8.append(punto)
	#simetria(pantalla,centro,(x,y))
	
	while y>x:
		if d<0:
			d=d+x*2+3
			x=x+1
		else:
			d=d+2*(x-y)+5
			x=x+1
			y=y-1
		#simetria(pantalla,centro,(x,y))
		punto=translacion(centro,(x,y))
		l.append(punto)
		punto=translacion(centro,(x,-y))
		l2.append(punto)
		punto=translacion(centro,(-x,y))
		l3.append(punto)
		punto=translacion(centro,(-x,-y))
		l4.append(punto)
		punto=translacion(centro,(y,x))
		l5.append(punto)
		punto=translacion(centro,(y,-x))
		l6.append(punto)
		punto=translacion(centro,(-y,x))
		l7.append(punto)
		punto=translacion(centro,(-y,-x))
		l8.append(punto)
	l5.reverse()
	l2.reverse()
	l8.reverse()
	l3.reverse()
	ltotal = l+l5+l6+l2+l4+l8+l7+l3
	return ltotal

def bresenhamrecta(pto1,pto2):

	l=[]
	dx=abs(pto2[0]-pto1[0])
	dy=abs(pto2[1]-pto1[1])
	x=pto1[0]
	y=pto1[1]
	hor=dy<dx
	if hor:		
		d=(2*dy)-dx
		dE=2*dy
		dNE=2*(dy-dx)
	else:
		d=(2*dx)-dy
		dE=2*dx
		dNE=2*(dx-dy)
	if (pto2[0]-pto1[0])>0:
		dirx=1
	else:
		dirx=-1
	if (pto2[1]-pto1[1])>0:
		diry=1
	else:
		diry=-1
	l.append((x,y))
	#pantalla.set_at((x,y),ROJO)

	if hor:
		while x!=pto2[0]:
			if d<=0:
				d=d+dE
			else:
				d=d+dNE
				y+=diry
			x+=dirx
			#pantalla.set_at((x,y),ROJO)
			l.append((x,y))
	else:
		while y!=pto2[1]:
			if d<=0:
				d=d+dE
			else:
				d=d+dNE
				x+=dirx
			y+=diry
			#pantalla.set_at((x,y),ROJO)
			l.append((x,y))
	#print (x,y)
	return l

def circunferenciaPuntoMedio(centro,r):
	l=[]
	x=0
	y=r
	d=5/4-r
	punto=translacion(centro,(x,y))
	l.append(punto)
	punto=translacion(centro,(x,-y))
	l.append(punto)
	punto=translacion(centro,(-x,y))
	l.append(punto)
	punto=translacion(centro,(-x,-y))
	l.append(punto)
	punto=translacion(centro,(y,x))
	l.append(punto)
	punto=translacion(centro,(y,-x))
	l.append(punto)
	punto=translacion(centro,(-y,x))
	l.append(punto)
	punto=translacion(centro,(-y,-x))
	l.append(punto)
	#simetria(pantalla,centro,(x,y))
	
	while y>x:
		if d<0:
			d=d+x*2+3
			x=x+1
		else:
			d=d+2*(x-y)+5
			x=x+1
			y=y-1
		#simetria(pantalla,centro,(x,y))
		punto=translacion(centro,(x,y))
		l.append(punto)
		punto=translacion(centro,(x,-y))
		l.append(punto)
		punto=translacion(centro,(-x,y))
		l.append(punto)
		punto=translacion(centro,(-x,-y))
		l.append(punto)
		punto=translacion(centro,(y,x))
		l.append(punto)
		punto=translacion(centro,(y,-x))
		l.append(punto)
		punto=translacion(centro,(-y,x))
		l.append(punto)
		punto=translacion(centro,(-y,-x))
		l.append(punto)
	return l