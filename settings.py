from itertools import izip
import pygame as pg

pg.init()

# game settings
TITLE = "Defender"
WIDTH = 640
HEIGHT = 480
FPS = 60
BACKGROUND = pg.image.load('img/background.jpg')
THEME_MUSIC = pg.mixer.music.load('snd/theme.wav')
HIGHSCORE = "highscore.txt"
AMOUNT_PLAYER_LIVES = 3


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# helpers
ADD_TUPLES = lambda xs, ys: tuple(x + y for x, y in izip(xs, ys))


# player
player_sprite = pg.sprite.Group()
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 29
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.05
PLAYER_ANIMATION_SPEED = 50
PLAYER_CRASH = pg.mixer.Sound('snd/player_crash.wav')
PLAYER_EXPLOSION = pg.mixer.Sound('snd/player_explosion.wav')
PLAYER_FRAMES = [pg.image.load('img/player/f1.png'),
                 pg.image.load('img/player/f2.png'),
                 pg.image.load('img/player/f3.png'),
                 pg.image.load('img/player/f4.png')]


# bullets
bullets = pg.sprite.Group()
BULLET_SPEED = 15
SHOOTING_SOUND = pg.mixer.Sound('snd/shooting_sound.wav')


# enemy
enemy_sprites = pg.sprite.Group()
ENEMY_EXPLOSION = pg.mixer.Sound('snd/explosion.wav')
ENEMY_SPAWN_RANGE = 250
ENEMY_VELOCITY_MIN = 2
ENEMY_VELOCITY_MAX = 5
ENEMY_ANIMATION_SPEED = 80
ENEMY_FRAMES = [pg.image.load('img/enemy/f1.png'),
                pg.image.load('img/enemy/f2.png'),
                pg.image.load('img/enemy/f3.png'),
                pg.image.load('img/enemy/f4.png'),
                pg.image.load('img/enemy/f5.png'),
                pg.image.load('img/enemy/f6.png')]


# ui settings
UI_HEIGHT = 75
SCORE_PER_KILL = 100
SCORE_LEADING_ZEROS = 5
SCORE_SIZE = 23
SCORE_X = 550
SCORE_Y = 15

PLAYER_LIVES_X = 25
PLAYER_LIVES_Y = 10
PLAYER_LIVES_OFFSET = 18

BIG_FONT_SIZE = 50
SMALL_FONT_SIZE = 30
