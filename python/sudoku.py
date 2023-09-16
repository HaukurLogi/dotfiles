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

def printLevel(level):
    for row in level:
        print(row) # Print sudoku table

def makeValidTable(grid):
    appendedNumbersInRow = []
    appendedNumbersInColumn = []

    for row in range(0,9):
        appendedNumbersInRow.clear()
        appendedNumbersInColumn.clear()
        for column in grid[row]:
            skipColumn = bool(randint(0,1))
            randomNumber = randint(1,9)
            randomColumn = randint(0,8)
            if grid[row][randomColumn] == 0 and not skipColumn: # Check if number isn't already taken
                if randomNumber not in appendedNumbersInRow:
                    if (randomColumn, randomNumber) not in appendedNumbersInColumn:
                        grid[row][randomColumn] = randomNumber
                        appendedNumbersInRow.append(randomNumber)
                        appendedNumbersInColumn.append((randomColumn, randomNumber))
    printLevel(grid)
    return grid # Returns edited grid

def placeNumber(level):
    x = int(input("X : ")) - 1
    y = int(input("Y : ")) - 1
    number = int(input("Number : "))

    level[x][y] = number # Places number in level

    printLevel(level)
    return level # Return edited level

level = makeValidTable(defaultGrid) # Create valid sudoku table


while True:
    level = placeNumber(level)
