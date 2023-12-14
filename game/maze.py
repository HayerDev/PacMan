import pygame

class Maze:
    def __init__(self):
        self.layout = [
            "XXXXXXXXXXXXXXXX",
            "X      X       X",
            "X XXXX XXX XXX X",
            "X X  X X   X X X",
            "X XXXX XXX XXX X",
            "X    X     X   X",
            "X XXXX X XXXX XX",
            "X X    X X    XX",
            "X XXXX XXX XXXXX",
            "X    X     X   X",
            "X XXXX X XXXXXX X",
            "X              X",
            "XXXXXXXXXXXXXXXX"
        ]

    def draw(self, screen):
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                if cell == "X":
                    color = (0, 0, 255)
                else:
                    color = (0, 0, 0 )

                pygame.draw.rect(screen, color, (x * 32, y * 32, 32, 32))

