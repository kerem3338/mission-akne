import pygame

pygame.font.init()

class Text:
    def __init__(self,text,fontanme,color,y,x,size):
        self.text=text
        self.font=pygame.font.SysFont(fontanme,size)
        self.color=color
        self.x=x
        self.y=y
        self.update()

    def change_text(self,text):
        self.text=text
        self.update()
        
    def goto(self,y,x):
        self.x=x
        self.y=y
        self.update()
    
   
        

    def update(self,center=False,screen=""):
        if center == False:
            self.surface=self.font.render(self.text,True,self.color)
            self.rect=self.surface.get_rect()
            self.rect.x=self.x
            self.rect.y=self.y  
        else:
            self.surface=self.font.render(self.text,True,self.color)
            self.rect=self.surface.get_rect(center=(screen.get_width()/2,screen.get_height()/2))

    def draw(self,screen,center=False):
        self.update(center=center,screen=screen)
        screen.blit(self.surface,self.rect)
