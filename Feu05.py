#~~> MrRøølåÐe <~~#

# Créez un programme qui trouve le plus court chemin entre
#  l’entrée et la sortie d’un labyrinthe en évitant les obstacles.

# Le labyrinthe est transmis en argument du programme.
#  La première ligne du labyrinthe contient les informations pour lire la carte : LIGNESxCOLS, caractère plein, vide, chemin, entrée et sortie du labyrinthe. 

# Le but du programme est de remplacer les caractères “vide” par des caractères “chemin” pour représenter le plus court chemin pour traverser le labyrinthe.
#  Un déplacement ne peut se faire que vers le haut, le bas, la droite ou la gauche.

import sys
from collections import deque

class MazeInfo:
    def __init__(self, full_car, empty_car, path_car, entry_car, exit_car):
        self.full_car = full_car
        self.empty_car = empty_car
        self.path_car = path_car
        self.entry_car = entry_car
        self.exit_car = exit_car

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
    expected_height, expected_lenght  = tuple(map(int, size.split('x')))

    for line in board:
        if len(line) != expected_lenght :
            quit_program("les lignes du plateau ne sont pas valide")
        for char in line:
            if char not in valid_car:
                quit_program("au moins un caractère n'est pas valide")
        
    if len(board) != expected_height:
        quit_program("la hauteur du plateau n'est pas valide")

    return True

def find_car_in_maze(board, given_car):
    positions = []
    for y,line in enumerate(board):
        for x, car in enumerate(line):
            if car == given_car:
                positions.append((y, x))
    return positions

def bfs(board, start, exits, maze_info) :
    queue = deque([(start[0],start[1], [])])
    visited = set()
    directions = [(0,-1),(0,1),(1,0),(-1,0)]

    while queue:
        y, x, path = queue.popleft()
        if(y,x) in visited:
            continue
        visited.add((y,x))
        path = path +[(y,x)]
        
        if(y,x) in exits :
            return path

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0<= ny <len(board)) and (0<= nx <len(board[0])):
                if board[ny][nx] in [maze_info.empty_car, maze_info.exit_car]:
                    queue.append((ny, nx, path))
    return None


def display_solved_maze (board_list, path_solution, maze_info):
    for y, line in enumerate(board_list):
        for x, char in enumerate(line):
            if char == maze_info.empty_car:
                if (y, x) in path_solution:
                    print(maze_info.path_car, end="")
                else:
                    print(f'{char}', end="")
            else:
                print(char, end="")
        print()

def main():
    handle_error(sys.argv)
    name_of_file_board = sys.argv[1]
    board_list , first_line = read_board(name_of_file_board)
    maze_info = MazeInfo(first_line[-5], first_line[-4], first_line[-3],first_line[-2], first_line[-1])
    start = find_car_in_maze(board_list,maze_info.entry_car)[0]
    exits = find_car_in_maze(board_list,maze_info.exit_car)

    if check_board(board_list, first_line):
        path = bfs(board_list, start, exits, maze_info)
        if path is None:
            print('Nous nous sommes perdus dans le labyrinthe')
        else:
            print(f'Le chemin le plus court est de {len(path) - 1} case(s) du départ')
            display_solved_maze(board_list, path, maze_info)

if __name__ == "__main__":
    main()