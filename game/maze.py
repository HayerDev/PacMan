import pygame

class Maze:
    def __init__(self):
        self.layout = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "X             x            x            X",
            "X XXXX XXXX XXXX XXXX XXXXXXXX XXXX XX X",
            "X X  X X  X X  X X  X X      X X  X X X",
            "X XXXX XXXX XXXX XXXX XXXXXX X XXXX X X",
            "X        X        X         X        X",
            "X XXXX XXXXXX X XXXXXX X XXXX XXXXXX XX",
            "X   XX X      X      X X    X X      XX",
            "XXX XX XXXXXX XXXXXX   XXXXXX X XXXXXX",
            "X      X    X      X X X    X X      X",
            "X XXXXXX XX XXXX X X XXXXXX X XXXXXX X",
            "X        X      X X      X X X      X",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        ]

    def draw(self, screen):
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == "X":
                    color = (0, 0, 255)
                else:
                    color = (0, 0, 0 )

                pygame.draw.rect(screen, color, (x * 32, y * 32, 32, 32))

