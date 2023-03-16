import pygame

from game import Game

game = Game(400, 400)

while game.gameRunning:
    game.update()
    game.draw()

pygame.quit()

print("Game closed")