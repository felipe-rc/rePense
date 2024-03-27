from dataclasses import dataclass
from utils.Materials import Material
from utils.constants import BIN_SPRITES
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
        self.surf = pygame.image.load(BIN_SPRITES[self.material]).convert()

    def selectBin(self):
        print(f'Selecionada a lixeira de tipo: {self.material}!')
        self.selected = True
