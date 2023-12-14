import pygame
from player import Player
from maze import Maze

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))  # Adjust as needed
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.maze = Maze()


if __name__ == "__main__":
    game = Game()