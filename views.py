import pygame
import constants as c
import scripting as s
from grid import Grid
from pill import Pill
from virus import Virus


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
                    running = False
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
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        print("READY TO PLAY")
                        screen.fill((255,255,255))
                        pygame.mixer.stop()
                        # Views.p1_game_screen(screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    c.HOVER_SFX.play()

            # Follow mouse position and handle clicks
            mouse_pos = pygame.mouse.get_pos()
            pressed = pygame.mouse.get_pressed()[0]
            
            for rect in level_rects:
                if rect.collidepoint(mouse_pos) and pressed:
                    level_number = str(level_rects.index(rect) + 1)
                    level_indicator_pos = (rect.left, rect.centery - 50)
                    c.P1_LEVEL = level_number
                    
            if low_rect.collidepoint(mouse_pos) and pressed:
                speed_indicator_pos = (336, 510)
                c.P1_SPEED = c.LOW
                print("low speed detected")
            if med_rect.collidepoint(mouse_pos) and pressed:
                speed_indicator_pos = (506, 510)
                c.P1_SPEED = c.MED
                print("med speed detected")
            if hi_rect.collidepoint(mouse_pos) and pressed:
                speed_indicator_pos = (681, 510)
                c.P1_SPEED = c.HI
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
                    running = False
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
                    c.P1_LEVEL = p1_level_number
            
            for rect in p2_level_rects:
                if rect.collidepoint(mouse_pos) and pressed:
                    p2_level_number = str(p2_level_rects.index(rect) + 1)
                    p2_level_indicator_pos = (rect.left, rect.centery + 5)
                    c.P2_LEVEL = p2_level_number
                    
            if p1_low_rect.collidepoint(mouse_pos) and pressed:
                p1_speed_indicator_pos = (336, 510)
                c.P1_SPEED = c.LOW
                print("low speed detected")
            if p1_med_rect.collidepoint(mouse_pos) and pressed:
                p1_speed_indicator_pos = (506, 510)
                c.P1_SPEED = c.MED
                print("med speed detected")
            if p1_hi_rect.collidepoint(mouse_pos) and pressed:
                p1_speed_indicator_pos = (681, 510)
                c.P1_SPEED = c.HI
                print("hi speed detected")
            
            if p2_low_rect.collidepoint(mouse_pos) and pressed:
                p2_speed_indicator_pos = (336, 600)
                c.P2_SPEED = c.LOW
                print("low speed detected")
            if p2_med_rect.collidepoint(mouse_pos) and pressed:
                p2_speed_indicator_pos = (506, 600)
                c.P2_SPEED = c.MED
                print("med speed detected")
            if p2_hi_rect.collidepoint(mouse_pos) and pressed:
                p2_speed_indicator_pos = (681, 600)
                c.P2_SPEED = c.HI
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

    def p2_game_screen(screen):
        clock = pygame.time.Clock()
        background = pygame.image.load("assets/screens/p2_game_board.png")
        c.MUSIC.play()
        
        # Initialize sprite groups
        p1_sprite_group = pygame.sprite.Group()
        virus_sprite_group = pygame.sprite.Group()
        block_sprite_group = pygame.sprite.Group()
        landed_sprite_group = pygame.sprite.Group()
        
        # Create grid objects for each player and add viruses
        p1_grid = Grid(c.P1_GRID_START[0], c.P1_GRID_START[1])
        p1_grid.set_virus_values(int(c.P1_LEVEL))

        # Create a sprite for each virus and render them to the screen
        for i in range(len(p1_grid.viruses)):
            row, column = p1_grid.viruses[i][0], p1_grid.viruses[i][1]
            width, height = s.convert_coords_to_tl_pixels(row, column, 1)
            virus = Virus(row, column, height, width, p1_grid.viruses[i][2])
            p1_grid.viruses[i].pop(2)
            virus_sprite_group.add(virus)
        
        # Set the step timer to delay piece movements
        STEP = pygame.USEREVENT + 1
        pygame.time.set_timer(STEP, c.P1_SPEED)
        running = True
        
        while running:
            # Create a pill if one isn't already in play
            if len(p1_sprite_group.sprites()) == 0:
                p1_pill = Pill()
                p1_sprite_group.add(p1_pill)
            
            # Track the pill positions to handle collisions
            p1_main_blocked = s.check_if_blocked(p1_grid, p1_pill.main_block)
            p1_secondary_blocked = s.check_if_blocked(p1_grid, p1_pill.second_block)
            p1_dropping_sprites, p1_dropping_coords = s.check_for_drops(p1_grid, landed_sprite_group, block_sprite_group)

            # poll for user events
            for event in pygame.event.get():
                if event.type == STEP:
                    # Check for dropping pieces
                    if p1_dropping_sprites:
                        s.drop_sprites(p1_grid, p1_dropping_sprites, p1_dropping_coords)
                        c.BLOCK_DROP_SFX.play() 
                    else:
                        if p1_main_blocked[2] or p1_secondary_blocked[2]:
                            p1_grid.set_cell_value(p1_pill.main_block[0], p1_pill.main_block[1], p1_pill.main_block[2])
                            p1_grid.set_cell_value(p1_pill.second_block[0], p1_pill.second_block[1], p1_pill.second_block[2])
                            landed_sprite_group.add(p1_pill)
                            p1_sprite_group.empty()
                            c.BLOCK_PLACE_SFX.play()
                            # Check for clears
                            p1_blocks_to_clear = p1_grid.check_horizontal_clears() + p1_grid.check_vertical_clears()
                            if p1_blocks_to_clear:
                                s.handle_clears(p1_grid, p1_blocks_to_clear, virus_sprite_group, landed_sprite_group, block_sprite_group, 1)
                        else:
                            p1_pill.move("down")   # comment this line out to disable gravity
                            c.MOVE_SFX.play()
                            
                if event.type == pygame.KEYDOWN:
                    # Close window
                    if event.type == pygame.QUIT:
                        running = False
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        print(p1_grid.cells)
                    if event.key == pygame.K_b:
                        print(p1_blocks_to_clear)
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
                        
            # Update screen sprites
            p1_sprite_group.update()
            screen.blit(background, (0,0))
            p1_sprite_group.draw(screen)
            landed_sprite_group.draw(screen)
            virus_sprite_group.draw(screen)
            block_sprite_group.draw(screen)
            
            pygame.display.flip()
            clock.tick(60) / 1000
        
        
        
        
        
        
        
