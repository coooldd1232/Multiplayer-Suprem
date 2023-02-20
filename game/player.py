import random
import pygame

class Player:
    def __init__(self):
        self.pos = [100, 100]
        self.radius = random.randint(5, 10)

    def updatePos(self, keys):
        if keys[pygame.K_RIGHT]:
            self.pos[0] += 1
        if keys[pygame.K_LEFT]:
            self.pos[0] -= 1
        if keys[pygame.K_UP]:
            self.pos[1] -= 1
        if keys[pygame.K_DOWN]:
            self.pos[1] += 1