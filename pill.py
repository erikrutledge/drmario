import pygame
import constants as c
import scripting as s

class Pill(pygame.sprite.Sprite):
    def __init__(self, player):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        pill_color_values = s.get_pill_id()
        pill_color_code = str(pill_color_values[0]) + str(pill_color_values[1])
        self.main_block = [0, 3, pill_color_values[0]]
        self.second_block = [0, 4, pill_color_values[1]]
        
        # Load image for sprite surface and attatch a rectangle
        self.image = pygame.Surface([c.CELL_SIZE * 2, c.CELL_SIZE])
        self.image = pygame.image.load(f"assets/sprites/pill_{pill_color_code}.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = s.convert_coords_to_tl_pixels(self.main_block[0], self.main_block[1], player)
                
    def is_horizontal(self):
        """ 
        Returns a bool value to indicate the positioning of the player pill.
        """
        if self.main_block[0] - self.second_block[0] == 0:
            return True
        else:
            return False
    
    def move(self, direction):
        """
        Updates the grid values and sprite location of the player pill 
        according to the direction string input.
        """
        if direction == "left":
            self.main_block[1] -= 1
            self.second_block[1] -= 1
            self.rect.left -= c.CELL_SIZE
        elif direction == "right":
            self.main_block[1] += 1
            self.second_block[1] += 1
            self.rect.right += c.CELL_SIZE
        elif direction == "down":
            self.main_block[0] += 1
            self.second_block[0] += 1
            self.rect.bottom += c.CELL_SIZE
        else:
            raise Exception("Direction not recognized")
    
    def drop_down(self):
        self.main_block[0] += 1
        self.second_block[0] += 1
        self.rect.bottom += c.CELL_SIZE
        
    
    def rotate(self):
        """
        Defines the counter clockwise rotation logic.
        """
        if self.is_horizontal():
            # define rotated sprite location
            x_destination = self.rect.left
            y_destination = self.rect.top - c.CELL_SIZE
            # rotate and translate sprite
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect.topleft = (x_destination, y_destination)
            
            # update cell information
            self.second_block[0] -= 1
            self.second_block[1] -= 1
        else:
            # define rotated sprite location
            x_destination = self.rect.left
            y_destination = self.rect.top + c.CELL_SIZE
            # rotate and translate sprite
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect.topleft = (x_destination, y_destination)
            
            # update cell information
            self.second_block[0] += 1
            self.second_block[1] += 1
            arbiter = self.main_block[2]
            self.main_block[2] = self.second_block[2]
            self.second_block[2] = arbiter
