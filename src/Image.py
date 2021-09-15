import pygame

class Image(object):
    def __init__(self, file_name, w, h):
        self.image = pygame.image.load(file_name).convert()
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (int(w), int(h)))
        self.rect = self.image.get_rect()

    def get_rect(self):
        return self.rect

    def get_image(self):
        return self.image

    def draw(self):
        pass