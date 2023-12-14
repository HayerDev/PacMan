import pygame

class Maze:
    def __init__(self):
        self.layout = [
            "XXXXXXXXXXXXXXXXXX",
            "X      X         X",
            "X XXXX XXXX XXXX X",
            "X X  X X      X  X",
            "X X XXXX XXXX XXXX",
            "X X       X      X",
            "X XXXX XXXX XX X X",
            "X    X X    X  X X",
            "X XXXX X XXXX XXXX",
            "X    X X    X    X",
            "X XXXX XXXX XXXX X",
            "X                X",
            "XXXXXXXXXXXXXXXXXX"
        ]
        self.dots = self.draw_dots()

    def draw_dots(self):
        dots = []
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == ' ':
                    dots.append(pygame.Rect(x * 32 + 12, y * 32 + 12, 8, 8))
        return dots

    def draw(self, screen):
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == "X":
                    color = (0, 0, 255)
                else:
                    color = (0, 0, 0 )

                pygame.draw.rect(screen, color, (x * 32, y * 32, 32, 32))

            for dot in self.dots:
                pygame.draw.rect(screen, (255, 255, 255), dot)