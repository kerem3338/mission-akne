"""
Mission Akne: Gun Fight

Bu oyun Akne'nin kullandığı motoru test etmek için hazırlanmış bir test oyunudur.

"""
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"
import engine
import pygame
import sys
import time

from engine.object import source_path


global screen
screen=engine.Window(600,400).getforlevel()
class Menu:
    def __init__(self):
        pass
        self.bg_color=pygame.Color("white")
    def load_once(self):
        self.screen=screen
        pygame.font.init()
        self.font=pygame.font.SysFont("Arial",30)

    def load(self):
        self.timer=engine.Timer()
        self.timer.start()
        while True:
            if self.timer.get_time() > 5:
                break
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            self.screen.fill(self.bg_color)
            pygame.draw.rect(self.screen,pygame.Color("red"),pygame.Rect(0,0,self.screen.get_width(),50))
            pygame.draw.rect(self.screen,pygame.Color("red"),pygame.Rect(0,self.screen.get_height()-50,self.screen.get_width(),50))
            
            x=self.font.render("Mission Akne: Gun Fight",True,pygame.Color("black"))
            self.screen.blit(x,(self.screen.get_width()/2-x.get_width()/2,self.screen.get_height()/2-x.get_height()/2))
            pygame.display.update()


        


class Fight:
    """Main game"""
    def __init__(self):
        pass
    def load_once(self):
        self.screen=screen
        self.player=engine.Player(x=32,y=self.screen.get_height()-(32*2),color=pygame.Color("yellow"))
        self.bot=engine.Player(x=self.screen.get_width()-(32*2),y=self.screen.get_height()-(32*2),color=pygame.Color("red"))
        self.level_end=engine.Object(80,self.screen.get_height()-80,50,100)

        self.sprites=engine.Spritesheet(source_path("sprites.png"))
        self.box1=engine.Object(self.screen.get_width()-(32*3),self.screen.get_height()-(32*2),32,32,isrect=False,readyimage=True,imagefile=self.sprites.get(0,3))
        self.box2=engine.Object(64,self.screen.get_height()-(32*2),32,32,isrect=False,readyimage=True,imagefile=self.sprites.get(0,3))
        self.box1.update()
        self.box2.update()

        self.bullet_counts={
            "player":4,
            "bot":4
        }

        
        self.ready=False

        
        self.pl_sit=True
        self.bot_sit=True

        self.player_bullets=[]
        self.bot_bullets=[]
        self.win=None
        self.wintext=""
        self.bulletspeed=9
        self.text=engine.Text("Wait","Arial",pygame.Color("black"),self.screen.get_height()/2,self.screen.get_width()/2,30)
        
    def controlend(self):
        if self.bot.health == 0:
            self.ready=False
            self.win="yellow"
            self.wintext=self.wintext=pygame.font.SysFont("arial",30).render("yellow Wins",False,pygame.Color("yellow"))
        if self.player.health == 0:
            self.ready=False
            self.win="red"
            self.wintext=pygame.font.SysFont("arial",30).render("Red Wins",False,pygame.Color("red"))
    
    def death(self):
        self.controlend()
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if i.key == pygame.K_SPACE:
                        pygame.quit()
                        os.system(source_path(f"{__file__}"))
                        sys.exit()
                        

            self.screen.fill(pygame.Color("white"))
            text_rect = self.wintext.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            restart_text=pygame.font.SysFont("arial",30).render("Press 'Space' for restart game",False,pygame.Color("green"))
            restart_rect=restart_text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/4))
            self.screen.blit(restart_text,restart_rect)
            self.screen.blit(self.wintext,text_rect)
            pygame.display.update()

    def load(self):
        self.timer=engine.Timer()
        self.timer.start()
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_UP:
                        if self.bot_sit:
                            self.bot.change_size(64,32)
                            self.bot.move("up",32)
                            self.bot_sit=False
                            

                    if i.key == pygame.K_DOWN:
                        if not self.bot_sit:
                            self.bot.change_size(32,32)
                            self.bot.move("down",32)
                            self.bot_sit=True

                    
                    if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                        if not self.bot_sit and self.ready:
                            if self.bullet_counts["bot"] != 0:
                                self.bot_bullets.append(engine.Bullet("bot",self.bot.x,self.bot.y,32,32,pygame.Color("red"),self.bulletspeed,"left"))
                                self.bullet_counts["bot"]-=1

                    #Player controls
                    if i.key == pygame.K_w:
                        if self.pl_sit:
                            self.player.change_size(64,32)
                            self.player.move("up",32)
                            self.pl_sit=False
                            

                    if i.key == pygame.K_s:
                        if not self.pl_sit:
                            self.player.change_size(32,32)
                            self.player.move("down",32)
                            self.pl_sit=True

                    if i.key == pygame.K_SPACE:
                        if not self.pl_sit:
                            if self.bullet_counts["player"] != 0 and self.ready:
                                self.player_bullets.append(engine.Bullet("player",self.player.x,self.player.y,32,32,pygame.Color("yellow"),self.bulletspeed,"right"))
                                self.bullet_counts["player"]-=1
            
            self.screen.fill(pygame.Color("white"))

            
            if self.timer.get_time() < 2:
                self.text.draw(self.screen,center=True)
            else:
                self.timer.stop()
                self.ready=True

            if self.bot.health == 0:
                self.death()
            if self.player.health == 0:
                self.death()

            for i in self.player_bullets:
                i.update()
                i.draw(self.screen)
                if i.x > self.screen.get_width() or i.x < 0:
                    self.player_bullets.remove(i)
                if i.rect.colliderect(self.bot.rect):
                    self.player_bullets.remove(i)
                    self.bot.health_change("sub",25)
                    self.bullet_counts["player"]+=1

            for i in self.bot_bullets:
                i.update()
                i.draw(self.screen)
                if i.x > self.screen.get_width() or i.x < 0:
                    self.bot_bullets.remove(i)
                if i.rect.colliderect(self.player.rect):
                    self.bot_bullets.remove(i)
                    self.player.health_change("sub",25)
                    self.bullet_counts["bot"]+=1
            
            if self.pl_sit:
                self.player.goto(x=32,y=self.screen.get_height()-(32*2))
            if self.bot_sit:
                self.bot.goto(x=self.screen.get_width()-(32*2),y=self.screen.get_height()-(32*2))
            x=engine.Platform(self.screen.get_height()-32,0)
            y=engine.Platform(self.screen.get_height()-32,self.screen.get_width()-(32*3))
            x.draw(self.screen)
            y.draw(self.screen)
            self.box1.draw(self.screen)
            self.box2.draw(self.screen)
            
            self.player.draw(self.screen)
            self.bot.draw(self.screen)
            pygame.display.update()

menu=engine.Level(Menu)
menu.run()

fight=engine.Level(Fight)
fight.run()