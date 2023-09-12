import pygame

VIEW = 0
    
pygame.mixer.init()
PAUSE_SFX = pygame.mixer.Sound("assets/sounds/pause.wav")
HOVER_SFX = pygame.mixer.Sound("assets/sounds/hover_beep.wav")
MOVE_SFX = pygame.mixer.Sound("assets/sounds/move.wav")
ROTATE_SFX = pygame.mixer.Sound("assets/sounds/rotate.wav")
BLOCK_PLACE_SFX = pygame.mixer.Sound("assets/sounds/block_place.wav")
BLOCK_DROP_SFX = pygame.mixer.Sound("assets/sounds/block_drop.wav")
CLEAR_SFX = pygame.mixer.Sound("assets/sounds/clear.wav")

MENU_SFX = pygame.mixer.Sound("assets/sounds/menu.wav")
CHILL_SFX = pygame.mixer.Sound("assets/sounds/chill.mp3")
FEVER_SFX = pygame.mixer.Sound("assets/sounds/fever.wav")

P1_COMBO_SFX = pygame.mixer.Sound("assets/sounds/p1_combo.wav")
P2_COMBO_SFX = pygame.mixer.Sound("assets/sounds/p2_combo.wav")
TOP_OUT_SFX = pygame.mixer.Sound("assets/sounds/top_out.wav")


CELL_SIZE = 32    # pixels
SCREEN_WIDTH = 1024    # pixels
SCREEN_HEIGHT = 960    # pixels
GAME_SPEED = 500  # 1000 ms = 1 second
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)    # pixels
FLOOR = 832    # pixels, x

LOW = 1000    # miliseconds
MED = 500    # miliseconds
HI = 250    # miliseconds
MUSIC = CHILL_SFX

P1_LEVEL = 10    # number of viruses
P1_SPEED = LOW
P1_GRID_START = [128, 320]    # pixels
P1_LEFT_WALL = 128    # pixels, x
P1_RIGHT_WALL = 384     # pixels, x

P2_LEVEL = 10    # number of viruses
P2_SPEED = LOW
P2_GRID_START = [736, 320]    # pixels
P2_LEFT_WALL = 640    # pixels, x 
P2_RIGHT_WALL = 896    # pixels, x
