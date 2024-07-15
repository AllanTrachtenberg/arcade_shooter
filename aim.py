from pygame.sprite import Sprite
from images import load_and_get_rect, reduce_and_get_rect

class Aim(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image_file = ("images/aim2.png")
        self.image, self.rect = load_and_get_rect(self.image_file)
        self.reduce_width = game.game_window.window_size[0] / 12.5
        self.reduce_height = game.game_window.window_size[0] / 12.5
        self.image, self.rect = reduce_and_get_rect(self.image, 
            self.reduce_width, self.reduce_height)
        self.rect.center = game.game_window.screen_rect.center
        self.aim_pos_x, self.aim_pos_y = (
            game.game_window.screen_rect.center[0], 
            game.game_window.screen_rect.center[1] / 2)
        
    def draw_aim(self, aim_pos_x, mouse_pos_y):
        self.rect.center = (aim_pos_x, mouse_pos_y)
        self.game.game_window.screen.blit(self.image, self.rect)

        