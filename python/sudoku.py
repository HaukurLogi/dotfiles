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

    level[y][x] = number # Places number in level

    seenX = []
    seenY = []

    for row in range(0,9):
        for column, number in enumerate(level[row]):
            if number != 0:
                if number not in seenX: # Check Row
                    seenX.append(number)
                if (column, number) not in seenY: # Check Column
                    seenY.append((column, number))
                else:
                    print("You lost!")
                    return 0

    printLevel(level)
    return level # Return edited level

level = makeValidTable(defaultGrid) # Create valid sudoku table

while True:
    level = placeNumber(level)
    if level == 0:
        break