# Simple pygame program

# Import and initialize the pygame library
import pygame
from display.Display import Display
from binClass.Bins import Bin
from utils.Materials import Material
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

# Run until the user asks to quit
running = True
while running:    
    plasticBin: Bin = Bin(Material.PLASTIC, 'red', K_a)
    screen.blit(plasticBin.surf, ((WIDTH * 4/6) + 64, HEIGHT - 64))
    paperBin: Bin = Bin(Material.PAPER, 'blue', K_a)
    screen.blit(paperBin.surf, ((WIDTH * 3/6) + 64, HEIGHT - 64))
    metalBin: Bin = Bin(Material.METAL, 'yellow', K_a)
    screen.blit(metalBin.surf, ((WIDTH * 2/6) + 64, HEIGHT - 64))
    glassBin: Bin = Bin(Material.GLASS, 'green', K_a)
    screen.blit(plasticBin.surf, ((WIDTH * 1/6) + 64, HEIGHT - 64))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_a:
                plasticBin.selectBin()
            if event.key == K_s:
                paperBin.selectBin()
            if event.key == K_d:
                metalBin.selectBin()
            if event.key == K_f:
                glassBin.selectBin()
            if event.key == K_ESCAPE:
                running = False

# Done! Time to quit.
pygame.quit()
