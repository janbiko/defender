from settings import *


class UI:
    def __init__(self, game):
        self.game = game
        self.draw_ui()

    def draw_ui(self):
        # drawing basic frames of the game ui
        pg.draw.line(self.game.screen, WHITE, (0, UI_HEIGHT), (WIDTH, UI_HEIGHT), 3)
        pg.draw.line(self.game.screen, WHITE, (WIDTH * 1 / 4, 0), (WIDTH * 1 / 4, UI_HEIGHT), 3)
        pg.draw.line(self.game.screen, WHITE, (WIDTH * 3 / 4, 0), (WIDTH * 3 / 4, UI_HEIGHT), 3)

        # placing player lives, score and highscore onto the ui frame
        self.display_player_lives()
        self.write_text("Highscore: " + str(self.game.highscore), SMALL_FONT_SIZE, WHITE, WIDTH / 2, UI_HEIGHT / 2.5)
        self.write_text("Score: " + str(self.game.score).zfill(SCORE_LEADING_ZEROS), SCORE_SIZE, WHITE, SCORE_X,
                        SCORE_Y)

    def display_player_lives(self):
        # resizing player sprite frame and drawing it on the screen dependent on
        # current player lives
        image = pg.transform.scale(PLAYER_FRAMES[0], (PLAYER_WIDTH / 2, PLAYER_HEIGHT / 2))
        lives_y = PLAYER_LIVES_Y
        for i in range(self.game.player_lives):
            self.game.screen.blit(image, (PLAYER_LIVES_X, lives_y))
            lives_y += PLAYER_LIVES_OFFSET

    def write_text(self, text, size, color, x, y):
        # helper function, to display text on screen
        font = pg.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.game.screen.blit(text_surface, text_rect)


class StartScreen:
    def __init__(self, game):
        self.game = game
        self.ui = UI(self.game)
        self.draw_start_screen()

    def draw_start_screen(self):
        # setting background for start screen
        self.game.screen.blit(BACKGROUND, [0, 0])

        # drawing highscore, game title and game instructions on screen
        self.ui.write_text("Highscore: " + str(self.game.highscore), SMALL_FONT_SIZE, WHITE, WIDTH / 2, UI_HEIGHT / 2.5)
        self.ui.write_text(TITLE, BIG_FONT_SIZE, WHITE, WIDTH / 2, HEIGHT / 4)
        self.ui.write_text("Use W, A, S, D to move", SMALL_FONT_SIZE, WHITE, WIDTH / 2, HEIGHT / 2)
        self.ui.write_text("and 'Space' to shoot.", SMALL_FONT_SIZE, WHITE, WIDTH / 2, HEIGHT / 1.75)
        self.ui.write_text("P r e s s   a n y   k e y   t o   p l a y", SMALL_FONT_SIZE, WHITE, WIDTH / 2, HEIGHT / 1.2)


class GameOverScreen:
    def __init__(self, game):
        self.game = game
        self.ui = UI(self.game)
        self.new_highscore = False
        self.check_for_highscore()
        self.draw_game_over_screen()
        self.reset_game()

    def draw_game_over_screen(self):
        # setting background for game over screen
        self.game.screen.blit(BACKGROUND, [0, 0])

        # drawing new highscore message on screen if highscore was beaten
        if self.new_highscore:
            self.ui.write_text("NEW HIGHSCORE !!!", SMALL_FONT_SIZE, WHITE, WIDTH / 2, HEIGHT / 1.5)
            self.new_highscore = not self.new_highscore

        # drawing highscore, game over message, achieved score and game instructions on screen
        self.ui.write_text("Highscore: " + str(self.game.highscore), SMALL_FONT_SIZE, WHITE, WIDTH / 2, UI_HEIGHT / 2.5)
        self.ui.write_text("G A M E   O V E R", BIG_FONT_SIZE, WHITE, WIDTH / 2, HEIGHT / 4)
        self.ui.write_text("Score: " + str(self.game.score), SMALL_FONT_SIZE, WHITE, WIDTH / 2, HEIGHT / 2)
        self.ui.write_text("P r e s s   a n y   k e y   t o   r e s t a r t", SMALL_FONT_SIZE, WHITE, WIDTH / 2,
                           HEIGHT / 1.2)

    def reset_game(self):
        # setting player lives back to 3, resetting the score and
        # emptying the enemy sprite group
        self.game.player_lives = AMOUNT_PLAYER_LIVES
        self.game.score = 0
        enemy_sprites.empty()

    def check_for_highscore(self):
        # check if achieved score is higher than current highscore
        # and save new highscore in 'highscore.txt'
        if self.game.score > self.game.highscore:
            self.game.highscore = self.game.score
            self.new_highscore = not self.new_highscore
            with open(HIGHSCORE, 'w') as highscore:
                highscore.write(str(self.game.score))

