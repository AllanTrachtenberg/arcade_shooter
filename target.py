import random
import pygame
from images import load_and_get_rect, reduce_and_get_rect

class Target(pygame.sprite.Sprite):
    def __init__(self, game, target_group, shelf_y):
        super().__init__()
        self.game = game
        self.target_group = target_group
        self.spawn_side = 0
        self.x = 0
        self.y = shelf_y
        self.reduce_width = self.game.game_window.window_size[0] / 12.5
        self.reduce_height = self.game.game_window.window_size[0] / 12.5
        self.initiate_target()

    def load_target_image(self):
        self.image_file = ("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/target1.png")
        self.image, self.rect = load_and_get_rect(self.image_file)
        self.image, self.rect = reduce_and_get_rect(self.image, self.reduce_width, self.reduce_height)
        self.rect.bottomleft = (self.x, self.y)
        
    def initiate_target(self):
        self.random_choice()
        self.set_spawn_side()

    def random_choice(self):
        self.spawn_side = random.choice([1,2])

    def set_spawn_side(self):
        if self.spawn_side == 1:
            self.x = 0
        else:
            self.x = self.game.game_window.window_size[0]

    def update_target_position(self):
        self.load_target_image()
        if self.rect.bottomright[0] > self.game.game_window.window_size[0] + 79 or (
            self.rect.bottomleft[0] < 0):
            self.initiate_target()
        if self.spawn_side == 1:
            self.x += 2 * self.target_group.target_speed
        else:
            self.x -= 2 * self.target_group.target_speed

    def reset(self):
        self.speed = 1
