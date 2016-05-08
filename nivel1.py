#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
 
# Colores
NEGRO = (0, 0, 0) 
BLANCO = (255, 255, 255) 
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
CELESTE = (153, 255, 204) 
PURPURA= (61, 6, 49)

LARGO_PANTALLA  = 800
ALTO_PANTALLA = 700
 
class Protagonista(pygame.sprite.Sprite): 
    """ Esta clase representa la barra inferior que controla el protagonista. """
    cambio_x = 0
    cambio_y = 0 
    
    Nivel = None     
 
    def __init__(self): 

        pygame.sprite.Sprite.__init__(self)         
        largo = 40
        alto = 50
        self.image = pygame.Surface([largo, alto])
        self.image.fill(ROJO)        
        self.rect = self.image.get_rect() 
       
    def update(self): 
        """ Desplazamos al protagonista.  """
        self.calc_grav()         
        self.rect.x += self.cambio_x
         

        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:

                self.rect.left = bloque.rect.right
 

        self.rect.y += self.cambio_y
         

        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False) 
        for bloque in lista_impactos_bloques:
 

            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom
 
            # Detenemos nuestro movimiento vertical
            self.cambio_y = 0
             
            if isinstance(bloque, PlataformaEnMovimiento):
                self.rect.x += bloque.cambio_x
 

    def calc_grav(self):
        """ Calculamos el efecto de la gravedad.  """
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35
 
        # Observamos si nos encontramos sobre el suelo. 
        if self.rect.y >= ALTO_PANTALLA - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height
 

    def jump(self):
        
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2
         
        
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA:
            self.cambio_y = -10
             
   
    def ir_izquierda(self):
        """ Es llamado cuando el usuario pulsa la flecha izquierda  """
        self.cambio_x = -6
 
    def ir_derecha(self):
        """ Es llamado cuando el usuario pulsa la flecha  derecha """
        self.cambio_x = 6
 
    def stop(self):
       
        self.cambio_x = 0
 

                   
class Plataforma(pygame.sprite.Sprite):
    """ Plataforma sobre la que el usuario puede saltar. """
    def __init__(self, largo, alto ):
       
        pygame.sprite.Sprite.__init__(self)
         
        self.image = pygame.Surface([largo, alto])
        self.image.fill(CELESTE)    
                 
        self.rect = self.image.get_rect()


class PlataformaColor(pygame.sprite.Sprite):
    """ Plataforma sobre la que el usuario puede saltar """
 
    def __init__(self, largo, alto, color):
      
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.Surface([largo, alto])
        self.image.fill(color)               
        self.rect = self.image.get_rect()

  
 
class PlataformaEnMovimiento(Plataforma): 
    cambio_x = 0
    cambio_y = 0
      
    limite_superior = 0
    limite_inferior = 0
    limite_izquierda = 0
    limite_derecha = 0
     
    protagonista = None
     
    Nivel = None
     
    def update(self):        
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
         
        # Comprobamos si hemos chocado contra el protagonista
        impacto = pygame.sprite.collide_rect(self, self.protagonista)
        if impacto:
            # Hemos impactado contra el protagonista. Lo empujamos a un lado
            # y asumimos que no impactará con ninguna otra cosa.
             
            if self.cambio_x < 0:
                self.protagonista.rect.right = self.rect.left
            else:
                # En caso contrario (desplazamiento a la izquierda), hacemos lo opuesto
                self.protagonista.rect.left = self.rect.right
 
        # Desplazar arriba/abajo
        self.rect.y += self.cambio_y
         
        # Comprobamos si hemos impactado con el protagonista
        impacto = pygame.sprite.collide_rect(self, self.protagonista)
        if impacto:
           # Hemos impactado contra el protagonista. Lo empujamos a un lado
           # y asumimos que no impactará con ninguna otra cosa.
             
           # Restablecemos nuestra posición basándonos en la parte superior/inferior
       # del objeto
            if self.cambio_y < 0:
                self.protagonista.rect.bottom = self.rect.top 
            else:
                self.protagonista.rect.top = self.rect.bottom
 
        # Comprobamos los límites y vemos si es necesario invertir el sentido
 
        if self.rect.bottom > self.limite_inferior or self.rect.top < self.limite_superior:
            self.cambio_y *= -1
             
        cur_pos = self.rect.x - self.nivel.desplazar_escenario
        if cur_pos < self.limite_izquierda or cur_pos > self.limite_derecha:
            self.cambio_x *= -1
 
