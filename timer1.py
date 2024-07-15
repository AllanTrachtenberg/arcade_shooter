import pygame
from pygame.mixer import Sound

class Timer():
    def __init__(self, game):
        self.game = game
        self.clock = pygame.time.Clock()
        self.fps_counter = 0
        self.seconds_counter = 0
        self.time_limit = 30
        self.timer = self.time_limit
        self.end_sound = Sound("sound/pathetic.wav")

    def start(self):
        self.fps_counter += 1
        if self.fps_counter == 60:
            self.timer -= 1
            self.fps_counter = 0
        if self.timer == 0:
            self.game.active = False
            self.end_sound.play()
            self.game.add_music()
            self.timer = self.time_limit

    def reset(self):
        self.seconds_counter = 0

    def draw(self):
        time_string = str(self.timer)
        self.image = self.game.font.render(f"Timer: {time_string}", True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.game.game_window.screen_rect.midbottom[0] / 2,
            self.game.game_window.screen_rect.midbottom[1])
        self.game.game_window.screen.blit(self.image, self.rect)
        