from dataclasses import dataclass
from utils.Materials import Material
from binClass.Bins import Bin
from playerClass.Player import Player
from numpy import random
import pygame

HEIGHT: int = 700
WIDTH: int = 700

@dataclass
class Trash(pygame.sprite.Sprite):
    xPosition: int
    material: Material
    yPosition: int = 0

    def __init__(self, material, screen):
        self.surf = pygame.Surface((32, 32))
        self.surf.fill((255, 255, 255))
        self.xPosition = random.randint(32, WIDTH - 32)
        screen.blit(self.surf, (self.xPosition, self.yPosition))
        pygame.display.flip()
        self.material = material


    def onClick(self, selectedBin: Bin, player: Player):
        if (selectedBin.material == self.material):
            self.purge()
        else:
            player.removePoint()
    

    def tick(self, player: Player):
        if (self.yPosition < HEIGHT):
            self.yPosition += 1
            return
        player.removePoint()
        self.purge()


    def purge(self):
        self.kill()
