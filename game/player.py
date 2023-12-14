class Player:
    def __init__(self):
        # Initialize player properties
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.speed = 3
        self.direction = pygame.Vector2(0, 0)


