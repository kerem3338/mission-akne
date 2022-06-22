import pygame
import time

class Timer:
    def __init__(self):
        self.first_start__time=time.time()
        self.pause=False

    def start(self):
        self.start_time=time.time()

    def pause(self):
        if not self.pause:
            self.pause_time=time.time()
            self.pause=True
        else:
            raise Exception("Timer is already paused")

    def get_time(self):
        return time.time()-self.start_time
        
    def stop(self):
        self.start_time=0
        
    def resume(self):
        self.start_time+=time.time()-self.pause_time