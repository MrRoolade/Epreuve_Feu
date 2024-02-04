#~~> MrRøølåÐe <~~#

# Trouver le plus grand carré
# Créez un programme qui remplace les caractères vides par des caractères plein pour 
# représenter le plus grand carré possible sur un plateau.
# Le plateau sera transmis dans un fichier.
# La première ligne du fichier contient les informations pour lire la carte : 
#   nombre de lignes du plateau, caractères pour “vide”, “obstacle” et “plein”.

#TO DO
#check la première ligne du plateau et intégrer les différents caractères
#les caractères présents dans la carte sont uniquement ceux de la première ligne 

import sys

def handle_error(user_value): 
    if len(user_value)!=2: 
        quit_program("veuillez rentrer un nom de fichier svp")

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
        quit_program("le fichier n'existe pas")

def check_board(board):
    for line in board:
        lg=len(line)
        if len(line) != lg or len(board) == 0:
            quit_program("le plateau n'est pas valide")
    return

def tallest_square(board):
    return max(len(board), len(board[0]))

def create_square(lg):
    square=[]
    for i in range(lg):
        square_line=[]
        for j in range(lg):
            square_line.append(".")
        square.append(square_line)
    return square

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
        # print ("Trouvé", end = "\n")
        # print (f'coordonnées : ({x}, {y})')
        return True , x , y
    else:
        return False

def replace_car_in_square(square, full_car):
    for line in square:
        for i in range(len(line)):
            line[i] = full_car
    return square


# Construit une représentation du plateau avec le motif trouvé à la position (x, y)
def display_pattern_in_board(board,square,x,y):

    if x is not None and y is not None:
        new_square = replace_car_in_square(square, "o")
        display = []
        for yb, row in enumerate(board):
            line = []
            for xb, _ in enumerate(row):
                # Vérifie si la position (x, y) se trouve dans la zone où le motif doit être affiché
                x_pattern =  x <= xb < x + max(len(row) for row in new_square)
                y_pattern =  y <= yb < y + len(new_square) 

                # Calcule les coordonnées relatives du motif par rapport au coin supérieur gauche du square
                if x_pattern and y_pattern :
                    yp = yb - y
                    xp = xb - x

                    # Vérifie si la position se trouve dans les limites du motif et récupère le caractère correspondant
                    if yp < len(new_square) and xp < len(new_square[yp]) :
                        line.append(new_square[yp][xp])
                    else:
                        line.append(board[yb][xb])
                else:
                    line.append(board[yb][xb])

            line = "".join(line)
            display.append(line)
        display = "\n".join(display)
        return display
    else:
        return "carré non trouvé"


def main():
    handle_error(sys.argv)
    name_of_file_board = sys.argv[1]
    board_list = read_board(name_of_file_board)
    check_board(board_list)
    side_square = tallest_square(board_list)
    i=0
    for i in range(side_square-i):
        actual_square = create_square(side_square-i)
        find_pattern_position(board_list,actual_square)
        if check_pattern_in_board(board_list,actual_square):
            _,x,y= check_pattern_in_board(board_list,actual_square)
            result = display_pattern_in_board(board_list,actual_square,x,y)
            print(result)
            break
   
if __name__ == "__main__":
    main()