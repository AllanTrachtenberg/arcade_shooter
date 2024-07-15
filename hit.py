from pygame.sprite import Sprite
from pygame import mouse
from images import load_and_get_rect

class Hit(Sprite):
    def __init__(self):
        super().__init__()
        self.hit_file = ("images/hit.png")
        self.image, self.rect = load_and_get_rect(self.hit_file)
        self.rect.center = mouse.get_pos()