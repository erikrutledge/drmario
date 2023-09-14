import pygame

# SCREEN VARIABLES
CELL_SIZE = 32    # pixels
SCREEN_WIDTH = 1024    # pixels
SCREEN_HEIGHT = 960    # pixels
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)    # pixels
SPEEDS = {"LOW": 1000,
          "MED": 500,
          "HI": 250}

# SINGLE PLAYER VARIABLES
LEVEL = 1
LEVEL_DISPLAY = (790, 610)
SPEED_DISPLAY = (790, 710)
VIRUS_DISPLAY = (790, 810)
GRID_START = [385, 320]
SPEED = SPEEDS["LOW"]

# MULTIPLAYER VARIABLES
P1_LEVEL = 1    # number of viruses
P1_GRID_START = [128, 320]    # pixels
P1_CROWN_START = [453, 330]
P1_SPEED = SPEEDS["LOW"]
P2_LEVEL = 1    # number of viruses
P2_GRID_START = [640, 320]    # pixels
P2_CROWN_START = [520, 330]
P2_SPEED = SPEEDS["LOW"]

# SOUNDS
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
MUSIC = FEVER_SFX

# NOT IMPLEMENTED YET
# P1_COMBO_SFX = pygame.mixer.Sound("assets/sounds/p1_combo.wav")
# P2_COMBO_SFX = pygame.mixer.Sound("assets/sounds/p2_combo.wav")
# TOP_OUT_SFX = pygame.mixer.Sound("assets/sounds/top_out.wav")