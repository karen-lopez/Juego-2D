
 
import pygame
 
"""
Constantes globales
"""
 
# Colores
NEGRO = (0, 0, 0) 
BLANCO = (255, 255, 255) 
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
CELESTE = (153, 255, 204) 

#  Dimensiones de la pantalla
LARGO_PANTALLA  = 800
ALTO_PANTALLA = 600
 
class Protagonista(pygame.sprite.Sprite): 
    """ Esta clase representa la barra inferior que controla el protagonista. """
   
    # -- Atributos 
    # Establecemos el vector velocidad del protagonista
    cambio_x = 0
    cambio_y = 0
     
     # Lista de todos los sprites contra los que podemos botar
    nivel = None
     

    def __init__(self): 

         
        # Llama al constructor padre 
        pygame.sprite.Sprite.__init__(self) 
       
        largo = 40
        alto = 50
	triangulo=pygame.Surface([largo, alto])
        self.image = triangulo
        self.image.fill(ROJO)        
        # Establecemos una referencia hacia la imagen rectangular.
        self.rect = self.image.get_rect()
	
       
    def update(self): 

        # Gravedad
        self.calc_grav()
         
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
	#self.rect.y += (abs(self.cambio_x)/2)*-1
         
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado         
            # izquierdo del objeto que hemos tocado
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right
 
        # Desplazar arriba/abajo
        self.rect.y += self.cambio_y
         
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False) 
        for bloque in lista_impactos_bloques:
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom
            # Detenemos nuestro movimiento vertical
            self.cambio_y = 0
 
    def calc_grav(self):
        """ Calculamos el efecto de la gravedad.  """
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35
 
        #Observamos si nos encontramos sobre el suelo. 
        if self.rect.y >= ALTO_PANTALLA - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height
 
    def saltar(self):
		
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2        
	
	#comprueba si choca en la parte de abajo con el piso o un bloque
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA:
	    #salta si no hay ostaculos
            self.cambio_y = -10
             

    def ir_izquierda(self):
        """ Es llamado cuando el usuario pulsa la flecha izquierda  """
        self.cambio_x = -6
 
    def ir_derecha(self):
        """ Es llamado cuando el usuario pulsa la flecha derecha  """
        self.cambio_x = 6
 
    def stop(self):
        """ Es llamado cuando el usuario abandona el teclado """
        self.cambio_x = 0


                    
class Plataforma(pygame.sprite.Sprite):
    """ Plataforma sobre la que el usuario puede saltar """
 
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


 
class Nivel():
   
     
    def __init__(self, protagonista):
        """ Constructor.  Requerido para cuando las plataformas
            que se desplazan colisionan con el protagonista. """
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista
        self.desplazar_escenario = 0
     
    # Actualizamos todo en este nivel
    def update(self):
        """ Actualizamos todo en este nivel."""
        self.listade_plataformas.update()
        self.listade_enemigos.update()
     
    def draw(self, pantalla):
        """ Dibujamos todo en este nivel. """
        pantalla.fill(AZUL)
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos.draw(pantalla)
         
    def escenario_desplazar(self, desplazar_x):
        """ Para cuando el usuario se desplaza a la izquierda/derecha y necesitamos mover 
        todo: """
        self.desplazar_escenario += desplazar_x
         
        for plataforma in self.listade_plataformas:
            plataforma.rect.x += desplazar_x
             
        for enemigo in self.listade_enemigos:
            enemigo.rect.x += desplazar_x


     
# Creamos las plataformas para el nivel
class Nivel_01(Nivel):

 
    def __init__(self, protagonista):
        """ Creamos el nivel 1. """    

        Nivel.__init__(self, protagonista)
        self.limitedel_nivel = -1000
 
	#ANCHO, ALTO, x, y
        nivel = [ [150, 35, 140, 525],
                  [210, 35, 800, 400],
                  [210, 35, 1000, 500],
                  [210, 35, 1120, 280],
                  ]

	bordes = [ [120, 600, -120, 0],
		   [1800, 2, 0, 0],
		   [120, 600, 1800, 0],
		   ]

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
 



def main():
    """ Programa Principal """
    pygame.init() 
        

    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA] 
    pantalla = pygame.display.set_mode(dimensiones) 
       
    pygame.display.set_caption("NIVEL 1") 
     

    protagonista = Protagonista()
 
    # Creamos todos los niveles
    listade_niveles = []
    listade_niveles.append(Nivel_01(protagonista))

     
    # Establecemos el nivel actual
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]
     
    listade_sprites_activas = pygame.sprite.Group()
    protagonista.nivel = nivel_actual
     
    protagonista.rect.x = 0
    protagonista.rect.y = ALTO_PANTALLA - protagonista.rect.height
    listade_sprites_activas.add(protagonista)
         

    hecho = False
       

    reloj = pygame.time.Clock() 
       
    # -------- Bucle Principal del Programa  ----------- 
    while not hecho: 
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT: #Si el usuario hizo click en salir
                hecho = True # Marcamos como hecho y salimos de este bucle
     
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    protagonista.ir_izquierda()
                if evento.key == pygame.K_RIGHT:
                    protagonista.ir_derecha()
                if evento.key == pygame.K_UP:
                    protagonista.saltar()
                     
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and protagonista.cambio_x < 0: 
                    protagonista.stop()
                if evento.key == pygame.K_RIGHT and protagonista.cambio_x > 0:
                    protagonista.stop()
 
        # Actualizamos al protagonista. 
        listade_sprites_activas.update()
         
        # Actualizamos los objetos en el nivel
        nivel_actual.update()
         
        # Si el protagonista se aproxima al borde derecho, desplazamos el escenario a la izquierda(-x)
        if protagonista.rect.x >= 500:
            diff = protagonista.rect.x - 500
            protagonista.rect.x = 500
            nivel_actual.escenario_desplazar(-diff)
     
        # Si el protagonista se aproxima al borde izquierdo, desplazamos el escenario a la derecha(+x)
        if protagonista.rect.x <= 120 and protagonista.rect.x>0:
            diff = 120 - protagonista.rect.x
            protagonista.rect.x = 120
            nivel_actual.escenario_desplazar(diff)
  
       

        nivel_actual.draw(pantalla)
        listade_sprites_activas.draw(pantalla)
         

           
        # Limitamos a 60 fps
        reloj.tick(60) 
       
        # Avanzamos y actualizamos la pantalla que ya hemos dibujado 
        pygame.display.flip() 
           
    
    pygame.quit()
 
if __name__ == "__main__":
    main()
