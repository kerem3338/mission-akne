import pygame
from engine.sprite import *
from pathlib import Path

SOURCEPATH = Path(__file__).parents[1]

def source_path(path):
    return os.path.abspath(os.path.join(SOURCEPATH, path))

class Object:
    def __init__(self,x,y,width,height,imagefile="",readyimage=False,isrect=True,color=pygame.Color("white")):
        self.x=x
        self.readyimage=readyimage
        self.y=y
        self.width=width
        self.height=height
        self.isrect=isrect
        self.imagefile=imagefile
        self.color=color

        if self.isrect:
            self.rect=pygame.Rect(x,y,width,height)
        else:
            if self.imagefile != "":
                if not self.readyimage:
                    self.image=pygame.image.load(self.imagefile)
                else:
                    self.image=imagefile
                self.rect=self.image.get_rect()
            else:
                raise Exception("Object must have an imagefile or be a rect")

    def change_image(self,imagefile):
        self.imagefile=imagefile
        self.image=pygame.image.load(self.imagefile)
        self.rect=self.image.get_rect()

    def update(self):
        if self.isrect:
            self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        else:
            self.rect=self.image.get_rect()
            self.rect.x=self.x
            self.rect.y=self.y
            self.width=self.rect.width
            self.height=self.rect.height
            
    def change_position(self,x,y):
        self.x=x
        self.y=y
        self.update()

    
    def draw(self,screen):
        if self.isrect:
            screen.fill(self.color,self.rect)
        else:
            screen.blit(self.image,self.rect)
            
class Platform:
    """Creates Platform"""
    def __init__(self,y,x,spritefile=source_path("sprites.png")):
        self.spritefile=spritefile
        self.sprites=Spritesheet(self.spritefile)
        self.left=self.sprites.get(0,0)
        self.center=self.sprites.get(0,1)
        self.right=self.sprites.get(0,2)
        self.y=y
        self.x=x
        self.rect=pygame.Rect(self.x,self.y,self.sprites.part_size[0]*3,self.sprites.part_size[1])
    
    def change_position(self,x,y):
        self.x=x
        self.y=y
        self.update()

    def update(self):
        self.rect=pygame.Rect(self.x,self.y,self.sprites.part_size[0]*3,self.sprites.part_size[1])
        
    def draw(self,screen):
        screen.blit(self.left,(self.x,self.y))
        screen.blit(self.center,(self.x+32,self.y))
        screen.blit(self.right,(self.x+64,self.y))
