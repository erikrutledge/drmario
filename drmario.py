import pygame
import constants as c
from views import Views

def __main__():
    
    # Initialize pygame and the game window
    pygame.init()
    screen = pygame.display.set_mode(c.SCREEN_SIZE)
    pygame.display.set_caption("Mockter Dario")
    icon = pygame.image.load("assets/sprites/the_doctor.png")
    pygame.display.set_icon(icon)
    
    Views.title_screen(screen)

if __name__ == '__main__':
    __main__()
