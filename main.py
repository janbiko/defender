from pygame.sprite import groupcollide
from player import *
from enemy import *
from ui import *


class Game:
    def __init__(self):
        # initializing game settings
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.mixer.music.play(loops=-1, start=0.0)
        self.running = True
        self.load_highscore()
        self.score = 0
        self.player_lives = AMOUNT_PLAYER_LIVES

    def new(self):
        # start new game
        self.player = Player(self)
        player_sprite.add(self.player)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # updating all sprites and checking for collisions
        # creating new enemies if required
        player_sprite.update()
        enemy_sprites.update()
        bullets.update()
        if len(enemy_sprites) < 10:
            self.enemy = Enemy(self)
            enemy_sprites.add(self.enemy)
        self.check_for_collisions()

    def events(self):
        # game loop events
        for event in pg.event.get():
            # check for quitting game
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            # capturing space bar event and execute
            # player shooting function
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.shoot()

    def draw(self):
        # continuously drawing every object on screen
        self.screen.blit(BACKGROUND, [0, 0])
        self.ui = UI(game)
        player_sprite.draw(self.screen)
        enemy_sprites.draw(self.screen)
        bullets.draw(self.screen)
        # flip screen after drawing is done
        pg.display.flip()

    def check_for_collisions(self):
        # check for collisions between enemies and player bullets
        # and increasing the score in case of a collision
        if groupcollide(bullets, enemy_sprites, True, True):
            ENEMY_EXPLOSION.play()
            self.score += SCORE_PER_KILL
        # check for collisions between enemies and player and
        # decreasing player lives in case of a collision
        if groupcollide(player_sprite, enemy_sprites, False, True):
            self.player_lives -= 1
            # ending the game if player is out of lives
            if self.player_lives == 0:
                self.player.kill()
                PLAYER_EXPLOSION.play()
                self.playing = False
            else:
                PLAYER_CRASH.play()

    def start_screen(self):
        # start screen
        StartScreen(self)
        pg.display.flip()
        self.wait_for_input()

    def go_screen(self):
        # game over screen
        if not self.running:
            return
        GameOverScreen(self)
        pg.display.flip()
        self.wait_for_input()

    def wait_for_input(self):
        # waiting for user input
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False

    def load_highscore(self):
        # loading highscore from 'highscore.txt'
        with open(HIGHSCORE, 'r+') as highscore:
            try:
                self.highscore = int(highscore.read())
            except:
                self.highscore = 0


game = Game()
game.start_screen()
while game.running:
    game.new()
    game.go_screen()

pg.quit()
