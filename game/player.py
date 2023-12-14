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
        self.move(maze)

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

    def move(self, maze):
        #lateral
        self.rect.x += self.direction.x * self.speed
        self.check_collision(maze, self.direction.x, 0)

        #vert
        self.rect.y += self.direction.y * self.speed
        self.check_collision(maze, 0, self.direction.y)

    def check_collision(self, maze, dx, dy):
        #look at each cell
        for y, row in enumerate(maze.layout):
            for x, cell in enumerate(row):
                if cell == 1:
                    wall_rect = pygame.Rect(x * 32, y * 32, 32, 32)
                    #movements wall hits
                    if self.rect.colliderect(wall_rect):
                        if dx > 0:
                            self.rect.right = wall_rect.left
                        if dx < 0:
                            self.rect.left = wall_rect.right
                        if dy > 0:
                            self.rect.bottom = wall_rect.top
                        if dy < 0:
                            self.rect.top = wall_rect.bottom

    def draw(self, screen):
        screen.blit(self.image, self.rect)
