from pygame.sprite import Sprite
from pygame import mouse
from images import load_and_get_rect, reduce_and_get_rect

class Hole(Sprite):
    def __init__(self, game):
        super().__init__()
        self.hole_file = ("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/bullet_hole_2.png")
        self.image, self.rect = load_and_get_rect(self.hole_file)
        self.reduce_width = game.game_window.window_size[0] / 14
        self.reduce_height = game.game_window.window_size[0] / 14
        self.image, self.rect = reduce_and_get_rect(self.image, 
            self.reduce_width, self.reduce_height)        
        self.rect.center = mouse.get_pos()
