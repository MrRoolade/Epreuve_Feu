#~~> MrRøølåÐe <~~#

# Trouver le plus grand carré
# Créez un programme qui remplace les caractères vides par des caractères plein pour 
# représenter le plus grand carré possible sur un plateau.
# Le plateau sera transmis dans un fichier.
# La première ligne du fichier contient les informations pour lire la carte : 
#   nombre de lignes du plateau, caractères pour “vide”, “obstacle” et “plein”.

import sys

def handle_error(user_value): 
    if len(user_value)!=2: 
        quit_program("veuillez rentrer un nom de fichier svp")

def quit_program(message):
    sys.exit(message)

def read_board(name_of_file):
    board = []
    try:
        with open(name_of_file, 'r') as f:
            for line  in f:
                line_array = list(line.rstrip())
                board.append(line_array)
            first_line = board.pop(0)
        return board, first_line
    except :
        quit_program("le fichier n'existe pas")

def check_board(board,first_line):
    for line in board:
        for char in line:
            if char not in first_line[1:-1]:
                quit_program("au moins un caractère n'est pas valide")
        
    expected_lenght=len(board[0])
    for line in board:
        if len(line) != expected_lenght or len(board) == 0:
            quit_program("le plateau n'est pas valide")
    return

def create_square(size, empty_car): 
    return [[empty_car] * size for _ in range(size)]

# Vérifie si le carré est présent dans le plateau à la position (x, y)
def check_pattern(board,square, x, y):
    for yp in range(len(square)):
        for xp in range(len(square[yp])):
            # Vérifie si la position du motif ne correspond pas à celle du plateau
            if board[y + yp][x + xp] != square[yp][xp]:
                return False
    return True

# Trouve la position du motif dans le plateau
def find_pattern_position(board, square):
    for y in range(len(board)-len(square)+1):
        for x in range(len(board[y])-len(square[0])+1):
            if check_pattern(board, square, x, y):
                return x, y
    return None, None

# Vérifie si le motif est présent dans le plateau
def check_pattern_in_board(board,square):
    x, y = find_pattern_position(board, square)
    if x is not None and y is not None:
        return True , x , y
    else:
        return False

def replace_car_in_square(square, full_car):
    for line in square:
        for i in range(len(line)):
            line[i] = full_car
    return square

# Construit une représentation du plateau avec le motif trouvé à la position (x, y)
def display_pattern_in_board(board,square,x,y,full_car):
    if x is None and y is None:
        return "carré non trouvé"
    
    new_square = replace_car_in_square(square,full_car)
    display = []
    for yb, row in enumerate(board):
        line = []
        for xb, char in enumerate(row):
            # Vérifie si la position (x, y) se trouve dans la zone où le motif doit être affiché
            x_pattern_exist =  x <= xb < x + max(len(row) for row in new_square)
            y_pattern_exist =  y <= yb < y + len(new_square) 

            # Calcule les coordonnées relatives du motif par rapport au coin supérieur gauche du square
            if x_pattern_exist and y_pattern_exist :
                yp = yb - y
                xp = xb - x
                line.append(new_square[yp][xp])
            else:
                line.append(char)

        display.append("".join(line))
    return "\n".join(display)


def main():
    handle_error(sys.argv)
    name_of_file_board = sys.argv[1]
    board_list , first_line = read_board(name_of_file_board)
    empty_car = first_line[1]
    full_car = first_line[-1]

    check_board(board_list, first_line)
    side_square = min(len(board_list), len(board_list[0]))
    
    actual_square = None
    for i in range(side_square,0,-1):
        actual_square = create_square(i,empty_car)
        if check_pattern_in_board(board_list,actual_square):
            break
        
    if actual_square:
        _,x,y = check_pattern_in_board(board_list,actual_square)
        result = display_pattern_in_board(board_list,actual_square,x,y,full_car)
        print(result)
   
if __name__ == "__main__":
    main()