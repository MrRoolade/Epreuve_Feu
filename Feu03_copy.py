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
            for line  in f:
                line_array = [ x.replace(".","0") for x in line if x != "\n"]
                list_rows.append(line_array)
        return list_rows
    except :
        quit_program("le fichier n'existe pas")

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
                print(str(board[i][j]) + "", end="")

def check_number(x,y,n,temp_board):

    for i in range(0, 9):
        if temp_board[i][x] == n and i != y:
            return False

    for i in range(0, 9):
        if temp_board[y][i] == n and i != x: 
            return False

    x0 = (x // 3) * 3 #trouve le coin des carrés intermédiaires
    y0 = (y // 3) * 3 #trouve le coin des carrés intermédiaires
    for xi in range(x0, x0 + 3):
        for yi in range(y0, y0 + 3):
            if temp_board[yi][xi] == n:
                return False    
    return True

def solve(temp_board):
    possible_tree=[]
    for y in range(0,9):
        for x in range(0,9):
            if temp_board[y][x] == 0 : 
                for n in range(1,10):
                    if check_number(x, y, n,temp_board):
                        temp_board[y][x] = n
                        possible_tree.append(temp_board.copy())
                        if temp_board.count(0) != 0 :
                            solve(possible_tree[-1])
                        # condition d'arret / versioning de board
                    else:
                        temp_board[y][x] = 0
                        temp_board = possible_tree.pop()
                        
                return temp_board

def main():
    name_of_file_board = "s1.txt"
    handle_error(sys.argv)
    board = read_rows(name_of_file_board)
    print(board)
    display_board(board)
    print(11*"=")
    result = solve(board)
    print(result)

    display_board(result)


if __name__ == "__main__":
    main()