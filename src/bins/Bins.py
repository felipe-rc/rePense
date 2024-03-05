from dataclasses import dataclass
from bins.Materials import Material
import pygame

@dataclass
class Bin(pygame.sprite.Sprite):
    material: Material
    color: str
    key: str
    selected: bool = False
    surf = pygame.Surface((64, 64))
    surf.fill((255, 255, 255))

    def selectBin(self):
        print('Selecionada!')
        self.selected = True
