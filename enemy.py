import random
from settings import *
vec = pg.math.Vector2


class Enemy (pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.cur_frame = 0
        self.last_update = 0
        self.perspective = True
        self.random_spawn()
        self.load_enemy_images()
        self.image = self.fly[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = self.random_velocity()

    def load_enemy_images(self):
        # loading enemy frames into array to work with in animation()-function
        self.fly = []
        for i in range(len(ENEMY_FRAMES)):
            self.fly.append(ENEMY_FRAMES[i])

    def update(self):
        # animating enemy
        self.animation()

        # deleting enemies if they reach a certain point on the opposite side
        # of their original spawnpoint
        if self.spawnpoint == 0:
            if self.rect.x > WIDTH + ENEMY_SPAWN_RANGE:
                self.kill()
        else:
            if self.rect.x < -ENEMY_SPAWN_RANGE:
                self.kill()

        # setting enemy to new position
        self.pos = self.pos + self.vel
        self.rect.center = self.pos

    def animation(self):
        # setting new enemy frame for player every 80 milliseconds
        cur_time = pg.time.get_ticks()
        if cur_time - self.last_update > ENEMY_ANIMATION_SPEED:
            self.last_update = cur_time
            self.cur_frame = (self.cur_frame + 1) % len(self.fly)
            self.image = self.fly[self.cur_frame]

    def random_spawn(self):
        # generating random spawnpoint within a given range,
        # either on the left or right side outside the screen
        self.spawnpoint = random.randrange(0, 2)
        if self.spawnpoint == 0:
            self.x = random.randrange(-ENEMY_SPAWN_RANGE, 0)
            self.y = random.randrange(UI_HEIGHT, HEIGHT)
        else:
            self.x = random.randrange(WIDTH, WIDTH + ENEMY_SPAWN_RANGE)
            self.y = random.randrange(UI_HEIGHT, HEIGHT)

    def random_velocity(self):
        # generating random velocity for enemies within a given range
        if self.spawnpoint == 0:
            return [random.randrange(ENEMY_VELOCITY_MIN, ENEMY_VELOCITY_MAX), 0]
        else:
            return [random.randrange(-ENEMY_VELOCITY_MAX, -ENEMY_VELOCITY_MIN), 0]
