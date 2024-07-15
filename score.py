import pygame

class Score():
    def __init__(self, game):
        self.game = game
        self.number = 0
        self.multi = 1
        self.level = 1        
        
    def draw(self):
        self.score_string = str(self.number)
        self.image = self.game.font.render(
            f"Score: {self.score_string}", True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.game.game_window.screen_rect.midbottom
        self.game.game_window.screen.blit(self.image, self.rect)

    def reset(self):
        self.number = 0
        self.multi = 1

    def draw_level(self):
        self.level_string = str(self.level)
        self.level_image = self.game.font.render(
            f"Level: {self.level_string}", True, (0, 0, 0))
        self.level_rect = self.level_image.get_rect()
        self.level_rect.midbottom = (
            self.game.game_window.screen_rect.bottomright[0] * (3/4),
            self.game.game_window.screen_rect.bottomright[1])
        self.game.game_window.screen.blit(self.level_image, self.level_rect)