from images import load_and_get_rect, reduce_and_get_rect

class Curtain():
    def __init__(self, game):
        self.game = game
        self.image_file_1 = ("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/cortina1.png")
        self.image_file_2 = ("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/cortina2.png")
        self.reduce_width = (game.game_window.window_size[0] / 2)
        self.reduce_height = (game.game_window.window_size[1])
        self.image_1, self.image_1_rect = load_and_get_rect(self.image_file_1)
        self.image_2, self.image_2_rect = load_and_get_rect(self.image_file_2)

        self.image_1, self.image_1_rect = reduce_and_get_rect(self.image_1,
            self.reduce_width, self.reduce_height)
        self.image_2, self.image_2_rect = reduce_and_get_rect(self.image_2,
            self.reduce_width, self.reduce_height)
        

    def draw_curtains(self):
        self.image_1_rect.topleft = self.game.game_window.screen_rect.topleft
        self.image_2_rect.topright = self.game.game_window.screen_rect.topright
        self.game.game_window.screen.blit(self.image_1, 
            self.image_1_rect)
        self.game.game_window.screen.blit(self.image_2, 
            self.image_2_rect)
