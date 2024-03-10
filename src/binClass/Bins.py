from dataclasses import dataclass
from utils.Materials import Material
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
        print(f'Selecionada a lixeira de tipo: {self.material}!')
        self.selected = True
