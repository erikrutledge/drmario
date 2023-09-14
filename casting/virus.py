import pygame
import constants as c

class Virus(pygame.sprite.Sprite):
    
    def __init__(self, row, column, height, width, color_id):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.color = color_id
        self.row = row
        self.column = column
        self.height = height
        self.width = width
        
        # Load image for sprite surface and attatch a rectangle
        self.image = pygame.Surface([c.CELL_SIZE, c.CELL_SIZE])
        self.image = pygame.image.load(f"assets/sprites/virus_{color_id}a.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (width, height)
