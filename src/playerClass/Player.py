from dataclasses import dataclass
import pygame

@dataclass
class Player(pygame.sprite.Sprite):
    health: int
    surf = pygame.Surface((64, 64))
    surf.fill((255, 255, 255))


    def removePoint(self):
        self.health = self.health - 1