from dataclasses import dataclass
from utils.Materials import Material
from playerClass.Player import Player
from numpy import random
import pygame

HEIGHT: int = 700
WIDTH: int = 350


@dataclass
class Trash(pygame.sprite.Sprite):
    material: Material
    xPosition: int
    yPosition: int = 0

    def __init__(self, material, screen):
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect()
        self.surf.fill((255, 255, 255))
        self.xPosition = random.randint(32, WIDTH - 32)
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
            self.yPosition += 16
            self.rect = self.surf.get_rect()
            self.rect.x = self.xPosition
            self.rect.y = self.yPosition
            screen.blit(self.surf, (self.xPosition, self.yPosition))
            return
        player.removePoint()
