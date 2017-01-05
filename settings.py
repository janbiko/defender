import pygame as pg

# game settings
TITLE = "Defender"
WIDTH = 640
HEIGHT = 480
FPS = 60

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BACKGROUND = pg.image.load('img/background.jpg')  # placeholder

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.05

# sprites
PLAYER_SPRITE = pg.image.load('img/player/player.png')  # placeholder
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 29
