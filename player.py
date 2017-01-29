from bullets import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.cur_frame = 0
        self.last_update = 0
        self.perspective = True
        self.load_player_images()
        self.image = self.fly_r[0]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec()
        self.acc = vec()

    def load_player_images(self):
        # loading player frames into array to work with in animation()-function
        self.fly_r = []
        for i in range(len(PLAYER_FRAMES)):
            self.fly_r.append(PLAYER_FRAMES[i])
        self.fly_l = []
        for frame in self.fly_r:
            self.fly_l.append(pg.transform.flip(frame, True, False))

    def update(self):
        # animating player
        self.animation()
        self.acc = vec()

        # capturing key events, to move player in into desired direction
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.perspective = False
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.perspective = True
            self.acc.x = PLAYER_ACC
        if keys[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC

        # calculating player movement
        self.acc = self.acc + self.vel * PLAYER_FRICTION
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel + 0.5 * self.acc

        # preventing player from getting outside the screen
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 0 + UI_HEIGHT:
            self.pos.y = 0 + UI_HEIGHT

        # setting player to new position
        self.rect.center = self.pos

    def animation(self):
        # setting new player frame for player every 50 milliseconds
        cur_time = pg.time.get_ticks()
        if cur_time - self.last_update > PLAYER_ANIMATION_SPEED:
            self.last_update = cur_time
            self.cur_frame = (self.cur_frame + 1) % len(self.fly_r)
            if self.perspective:
                self.image = self.fly_r[self.cur_frame]
            else:
                self.image = self.fly_l[self.cur_frame]

    def shoot(self):
        # shooting bullet into current perspective
        if self.perspective:
            self.bullet = BulletR(self.rect.center, self.rect.top, self)
        else:
            self.bullet = BulletL(self.rect.center, self.rect.top, self)
        SHOOTING_SOUND.play()
        bullets.add(self.bullet)
