from pygame import display, time

class GameWindow():
    def __init__(self):
        #Resolution
        self.monitors = display.get_desktop_sizes() #(width x height)
        self.window_size = (
            self.monitors[0][0] / 2, self.monitors[0][1] / 2) #(width x height)
        self.screen = display.set_mode(self.window_size)
        self.screen_rect = self.screen.get_rect()

    def draw_screen(self):
        self.screen.fill((179, 218, 255))
