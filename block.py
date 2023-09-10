import pygame
import constants as c

class Block(pygame.sprite.Sprite):
    def __init__(self, block_info, top_left_pixels):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.row = block_info[0]
        self.column = block_info[1]
        self.main_block = [self.row, self.column]
        self.color_id = block_info[2]
        
        # Load image for sprite surface and attatch a rectangle
        self.image = pygame.Surface([c.CELL_SIZE, c.CELL_SIZE])
        self.image = pygame.image.load(f"assets/sprites/block_{self.color_id}.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = top_left_pixels
        
    def drop_down(self):
        self.row += 1
        self.rect.bottom += c.CELL_SIZE
        