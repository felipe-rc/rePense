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
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
HEIGHT: int = 700
WIDTH: int = 700

# Set up the drawing window
display: Display = Display(WIDTH, HEIGHT)
screen = display.createScreen()
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 10000)

# Initialize Player
player: Player = Player()
screen.blit(player.surf, ((WIDTH * 3/4), HEIGHT - 70))

plasticBin: Bin = Bin(Material.PLASTIC, 'red', K_a)
paperBin: Bin = Bin(Material.PAPER, 'blue', K_a)
metalBin: Bin = Bin(Material.METAL, 'yellow', K_a)
glassBin: Bin = Bin(Material.GLASS, 'green', K_a)
trashList: dict = {
    Material.PLASTIC: list(),
    Material.PAPER: list(),
    Material.METAL: list(),
    Material.GLASS: list()
}


# Run until the user asks to quit
def main():
    running: bool = True
    createBasicScreen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                processKeyPress[event.key]()
            if event.type == TIMEREVENT:
                material: Material = Material.generateRandomMaterial()
                trashList[material].append(Trash(material, screen))
                print(trashList)
    # Done! Time to quit.
    pygame.quit()


def createBasicScreen():
    screen.blit(plasticBin.surf, ((WIDTH * 1/8), HEIGHT - 70))
    screen.blit(paperBin.surf, ((WIDTH * 2/8), HEIGHT - 70))
    screen.blit(metalBin.surf, ((WIDTH * 3/8), HEIGHT - 70))
    screen.blit(glassBin.surf, ((WIDTH * 4/8), HEIGHT - 70))
    pygame.display.flip()


# def closeGame():
#     running = False

processKeyPress: dict = {
    K_a: plasticBin.selectBin,
    K_s: paperBin.selectBin,
    K_d: metalBin.selectBin,
    K_f: glassBin.selectBin,
    # K_ESCAPE: closeGame,
}

if __name__ == "__main__":
    main()