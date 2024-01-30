#~~> MrRøølåÐe <~~#
# Créez un programme qui trouve et affiche la solution d’un Sudoku.
#fkjdhfkj

import sys
import re

def handle_error(user_value): 
    if len(user_value)!=2: 
        quit_program("veuillez rentrer deux noms de fichier svp")

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

def  read_columns(list_rows): #rotate the grid
    list_columns = []
    for i in range(9) :
        columns_array = [list_rows[j][i] for j in range(9)]
        list_columns.append(columns_array) 
    return list_columns

def read_square(list_rows):
    list_square = []
    start = 0
    end = 3
    for skip in range (0,9,3):
        list_temp = []
        for step in range(0,9,3):
            for i in range(start+step, end+step) :
                square_array = [list_temp.append(list_rows[j][i]) for j in range(start+skip ,end+skip)]
            list_square.append(list_temp)
            list_temp =[] 
    return list_square

def find_all_number_missed(solve_list, list):
    soluce_line = []
    for line in list :
        line = set(line)
        union = solve_list - line
        soluce_line.append(union)
    return soluce_line

def when_just_one_number_to_find(list_rows, soluce_row):
    for i, row in enumerate(list_rows):
        if len(soluce_row[i]) == 1:
            index_to_replace = list_rows[i].index('0')
            list_rows[i][index_to_replace] = soluce_row[i].pop()
    return list_rows

def main():
    name_of_file_board = "s.txt"
    handle_error(sys.argv)
    board = read_rows(name_of_file_board)

    #r.[1-9]

    solve_list = set ( str(x) for x in range(10) if x != 0 )
    # print (solve_list)

    list_rows = board
    
    # list_squares = read_square(board)

    soluce_row = find_all_number_missed(solve_list, list_rows)
    
    # soluce_square = find_all_number_missed(solve_list, list_squares)

    # list_rows = when_just_one_number_to_find(list_rows, soluce_row)
    # list_columns = read_columns(list_rows)
    # soluce_column = find_all_number_missed(solve_list, list_columns)
    # list_columns = when_just_one_number_to_find(list_columns, soluce_column)
    # list_rows = read_columns(list_columns)

    print(list_rows)
    solve(list_rows)

def solve(board):
    
    grid = board
    for y in range(9):
        for x in range(9):
            grid[y][x] = int(grid[y][x])
            if grid[y][x] == "0" : 
                for n in range(9):
                    if n not in grid[y] or [grid[y][x] for y in range(9)]:
                        grid[y][x] = str(n)
                print(grid[y], end=" ")
                    # solve(board)

    
    # print(list_rows)
    # print(list_columns)
    # print(list_squares)

    # result = ["".join(row) for row in list_rows ]
    # total = ["\n".join(line) for line in result]
    # for line in result :
    #     print(line)
   
if __name__ == "__main__":
    main()