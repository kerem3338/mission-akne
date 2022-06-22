import pygame


class Bullet:
    def __init__(self,sender,x,y,width,height,color,speed,direction:str):
        self.x=x
        self.sender=sender
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.speed=speed
        self.direction=direction
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.lock=False
    def kill(self):
        self.lock=True

    def update(self):
        if not self.lock:
            if self.direction=="left":
                self.x-=self.speed
            elif self.direction=="right":
                self.x+=self.speed
            self.rect.x=self.x
            self.rect.y=self.y
            self.rect.width=self.width
            self.rect.height=self.height
            self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        else:
            print("this bullet locked")
    def draw(self,screen):
        if not self.lock:
            pygame.draw.rect(screen,self.color,self.rect)
        else:
            print("this bullet locked")
