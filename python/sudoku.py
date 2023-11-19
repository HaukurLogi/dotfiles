from random import randint


defaultGrid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

def print_level(level):
    for row in level:
        print(row) # Print sudoku table

def make_valid_table(grid):
    appended_numbers_in_row = []
    appended_numbers_in_column = []

    for row in range(0,9):
        appended_numbers_in_row.clear()
        for column in grid[row]:
            skip_column = bool(randint(0,1))
            random_number = randint(1,9)
            random_column = randint(0,8)
            if grid[row][random_column] == 0 and not skip_column: # Check if number isn't already taken
                if random_number not in appended_numbers_in_row:
                    if (random_column, random_number) not in appended_numbers_in_column:
                        grid[row][random_column] = random_number
                        appended_numbers_in_row.append(random_number)
                        appended_numbers_in_column.append((random_column, random_number))
    print_level(grid)
    return grid # Returns edited grid

def place_number(level):
    x = int(input("X : ")) - 1
    y = int(input("Y : ")) - 1
    number = int(input("Number : "))

    if level[y][x] == 0:
        level[y][x] = number # Places number in level
    else:
        print("Invalid placement! :/")

    seen_x = []
    seen_y = []

    for row in range(0,9):
        for column, number in enumerate(level[row]):
            if number != 0:
                if number not in seen_x: # Check Row
                    seen_x.append(number)
                    return level
                if (column, number) not in seen_y: # Check Column
                    seen_y.append((column, number))
                    return level
                if number in seen_x or (column, number) in seen_y:
                    print("You lost!")
                    return False

    print_level(level)

level = make_valid_table(defaultGrid) # Create valid sudoku table

while True:
    level = place_number(level)
    if not level:
        break