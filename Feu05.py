#~~> MrRøølåÐe <~~#

# Créez un programme qui trouve le plus court chemin entre
#  l’entrée et la sortie d’un labyrinthe en évitant les obstacles.

# Le labyrinthe est transmis en argument du programme.
#  La première ligne du labyrinthe contient les informations pour lire la carte : LIGNESxCOLS, caractère plein, vide, chemin, entrée et sortie du labyrinthe. 

# Le but du programme est de remplacer les caractères “vide” par des caractères “chemin” pour représenter le plus court chemin pour traverser le labyrinthe.
#  Un déplacement ne peut se faire que vers le haut, le bas, la droite ou la gauche.
# 

# TO DO : trouver le depart
# fonction de lecture de posibilité autour d'une case
# choisir un chemin
# fonction ou condition de fin de la récursivité 


import sys

def handle_error(user_value): 
    if len(user_value)!=2: 
        quit_program("veuillez rentrer un nom de fichier svp")

def quit_program(message):
    sys.exit(message)

def read_board(name_of_file):
    map = []
    try:
        with open(name_of_file, 'r') as f:
            for line  in f:
                line_array = list(line.rstrip())
                map.append(line_array)
            first_line = map.pop(0)
        return map, first_line
    except :
        quit_program("le fichier n'existe pas")

def check_board(board,first_line):
    valid_car = set(first_line[-5:])
    size="".join(first_line[:-5])
    expected_size = tuple(map(int, size.split('x')))
    expected_lenght , expected_height = expected_size

    for line in board:
        if len(line) != expected_lenght :
            quit_program("le plateau n'est pas valide")
        for char in line:
            if char not in valid_car:
                quit_program("au moins un caractère n'est pas valide")
        
    if len(board) != expected_height:
        quit_program("le plateau n'est pas valide")

    return

def find_entry(board, entry_car):
    for y,line in enumerate(board):
        for x, car in enumerate(line):
            if car == entry_car:
                return x, y    
    return None

def main():
    handle_error(sys.argv)
    name_of_file_board = sys.argv[1]
    board_list , first_line = read_board(name_of_file_board)
    full_car = first_line[-5]
    empty_car = first_line[-4]
    path_car = first_line[-3]
    entry_car = first_line[-2]
    exit_car = first_line[-1]

    check_board(board_list, first_line)   

    x,y = find_entry(board_list,entry_car) 
    print(x)
    print(y)
    for line in board_list:
        print("".join(line))

if __name__ == "__main__":
    main()