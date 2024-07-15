import pygame
    
def load_and_get_rect(image_file):
    image = pygame.image.load(image_file)
    rect = image.get_rect()
    return (image, rect)

def reduce_and_get_rect(image, width, height):
    image_reduced = pygame.transform.scale(image, (width, height))
    rect = image_reduced.get_rect()
    return (image_reduced, rect)
