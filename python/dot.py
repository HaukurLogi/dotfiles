import random
import time

GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_MIDDLE = int(GRID_WIDTH / 2)


ACTIVE_CELL = "#"
EMPTY_CELL = " "
PLACED_CELL = "X"

SLEEP_TIME = 0.1

BLOCKS = [
    [[[0, 0], [1, 0], [2, 0], [3, 0]], [[1, 0], [1, 1], [1, 2], [1, 3]]], # Straight block
    [[[0, 1], [1, 0], [1, 1], [1, 2]], [[0, 1], [1, 0], [1, 1], [1, 2]]]  # Triangle block
]                                                                          

def initialize_grid():
    return [[EMPTY_CELL] * GRID_WIDTH for _ in range(GRID_HEIGHT)] # Create and initialize the playable grid

def clear_current_position(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == ACTIVE_CELL: # If the cell is active, clear it
                grid[row][column] = EMPTY_CELL

def print_grid(grid): # Print the current grid
    # Printing Grid
    for row in grid:
        print(" ".join(row))

    

def update_grid(grid, value, coordinates):
    clear_current_position(grid) # Clear the grid before placing the next cell
    for new_coordinate in coordinates:
        row, column = new_coordinate[0], new_coordinate[1] # Define the current y, x coordinates
        grid[row][column] = value # Place the cell at the current coordinates
    print_grid(grid)

def can_move_down(grid, coordinates):
    next_coordinates = [[coordinate[0] + 1, coordinate[1]] for coordinate in coordinates] # Get the next coordinates to determine if it can be moved

    if any(next_coordinate[0] >= GRID_HEIGHT or grid[next_coordinate[0]][next_coordinate[1]] == PLACED_CELL for next_coordinate in next_coordinates): # If the next coordinate is either a placed cell or the floor the cell becomes placed
        return False
    return True

def move_auto_down(grid, placed_coordinates, coordinates, delay):
    while True:
        time.sleep(delay)  # Block goes down every 'delay' seconds
        update_grid(grid, ACTIVE_CELL, coordinates)

        # Check if the block has reached the bottom
        if can_move_down(grid, coordinates):
            for row in range(len(coordinates)):
                coordinates[row][0] += 1 # Moved block down if can_move_down returns false
        else:
            placed_coordinates.append(coordinates) # Append the placed cells to placed coordinates array
            update_grid(grid, PLACED_CELL, coordinates) # Update the block with placed cells
            main(grid, placed_coordinates) # Spawn new block
            break
        

def main(grid, placed_coordinates):
    random_block = random.randint(0, len(BLOCKS) - 1)
    block_orientation = 0  # for every 1 is a 90-degree turn
    current_block_coordinates = BLOCKS[random_block][block_orientation]

    move_auto_down(grid, placed_coordinates, current_block_coordinates, SLEEP_TIME)

if __name__ == "__main__":
    grid = initialize_grid()
    placed_block_coordinates = []
    main(grid, placed_block_coordinates)