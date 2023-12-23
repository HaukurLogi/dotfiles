import copy
import random
from pynput import keyboard
import os
import time

GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_TOP = 0
GRID_MIDDLE = int(GRID_WIDTH / 2)

ACTIVE_CELL = "#"
EMPTY_CELL = " "
PLACED_CELL =    "X"

SLEEP_TIME = 0.1

BLOCKS = [
    [[[GRID_TOP, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 2, GRID_MIDDLE], [GRID_TOP + 3, GRID_MIDDLE]], 
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP, GRID_MIDDLE + 2], [GRID_TOP,  GRID_MIDDLE + 3]]], # I-block

    [[[GRID_TOP, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1]],
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1]]], # O-block

    [[[GRID_TOP, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 2, GRID_MIDDLE]], 
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP, GRID_MIDDLE + 2]],
    [[GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 2, GRID_MIDDLE + 1]],
    [[GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 2]]],  # T-block

    [[[GRID_TOP, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 2]],
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 2, GRID_MIDDLE]],
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 2], [GRID_TOP, GRID_MIDDLE + 2]],
    [[GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 2, GRID_MIDDLE + 1], [GRID_TOP + 2, GRID_MIDDLE]]], # J-block

    [[[GRID_TOP, GRID_MIDDLE + 2], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 2]],
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 2, GRID_MIDDLE], [GRID_TOP + 2, GRID_MIDDLE + 1]],
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP, GRID_MIDDLE + 2]],
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 2, GRID_MIDDLE + 1]]], # L-block 

    [[[GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP, GRID_MIDDLE + 2], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1]],
    [[GRID_TOP, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 2, GRID_MIDDLE + 1]]], # S-block

    [[[GRID_TOP, GRID_MIDDLE], [GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 2]],
    [[GRID_TOP, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE + 1], [GRID_TOP + 1, GRID_MIDDLE], [GRID_TOP + 2, GRID_MIDDLE]]] # Z-block
]      

grid = [[EMPTY_CELL] * GRID_WIDTH for _ in range(GRID_HEIGHT)] # Directly initialize the grid
placed_block_coordinates = []  # Define placed block coordinates

