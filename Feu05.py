#~~> MrRøølåÐe <~~#

# Créez un programme qui trouve le plus court chemin entre
#  l’entrée et la sortie d’un labyrinthe en évitant les obstacles.

# Le labyrinthe est transmis en argument du programme.
#  La première ligne du labyrinthe contient les informations pour lire la carte : LIGNESxCOLS, caractère plein, vide, chemin, entrée et sortie du labyrinthe. 

# Le but du programme est de remplacer les caractères “vide” par des caractères “chemin” pour représenter le plus court chemin pour traverser le labyrinthe.
#  Un déplacement ne peut se faire que vers le haut, le bas, la droite ou la gauche.

# TO DO :
# trouver LE chemin le plsu court
# afficher le labyrinthe avec le chemin le plus court


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

    return expected_size

def find_car_in_maze(board, given_car):
    for y,line in enumerate(board):
        for x, car in enumerate(line):
            if car == given_car:
                return (x, y)
    return None

def create_ref_maze(size):
    return [[0] * size[0] for _ in range(size[1])]

def is_valid(board, visited, x, y, empty_car, entry_car, exit_car, path_car):
    if board[x][y] == empty_car and visited[x][y] ==0 and 0<x<len(board[x]) and 0<y<len(board):
        return True
    if board[x][y] == entry_car and visited[x][y] ==0 and 0<x<len(board[x]) and 0<y<len(board):
        return True
    if board[x][y] == exit_car and visited[x][y] ==0 and 0<x<len(board[x]) and 0<y<len(board):
        return True
    if board[x][y] == path_car and visited[x][y] ==0 and 0<x<len(board[x]) and 0<y<len(board):
        return True
    return False
    
def find_shortest_path(board, visited, end, i, j, empty_car,entry_car, exit_car,path_car, min_dist, dist):
    print(f'exploring : {i}, {j}')
    print(end)
    #condition d'arret
    if (i, j) == end:
        print("we arrived")
        return min(min_dist, dist)
    
    visited[i][j] = 1

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx , dy in directions:
        new_i, new_j = i + dx, j + dy 
        if is_valid(board, visited, new_i, new_j, empty_car, entry_car, exit_car,path_car):
            print("moving to", new_i, new_j)
            min_dist = find_shortest_path(board, visited, end, new_i, new_j, empty_car,path_car, min_dist, dist + 1)

    #backtrack
    visited[i][j] = 0

    return min_dist

def main():
    handle_error(sys.argv)
    name_of_file_board = sys.argv[1]
    board_list , first_line = read_board(name_of_file_board)
    full_car = first_line[-5]
    empty_car = first_line[-4]
    path_car = first_line[-3]
    entry_car = first_line[-2]
    exit_car = first_line[-1]

    print(empty_car, entry_car, exit_car, full_car, path_car)
    size = check_board(board_list, first_line)   
    visited = create_ref_maze(size)
    
    start = find_car_in_maze(board_list,entry_car) 
   
    end = find_car_in_maze(board_list,exit_car)
    # print(end)
    dist = 0
    min_dist= int()

    min_dist = find_shortest_path(board_list, visited, end, start[0],start[1], empty_car,entry_car, exit_car,path_car, min_dist, dist)
    print(min_dist, 'ok')

    for line in board_list:
        print("".join(line))

if __name__ == "__main__":
    main()