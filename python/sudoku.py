from random import randint

defaultgrid = [
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

appendedNumbersInRow = []
appendedNumbersInColumn = []

for row in range(0,9):
    appendedNumbersInRow.clear()
    for column in defaultgrid[row]:
        randomNumber = randint(1,9)
        randomColumn = randint(0,8)
        if defaultgrid[row][randomColumn] == 0:
            if randomNumber not in appendedNumbersInRow:
                if (randomColumn, randomNumber) not in appendedNumbersInColumn:
                    defaultgrid[row][randomColumn] = randomNumber
                    appendedNumbersInRow.append(randomNumber)
                    appendedNumbersInColumn.append((randomColumn, randomNumber))
            

for column in defaultgrid:
    print(column) # Print sudoku table
