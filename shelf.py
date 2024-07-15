from images import load_and_get_rect, reduce_and_get_rect

class Shelf():
    def __init__(self, game):
        self.game = game
        self.image_file_1 = ("images/shelf.png")
        self.transform_width = (game.game_window.window_size[0])
        self.transform_height = (game.game_window.window_size[1] / 20)
        self.image_1, self.image_1_rect = load_and_get_rect(self.image_file_1)
        self.image_1, self.image_1_rect = reduce_and_get_rect(self.image_1,
            self.transform_width, self.transform_height)
        self.topshelf_y = self.game.game_window.window_size[1] / 2.1
        self.bottomshelf_y = self.game.game_window.window_size[1] / 1.4

    def draw_shelfs(self):
        self.image_1_rect.topleft = (0, self.topshelf_y)
        self.game.game_window.screen.blit(self.image_1, 
            self.image_1_rect)
        self.image_1_rect.topleft = (0, self.bottomshelf_y)
        self.game.game_window.screen.blit(self.image_1, 
            self.image_1_rect)