#~~> MrRøølåÐe <~~#
# Créez un programme qui affiche la position de l’élément le plus en haut à gauche (dans l’ordre) d’une forme au sein d’un plateau.

import sys

def handle_error(user_value): 
    if len(user_value)!=3: 
        quit_program("veuillez rentrer deux noms de fichier svp")

def quit_program(message):
    sys.exit(message)

def define_map_board_list(name_of_file):
    board_coordinates = []
    with open(name_of_file, 'r') as f:
        for line  in f:
            line_array = [ x for x in line if x != "\n"]
            board_coordinates.append(line_array)
    return board_coordinates

def define_map_pattern_list(name_of_file):
    pattern_coordinates = []
    with open(name_of_file, 'r') as f:
        for line in f:
            line_array = [ x for x in line if x != "\n"  ]
            pattern_coordinates.append(line_array)
    return pattern_coordinates

def find_pattern_position(board, pattern):
    for y in range(len(board)-len(pattern)+1):
        for x in range(len(board[y])-len(pattern[y])+1):
            if check_pattern(board, pattern, x, y):
                return x, y
    return None, None

def check_pattern(board,pattern, x, y):
    for yp in range(len(pattern)):
        for xp in range(len(pattern[yp])):
            if pattern[yp][xp] != " " and board[y + yp][x + xp] != pattern[yp][xp]:
                return False
    return True
           
def display_result(result, x, y):
    if result:
        print ("Trouvé", end = "\n")
        print (f'coordonnées : ({x}, {y})')

        return True  # Motif trouvé à la position (y, x)
    else:
        print ("PAS Trouvé", end = "\n")
        return False  # Motif non trouvé dans le tableau 
    
def check_pattern_in_board(board,pattern):
    x, y = find_pattern_position(board, pattern)
    display_result(x is not None and y is not None, x, y)
    return x is not None and y is not None

def main():
    handle_error(sys.argv)
    name_of_file_board = "board.txt"
    name_of_file_pattern = "to_find.txt"

    board_list = define_map_board_list(name_of_file_board)
    pattern_list = define_map_pattern_list(name_of_file_pattern)

    result = check_pattern_in_board(board_list,pattern_list)
   

if __name__ == "__main__":
    main()