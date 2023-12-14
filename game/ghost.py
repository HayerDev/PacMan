import pygame
import random

class Ghost:
    def __init__(self, ghost_type, start_pos, maze):
        self.type = ghost_type
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect(topleft=start_pos)
        self.maze = maze
        self.speed = 2
        self.direction = pygame.Vector2(random.choice([-1, 1]), 0)

    def change_direction(self):
        #stoichastic direction change
        if random.choice([True, False]):
            self.direction = pygame.Vector2(0, random.choice([-1, 1]))
        else:
            self.direction = pygame.Vector2(random.choice([-1, 1]), 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
