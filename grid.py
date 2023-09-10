import random

class Grid(object):
    def __init__(self, start_x, start_y):

        self.cells = []
        self.viruses = []
        self.start_x = start_x
        self.start_y = start_y
        # self.cell_size = cell_size
        # self.columns = columns
        # self.rows = rows

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

    def set_virus_values(self, quantity):
        """
        Adds the specified quantity of viruses to the grid with random locations and colors.
        """
        while len(self.viruses) < quantity:
            random_row = random.randint(5, 15)
            random_column = random.randint(0,7)
            random_color = random.randint(1,3)

            cell = [random_row, random_column, random_color]
            
            # Check if the cell is occupied before adding it to the list
            if self.get_cell_value(cell[0], cell[1]) == 0:
                self.set_cell_value(random_row, random_column, random_color)
                self.viruses.append(cell)

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
        adjacent_colors = []
        row_counter = 0
        
        for row in self.cells:
            column_counter = 0
            for column in row:
                if len(adjacent_colors) == 0 and column != 0:
                    adjacent_colors.append(column)
                    adjacent_coords.append([row_counter, column_counter])
                    column_counter += 1
                elif column != 0 and column == adjacent_colors[0]:
                    adjacent_colors.append(column)
                    adjacent_coords.append([row_counter, column_counter])
                    column_counter += 1
                elif len(adjacent_colors) >= 4:
                    pass
                else:
                    adjacent_colors.clear()
                    adjacent_coords.clear()
                    adjacent_colors.append(column)
                    adjacent_coords.append([row_counter, column_counter])
                    column_counter += 1
                
            if len(adjacent_colors) >= 4:
                coords_to_clear += adjacent_coords
                adjacent_colors.clear()
                adjacent_coords.clear()
            row_counter += 1
            
        return coords_to_clear
            
    def check_vertical_clears(self):
        """ 
        Scans through each column of the grid and returns a list of cell coordinates
        that need to be cleared
        """
        coords_to_clear = []
        adjacent_coords = []
        adjacent_colors = []
        
        for column in range(8):
            row_counter = 0
            for row in self.cells:
                if len(adjacent_colors) == 0 and row[column] != 0:
                    adjacent_colors.append(row[0])
                    adjacent_coords.append([row_counter, column])
                    row_counter += 1
                elif row[column] != 0 and adjacent_colors[0] == row[column]:
                    adjacent_colors.append(row[column])
                    adjacent_coords.append([row_counter, column])
                    row_counter += 1
                elif len(adjacent_colors) >= 4:
                    pass
                else:
                    adjacent_colors.clear()
                    adjacent_coords.clear()
                    adjacent_colors.append(row[column])
                    adjacent_coords.append([row_counter, column])
                    row_counter += 1
                
            if len(adjacent_colors) >= 4:
                coords_to_clear += adjacent_coords
                adjacent_colors.clear()
                adjacent_coords.clear()

        return coords_to_clear
