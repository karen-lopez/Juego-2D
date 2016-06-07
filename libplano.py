import pygame
import math
import sys

ANCHO=800
ALTO=700
ROJO=(255,0,0) #rojo
centro=(ANCHO/2,ALTO/2)

def leer(asj):
    val=raw_input(asj)
    return int(val)

def Plano(ancho,alto,pantalla):
    iniy=(ancho/2,0)
    finy=(ancho/2,alto)
    inix=(0,alto/2)
    finx=(ancho,alto/2)
    pygame.draw.line(pantalla, ROJO, inix,finx, 1) #linea horizontal del plano cartesiano
    pygame.draw.line(pantalla, ROJO, iniy, finy, 1) #linea vertical del plano cartesiano
    pygame.display.flip()

def origen(ancho,alto):
    return ancho/2,alto/2

def translacion(origen,punto): 
    x2=origen[0]+punto[0]
    y2=origen[1]-punto[1]
    return (x2,y2)

def sumarvectores(vec1,vec2):
    x=vec1[0]+vec2[0]
    y=vec1[1]+vec2[1]
    return (x,y)
    
def poligno(tamano): 	
	lista = []
	for i in range (int(tamano)):		
		x=leer("Digite x vector 1: ")
		y=leer("Digite y vector 1: ")
		p1=(x,y)
		p1=translacion(centro,p1)
		lista.append(p1)
		pygame.display.flip()
	return lista    
	
def rotacion(punto,teta):
    x=punto[0]
    y=punto[1]
    xr=(x*math.cos(math.radians(teta)))-(y*math.sin(math.radians(teta)))
    yr=(x*math.sin(math.radians(teta)))+(y*math.cos(math.radians(teta)))
    return (xr,yr)	
    
def poligono(pantalla,centro,radio,num):	
    teta=(2*math.pi)/num
    n=0
    xi=radio*math.cos(n*teta)
    yi=radio*math.sin(n*teta)
    pto=translacion(centro,(xi,yi))
    while(n<num):
		n=n+1
		xf=radio*math.cos(n*teta)
		yf=radio*math.sin(n*teta)
		pto2=translacion(centro,(xf,yf))
		pygame.draw.line(pantalla,ROJO,pto,pto2)
		pto=pto2
	
def Escalar(vec1,vec2):
    x=vec1[0]*vec2[0]
    y=vec1[1]*vec2[1]
    return (x,y)
    
def poligono2 (centro,radio,num):	
	teta=(2*math.pi)/num
	listade = []
	n=0         
	for i in range (int(num)):
		xi=radio*math.cos(n*teta)
		yi=radio*math.sin(n*teta)
		pto = translacion(centro,(xi,yi))
		pn = pto
		pj = (int(pn[0])+250,250-int(pn[1]))
		listade.append(pj)
		pygame.display.flip()		
	return listade	 	

def estrella(pantalla,centro,radio):
    num=5
    teta=(2*math.pi)/num
    n=0
    xi=radio*math.cos(n*teta)
    yi=radio*math.sin(n*teta)
    pto=traslacion(centro,(xi,yi))
    l=[]
    l.append(pto)
    while(n<num-1):
        n=n+1
        xf=radio*math.cos(n*teta)
        yf=radio*math.sin(n*teta)
        pto=traslacion(centro,(xf,yf))
        l.append(pto)
    pygame.draw.line(pantalla,AZUL,l[0],l[2])
    pygame.draw.line(pantalla,AZUL,l[0],l[3])
    pygame.draw.line(pantalla,AZUL,l[1],l[3])
    pygame.draw.line(pantalla,AZUL,l[1],l[4])
    pygame.draw.line(pantalla,AZUL,l[2],l[4])
    
def disertacionx(vec1,vec2):
    x=vec2[0]-vec1[0]   
    return (x)  
      
def disertaciony(vec1,vec2):
    y=vec2[1]-vec1[1]
    return (y)     

def pendiente(v1,v2):
    t=v1/v2
    return (t) 
