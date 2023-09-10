import pygame
from grid import Grid
from pill import Pill
from virus import Virus
import constants as c
import scripting as s

pygame.init()

# Initialize screen elements 
screen = pygame.display.set_mode(c.SCREEN_SIZE)
pygame.display.set_caption("Mockter Dario")
icon = pygame.image.load("assets/sprites/the_doctor.png")
pygame.display.set_icon(icon)
background = pygame.image.load("assets/sprites/game_board_blue.png")
c.CHILL_SFX.play(-1)

# Initialize sprite groups
p1_sprite_group = pygame.sprite.Group()
virus_sprite_group = pygame.sprite.Group()
block_sprite_group = pygame.sprite.Group()
landed_sprite_group = pygame.sprite.Group()

# Initialize game clock and timer based variables
clock = pygame.time.Clock()
next_step = 0
dt = 0
running = True

# Create grid objects for each player and add viruses
p1_grid = Grid(c.P1_GRID_START[0], c.P1_GRID_START[1])
p1_grid.set_virus_values(c.P1_LEVEL)

# Create a sprite for each virus and render them to the screen
for i in range(len(p1_grid.viruses)):
    row, column = p1_grid.viruses[i][0], p1_grid.viruses[i][1]
    width, height = s.convert_coords_to_tl_pixels(row, column, 1)
    virus = Virus(row, column, height, width, p1_grid.viruses[i][2])
    p1_grid.viruses[i].pop(2)
    virus_sprite_group.add(virus)
    
while running:
    # Create a pill if one isn't already in play
    if len(p1_sprite_group.sprites()) == 0:
        p1_pill = Pill()
        p1_sprite_group.add(p1_pill)
    
    # Track the pill positions to handle collisions
    p1_main_blocked = s.check_if_blocked(p1_grid, p1_pill.main_block)
    p1_secondary_blocked = s.check_if_blocked(p1_grid, p1_pill.second_block)
    # Check for clears
    p1_blocks_to_clear = p1_grid.check_horizontal_clears() + p1_grid.check_vertical_clears()
    if p1_blocks_to_clear:
        s.handle_clears(p1_grid, p1_blocks_to_clear, virus_sprite_group, landed_sprite_group, block_sprite_group, 1)

    # Set the step timer to delay piece movements
    current_time = pygame.time.get_ticks()
    if current_time > next_step:
        next_step += c.GAME_SPEED
        
        # Check for dropping pieces
        p1_dropping_sprites, p1_dropping_coords = s.check_for_drops(p1_grid, landed_sprite_group, block_sprite_group)
        if p1_dropping_sprites:
            s.drop_sprites(p1_grid, p1_dropping_sprites, p1_dropping_coords)
            c.BLOCK_DROP_SFX.play()
            
        else:
            if not p1_main_blocked[2] and not p1_secondary_blocked[2]:
                p1_pill.move("down")   # comment this line out to disable gravity
                c.MOVE_SFX.play()
                pass
            else:
                p1_grid.set_cell_value(p1_pill.main_block[0], p1_pill.main_block[1], p1_pill.main_block[2])
                p1_grid.set_cell_value(p1_pill.second_block[0], p1_pill.second_block[1], p1_pill.second_block[2])
                landed_sprite_group.add(p1_pill)
                p1_sprite_group.empty()
                c.BLOCK_PLACE_SFX.play()

    # poll for user events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not p1_dropping_sprites:
                # P1 controls
                if event.key == pygame.K_a:
                    if not p1_main_blocked[0] and not p1_secondary_blocked[0]:
                        p1_pill.move("left")
                        c.MOVE_SFX.play()
                elif event.key == pygame.K_d:
                    if not p1_main_blocked[1] and not p1_secondary_blocked[1]:
                        p1_pill.move("right")
                        c.MOVE_SFX.play()
                elif event.key == pygame.K_s:
                    if not p1_main_blocked[2] and not p1_secondary_blocked[2]:
                        p1_pill.move("down")
                        c.MOVE_SFX.play()
                elif event.key == pygame.K_w:
                    if not p1_pill.is_horizontal() and p1_pill.main_block[1] == 7 or p1_main_blocked[1]:
                        p1_pill.move("left")
                        p1_pill.rotate()
                        c.ROTATE_SFX.play()
                    if p1_pill.is_horizontal() and p1_main_blocked[3]:
                        pass
                    else:
                        p1_pill.rotate()
                        c.ROTATE_SFX.play()
            if event.key == pygame.K_SPACE:
                print(p1_grid.cells)
            if event.key == pygame.K_b:
                print(p1_blocks_to_clear)
            
            # Close window
            if event.type == pygame.QUIT:
                running = False
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Update screen sprites
    p1_sprite_group.update()
    screen.blit(background, (0,0))
    p1_sprite_group.draw(screen)
    landed_sprite_group.draw(screen)
    virus_sprite_group.draw(screen)
    block_sprite_group.draw(screen)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.display.quit()
pygame.quit()
