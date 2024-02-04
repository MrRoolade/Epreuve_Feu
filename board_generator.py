import sys
import random

if len(sys.argv) != 4:
    print("paramètres nécessaires : x y densité")
    sys.exit()

x = int(sys.argv[1])
y = int(sys.argv[2])
density = int(sys.argv[3])

print(f"{y}.xo")
for i in range(y + 1):
    for j in range(x + 1):
        print('x' if random.randint(0, y) * 2 < density else '.', end='')
    print()
