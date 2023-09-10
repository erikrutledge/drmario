    for cell in cell_list:
        if cell in grid.viruses:
            grid.viruses.remove(cell)
            sprite = find_virus_sprite(cell[0], cell[1], virus_sprite_group)
            sprite.kill()
            print("Virus detected and eliminated")
            grid.set_cell_value(cell[0], cell[1], 0)
            
        elif cell in grid.blocks:
            grid.blocks.remove(cell)
            sprite = find_virus_sprite(cell[0], cell[1], block_sprite_group)
            sprite.kill()
            print("single block detected and eliminated")
            grid.set_cell_value(cell[0], cell[1], 0)
            
        else:
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
                grid.blocks.append([block_info[0], block_info[1]])
                print("main side of block detected and eliminated")
                
            elif side_to_remove == 2:
                grid.set_cell_value(sprite.second_block[0], sprite.second_block[1], 0)
                sprite.kill()
                
                block_info = sprite.main_block
                top_left_pixels = convert_coords_to_tl_pixels(block_info[0], block_info[1], player)
                block = Block(block_info, top_left_pixels)
                block_sprite_group.add(block)
                grid.blocks.append([block_info[0], block_info[1]])
                print("secondary side of block detected and eliminated")
                
            else:
                raise Exception("Error determining how to handle pill elimination.")