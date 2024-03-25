from dataclasses import dataclass
import pygame
from utils.constants import COLORS


@dataclass
class Player(pygame.sprite.Sprite):
    health: int = 20
    surf = pygame.Surface((64, 64))
    surf.fill(COLORS['mix'])

    def removePoint(self):
        self.health -= 1

    def addPoint(self):
        self.health += 1
