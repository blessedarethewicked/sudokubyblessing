#drawing of the grid

#draw_grid the fist function that i made
#it works with normal user input
def draw_grid(grid):
        for row in range(0,9):
                print(grid[row])
        print("\n")

# you need this functio when drawing
#the grid that has been read if from
#a file
def draw_grid_from_file(grid):
        for row in range(0,9):
                print(grid[row])
        print("\n")

#this one allows for the user to play
#and update the game on the fly
def update_grid(p):
        p.grid[p.x_pos][p.y_pos] = p.value
        return p.grid
def update_grid2(row,col,update_num ,grid):
        grid[row][col] = update_num
        #draw_grid(grid)
        return grid
