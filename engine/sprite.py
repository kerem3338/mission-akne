import pygame
import os
import sys

class Spritesheet:
    def __init__(self, filename,info_file=""):
        try:
            self.sheet = pygame.image.load(filename)
        except pygame.error as e:
            print("Unable to load spritesheet image:", filename)
            raise(e)
        self.part_size = (32,32)
        self.info_file=info_file

    def get(self,y,x):
        return self.sheet.subsurface(pygame.Rect(x*self.part_size[0],y*self.part_size[1],self.part_size[0],self.part_size[1]))
