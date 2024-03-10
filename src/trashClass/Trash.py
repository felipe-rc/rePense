from dataclasses import dataclass
from utils.Materials import Material
from binClass.Bins import Bin
from playerClass.Player import Player
import pygame

@dataclass
class Trash(pygame.sprite.Sprite):
    material: Material
    surf = pygame.Surface((32, 32))
    surf.fill((255, 255, 255))


    def onClick(self, selectedBin: Bin, player: Player):
        if (selectedBin.material == self.material):
            self.purge()
        else:
            player.removePoint()


    def purge(self):
        self.kill()
