from utils.Materials import Material

COLORS: dict = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'mix': (125, 125, 125)
}

TRASH_COLORS: dict = {
    Material.PLASTIC: (255, 0, 0),
    Material.PAPER: (0, 0, 255),
    Material.METAL: (0, 255, 0),
    Material.GLASS: (255, 255, 0),
}

BIN_SPRITES: dict = {
    Material.PLASTIC: 'assets/sprites/plasticBin.png',
    Material.PAPER: 'assets/sprites/paperBin.png',
    Material.METAL: 'assets/sprites/metalBin.png',
    Material.GLASS: 'assets/sprites/glassBin.png'
}

HEIGHT: int = 700
WIDTH: int = 700
