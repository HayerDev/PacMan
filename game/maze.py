import pygame

class Maze:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.layout = MazeGen()
        