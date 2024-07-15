from images import load_and_get_rect, reduce_and_get_rect
from pygame.mixer import Sound

class PlayButton():
    def __init__(self, game):
        self.game = game
        self.image_file = ("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/play.png")
        self.image, self.image_rect = load_and_get_rect(self.image_file)
        self.play_sound = Sound("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/sound/coin.mp3")

    def draw_play_button(self):
        self.image_rect.center = self.game.game_window.screen_rect.center
        self.game.game_window.screen.blit(self.image, self.image_rect)

    def check_play_press(self):
        button_clicked = self.image_rect.collidepoint(self.game.mouse_position)
        if button_clicked:
            self.game.active = True
            self.play_sound.play()