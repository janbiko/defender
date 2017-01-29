from settings import *


class BulletR(pg.sprite.Sprite):
    def __init__(self, x, y, player):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pg.Surface((20, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.center = ADD_TUPLES(x, (PLAYER_WIDTH / 2, 0))
        self.speed_x = BULLET_SPEED

    def update(self):
        # setting bullet to new position
        self.rect.x = self.rect.x + self.speed_x
        # destroy bullet if it leaves screen
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()


class BulletL(pg.sprite.Sprite):
    def __init__(self, x, y, player):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pg.Surface((20, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.center = ADD_TUPLES(x, (-PLAYER_WIDTH / 2, 0))
        self.speed_x = BULLET_SPEED

    def update(self):
        # setting bullet to new position
        self.rect.x = self.rect.x - self.speed_x
        # destroy bullet if it leaves screen
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()
