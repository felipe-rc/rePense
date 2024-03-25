import pygame
from display.Display import Display
from binClass.Bins import Bin
from utils.Materials import Material
from playerClass.Player import Player
from trashClass.Trash import Trash
from pygame.locals import (
    K_a,
    K_s,
    K_d,
    K_f,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONUP
)

pygame.init()
HEIGHT: int = 700
WIDTH: int = 700

# Initialize Player
player: Player = Player()


# Set up the drawing window
display: Display = Display(WIDTH, HEIGHT)
screen = display.createScreen()
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, (10000 - (player.health * 100)))

screen.blit(player.surf, ((WIDTH * 3/4), HEIGHT - 70))
plasticBin: Bin = Bin(Material.PLASTIC, 'red', K_a)
paperBin: Bin = Bin(Material.PAPER, 'blue', K_s)
metalBin: Bin = Bin(Material.METAL, 'yellow', K_d)
glassBin: Bin = Bin(Material.GLASS, 'green', K_f)
trashList: list = list()


# Run until the user asks to quit
def main():
    selectedBin: Bin = plasticBin
    running: bool = True
    createBasicScreen()
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                selectedBin = processKeyPress[event.key]
            if event.type == MOUSEBUTTONUP:
                processClick(event, selectedBin)
            if event.type == TIMEREVENT:
                trashProcess()
                material: Material = Material.generateRandomMaterial()
                trashList.append(Trash(material, screen))
                print(trashList)
    pygame.quit()


def createBasicScreen():
    screen.blit(plasticBin.surf, ((WIDTH * 1/8), HEIGHT - 70))
    screen.blit(paperBin.surf, ((WIDTH * 2/8), HEIGHT - 70))
    screen.blit(metalBin.surf, ((WIDTH * 3/8), HEIGHT - 70))
    screen.blit(glassBin.surf, ((WIDTH * 4/8), HEIGHT - 70))
    pygame.display.flip()


def trashProcess():
    for trash in trashList:
        trash.tick(player, screen)
    pygame.display.flip()


def processClick(event, selectedBin):
    for trash in trashList:
        if trash.rect.collidepoint(event.pos):
            if selectedBin.material == trash.material:
                auxSurf = pygame.Surface((32, 32))
                auxSurf.fill((0, 0, 0, 0))
                screen.blit(auxSurf, (trash.xPosition, trash.yPosition))
                trashList.remove(trash)
                pygame.display.flip()
                player.addPoint()
            else:
                player.removePoint()
    pygame.time.set_timer(TIMEREVENT, 10000 - player.health * 200)


processKeyPress: dict = {
    K_a: plasticBin,
    K_s: paperBin,
    K_d: metalBin,
    K_f: glassBin,
}

if __name__ == "__main__":
    main()