class Nivel():
     
    def __init__(self, protagonista):
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista
         
        # Imagen de fondo
        self.imagende_fondo = None
         
        # Cuán lejos a la izquierda/derecha se ha desplazado el escenario
	self.desplazar_escenario = 0
	self.limitedel_nivel = -1000
     
    # update todo en este Nivel
    def update(self):
        """ update todo en este Nivel."""
        self.listade_plataformas.update()
        self.listade_enemigos.update()
     
    def draw(self, pantalla):
        """ draw todo en este Nivel. """
        pantalla.fill(PURPURA)
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos.draw(pantalla)
         
    def escenario_desplazar(self, desplazar_x):
        """ Cuando el usuario se mueve de izquierda/derecha y necesitamos que todo se desplace: """
         
        # Llevamos la cuenta de la cantidad de desplazamiento
        self.desplazar_escenario += desplazar_x
         
        # Iteramos a través de todas las listas de sprites y desplazamos
        for Plataforma in self.listade_plataformas:
            Plataforma.rect.x += desplazar_x
             
        for enemigo in self.listade_enemigos:
            enemigo.rect.x += desplazar_x
     
# Creamos las Plataformas para el Nivel
class Nivel_01(Nivel):
    """ Definición para el Nivel 1. """
 
    def __init__(self, protagonista):
        """ Crear Nivel 1. """
         
        # Llamada al constructor padre
        Nivel.__init__(self, protagonista)
 
        self.limitedel_nivel = -1500
         
        #ANCHO, ALTO, x, y
        nivel = [ [150, 35, 140, 625],
                  [150, 35, 0, 375],
                  [150, 35, 580, 625],
		  [150, 35, 1000, 375],
		  [250, 35, 1320, 500],
		  [300, 35, 630, 250],
                  ]

	bordes = [ [120, 700, -120, 0],
		   [2000, 2, 0, 0],
		   [220, 600, 1800, 100],
		   ]

         
        # Iteramos a través del array anterior y añadimos Plataformas
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(bloque)

	for plataformaColor in bordes:
            borde = PlataformaColor(plataformaColor[0], plataformaColor[1], NEGRO)
            borde.rect.x = plataformaColor[2]
            borde.rect.y = plataformaColor[3]
            borde.protagonista = self.protagonista
            self.listade_plataformas.add(borde)

         
        #Plataforma movil no.1
					#ancho, alto
	bloque = PlataformaEnMovimiento(150, 35) 
        bloque.rect.x = 360
        bloque.rect.y = 500
        bloque.limite_izquierda = 360
        bloque.limite_derecha = 700
        bloque.cambio_x = 1
        bloque.protagonista = self.protagonista
        bloque.nivel = self
        self.listade_plataformas.add(bloque)
                         
 
 
def main():
    """ Programa Principal """
    pygame.init() 
        
    # Establecemos el alto y largo de la pantalla 
    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA] 
    pantalla = pygame.display.set_mode(dimensiones) 
       
    pygame.display.set_caption("Plataformer y Plataformas en Movimiento") 
     
    # Creamos al protagonista
    protagonista = Protagonista()
 
    # Creamos todos los Niveles
    listade_niveles = []
    listade_niveles.append( Nivel_01(protagonista) )
     
    # Establecemos el Nivel actual
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]
     
    listade_sprites_activas = pygame.sprite.Group()
    protagonista.nivel = nivel_actual
     
    protagonista.rect.x = 340
    protagonista.rect.y = ALTO_PANTALLA - protagonista.rect.height
    listade_sprites_activas.add(protagonista)
         
    # Iteramos hasta que el usuario hace click sobre el botón de salir.
    hecho = False
       
    # Usado para gestionar cuán rápido se actualiza la pantalla.
    reloj = pygame.time.Clock() 
       
    # -------- Bucle Principal del Programa ----------- 
    while not hecho: 
        for evento in pygame.event.get(): # El usuario realizó alguna acción 
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en salir
                hecho = True # Marcamos como hecho y salimos de este bucle
     
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    protagonista.ir_izquierda()
                if evento.key == pygame.K_RIGHT:
                    protagonista.ir_derecha()
                if evento.key == pygame.K_UP:
                    protagonista.jump()
                     
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and protagonista.cambio_x < 0: 
                    protagonista.stop()
                if evento.key == pygame.K_RIGHT and protagonista.cambio_x > 0:
                    protagonista.stop()
 
        # Actualizamos al protagonista. 
        listade_sprites_activas.update()
         
        # Actualizamos los objetos en el Nivel
        nivel_actual.update()
         
        # Si el protagonista se aproxima al borde derecho, desplazamos el escenario a la izquierda(-x)
        if protagonista.rect.x >= 550:
            diff = protagonista.rect.x - 550
            protagonista.rect.x = 550
            nivel_actual.escenario_desplazar(-diff)
     
        # Si el protagonista se aproxima al borde izquierdo, desplazamos el escenario a la derecha(+x)
        if protagonista.rect.x <= 120:
            diff = 120 - protagonista.rect.x
            protagonista.rect.x = 120
            nivel_actual.escenario_desplazar(diff)
  
             
        nivel_actual.draw(pantalla)
        listade_sprites_activas.draw(pantalla)
           

        # Limitamos a 60 fps
        reloj.tick(60) 
       
        
        pygame.display.flip() 
           

    pygame.quit()
 
if __name__ == "__main__":
    main()
