from ast import walk
import pygame
import os
import sys,time

class Player:
    def __init__(self,isrect=True,imagefile="",x=0,y=0,width=32,height=32,color=(225,255,0),speed=5):
        self.isrect=isrect
        self.imagefile=imagefile
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.speed=speed
        self.walk=False
        self.walk_pos=None
        self.health=100
        self._maxhealth=100
        if self.isrect:
            self.rect=pygame.Rect(x,y,self.width,self.height)
        else:
            if self.imagefile != "":
                self.image=pygame.image.load(self.imagefile)
                self.rect=self.image.get_rect()
            else:
                raise Exception("Player must have an imagefile or be a rect")

        self.movement_rects={
            "normal":self.rect
        }
        self.current_movement_rect="normal"
    def health_change(self,type,amount):
        if type=="add":
            self.health+=amount
        elif type=="eq":
            self.health=amount
        elif type=="sub":
            self.health-=amount
    
    def update(self):
        if self.isrect:
            self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        else:
            self.rect=self.image.get_rect()
            self.rect.x=self.x
            self.rect.y=self.y
            self.width=self.rect.width
            self.height=self.rect.height

    def goto(self,x,y):
        self.x=x
        self.y=y
        self.update()

    def change_size(self,height,width):
        self.width=width
        self.height=height
        self.update()

    def move(self,action,speed=None):
        if speed == None: speed=self.speed
        else: speed=speed

        """TODO: change movement sprites"""
        if action == "left":
            self.x-=speed
        elif action == "right":
            self.x+=speed
        elif action == "up":
            self.y-=speed
        elif action == "down":
            self.y+=speed
        else:
            raise Exception("Invalid action")
        self.update()

    def draw(self,screen):
        if self.isrect:
            pygame.draw.rect(screen,self.color,self.rect)
        else:
            screen.blit(self.image,self.rect)
