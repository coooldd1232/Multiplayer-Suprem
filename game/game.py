import pygame
import time

from network import Network
from player import Player

class Game:
    def __init__(self, SCREENWIDTH, SCREENHEIGHT):
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT

        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("CAPTION")

        self.network = Network()
        
        self.clock = pygame.time.Clock()

        self.player = Player()

        self.gameRunning = True

        self.buffer = []
        self.bufferUsed = 0

    def update(self):
        # keeps the game running at 120 fps
        self.clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = False
                self.player.connected = False
        
        keys = pygame.key.get_pressed()
        self.player.updatePos(keys)
        self.network.latestPlayerClass = self.player

        # update player buffer
        self.buffer.append([self.network.latestPlayersDictionary, time.time()])
        try:
            if self.buffer[-2] == [self.network.latestPlayersDictionary, time.time()]:
                self.buffer.pop(-1)
        except:
            pass


        for bufferElement in self.buffer:
            if bufferElement[1] < time.time() - 0.2 and len(self.buffer) >= 2:
                self.buffer.remove(bufferElement)
                self.bufferUsed = 0
            else:
                break


    def draw(self):
        self.screen.fill((0, 0, 0))
        bufferedPlayers = self.buffer[0][0] # bufferedPlayers is a dictionary of all the players
        for playerAddr in bufferedPlayers:
            if playerAddr != self.network.clientConnection: # we don't want to draw our own player here
                if bufferedPlayers[playerAddr]: # if there is a player class there
                    if self.bufferUsed == 0:
                        pygame.draw.circle(self.screen, 'red', (bufferedPlayers[playerAddr].pos.x, bufferedPlayers[playerAddr].pos.y), bufferedPlayers[playerAddr].radius)
                        self.bufferUsed += 1
                    else:
                        # linear interpolate between the buffers position, and how many frames past the buffer we are.
                        #firstBufferPos = bufferedPlayers[playerAddr].pos
                        #nextBufferPos = self.buffer[1][0][playerAddr].pos
                        #nextBufferPos - firstBufferPos

                        #pygame.draw.circle(self.screen, 'red', bufferedPlayers[playerAddr].pos, bufferedPlayers[playerAddr].radius)
                        self.bufferUsed += 1
        pygame.draw.circle(self.screen, 'blue', (self.player.pos.x, self.player.pos.y), self.player.radius)

        pygame.display.flip()