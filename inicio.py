#!/usr/bin/env python
import pygame
from juego import Game
#---------------------
# Screen dimensions:
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
#---------------------
def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
   
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #Set the title of the window:
    pygame.display.set_caption("EL VIAJE DE MARGERY")
    #Set the mouse invisible.
    pygame.mouse.set_visible(False)
    #Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    try:
        game = Game(screen) #Create Game Object;
    except pygame.error:
        done = True
    # -------- Main Program Loop -----------
    while not done:
        done = game.eventHandler()
        # Game logic
        game.run_logic()
        # --- Drawing code should go here
        game.displayFrame(screen)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # --- Limit to 30 frames per second
        clock.tick(40)
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == '__main__':
    main()
