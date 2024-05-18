# générateur de labyrinthe
# La première ligne du labyrinthe contient les informations pour lire la carte : 
# LIGNESxCOLS, caractère plein, vide, chemin, entrée et sortie du labyrinthe. 


import sys
import random

if len(sys.argv) < 3 or len(sys.argv[3]) < 5:
    print("params needed: height width characters")
else:
    height, width, chars = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    entry = random.randint(2, width - 3)
    first_exit = random.randint(2, width - 3)
    second_exit = random.randint(2, width - 3)
    print(f"{height}x{width}{sys.argv[3]}")
    for y in range(height):
        for x in range(width):
            if y == 0 and x == entry:
                print(chars[3], end="") # ENTREE
            elif y == height - 1 and x == first_exit:
                print(chars[4], end="") # SORTIE n°1
            elif y == second_exit and x == width - 1 :
                print(chars[4], end="") # SORTIE n°2
            elif 1 <= y <= height - 2 and 1 <= x <= width - 2 and random.randint(0, 99) > 20:
                print(chars[1], end="") # VIDE
            else:
                print(chars[0], end="") # PLEIN
        print()

#exemple = labyrinthe_generator.py 10 10 "#.o12"