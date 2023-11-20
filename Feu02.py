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
            print(pattern_coordinates)
        return pattern_coordinates
    except: 
        quit_program("le fichier 2 n'existe pas")

def check_pattern(board,pattern, x, y):
    for yp in range(len(pattern)):
        for xp in range(len(pattern[yp])):
            if pattern[yp][xp] != "-" and board[y + yp][x + xp] != pattern[yp][xp]:
                return False
    return True
           
def find_pattern_position(board, pattern):
    for y in range(len(board)-len(pattern)+1):
        for x in range(len(board[y])-len(pattern[y])+1):
            if check_pattern(board, pattern, x, y):
                return x, y
    return None, None

def display_result(result, x, y, board, pattern):
    if result:
        print ("Trouvé", end = "\n")
        print (f'coordonnées : ({x}, {y})')
        display = display_pattern_in_board(board,pattern, x, y)
        print (display)
        return True  # Motif trouvé à la position (y, x)
    else:
        print ("PAS Trouvé", end = "\n")
        return False  # Motif non trouvé dans le tableau 
    
def display_pattern_in_board(board,pattern, x, y):
    display = []
    for yb in range(len(board)):
        line = []
        for xb in range(len(board[yb])):
            if  x <= xb < x + max(len(row) for row in pattern) and y <= yb < y +len(pattern) :
                yp = yb - y
                xp = xb - x
                if yp < len(pattern) and xp < len(pattern[yp]):
                    if pattern[yp][xp] != "-" :
                        line.append(pattern[yp][xp])
                    else:
                        line.append("-")
                else:
                    line.append("-")
            else:
                line.append("-")
        line = "".join(line)
        display.append(line)
    display = "\n".join(display)
    return display

def check_pattern_in_board(board,pattern):
    x, y = find_pattern_position(board, pattern)
    display_result(x is not None and y is not None, x, y,board,pattern)
    return x is not None and y is not None

def main():
    name_of_file_board = sys.argv[1]
    name_of_file_pattern = sys.argv[2]
    handle_error(sys.argv)

    board_list = read_board(name_of_file_board)
    pattern_list = read_pattern(name_of_file_pattern)

    result = check_pattern_in_board(board_list,pattern_list)
   

if __name__ == "__main__":
    main()