import pygame
import socket
import threading
import random

from network import Network
from player import Player

network = Network()

SCREENWIDTH = 400
SCREENHEIGHT = 400
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("GG JIT")

clock = pygame.time.Clock()

player = Player()

gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    keys = pygame.key.get_pressed()
    player.updatePos(keys)
    network.latestPlayerClass = player

    screen.fill('black')
    # draw ALL players, including YOURSELF
    lPlayers = network.latestPlayerDictionary
    for playerAddr in lPlayers:
        if lPlayers[playerAddr] is not None:
            pygame.draw.circle(screen, 'red', lPlayers[playerAddr].pos, lPlayers[playerAddr].radius)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()