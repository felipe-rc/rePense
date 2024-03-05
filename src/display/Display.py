import pygame
from dataclasses import dataclass

@dataclass
class Display:
    width: int = 1920
    height: int = 1080
    background: tuple = (0, 0, 0)

    def createScreen(self):
        screen: pygame.display = pygame.display.set_mode([self.width, self.height])
        screen.fill(self.background)
        return screen
