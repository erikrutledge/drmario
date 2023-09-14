import random
import scripting as s
import constants as c
from .virus import Virus

class Grid(object):
    def __init__(self, start_x, start_y):

        self.cells = []
        self.viruses = []
        self.start_x = start_x
        self.start_y = start_y

        # Initialize empty grid
        self.cells = [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0]]
                
    def add_viruses(self, quantity, virus_sprite_group, player):
        """
        Adds the specified quantity of viruses to the grid with random locations and colors.
        """
        # Update the grid cell values for each virus
        while len(self.viruses) < quantity:
            random_row = random.randint(5, 15)
            random_column = random.randint(0,7)
            random_color = random.randint(1,3)

            cell = [random_row, random_column, random_color]
            
            # Check if the cell is occupied before adding it to the list
            if self.get_cell_value(cell[0], cell[1]) == 0:
                self.set_cell_value(random_row, random_column, random_color)
                self.viruses.append(cell)
                # Add the virus sprites to the screen
                width, height = s.convert_coords_to_tl_pixels(random_row, random_column, player)
                virus = Virus(random_row, random_column, height, width, random_color)
                virus_sprite_group.add(virus)

    def set_cell_value(self, row, column, new_cell_id):
        """
        Sets the value of the cell given row and column. New_cell_id represents desired
        value, Red = 1, Yellow = 2, Blue = 3.
        """
        self.cells[row][column] = new_cell_id

    def get_cell_value(self, row, column):
        """ 
        Returns the integer value of the cell located at the input row and column.
        """
        return self.cells[row][column]
    
    def check_horizontal_clears(self):
        """ 
        Scans through each row of the grid and returns a list of cell coordinates
        that need to be cleared
        """
        coords_to_clear = []
        adjacent_coords = []
        row_counter = 0
        
        for row in self.cells:
            column_counter = 0
            for color in row:
                # See row_clear_logic.png for flowchart logic
                if color == 0:
                    if len(adjacent_coords) >= 4:
                        coords_to_clear += adjacent_coords
                    adjacent_coords.clear()
                elif len(adjacent_coords) == 0:
                    adjacent_coords.append([row_counter, column_counter, color])
                elif color == adjacent_coords[0][2]:
                    if row_counter == adjacent_coords[0][0]:
                        adjacent_coords.append([row_counter, column_counter, color])
                elif len(adjacent_coords) >= 4:
                    coords_to_clear += adjacent_coords
                    adjacent_coords.clear()
                    adjacent_coords.append([row_counter, column_counter, color])
                else:
                    adjacent_coords.clear()
                    adjacent_coords.append([row_counter, column_counter, color])
                column_counter += 1
            row_counter += 1
            
        return coords_to_clear
            
    def check_vertical_clears(self):
        """ 
        Scans through each column of the grid and returns a list of cell coordinates
        that need to be cleared
        """
        coords_to_clear = []
        adjacent_coords = []
        
        for column in range(8):
            row_counter = 0
            for row in self.cells:
                if row[column] == 0:
                    if len(adjacent_coords) >= 4:
                        coords_to_clear += adjacent_coords
                    adjacent_coords.clear()
                elif len(adjacent_coords) == 0:
                    adjacent_coords.append([row_counter, column, row[column]])
                elif row[column] == adjacent_coords[0][2]:
                    if column == adjacent_coords[0][1]:
                        adjacent_coords.append([row_counter, column, row[column]])
                elif len(adjacent_coords) >= 4:
                    coords_to_clear += adjacent_coords
                    adjacent_coords.clear()
                    adjacent_coords.append([row_counter, column, row[column]])
                else:
                    adjacent_coords.clear()
                    adjacent_coords.append([row_counter, column, row[column]])
                row_counter += 1

        return coords_to_clear
    
    def clear_grid(self):
        row_counter = 0
        for row in self.cells:
            column_counter = 0
            for column in row:
                self.set_cell_value(row_counter, column_counter, 0)
                column_counter += 1
            row_counter += 1

    def reset_board(grid, sprite_group, virus_sprite_group, block_sprite_group, landed_sprite_group, player):
        sprite_group.empty()
        virus_sprite_group.empty()
        block_sprite_group.empty()
        landed_sprite_group.empty()
        grid.clear_grid()
        grid.viruses.clear()
        if player == 1:
            level = c.P1_LEVEL
        elif player == 2:
            level = c.P2_LEVEL
        grid.add_viruses(level, virus_sprite_group, player)

grid = Grid(100,100)
print(grid.cells)
grid.clear_grid()
print(grid.cells)