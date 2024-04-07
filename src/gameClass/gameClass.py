from dataclasses import dataclass
import pygame
from binClass.Bins import Bin
from utils.Materials import Material
from playerClass.Player import Player
from trashClass.Trash import Trash
from model.model import Model
from utils.constants import WIDTH, HEIGHT
from pygame.locals import (
    K_a,
    K_s,
    K_d,
    K_f,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONUP
)


@dataclass
class Game:

    def __init__(self, screen):
        self.screen = screen
        pygame.display.update()
        # Initialize Player
        self.player: Player = Player()
        # Initialize Model
        self.model: Model = Model()
        self.TIMEREVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMEREVENT, (10000 - (self.player.health * 100)))

        self.plasticBin: Bin = Bin(Material.PLASTIC, 'red', K_a)
        self.paperBin: Bin = Bin(Material.PAPER, 'blue', K_s)
        self.metalBin: Bin = Bin(Material.METAL, 'yellow', K_d)
        self.glassBin: Bin = Bin(Material.GLASS, 'green', K_f)
        self.trashList: list = list()
        self.processKeyPress: dict = {
            K_a: self.plasticBin,
            K_s: self.paperBin,
            K_d: self.glassBin,
            K_f: self.metalBin,
        }
        self.highScore: int = 20
        self.selectedBin: Bin = self.plasticBin

    def start(self):
        running: bool = True
        self.createBasicScreen()
        while running:
            if self.player.health <= 0:
                running = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    self.selectedBin = self.processKeyPress[event.key]
                if event.type == MOUSEBUTTONUP:
                    self.processClick(event, self.selectedBin, self.highScore)
                if event.type == self.TIMEREVENT:
                    self.trashProcess()
                    material: Material = Material.generateRandomMaterial()
                    self.trashList.append(Trash(material, self.screen))
        self.savePoints(self.highScore)
        pygame.quit()

    def createBasicScreen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.surf, ((WIDTH * 3 / 4), HEIGHT - 70))
        self.screen.blit(self.plasticBin.surf, ((WIDTH * 1 / 8), HEIGHT - 70))
        self.screen.blit(self.paperBin.surf, ((WIDTH * 2 / 8), HEIGHT - 70))
        self.screen.blit(self.metalBin.surf, ((WIDTH * 3 / 8), HEIGHT - 70))
        self.screen.blit(self.glassBin.surf, ((WIDTH * 4 / 8), HEIGHT - 70))
        pygame.display.flip()

    def trashProcess(self):
        for trash in self.trashList:
            trash.tick(self.player, self.screen)
        pygame.display.flip()

    def processClick(self, event, selectedBin, highScore):
        for trash in self.trashList:
            if trash.rect.collidepoint(event.pos):
                if selectedBin.material == trash.material:
                    auxSurf = pygame.Surface((32, 32))
                    auxSurf.fill((0, 0, 0, 0))
                    self.screen.blit(auxSurf, (trash.xPosition, trash.yPosition))
                    self.trashList.remove(trash)
                    pygame.display.flip()
                    self.player.addPoint()
                    if self.player.health > highScore:
                        highScore = self.player.health
                else:
                    self.player.removePoint()
        pygame.time.set_timer(self.TIMEREVENT, 10000 - self.player.health * 200)

    def savePoints(self, highScore):
        self.model.savePoints(highScore)
