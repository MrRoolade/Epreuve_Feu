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

def is_valid(board, visited, x, y, valid_car):
#    print(x, y, board[y][x])
#    print(valid_car)

   return board[y][x] in valid_car and visited[y][x] ==0 and 0<=y<len(board[x]) and 0<=x<len(board)
        
    
def find_shortest_path(board, visited, end, i, j, maze_info, min_dist, dist):
    print(f'exploring : {i}, {j}')
    print(end, i,j)
    #condition d'arret
    if i == end[1] and j == end[0]:
        print("we arrived")
        return min(min_dist, dist)
    
    visited[j][i] = 1

    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx, dy in directions:
        new_i, new_j = i + dx, j + dy 
        # print(new_i, new_j)
        if is_valid(board, visited, new_i, new_j, [maze_info.empty_car, maze_info.entry_car, maze_info.exit_car, maze_info.path_car]):
            print("moving to", new_i, new_j)
            min_dist = find_shortest_path(board, visited, end, new_i, new_j, maze_info, min_dist, dist + 1)
        # verif = is_valid(board, visited, new_i, new_j, [maze_info.empty_car, maze_info.entry_car, maze_info.exit_car, maze_info.path_car])
        print(f' pascool')

    #backtrack
    visited[j][i] = 0

    return min_dist

def main():
    handle_error(sys.argv)
    name_of_file_board = sys.argv[1]
    board_list , first_line = read_board(name_of_file_board)

    maze_info = MazeInfo(first_line[-5], first_line[-4], first_line[-3],first_line[-2], first_line[-1])
    print(maze_info.__dict__)

    size = check_board(board_list, first_line)   
    visited = create_ref_maze(size)
    
    start = find_car_in_maze(board_list,maze_info.entry_car) 
   
    end = find_car_in_maze(board_list,maze_info.exit_car)
    # print(end)
    dist = 0
    min_dist= int()

    min_dist = find_shortest_path(board_list, visited, end, start[0],start[1], maze_info, min_dist, dist)
    print(min_dist, 'ok')

    for line in board_list:
        print("".join(line))

if __name__ == "__main__":
    main()