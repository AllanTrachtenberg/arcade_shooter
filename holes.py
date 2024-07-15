import pygame
from hole import Hole
from hit import Hit

class Holes():
    def __init__(self, game):
        self.game = game
        self.holes = pygame.sprite.Group()
        self.hits = pygame.sprite.Group()
        self.shot_sound = pygame.mixer.Sound("sound/shot.mp3")
        self.shot_sound.set_volume(0.3)
        self.missed = 0
        self.missed_sound = pygame.mixer.Sound("sound/haha.mp3")

    def add_hole(self):
        if len(self.holes) > 4:
            self.holes.remove(self.holes.sprites()[0])
        new_hole = Hole(self.game)
        self.holes.add(new_hole)
        self.shot_sound.play()
        self.add_hit()

    def add_hit(self):    
        hit = Hit()
        self.hits.add(hit)

    def check_collisions(self):
        self.collision = pygame.sprite.groupcollide(
            self.game.target_group.targets, self.hits, True, True)
        if self.collision:
            self.game.score.number += 1 * self.game.score.multi
            self.missed = 0
        self.game.target_group.check_if_empty()
        self.hits.empty()

    def reset(self):
        self.holes.empty()

    def missed_mock(self):
        if self.missed == 3:
            self.missed_sound.play()
            self.missed = 0