#~~> MrRøølåÐe <~~#
# Créez un programme qui affiche la position de l’élément le plus en haut à gauche (dans l’ordre) d’une forme au sein d’un plateau.

import sys

def handle_error(user_value): 
    if len(user_value)!=3: 
        quit_program("veuillez rentrer deux noms de fichier svp")

def quit_program(message):
    sys.exit(message)

def read_board(name_of_file):
    board_coordinates = []
    try:
        with open(name_of_file, 'r') as f:
            for line  in f:
                line_array = [ x for x in line if x != "\n"]
                board_coordinates.append(line_array)
        return board_coordinates
    except :
        quit_program("le fichier 1 n'existe pas")

def read_pattern(name_of_file):
    pattern_coordinates = []
    try:
        with open(name_of_file, 'r') as f:
            for line in f:
                line_array = [ x for x in line.replace(" ","-") if x != "\n" ]
                pattern_coordinates.append(line_array)
        return pattern_coordinates
    except: 
        quit_program("le fichier 2 n'existe pas")

# Vérifie si le motif est présent dans le plateau à la position (x, y)
def check_pattern(board,pattern, x, y):
    for yp in range(len(pattern)):
        for xp in range(len(pattern[yp])):
            # Vérifie si la position du motif ne correspond pas à celle du plateau
            if pattern[yp][xp] != "-" and board[y + yp][x + xp] != pattern[yp][xp]:
                return False
    return True

# Trouve la position du motif dans le plateau
def find_pattern_position(board, pattern):
    for y in range(len(board)-len(pattern)+1):
        for x in range(len(board[y])-len(pattern[y])+1):
            if check_pattern(board, pattern, x, y):
                return x, y
    return None, None

# Vérifie si le motif est présent dans le plateau
def check_pattern_in_board(board,pattern):
    x, y = find_pattern_position(board, pattern)
    if x is not None and y is not None:
        print ("Trouvé", end = "\n")
        print (f'coordonnées : ({x}, {y})')
        display = display_pattern_in_board(board,pattern, x, y)
        return display  # Motif trouvé à la position (y, x)
    else:
        display = "PAS Trouvé"
        return display  # Motif non trouvé dans le tableau
    
# Construit une représentation du plateau avec le motif trouvé à la position (x, y)
def display_pattern_in_board(board,pattern, x, y):
    display = []
    for yb, row in enumerate(board):
        line = []
        for xb, _ in enumerate(row):# "_" est utilisé pour représenter une variable qui n'est pas utilisée dans le contexte
            # Vérifie si la position (x, y) se trouve dans la zone où le motif doit être affiché
            x_pattern =  x <= xb < x + max(len(row) for row in pattern)
            y_pattern =  y <= yb < y + len(pattern) 

            # Calcule les coordonnées relatives du motif par rapport au coin supérieur gauche du pattern
            if x_pattern and y_pattern :
                yp = yb - y
                xp = xb - x

                # Vérifie si la position se trouve dans les limites du motif et récupère le caractère correspondant
                if yp < len(pattern) and xp < len(pattern[yp]) and pattern[yp][xp] != "-" :
                    line.append(pattern[yp][xp])
                else:
                    line.append("-")
            else:
                line.append("-")

        line = "".join(line)
        display.append(line)
        
    display = "\n".join(display)
    return display

def main():
    name_of_file_board = sys.argv[1]
    name_of_file_pattern = sys.argv[2]
    handle_error(sys.argv)

    board_list = read_board(name_of_file_board)
    pattern_list = read_pattern(name_of_file_pattern)

    result = check_pattern_in_board(board_list,pattern_list)
    print(result)
   
if __name__ == "__main__":
    main()