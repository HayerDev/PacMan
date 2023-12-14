import pygame
from game.player import Player
from game.ghost import Ghost
from game.maze import Maze

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Adjust as needed
        self.clock = pygame.time.Clock()
        self.running = True
        self.maze = Maze()
        self.player = Player()
        self.ghosts = [Ghost('blinky', (100, 100), self.maze),
                       Ghost('pinky', (200, 100), self.maze),
                       Ghost('inky', (300, 100), self.maze),
                       Ghost('clyde', (400, 100), self.maze)
                      ]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            self.maze.draw(self.screen)
            self.player.update(self.maze)
            self.player.draw(self.screen)

            for ghost in self.ghosts:
                ghost.update()
                ghost.draw(self.screen)
                if self.player.rect.colliderect(ghost.rect):
                    #print humiliating msg and exit game
                    print("Ha, you lose!")
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
