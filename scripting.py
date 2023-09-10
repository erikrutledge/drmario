import random
import constants as c
from block import Block

def get_pill_id():
    """ 
    Returns a randomly selected pill id to represent the different 
    combinations of pill colors.  ex: [3,1] = blue & red pill.
    """
    pill_id = [random.randint(1,3), random.randint(1, 3)]
    return pill_id

def convert_tl_pixel_to_coords(width, height, player):
    """ 
    Converts x and y pixel values to their corresponding grid row and column.
    Row and column outputs are grid independent.
    """
    if player == 1:
        start_location = c.P1_GRID_START
    elif player == 2:
        start_location = c.P2_GRID_START
    else:
        raise Exception("Player value not recognized")
    column = width - (start_location[0] / c.CELL_SIZE)
    row = height - (start_location[1]/ c.CELL_SIZE)
    return column, row

def convert_coords_to_tl_pixels(row, column, player):
    """ 
    Converts row and column integers to their corresponding pixel values,
    the player input checks that the pieces are placed on the correct grid.
    """
    if player == 1:
        start_location = c.P1_GRID_START
    elif player == 2:
        start_location = c.P2_GRID_START
    else:
        raise Exception("Player value not recognized.")
    width =  (column * c.CELL_SIZE) + start_location[0]
    height = (row * c.CELL_SIZE) + start_location[1]
    return width, height

def check_if_blocked(grid, current_position):
    """ 
    Returns a list of bool values determining which direction is blocked
    order: left, right, down, up.
    """
    blocked = [False, False, False, False]
    if current_position[1] == 0:    # touching left wall?
        blocked[0] = True
    else:
        if grid.get_cell_value(current_position[0], current_position[1] - 1) != 0:    # check left
            blocked[0] = True
    if current_position[1] == 7:    # touching right wall?
        blocked[1] =  True
    else: 
        if grid.get_cell_value(current_position[0], current_position[1] + 1) != 0:    # check right
            blocked[1] = True
    if current_position[0] == 15:    # touching floor?
        blocked[2] = True
    else:
        if grid.get_cell_value(current_position[0] + 1, current_position[1]) != 0:    # check down
            blocked[2] = True
    if current_position[0] == 0:    # touching ceiling?
        blocked[3] = True
    else:
        if grid.get_cell_value(current_position[0] - 1, current_position[1]) != 0:
            blocked[3] = True
    return blocked

def can_drop(grid, current_position):
    """ 
    Returns a bool value determining if the object is blocked from dropping.
    """
    blocked = False
    if current_position[0] == 15:    # touching floor?
        blocked = True
    else:
        if grid.get_cell_value(current_position[0] + 1, current_position[1]) != 0:    # check down
            blocked = True
    return blocked

def handle_clears(grid, cell_list, virus_sprite_group, landed_sprite_group, block_sprite_group, player):
    """
    Takes a list of the cell coordinates as an input, updates grid values, 
    corrects virus list, and deletes corresponding sprite objects.
    """
    
    for cell in cell_list:
        if cell in grid.viruses:
            # if cell is a virus
            grid.viruses.remove(cell)
            sprite = find_virus_sprite(cell[0], cell[1], virus_sprite_group)
            sprite.kill()
            print("Virus detected and eliminated")
            grid.set_cell_value(cell[0], cell[1], 0)
            
        elif find_virus_sprite(cell[0], cell[1], block_sprite_group) != None:
            # if cell is a block:
            sprite = find_virus_sprite(cell[0], cell[1], block_sprite_group)
            sprite.kill()
            print("single block detected and eliminated")
            grid.set_cell_value(cell[0], cell[1], 0)

        else:
            # if cell is a pill
            sprite, side_to_remove = find_pill_sprite(cell[0], cell[1], landed_sprite_group) 
            if side_to_remove == 0:
                pass
            elif side_to_remove == 1:
                grid.set_cell_value(sprite.main_block[0], sprite.main_block[1], 0)
                sprite.kill()
                
                block_info = sprite.second_block
                top_left_pixels = convert_coords_to_tl_pixels(block_info[0], block_info[1], player)
                block = Block(block_info, top_left_pixels)
                block_sprite_group.add(block)
                print("main side of block detected and eliminated")
                
            elif side_to_remove == 2:
                grid.set_cell_value(sprite.second_block[0], sprite.second_block[1], 0)
                sprite.kill()
                
                block_info = sprite.main_block
                top_left_pixels = convert_coords_to_tl_pixels(block_info[0], block_info[1], player)
                block = Block(block_info, top_left_pixels)
                block_sprite_group.add(block)
                print("secondary side of block detected and eliminated")
                
            else:
                raise Exception("Error determining how to handle pill elimination.")
            c.CLEAR_SFX.play()

def find_virus_sprite(row, column, sprite_group):
    """
    Returns the virus sprite object given the row and column.
    """
    for sprite in sprite_group.sprites():
        if sprite.row == row and sprite.column == column:
            return sprite
    
    return None
    
def find_pill_sprite(row, column, sprite_group):
    """
    Returns the pill sprite object at the given row and column and which side of 
    the pill should be eliminated. 1 = remove main block, 2 = remove second block
    """
    side_to_remove = 0
    sprite = None
    for pill in sprite_group.sprites():
        if [pill.main_block[0], pill.main_block[1]] == [row, column]:
            side_to_remove = 1
            sprite = pill
        elif [pill.second_block[0], pill.second_block[1]] == [row, column]:
            side_to_remove = 2
            sprite = pill
        else:
            pass
        
    return sprite, side_to_remove

def check_for_drops(grid, landed_sprite_group, block_sprite_group):
    """ 
    Scans through each sprite in the landed and block sprite groups and returns
    a list of the blocks able to be dropped.
    """
    sprites_to_drop = []
    coords_to_drop = []
    for sprite in block_sprite_group:
        blocked = can_drop(grid, [sprite.row, sprite.column])
        if not blocked:
            sprites_to_drop.append(sprite)
            coords_to_drop.append([sprite.row, sprite.column])
    for sprite in landed_sprite_group:
        main_blocked = can_drop(grid, [sprite.main_block[0], sprite.main_block[1]])
        second_blocked = can_drop(grid, [sprite.second_block[0], sprite.second_block[1]])
        if not main_blocked and not second_blocked:
            sprites_to_drop.append(sprite)
            coords_to_drop.append([sprite.main_block[0], sprite.main_block[1]])
            coords_to_drop.append([sprite.second_block[0], sprite.second_block[1]])

    return sprites_to_drop, coords_to_drop

def drop_sprites(grid, sprite_list, coord_list):
    """
    Move each of the sprite images from the input list down until they land. Update grid
    values to match.
    """
    counter = 0
    for sprite in sprite_list:
        sprite.drop_down()
        
        color = grid.get_cell_value(coord_list[counter][0], coord_list[counter][1])
        grid.set_cell_value(coord_list[counter][0], coord_list[counter][1], 0)
        grid.set_cell_value(coord_list[counter][0] + 1, coord_list[counter][1], color)
        counter += 1
