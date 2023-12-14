import pygame

class Maze:
    def __init__(self):
        self.layout = [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "X            X           X             X",
            "X XXXX XXXX XXX XXXX XXXX XXXX XXXX XX X",
            "X X  X X  X X   X  X X   X X  X X  X X X",
            "X XXXX XXXX XXX XXXX XXXX X XXXX XXXX X",
            "X        X       X        X           X",
            "X XXXX XXXX X XXXXXX X XXXX XXXXXX XXXX",
            "X   XX X    X       X X    X X       XX",
            "XXX XX XXXX XXXXXX   XXXXXX X XXXXXXXXX",
            "X      X    X       X X    X X        X",
            "X XXXXXX XX XXXX X X XXXXXX X XXXXXXX X",
            "X        X      X X       X X        X",
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

