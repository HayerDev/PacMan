import pygame
import random

class Ghost:
    def __init__(self, ghost_type, maze):
        self.type = ghost_type
        # load the appropriate icon based off ghost typoe
        self.original_image = pygame.image.load(f'./icons/{self.type}.png')
        self.image = pygame.transform.scale(self.original_image, (26, 26))
        self.maze = maze
        self.speed = 2
        self.direction = random.choice([pygame.Vector2(1, 0), pygame.Vector2(-1, 0),
                                        pygame.Vector2(0, 1), pygame.Vector2(0, -1)])
        self.rect = self.image.get_rect(topleft=self.find_random_position())

    def find_random_position(self):
        while True:
            x = random.randint(0, len(self.maze.layout[0]) - 1)
            y = random.randint(0, len(self.maze.layout) - 1)
            if self.maze.layout[y][x] == ' ':
                return x * 32, y * 32

    def update(self):
        next_rect = self.rect.move(self.direction.x * self.speed, self.direction.y * self.speed)
        for y, row in enumerate(self.maze.layout):
            for x, cell in enumerate(row):
                if cell == 'X':
                    wall_rect = pygame.Rect(x * 32, y * 32, 32, 32)
                    if next_rect.colliderect(wall_rect):
                        self.change_direction()
                        return

        self.rect = next_rect

    def change_direction(self):
        directions = [pygame.Vector2(1, 0), pygame.Vector2(-1, 0),
                      pygame.Vector2(0, 1), pygame.Vector2(0, -1)]
        #dont allow reverse
        directions.remove(-self.direction)
        self.direction = random.choice(directions)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

