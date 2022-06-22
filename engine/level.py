import pygame
import sys,os,time,getpass

class Level:
    def __init__(self,levelclass):
        self.levelclass = levelclass

    def run(self):
        self.levelclass=self.levelclass()
        self.levelclass.load_once()
        
        
        try:
            self.screen=self.levelclass.screen
        except AttributeError:
            raise AttributeError("Level class must have a screen attribute")
        
        self.levelclass.load()
       