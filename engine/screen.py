import pygame

class Window:
    def __init__(self,width,height,title="Akne Engine"):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
    def getforlevel(self):
        return self.screen