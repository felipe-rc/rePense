from dataclasses import dataclass
from utils.Materials import Material
from playerClass.Player import Player
from numpy import random
import pygame

from utils.constants import WIDTH, HEIGHT, TRASH_COLORS


@dataclass
class Trash(pygame.sprite.Sprite):
    material: Material
    xPosition: int
    yPosition: int = 0

    def __init__(self, material, screen):
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect()
        self.surf.fill(TRASH_COLORS[material])
        self.xPosition = random.randint(32, (int(WIDTH / 2) - 32))
        self.rect.x = self.xPosition
        self.rect.y = self.yPosition
        screen.blit(self.surf, (self.xPosition, self.yPosition))
        pygame.display.flip()
        self.material = material

    def tick(self, player: Player, screen):
        if self.yPosition < HEIGHT - 64:
            auxSurf = pygame.Surface((32, 32))
            auxSurf.fill((0, 0, 0, 0))
            screen.blit(auxSurf, (self.xPosition, self.yPosition))
            self.yPosition += 37
            self.rect = self.surf.get_rect()
            self.rect.x = self.xPosition
            self.rect.y = self.yPosition
            screen.blit(self.surf, (self.xPosition, self.yPosition))
            return
        player.removePoint()
