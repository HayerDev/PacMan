import pygame
import random

class Ghost:
    def __init__(self, ghost_type, start_pos, maze):
        self.type = ghost_type
        #load the appropriate icon based off ghost typoe
        self.original_image = pygame.image.load(f'./icons/{self.type}.png')
        self.image = pygame.transform.scale(self.original_image, (26, 26))
        self.rect = self.image.get_rect(topleft=(500,35))
        self.maze = maze
        self.speed = 2
        self.direction = pygame.Vector2(random.choice([-1, 1]), 0)

    def update(self):
        #initiate direction change randomly
        #and check collisions
        if random.choice([True, False]):
            self.change_direction()

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        for y, row in enumerate(self.maze.layout):
            for x, cell in enumerate(row):
                if cell == 'X':
                    wall_rect = pygame.Rect(x * 32, y * 32, 32, 32)
                    if self.rect.colliderect(wall_rect):
                        self.change_direction()
                        break

    def change_direction(self):
        #stoichastic direction change
        if random.choice([True, False]):
            self.direction = pygame.Vector2(0, random.choice([-1, 1]))
        else:
            self.direction = pygame.Vector2(random.choice([-1, 1]), 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
