import random
import pygame

from vector2 import Vector2

class Player:
    ID = 0
    def __init__(self):
        self.pos = Vector2(100, 100)
        self.radius = random.randint(5, 10)

    def updatePos(self, keys):
        if keys[pygame.K_d]:
            self.pos.x += 1
        if keys[pygame.K_a]:
            self.pos.x -= 1
        if keys[pygame.K_w]:
            self.pos.y -= 1
        if keys[pygame.K_s]:
            self.pos.y += 1