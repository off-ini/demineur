import pygame
from .Image import Image

class Surf(object):
    def __init__(self, screen, color=(255,255,255), rect=(0,0, 30,30)):
        self.status = -1
        self.opened = 0
        self.body = rect
        self.rect = pygame.draw.rect(screen, color, self.body)

    def setBody(x,y,w,h):
        self.body = (x,y,w,h)

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
    
    def draw(self, screen):
        BLACK, WHITE = (0,0,0), (255,255,255)
        img_f = Image("assets/f.png", self.body[2], self.body[3])
        img_d = Image("assets/d.png", self.body[2], self.body[3])
        img_b = Image("assets/b.png", self.body[2], self.body[3])
        img_b1 = Image("assets/b1.png", self.body[2], self.body[3])

        img_0 = Image("assets/0.png", self.body[2], self.body[3])
        img_1 = Image("assets/1.png", self.body[2], self.body[3])
        img_2 = Image("assets/2.png", self.body[2], self.body[3])
        img_3 = Image("assets/3.png", self.body[2], self.body[3])
        img_4 = Image("assets/4.png", self.body[2], self.body[3])
        img_5 = Image("assets/5.png", self.body[2], self.body[3])
        img_6 = Image("assets/6.png", self.body[2], self.body[3])
        img_7 = Image("assets/7.png", self.body[2], self.body[3])
        img_8 = Image("assets/8.png", self.body[2], self.body[3])

        if self.opened == 1:
            if self.status == 0:
                screen.blit(img_0.get_image(), (self.body[0], self.body[1]))
            elif self.status == 1:
                screen.blit(img_1.get_image(), (self.body[0], self.body[1]))
            elif self.status == 2:
                screen.blit(img_2.get_image(), (self.body[0], self.body[1]))
            elif self.status == 3:
                screen.blit(img_3.get_image(), (self.body[0], self.body[1]))
            elif self.status == 4:
                screen.blit(img_4.get_image(), (self.body[0], self.body[1]))
            elif self.status == 5:
                screen.blit(img_5.get_image(), (self.body[0], self.body[1]))
            elif self.status == -6:
                screen.blit(img_6.get_image(), (self.body[0], self.body[1]))
            elif self.status == 7:
                screen.blit(img_7.get_image(), (self.body[0], self.body[1]))
            elif self.status == 8:
                screen.blit(img_8.get_image(), (self.body[0], self.body[1]))
            elif self.status == 10:
                screen.blit(img_b.get_image(), (self.body[0], self.body[1]))
            elif self.status == 11:
                screen.blit(img_b1.get_image(), (self.body[0], self.body[1]))
            else:
                screen.blit(img_f.get_image(), (self.body[0], self.body[1]))
        elif self.opened == 0:
            screen.blit(img_f.get_image(), (self.body[0], self.body[1]))
        elif self.opened == 2:
            screen.blit(img_d.get_image(), (self.body[0], self.body[1]))