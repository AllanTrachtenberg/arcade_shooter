import pygame
from target import Target

class TargetGroup():
    def __init__(self, game):
        self.game = game
        self.targets = pygame.sprite.Group()
        self.target_speed = 1
        self.add_targets()

    def add_targets(self):
        self.shelf_y = self.game.shelf.topshelf_y
        self.add_target()
        self.shelf_y = self.game.shelf.bottomshelf_y
        self.add_target()

    def add_target(self):
        target = Target(self.game, self, self.shelf_y)
        self.targets.add(target)

    def draw_targets(self):
        self.update_targets_position()
        self.targets.draw(self.game.game_window.screen)
        
    def update_targets_position(self):
        for target in self.targets:
            target.update_target_position()

    def check_if_empty(self):
        if not self.targets:
            self.add_targets()
            self.target_speed += 1
            self.game.score.multi += 1

    def reset(self):
        self.target_speed = 1
        self.targets.empty()
        self.add_targets()
