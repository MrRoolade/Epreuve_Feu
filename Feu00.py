import sys

def handle_error(user_value): 
    try:
        if len(user_value) != 3:
            quit_program("veuillez entrer 2 nombres")
        for value in user_value[1:]:
            if not value.isdigit() :
                quit_program("veuillez entrer des nombres valides")
    except (ValueError, IndexError):
        quit_program("error")

def quit_program(message):
    sys.exit(message)

def first_and_last_line(arg):
    if arg == 1:
        print("o")
    elif arg > 1 :
        print(f'o{"-"*(arg-2)}o')

def intermediate_line(arg):
    if arg > 1 :
        print(f'|{" "*(arg-2)}|')

def display_rectangle( long, haut) :
    for h in range(haut) :
        if h == 0 or h == haut-1:
            first_and_last_line(long)
        else :
            intermediate_line(long)


def main():

    handle_error(sys.argv)

    longueur = int(sys.argv[1])
    hauteur = int(sys.argv[2])

    display_rectangle( longueur, hauteur)

    

if __name__ == "__main__":
    main()