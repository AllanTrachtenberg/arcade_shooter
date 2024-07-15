import pygame

class Images():
    def __init__(self, game):
        self.game = game
        
        #reduce settings
        self.reduce_ratio = (game.game_window.window_size[0] / 12.5)
        self.reduce_ratio_curtain_width = (game.game_window.window_size[0] / 2)
        self.reduce_ratio_curtain_height = (game.game_window.window_size[1])
        
        #image files paths
        self.bullet_hole_file = (#"learning_and_personal_development/"
            "profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/bullet_hole_2.png")
        self.hit_file = ("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/hit.png")
        self.play_file = ("profesional/computacion_e_informatica/"
            "python/playground/pygame/game_1/images/play.png")
        
        #initialize game images
        self.hit, self.hit_rect = self.initialize_image(
            self.hit_file)
        self.play, self.play_rect = self.initialize_image(
            self.play_file)
        
    def bullet_hole_create(self):    
        self.bullet_hole, self.bullet_hole_rect = (
            self.initialize_image(self.bullet_hole_file, True))
    
    def initialize_image(self, image, reduce=False, curtain=False):
        image = pygame.image.load(image)
        if reduce and curtain:
            image_reduced = pygame.transform.scale(image, 
                (self.reduce_ratio_curtain_width, 
                 self.reduce_ratio_curtain_height))
        elif reduce:    
            image_reduced = pygame.transform.scale(image, 
                (self.reduce_ratio, self.reduce_ratio))
        else:
            image_reduced = image

        rect = image_reduced.get_rect()
        return (image_reduced, rect)
    
def load_and_get_rect(image_file):
    image = pygame.image.load(image_file)
    rect = image.get_rect()
    return (image, rect)

def reduce_and_get_rect(image, width, height):
    image_reduced = pygame.transform.scale(image, (width, height))
    rect = image_reduced.get_rect()
    return (image_reduced, rect)
