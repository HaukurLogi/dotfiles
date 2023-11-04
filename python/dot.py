dot = "."
dotPos = [0, 0]
#         0, 1
#         x, y

#                           Y
grid = [ #                  |
    ["", "", "", "", ""], # 0
    ["", "", "", "", ""], # 1
    ["", "", "", "", ""], # 2
    ["", "", "", "", ""], # 3 
    ["", "", "", "", ""]  # 4
# X - 0   1   2   3   4 
]


def drawMap(erase, x, y):
    if erase:
        grid[x][y] = ""
    else:
        grid[x][y] = dot

    for row in grid:
        print(row)

def move():
    while True: 
        movement = str(input("Movement : ")).lower()

        if movement == "w":
            drawMap(True, dotPos[0], dotPos[1])
            if dotPos[0] > 0:
                dotPos[0] -= 1
        elif movement == "a":
            drawMap(True, dotPos[0], dotPos[1])
            if dotPos[1] > 0:
                dotPos[1] -= 1
        elif movement == "s":
            drawMap(True, dotPos[0], dotPos[1])
            if dotPos[0] < 4:
                dotPos[0] += 1
        elif movement == "d":
            drawMap(True, dotPos[0], dotPos[1])
            if dotPos[1] < 4:
                dotPos[1] += 1
        else:
            print("Huh? :/")
            move()

        drawMap(False, dotPos[0], dotPos[1])

while True:
    move()