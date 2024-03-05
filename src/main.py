# Simple pygame program

# Import and initialize the pygame library
import pygame
from display.Display import Display
from bins.Bins import Bin
from bins.Materials import Material
from pygame.locals import (
    K_a,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Set up the drawing window
display: Display = Display(700, 700)
screen = display.createScreen()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    binTest: Bin = Bin(Material.PLASTIC, 'red', K_a)
    screen.blit(binTest.surf, (700/2, 700/2))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                binTest.selectBin()
            if event.key == K_ESCAPE:
                running = False

# Done! Time to quit.
pygame.quit()