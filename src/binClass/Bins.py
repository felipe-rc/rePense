from dataclasses import dataclass
from utils.Materials import Material
from utils.constants import COLORS
import pygame

@dataclass
class Bin(pygame.sprite.Sprite):
    material: Material
    color: str
    key: str
    selected: bool = False
    
    def __init__(self, material, color, key):
        self.material = material
        self.color = color
        self.key = key
        self.surf = pygame.Surface((64, 64))
        self.surf.fill(COLORS[self.color])

    def selectBin(self, selectedBin):
        print(f'Selecionada a lixeira de tipo: {self.material}!')
        self.selected = True
        selectedBin = self
