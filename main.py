import pygame
from game.player import Player
from game.ghost import Ghost
from game.maze import Maze

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600)) # ADjust as needed
        pygame.mixer.init()
        self.background_music = pygame.mixer.music.load('sound/retroarcadeTrimmed.mp3')
        self.eat_sound = pygame.mixer.Sound('sound/pacmanEatingTrimmed.mp3')
        # Loop background theme forever, but you'll probably lose before then!
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.maze = Maze()
        self.player = Player()
        self.ghosts = [Ghost('blinky', self.maze),
                       Ghost('pinky', self.maze),
                       Ghost('inky', self.maze),
                       Ghost('clyde', self.maze)]
        self.score = 0
        #added states
        self.state = "menu"

    def run(self):
        while True:
            if self.state == "menu":
                self.show_menu()
            elif self.state == "running":
                self.run_game()
            elif self.state == "game_over":
                self.show_game_over()

    def show_menu(self):
        while self.state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.collidepoint(event.pos):
                        self.state = "running"

            self.screen.fill((0, 0, 0))
            self.play_button = pygame.draw.rect(self.screen, (0, 255, 0), (300, 250, 200, 100))
            self.draw_text("Play", 40, (255, 255, 255), self.play_button.center)

            pygame.display.flip()
            self.clock.tick(60)

    def run_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

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
                self.state = "game_over"

        pygame.display.flip()
        self.clock.tick(60)

    def show_game_over(self):
        while self.state == "game_over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.replay_button.collidepoint(event.pos):
                        self.reset_game()
                        self.state = "running"
                    elif self.exit_button.collidepoint(event.pos):
                        pygame.quit()
                        return

            self.screen.fill((0, 0, 0))
            self.draw_text(f"Final Score: {self.score}", 40, (255, 255, 255), (400, 200))
            self.replay_button = pygame.draw.rect(self.screen, (0, 255, 0), (300, 300, 200, 50))
            self.exit_button = pygame.draw.rect(self.screen, (255, 0, 0), (300, 400, 200, 50))
            self.draw_text("Replay", 30, (255, 255, 255), self.replay_button.center)
            self.draw_text("Exit", 30, (255, 255, 255), self.exit_button.center)

            pygame.display.flip()
            self.clock.tick(60)

    def reset_game(self):
        self.player = Player()
        self.ghosts = [Ghost('blinky', self.maze),
                       Ghost('pinky', self.maze),
                       Ghost('inky', self.maze),
                       Ghost('clyde', self.maze)]
        self.score = 0

    def draw_text(self, text, size, color, position):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)

    def check_dot_collision(self):
        for dot in self.maze.dots[:]:
            if self.player.rect.colliderect(dot):
                self.maze.dots.remove(dot)
                self.eat_sound.play()
                self.score += 1
                if not self.maze.dots:
                    self.state = "game_over"


if __name__ == "__main__":
    game = Game()
    game.run()
