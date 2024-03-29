#~~> MrRøølåÐe <~~#
# Créez un programme qui trouve et affiche la solution d’un Sudoku.

import sys

def handle_error(user_value): 
    if len(user_value)!=2: 
        quit_program("veuillez rentrer un nom de fichier svp")

def quit_program(message):
    sys.exit(message)

def read_rows(name_of_file):
    list_rows = []
    try:
        with open(name_of_file, 'r') as f:
            for line in f:
                line_array = [0 if x=="." else x for x in line]
                list_rows.append(line_array)
        return list_rows
    except :
        quit_program("le fichier n'existe pas")

def is_valid_board(board):
    if len(board) != 9:
        return False

    for row in board:
        cleaned_row = [element for element in row if element != "\n"]

        if len(cleaned_row) != 9:
            return False
        for element in cleaned_row:
            str_element = str(element)
            if not str_element.isdigit() or '\n' in str_element:
                return False

    return True        

def display_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("---+---+---")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]), end="")

def check_number(x,y,n,temp_board):
    for i in range(9):
        if int(temp_board[i][x]) == n:
            return False

    for i in range(9):
        if int(temp_board[y][i]) == n: 
            return False

    x0 = (x // 3) * 3 #trouve le coin des carrés intermédiaires
    y0 = (y // 3) * 3 #trouve le coin des carrés intermédiaires
    for xi in range(x0, x0 + 3):
        for yi in range(y0, y0 + 3):
            if int(temp_board[yi][xi]) == n:
                return False    
    return True

def solve(temp_board):
    empty_cell = find_empty_cell(temp_board)
    if not empty_cell:
        return temp_board  # La grille est déjà complète
    
    y, x = empty_cell
    
    for n in range(1, 10):
        if check_number(x, y, n, temp_board):
            temp_board[y][x] = n
            if solve(temp_board):
                return temp_board
        temp_board[y][x] = 0
    return None

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if int(board[i][j])== 0:
                return (i, j)
    return None

def main():
    handle_error(sys.argv)
    try:
        board = read_rows(sys.argv[1])
        if not is_valid_board(board):
            quit_program("grille de départ non valide")
        print("grille de départ OK")
        display_board(board)
        print(11*"=")
        result = solve(board)
        if result:
            print("solution trouvée")
            display_board(result)
        else:
            print("aucune solution trouvée")
    except Exception as e:
        quit_program(f"une erreur s'est produite : {str(e)}")

if __name__ == "__main__":
    main()