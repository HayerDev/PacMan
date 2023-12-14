import pygame
from game.player import Player
from game.ghost import Ghost
from game.maze import Maze

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Adjust as needed
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load('sound/retroarcadeTrimmed.mp3')
        self.eat_sound = pygame.mixer.Sound('sound/pacmanEatingTrimmed.mp3')
        # Loop background theme forever, but you'll probably lose before then!
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.running = True
        self.maze = Maze()
        self.player = Player()
        self.ghosts = [Ghost('blinky',  self.maze),
                       Ghost('pinky',  self.maze),
                       Ghost('inky',  self.maze),
                       Ghost('clyde',  self.maze)
                      ]
        self.score = 0

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            self.maze.draw(self.screen)
            self.player.update(self.maze)
            self.player.draw(self.screen)

            self.check_dot_collision()

            for ghost in self.ghosts:
                ghost.update()
                ghost.draw(self.screen)
                if self.player.rect.colliderect(ghost.rect):
                    #print humiliating msg and exit game
                    print(f"Ha, you lose! Final Score: {self.score}")
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def check_dot_collision(self):
        for dot in self.maze.dots[:]:
            if self.player.rect.colliderect(dot):
                self.maze.dots.remove(dot)
                self.eat_sound.play()
                self.score += 1


if __name__ == "__main__":
    game = Game()
    game.run()
