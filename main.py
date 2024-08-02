import pygame
import sys
from aim import Aim
from game_window import GameWindow
from curtain import Curtain
from shelf import Shelf
from timer1 import Timer
from target_group import TargetGroup
from play_button import PlayButton
from score import Score
from holes import Holes

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Arcade Shooter")
        self.font = pygame.font.SysFont(None, 48)
        self.game_window = GameWindow()
        self.aim = Aim(self)
        self.curtains = Curtain(self)
        self.shelf = Shelf(self)
        self.timer1 = Timer(self)
        self.score = Score(self)
        self.target_group = TargetGroup(self)
        self.play_button = PlayButton(self)
        self.holes = Holes(self)
        self.mouse_position = (0, 0)
        self.active = False
        self.game_on()
    
    def game_run(self):
        while self.active:
            self.run_first_elements()
            self.timer1.start()
            self._check_user_input()
            self.aim.draw_aim(self.aim.aim_pos_x, self.aim.aim_pos_y)
            pygame.display.flip()        
            
    def game_on(self):
        self.add_music()
        while True:
            if not self.active:
                self.run_first_elements()
                self.play_button.draw_play_button()
                self.play_button.check_play_press()
                self.aim.draw_aim(self.aim.aim_pos_x, self.aim.aim_pos_y)
            else:
                self.reset_elements()
                self.stop_music()
                self.game_run()
            pygame.display.flip()

    def run_first_elements(self):
        pygame.mouse.set_visible(False)
        self.timer1.clock.tick(60)
        self._check_user_input()
        self.game_window.draw_screen()
        self.shelf.draw_shelfs()
        self.holes.holes.draw(self.game_window.screen)
        self.target_group.draw_targets()
        self.curtains.draw_curtains()
        self.score.draw()
        self.score.draw_level()
        self.timer1.draw()

    def reset_elements(self):
        self.score.reset()
        self.timer1.reset()
        self.mouse_position = (0, 0)
        self.target_group.reset()
        self.holes.reset()
    
    def _check_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                self.aim.aim_pos_x, self.aim.aim_pos_y = (
                    pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.active: 
                    if event.button == 1:
                        self.holes.add_hole()
                        self.holes.check_collisions()
                        if not self.holes.collision:
                            self.score.number -= 1
                            self.holes.missed += 1
                            self.holes.missed_mock()
                if not self.active:
                    self.mouse_position = pygame.mouse.get_pos()
                    self.play_button.check_play_press()

    def add_music(self):
        pygame.mixer.music.load("sound/muchacho.mp3")
        pygame.mixer.music.play(-1)
    
    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == '__main__':
    game = Game()            