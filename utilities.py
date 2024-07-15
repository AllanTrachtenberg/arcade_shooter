import pygame

def initialize_image(self, ratio):
        image = pygame.image.load(self.settings.bullet_hole_image)
        transform_ratio = (self.game.monitors_dic["monitor_1"]["width"] / ratio)
        image_reduced = pygame.transform.scale(image, 
            (transform_ratio, transform_ratio))
        self.rect = image_reduced.get_rect()
        self.rect.center = (self.game.bullet_hole_mouse_pos_x, 
            self.game.bullet_hole_mouse_pos_y)
        self.image = image_reduced