def clear_current_position(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == ACTIVE_CELL: # If the cell is active, clear it
                grid[row][column] = EMPTY_CELL

def print_grid(grid): # Print the current grid
    for row in grid:
        print(EMPTY_CELL.join(row))

def update_grid(grid, value, coordinates):
    clear_current_position(grid) # Clear the grid before placing the next cell
    for new_coordinate in coordinates:
        row, column = new_coordinate[0], new_coordinate[1] # Define the current y, x coordinates
        grid[row][column] = value # Place the cell at the current coordinates
    os.system("clear ")
    print_grid(grid)

def can_move_down(grid, coordinates):
    next_coordinates = [[coordinate[0] + 1, coordinate[1]] for coordinate in coordinates] # The coordinates if the block were to move down

    if any(next_coordinate[0] >= GRID_HEIGHT or grid[next_coordinate[0]][next_coordinate[1]] == PLACED_CELL for next_coordinate in next_coordinates): # If the next coordinate is either a placed cell or the floor the cell becomes placed
        return False
    return True

def can_move_right(grid, coordinates):
    next_coordinates = [[coordinate[1] + 1, coordinate[1]] for coordinate in coordinates] # The coordinates if the block were to move right
    next_rightmost_pixel = max(coordinate[1] for coordinate in coordinates) + 1

    if any(next_rightmost_pixel >= GRID_WIDTH or grid[next_coordinate[0]][next_coordinate[1]] == PLACED_CELL for next_coordinate in next_coordinates): # If the next coordinate is either a placed cell or the wall the cell becomes placed
        return False
    return True

def can_move_left(grid, coordinates):
    next_coordinates = [[coordinate[1] - 1, coordinate[1]] for coordinate in coordinates] #The coordinates if the block were to move left
    next_leftmost_pixel = min(coordinate[1] for coordinate in coordinates) - 1

    if any(next_leftmost_pixel <= GRID_WIDTH - GRID_WIDTH or grid[next_coordinate[0]][next_coordinate[1]] == PLACED_CELL for next_coordinate in next_coordinates): # If the next coordinate is either a placed cell or the wall the cell becomes placed
        return False 
    return True 

def move_auto_down(grid, placed_coordinates, coordinates, delay):      
    while True:
        time.sleep(delay)  # Block goes down every 'delay' seconds
        update_grid(grid, ACTIVE_CELL, coordinates)
 
        # Check if the block has reached the bottom or a placed block
        if can_move_down(grid, coordinates):
            for pixel in range(len(coordinates)):
                coordinates[pixel][0] += 1 # Move block down if can_move_down returns true
        else:
            placed_coordinates.append(coordinates) # Append the placed cells to placed coordinates array
            update_grid(grid, PLACED_CELL, coordinates) # Update the block with placed cells
            create_new_block(grid, placed_coordinates) # Spawn new block     


def rotate(coordinates, block, orientation, max_orientation):
    if orientation <= max_orientation:
        orientation += 1
        rotated_coordinates = BLOCKS[block][orientation] # Makes new block with the changed orientation

        for rotated_coordinate in rotated_coordinates:
            for coordinate in coordinates:
                y_diff = coordinate[0] - rotated_coordinate[0] # The difference between the beginning y and the y level at which the rotate function was called
                x_diff = coordinate[1] - rotated_coordinate[1] # The difference between the beginning x and the x level at which the rotate function was called

        for pixel in range(len(rotated_coordinates)):
            rotated_coordinates[pixel][0] += y_diff # Equalize differences
            rotated_coordinates[pixel][1] += x_diff # Equalize differences

        return rotated_coordinates
    else:
        max_orientation = 0
        return coordinates
   
def move_right(grid, coordinates):
    if can_move_right(grid, coordinates):
        for pixel in range(len(coordinates)):
            coordinates[pixel][1] += 1 # Moves block right if can_move_right returns true

def move_left(grid, coordinates):
    if can_move_left(grid, coordinates):
        for pixel in range(len(coordinates)):
            coordinates [pixel][1] -= 1 # Moves block right if can_move_left returns true

def on_press(key, grid, random_block, coordinates, orientation, max_orientation):
    if key == keyboard.Key.space:
        coordinates[:] = rotate(coordinates, random_block, orientation, max_orientation) # If space is pressed then define coordinates to rotated coordinates
    if key == keyboard.Key.right:
        move_right(grid, coordinates) # Call move right function if right arrow pressed
    if key == keyboard.Key.left:
        move_left(grid, coordinates) # Call move left function if right arrow pressed

def user_movement(grid, placed_coordinates, coordinates, random_block, orientation, max_orientation):
    listener = keyboard.Listener(on_press=lambda key: on_press(key, grid, random_block, coordinates, orientation, max_orientation)) # "Listen" to the keyboard and call the on_press function if key pressed
    listener.start() # Start listener

def create_new_block(grid, placed_coordinates):
    random_block = random.randint(0, len(BLOCKS) - 1) # Chooses random block from all blocks
    block_orientation = 0 # Starting block orientation
    max_block_orientation = len(BLOCKS[random_block])  # for every 1 is a 90-degree turn
    current_block_coordinates = copy.deepcopy(BLOCKS[random_block][block_orientation]) # Make a copy of the block to ensure the BLOCK variable doesn't change
    
    user_movement(grid, placed_coordinates, current_block_coordinates, random_block, block_orientation, max_block_orientation) # Start the user movement
    move_auto_down(grid, placed_coordinates, current_block_coordinates, SLEEP_TIME)  # Start the auto down
    
if __name__ == "__main__":
    create_new_block(grid, placed_block_coordinates)  # Let the games begin!