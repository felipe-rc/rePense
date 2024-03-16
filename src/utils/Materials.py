from enum import Enum
from numpy import random

class Material(Enum):
    PAPER = 0
    PLASTIC = 1
    GLASS = 2
    METAL = 3


    def generateRandomMaterial():
        return Material(random.randint(3))
