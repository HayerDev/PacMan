import pygame
class Player:
    def __init__(self):
        # Initialize player properties
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.speed = 3
        self.direction = pygame.Vector2(0, 0)

    def update(self, maze):
        self.handle_keys()

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction = pygame.Vector2(-1, 0)
        elif keys[pygame.K_d]:
            self.direction = pygame.Vector2(1, 0)
        elif keys[pygame.K_w]:
            self.direction = pygame.Vector2(0, -1)
        elif keys[pygame.K_s]:
            self.direction = pygame.Vector2(0, 1)

