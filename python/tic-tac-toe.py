class Grid:
    def __init__(self, width, height, with_coordinates=False):
        self.width = width
        self.height = height
        if with_coordinates:
            self.grid = [[(row, column) for column in range(self.width)] for row in range(self.height)]
        else:
            self.grid = [[" "] * self.width for _ in range(self.height)]

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in line) for line in self.grid)

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value

def check_winner(grid):
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] and grid[0][column] != " ":
            return grid[0][column]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " ":
        return grid[0][2]
    return " "    

def place_marker(grid, row, column, marker):
    if grid[row][column] == " ":
        grid[row][column] = marker
        return True
    return False

def switch_marker(marker_1, marker_2, marker):
    return marker_1 if marker == marker_2 else marker_2

board = Grid(3, 3)
board_with_coordinates = Grid(3, 3, with_coordinates=True)

X = "X"
O = "O"

current_marker = X

while True:
    print(board)
    print(board_with_coordinates)

    row = int(input("Enter row: "))
    column = int(input("Enter column: ")) 

    place_marker(board, row, column, current_marker)
    current_marker = switch_marker(X, O, current_marker)
    winner = check_winner(board)

    if winner != " ": 
        print(f"{winner} wins!")
        break