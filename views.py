import pygame
import constants as c
import scripting as s
from casting.grid import Grid
from casting.pill import Pill

# pygame.init()
# screen = pygame.display.set_mode((c.SCREEN_SIZE))
# Views.title_screen(screen)
# Views.p1_options_screen(screen)
# Views.p2_options_screen(screen)

class Views():
    
    def title_screen(screen):
        clock = pygame.time.Clock()
        background = pygame.image.load("assets/screens/title_screen.png")
        c.MENU_SFX.play(-1)

        indicator = pygame.image.load("assets/sprites/title_screen_selector.png")
        
        p1_selector = pygame.draw.rect(screen, (0,0,0), (275, 660, 490, 60))
        p2_selector = pygame.draw.rect(screen, (0,0,0), (275, 720, 490, 60))
        
        p1_handled = False
        p2_handled = False
        running = True
        
        while running:
            screen.blit(background, (0, 0))
            
            # Close the window on ESCAPE or x-ing out
            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Follow mouse position and mouse_1 clicks
            mouse_pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()[0]
            
            if p1_selector.collidepoint(mouse_pos):
                screen.blit(indicator, (275, 672))
                if not p1_handled:
                    c.HOVER_SFX.play()
                    print("hovering p1")
                    p1_handled = True
                if pressed:
                    print("1 Player game selected")
                    screen.fill((255,255,255))
                    pygame.mixer.stop()
                    Views.p1_options_screen(screen)
            else:
                p1_handled = False
                
            if p2_selector.collidepoint(mouse_pos):
                screen.blit(indicator, (275, 732))
                if not p2_handled:
                    c.HOVER_SFX.play()
                    print("hovering p2")
                    p2_handled = True
                if pressed:
                    print("2 Player game selected")
                    screen.fill((255,255,255))
                    pygame.mixer.stop()
                    Views.p2_options_screen(screen)
            else:
                p2_handled = False

            pygame.display.flip()
            clock.tick(60) / 1000
            
    def p1_options_screen(screen):
        clock = pygame.time.Clock()
        background = pygame.image.load("assets/screens/p1_menu.png")
        c.MENU_SFX.play(-1)
        
        # Create a sliding bar to select virus level
        level_rects = []
        pos = [320, 320, 20, 70]
        for level in range(0,20):
            rect = pygame.draw.rect(screen, (0,0,0), (pos[0], pos[1], pos[2], pos[3]))  # left, top, width, height
            level_rects.append(rect)
            pos[0] += 20
        print(len(level_rects))
        
        font = pygame.font.Font("assets/fonts/8bit_nintendo.ttf", 32)
        level_number = '1'
        level_indicator = pygame.image.load("assets/sprites/level_selector_p1.png")
        level_indicator_pos =  (315, 305)
        running = True

        # Create buttons to select speed
        low_rect = pygame.draw.rect(screen, (0,0,0), (315,530,150,75))
        med_rect = pygame.draw.rect(screen, (0,0,0), (465,530,190,75))
        hi_rect = pygame.draw.rect(screen, (0,0,0), (660,530,150,75))
        
        speed_indicator = pygame.image.load("assets/sprites/speed_selector_p1.png")
        speed_indicator_pos = (336, 510)
        
        # Create buttons to select music
        fever_rect = pygame.draw.rect(screen, (0,0,0), (180,730,250,70))
        chill_rect = pygame.draw.rect(screen, (0,0,0), (430,730,270,70))
        off_rect = pygame.draw.rect(screen, (0,0,0), (700,730,180,70))
        
        music_indicator = pygame.image.load("assets/sprites/speed_selector_p1.png")
        music_indicator_pos = (257, 705)
        
        while running:
            screen.blit(background, (0, 0))
            screen.blit(font.render(level_number, True, (255,255,255), (0,0,0)), (775, 290))
            screen.blit(level_indicator, level_indicator_pos)
            screen.blit(speed_indicator, speed_indicator_pos)
            screen.blit(music_indicator, music_indicator_pos)
            
            # Close the window on ESCAPE or x-ing out
            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        print("READY TO PLAY")
                        screen.fill((255,255,255))
                        pygame.mixer.stop()
                        Views.p1_game_screen(screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    c.HOVER_SFX.play()

            # Follow mouse position and handle clicks
            mouse_pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()[0]
            
            for rect in level_rects:
                if rect.collidepoint(mouse_pos) and pressed:
                    level_number = str(level_rects.index(rect) + 1)
                    level_indicator_pos = (rect.left, rect.centery - 50)
                    c.LEVEL = int(level_number)
                    
            if low_rect.collidepoint(mouse_pos) and pressed:
                speed_indicator_pos = (336, 510)
                c.SPEED = c.SPEEDS["MED"]
                print("low speed detected")
            if med_rect.collidepoint(mouse_pos) and pressed:
                speed_indicator_pos = (506, 510)
                c.SPEED = c.SPEEDS["MED"]
                print("med speed detected")
            if hi_rect.collidepoint(mouse_pos) and pressed:
                speed_indicator_pos = (681, 510)
                c.SPEED = c.SPEEDS["HI"]
                print("hi speed detected")
                
            if fever_rect.collidepoint(mouse_pos) and pressed:
                music_indicator_pos = (257, 705)
                c.MUSIC = c.FEVER_SFX
                print("fever music detected")
            if chill_rect.collidepoint(mouse_pos) and pressed:
                music_indicator_pos = (500, 705)
                c.MUSIC = c.CHILL_SFX
                print("chill music detected")
            if off_rect.collidepoint(mouse_pos) and pressed:
                music_indicator_pos = (745, 705)
                c.MUSIC = None
                print("music off")
                
            pygame.display.flip()
            clock.tick(60) / 1000
        

    def p2_options_screen(screen):
        clock = pygame.time.Clock()
        background = pygame.image.load("assets/screens/p2_menu.png")
        c.MENU_SFX.play(-1)
        
        # Create two sliding bars to select virus level
        p1_level_rects = []
        p2_level_rects = []
        pos = [320, 290, 20, 65]
        for level in range(0,20):
            p1_rect = pygame.draw.rect(screen, (0,0,0), (pos[0], pos[1], pos[2], pos[3]))  # left, top, width, height
            p1_level_rects.append(p1_rect)
            p2_rect = pygame.draw.rect(screen, (0,0,0), (pos[0], pos[1] + 65, pos[2], pos[3]))  # left, top, width, height
            p2_level_rects.append(p2_rect)
            pos[0] += 20
        
        # Create text rectangles to show virus level
        font = pygame.font.Font("assets/fonts/8bit_nintendo.ttf", 32)
        p1_level_number = '1'
        p1_level_indicator = pygame.image.load("assets/sprites/level_selector_p1.png")
        p1_level_indicator_pos =  (315, 300)
        
        p2_level_number = '1'
        p2_level_indicator = pygame.image.load("assets/sprites/level_selector_p2.png")
        p2_level_indicator_pos =  (315, 380)
    
        # Create buttons to select speed
        p1_low_rect = pygame.draw.rect(screen, (0,0,0), (315,510,150,55))
        p1_med_rect = pygame.draw.rect(screen, (0,0,0), (465,510,190,55))
        p1_hi_rect = pygame.draw.rect(screen, (0,0,0), (660,510,150,55))
        
        p1_speed_indicator = pygame.image.load("assets/sprites/speed_selector_p1.png")
        p1_speed_indicator_pos = (336, 510)
        
        p2_low_rect = pygame.draw.rect(screen, (0,0,0), (315,565,150,55))
        p2_med_rect = pygame.draw.rect(screen, (0,0,0), (465,565,190,55))
        p2_hi_rect = pygame.draw.rect(screen, (0,0,0), (660,565,150,55))
        
        p2_speed_indicator = pygame.image.load("assets/sprites/speed_selector_p2.png")
        p2_speed_indicator_pos = (336, 600)
        
        # Create buttons to select music
        fever_rect = pygame.draw.rect(screen, (0,0,0), (180,730,250,70))
        chill_rect = pygame.draw.rect(screen, (0,0,0), (430,730,270,70))
        off_rect = pygame.draw.rect(screen, (0,0,0), (700,730,180,70))
        
        music_indicator = pygame.image.load("assets/sprites/speed_selector_p1.png")
        music_indicator_pos = (257, 705)
        
        running = True
        while running:
            screen.blit(background, (0, 0))
            screen.blit(font.render(p1_level_number, True, (255,255,255), (0,0,0)), (775, 285))
            screen.blit(p1_level_indicator, p1_level_indicator_pos)
            screen.blit(p1_speed_indicator, p1_speed_indicator_pos)
            screen.blit(font.render(p2_level_number, True, (255,255,255), (0,0,0)), (775, 385))
            screen.blit(p2_level_indicator, p2_level_indicator_pos)
            screen.blit(p2_speed_indicator, p2_speed_indicator_pos)
            screen.blit(music_indicator, music_indicator_pos)
            
            # Close the window on ESCAPE or x-ing out
            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        print("READY TO PLAY")
                        screen.fill((255,255,255))
                        pygame.mixer.stop()
                        Views.p2_game_screen(screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    c.HOVER_SFX.play()
    
            # Follow mouse position and handle clicks
            mouse_pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()[0]
            
            for rect in p1_level_rects:
                if rect.collidepoint(mouse_pos) and pressed:
                    p1_level_number = str(p1_level_rects.index(rect) + 1)
                    p1_level_indicator_pos = (rect.left, rect.centery - 25)
                    c.P1_LEVEL = int(p1_level_number)
            
            for rect in p2_level_rects:
                if rect.collidepoint(mouse_pos) and pressed:
                    p2_level_number = str(p2_level_rects.index(rect) + 1)
                    p2_level_indicator_pos = (rect.left, rect.centery + 5)
                    c.P2_LEVEL = int(p2_level_number)
                    
            if p1_low_rect.collidepoint(mouse_pos) and pressed:
                p1_speed_indicator_pos = (336, 510)
                c.P1_SPEED = c.SPEEDS["LOW"]
                print("low speed detected")
            if p1_med_rect.collidepoint(mouse_pos) and pressed:
                p1_speed_indicator_pos = (506, 510)
                c.P1_SPEED = c.SPEEDS["MED"]
                print("med speed detected")
            if p1_hi_rect.collidepoint(mouse_pos) and pressed:
                p1_speed_indicator_pos = (681, 510)
                c.P1_SPEED = c.SPEEDS["HI"]
                print("hi speed detected")
            
            if p2_low_rect.collidepoint(mouse_pos) and pressed:
                p2_speed_indicator_pos = (336, 600)
                c.P2_SPEED = c.SPEEDS["LOW"]
                print("low speed detected")
            if p2_med_rect.collidepoint(mouse_pos) and pressed:
                p2_speed_indicator_pos = (506, 600)
                c.P2_SPEED = c.SPEEDS["MED"]
                print("med speed detected")
            if p2_hi_rect.collidepoint(mouse_pos) and pressed:
                p2_speed_indicator_pos = (681, 600)
                c.P2_SPEED = c.SPEEDS["HI"]
                print("hi speed detected")
                
            if fever_rect.collidepoint(mouse_pos) and pressed:
                music_indicator_pos = (257, 705)
                c.MUSIC = c.FEVER_SFX
                print("fever music detected")
            if chill_rect.collidepoint(mouse_pos) and pressed:
                music_indicator_pos = (500, 705)
                c.MUSIC = c.CHILL_SFX
                print("chill music detected")
            if off_rect.collidepoint(mouse_pos) and pressed:
                music_indicator_pos = (745, 705)
                c.MUSIC = None
                print("music off")
                
            pygame.display.flip()
            clock.tick(60) / 1000
            
    def p1_game_screen(screen):
        clock = pygame.time.Clock()
        font = pygame.font.Font("assets/fonts/8bit_nintendo.ttf", 32)
        background = pygame.image.load("assets/screens/p1_game_board.png")
        
        if c.MUSIC:
            c.MUSIC.play()
        # Initialize sprite groups
        sprite_group = pygame.sprite.Group()
        virus_sprite_group = pygame.sprite.Group()
        block_sprite_group = pygame.sprite.Group()
        landed_sprite_group = pygame.sprite.Group()
        
        # Create grid object and add viruses
        grid = Grid(c.GRID_START[0], c.GRID_START[1])
        grid.add_viruses(c.LEVEL, virus_sprite_group, 0)
        
        # Initialize the speed display variable
        speed_display = list(c.SPEEDS.keys())[list(c.SPEEDS.values()).index(c.SPEED)]
        
        # Set the step timer to delay piece movements
        STEP = pygame.USEREVENT + 1
        pygame.time.set_timer(STEP, c.SPEED)
        
        # pill = Pill(0)
        # sprite_group.add(pill)
        
        running = True
        while running:
            # Detect if the new pill is blocked at the top
            if grid.get_cell_value(0, 3) != 0:
                print("GAME OVER")
                screen.blit(pygame.image.load("assets/sprites/game_over.png"), (0,0))
                pygame.time.wait(3000)
                running = False
            # Detect if all the viruses are eliminated
            if not grid.viruses:
                print("YOU WIN")
                pygame.time.wait(3000)
                running = False
            
            # Create a pill if one isn't already in play
            if len(sprite_group.sprites()) == 0:
                pill = Pill(0)
                sprite_group.add(pill)
            
            # Track the pill positions to handle collisions
            main_blocked = s.check_if_blocked(grid, pill.main_block)
            secondary_blocked = s.check_if_blocked(grid, pill.second_block)
            dropping_sprites, dropping_coords = s.check_for_drops(grid, landed_sprite_group, block_sprite_group)
            blocks_to_clear = grid.check_horizontal_clears() + grid.check_vertical_clears()
            # poll for user events
            for event in pygame.event.get():
                if event.type == STEP:
                    # Check for clears
                    if blocks_to_clear:
                        s.handle_clears(grid, blocks_to_clear, virus_sprite_group, landed_sprite_group, block_sprite_group, 0)
                    # Check for dropping pieces
                    elif dropping_sprites:
                        s.drop_sprites(grid, dropping_sprites, dropping_coords)
                        c.BLOCK_DROP_SFX.play() 
                    elif main_blocked[2] or secondary_blocked[2]:
                        grid.set_cell_value(pill.main_block[0], pill.main_block[1], pill.main_block[2])
                        grid.set_cell_value(pill.second_block[0], pill.second_block[1], pill.second_block[2])
                        landed_sprite_group.add(pill)
                        sprite_group.empty()
                        c.BLOCK_PLACE_SFX.play()
                    else:
                        pill.move("down")   # comment this line to disable gravity
                        c.MOVE_SFX.play()
                            
                if event.type == pygame.KEYDOWN:
                    # Close window
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        pygame.display.quit()
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        print(grid.cells)
                        #### PAUSE GAME
                    if not dropping_sprites:
                        # Controls
                        if event.key == pygame.K_a:
                            if not main_blocked[0] and not secondary_blocked[0]:
                                pill.move("left")
                                c.MOVE_SFX.play()
                        elif event.key == pygame.K_d:
                            if not main_blocked[1] and not secondary_blocked[1]:
                                pill.move("right")
                                c.MOVE_SFX.play()
                        elif event.key == pygame.K_s:
                            if not main_blocked[2] and not secondary_blocked[2]:
                                pill.move("down")
                                c.MOVE_SFX.play()
                        elif event.key == pygame.K_w:
                            if not pill.is_horizontal() and pill.main_block[1] == 7 or main_blocked[1]:
                                pill.move("left")
                                pill.rotate()
                                c.ROTATE_SFX.play() 
                            elif pill.is_horizontal() and main_blocked[3]:
                                pass
                            else:
                                pill.rotate()
                                c.ROTATE_SFX.play() 
            # Update screen sprites
            sprite_group.update()
            screen.blit(background, (0,0))
            screen.blit(font.render(str(c.LEVEL), True, (0,0,0), (210,211,255)), c.LEVEL_DISPLAY)
            screen.blit(font.render(speed_display, True, (0,0,0), (210,211,255)), c.SPEED_DISPLAY)
            screen.blit(font.render(str(len(grid.viruses)), True, (0,0,0), (210,211,255)), c.VIRUS_DISPLAY)
            sprite_group.draw(screen)
            landed_sprite_group.draw(screen)
            virus_sprite_group.draw(screen)
            block_sprite_group.draw(screen)
            
            pygame.display.flip()
            clock.tick(60) / 1000
            
        # Clear the screen and stop music when exiting this view
        screen.fill((255,255,255))
        pygame.mixer.stop()
        
    def p2_game_screen(screen):
        clock = pygame.time.Clock()
        background = pygame.image.load("assets/screens/p2_game_board.png")
        if c.MUSIC:
            c.MUSIC.play()
        
        p1_wins = []
        p2_wins = []
        crown_list = []
        
        # Initialize sprite groups
        p1_sprite_group = pygame.sprite.Group()
        p1_virus_sprite_group = pygame.sprite.Group()
        p1_block_sprite_group = pygame.sprite.Group()
        p1_landed_sprite_group = pygame.sprite.Group()
        
        p2_sprite_group = pygame.sprite.Group()
        p2_virus_sprite_group = pygame.sprite.Group()
        p2_block_sprite_group = pygame.sprite.Group()
        p2_landed_sprite_group = pygame.sprite.Group()
        
        # Create grid objects for each player and add viruses
        p1_grid = Grid(c.P1_GRID_START[0], c.P1_GRID_START[1])
        p1_grid.add_viruses(c.P1_LEVEL, p1_virus_sprite_group, 1)
        
        p2_grid = Grid(c.P2_GRID_START[0], c.P2_GRID_START[1])
        p2_grid.add_viruses(c.P2_LEVEL, p2_virus_sprite_group, 2)

        # Set the step timer to delay piece movements
        P1_STEP = pygame.USEREVENT + 1
        P2_STEP = pygame.USEREVENT + 2
        pygame.time.set_timer(P1_STEP, c.P1_SPEED)
        pygame.time.set_timer(P2_STEP, c.P2_SPEED)
        running = True
        
        while running:   
            # Create a pill is there isn't one in play
            if len(p1_sprite_group.sprites()) == 0:
                p1_pill = Pill(1)
                p1_sprite_group.add(p1_pill)
            if len(p2_sprite_group.sprites()) == 0:
                p2_pill = Pill(2)
                p2_sprite_group.add(p2_pill)
                
            # Detect if the game is over
            if len(p1_wins) == 3:
                print("P1 WINS")
                gameover = pygame.image.load("assets/sprites/game_over.png")
                screen.blit(gameover, (0,0))                    
                pygame.time.wait(3000)
                running = False
            elif len(p2_wins) == 3:
                print("P2 WINS")
                gameover = pygame.image.load("assets/sprites/game_over.png")
                screen.blit(gameover, (0,0))                    
                pygame.time.wait(3000)
                running = False
                
            # Detect if the new pill is blocked at the top
            if p1_grid.get_cell_value(0, 3) != 0 or p1_grid.get_cell_value(0,4) != 0:
                print("P2 won that round")
                p2_wins.append('win')
                s.add_crowns(p2_wins, crown_list, 2)
                pygame.time.wait(3000)
                p1_grid.reset_board(p1_sprite_group, p1_virus_sprite_group,
                              p1_block_sprite_group, p1_landed_sprite_group, 1)
                p2_grid.reset_board(p2_sprite_group, p2_virus_sprite_group,
                              p2_block_sprite_group, p2_landed_sprite_group, 2)
            elif p2_grid.get_cell_value(0, 3) != 0 or p2_grid.get_cell_value(0,4) != 0:
                print("P1 won that round")
                p1_wins.append('win')
                s.add_crowns(p1_wins, crown_list, 1)
                pygame.time.wait(3000)
                p1_grid.reset_board(p1_sprite_group, p1_virus_sprite_group,
                              p1_block_sprite_group, p1_landed_sprite_group, 1)
                p2_grid.reset_board(p2_sprite_group, p2_virus_sprite_group,
                              p2_block_sprite_group, p2_landed_sprite_group, 2)
            # Check if all viruses are eliminated
            elif len(p1_grid.viruses) == 0:
                print("P1 won that round")
                p1_wins.append('win')
                s.add_crowns(p1_wins, crown_list, 1)
                pygame.time.wait(3000)
                p1_grid.reset_board(p1_sprite_group, p1_virus_sprite_group,
                              p1_block_sprite_group, p1_landed_sprite_group, 1)
                p2_grid.reset_board(p2_sprite_group, p2_virus_sprite_group,
                              p2_block_sprite_group, p2_landed_sprite_group, 2)
            elif len(p2_grid.viruses) == 0:
                print("P2 won that round")
                p2_wins.append('win')
                s.add_crowns(p2_wins, crown_list, 2)
                pygame.time.wait(3000)
                p1_grid.reset_board(p1_sprite_group, p1_virus_sprite_group,
                              p1_block_sprite_group, p1_landed_sprite_group, 1)
                p2_grid.reset_board(p2_sprite_group, p2_virus_sprite_group,
                              p2_block_sprite_group, p2_landed_sprite_group, 2)
                
            # Track the pill positions to handle collisions
            p1_main_blocked = s.check_if_blocked(p1_grid, p1_pill.main_block)
            p1_secondary_blocked = s.check_if_blocked(p1_grid, p1_pill.second_block)
            p1_dropping_sprites, p1_dropping_coords = s.check_for_drops(p1_grid, p1_landed_sprite_group, p1_block_sprite_group)
            
            p2_main_blocked = s.check_if_blocked(p2_grid, p2_pill.main_block)
            p2_secondary_blocked = s.check_if_blocked(p2_grid, p2_pill.second_block)
            p2_dropping_sprites, p2_dropping_coords = s.check_for_drops(p2_grid, p2_landed_sprite_group, p2_block_sprite_group)

            p1_blocks_to_clear = p1_grid.check_horizontal_clears() + p1_grid.check_vertical_clears()
            p2_blocks_to_clear = p2_grid.check_horizontal_clears() + p2_grid.check_vertical_clears()

            
            # poll for user events
            for event in pygame.event.get():
                if event.type == P1_STEP:
                    # Check for dropping pieces
                    if p1_dropping_sprites:
                        s.drop_sprites(p1_grid, p1_dropping_sprites, p1_dropping_coords)
                        c.BLOCK_DROP_SFX.play() 
                    else:
                        if p1_main_blocked[2] or p1_secondary_blocked[2]:
                            p1_grid.set_cell_value(p1_pill.main_block[0], p1_pill.main_block[1], p1_pill.main_block[2])
                            p1_grid.set_cell_value(p1_pill.second_block[0], p1_pill.second_block[1], p1_pill.second_block[2])
                            p1_landed_sprite_group.add(p1_pill)
                            p1_sprite_group.empty()
                            c.BLOCK_PLACE_SFX.play()
                            # Check for clears
                            if p1_blocks_to_clear:
                                s.handle_clears(p1_grid, p1_blocks_to_clear, p1_virus_sprite_group, p1_landed_sprite_group, p1_block_sprite_group, 1)
                        else:
                            p1_pill.move("down")   # comment this line out to disable gravity
                            c.MOVE_SFX.play()
                            
                if event.type == P2_STEP:
                    # Check for dropping pieces
                    if p2_dropping_sprites:
                        s.drop_sprites(p2_grid, p2_dropping_sprites, p2_dropping_coords)
                        c.BLOCK_DROP_SFX.play() 
                    else:
                        if p2_main_blocked[2] or p2_secondary_blocked[2]:
                            p2_grid.set_cell_value(p2_pill.main_block[0], p2_pill.main_block[1], p2_pill.main_block[2])
                            p2_grid.set_cell_value(p2_pill.second_block[0], p2_pill.second_block[1], p2_pill.second_block[2])
                            p2_landed_sprite_group.add(p2_pill)
                            p2_sprite_group.empty()
                            c.BLOCK_PLACE_SFX.play()
                            # Check for clears
                            if p2_blocks_to_clear:
                                s.handle_clears(p2_grid, p2_blocks_to_clear, p2_virus_sprite_group, p2_landed_sprite_group, p2_block_sprite_group, 2)
                        else:
                            p2_pill.move("down")   # comment this line out to disable gravity
                            c.MOVE_SFX.play()
                            
                if event.type == pygame.KEYDOWN:
                    # Close window
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        pygame.display.quit()
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        print(p1_grid.cells)
                        ##### Write logic here to pause the game
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
                            elif p1_pill.is_horizontal() and p1_main_blocked[3]:
                                pass
                            else:
                                p1_pill.rotate()
                                c.ROTATE_SFX.play()
                    
                    if not p2_dropping_sprites:
                        # P2 controls
                        if event.key == pygame.K_LEFT:
                            if not p2_main_blocked[0] and not p2_secondary_blocked[0]:
                                p2_pill.move("left")
                                c.MOVE_SFX.play()
                        elif event.key == pygame.K_RIGHT:
                            if not p2_main_blocked[1] and not p2_secondary_blocked[1]:
                                p2_pill.move("right")
                                c.MOVE_SFX.play()
                        elif event.key == pygame.K_DOWN:
                            if not p2_main_blocked[2] and not p2_secondary_blocked[2]:
                                p2_pill.move("down")
                                c.MOVE_SFX.play()
                        elif event.key == pygame.K_UP:
                            if not p2_pill.is_horizontal() and p2_pill.main_block[1] == 7 or p2_main_blocked[1]:
                                p2_pill.move("left")
                                p2_pill.rotate()
                                c.ROTATE_SFX.play()
                            elif p2_pill.is_horizontal() and p2_main_blocked[3]:
                                pass
                            else:
                                p2_pill.rotate()
                                c.ROTATE_SFX.play()
                        
            # Update screen sprites
            screen.blit(background, (0,0))
            for crown in crown_list:
                screen.blit(crown[0], (crown[1],crown[2]))
            p1_sprite_group.update()
            p1_sprite_group.draw(screen)
            p1_landed_sprite_group.draw(screen)
            p1_virus_sprite_group.draw(screen)
            p1_block_sprite_group.draw(screen)
            
            p2_sprite_group.update()
            p2_sprite_group.draw(screen)
            p2_landed_sprite_group.draw(screen)
            p2_virus_sprite_group.draw(screen)
            p2_block_sprite_group.draw(screen)
            
            pygame.display.flip()
            clock.tick(60) / 1000
            
        # Clear the screen and stop music when exiting this view
        screen.fill((255,255,255))
        pygame.mixer.stop()
        