import solving_flags
import read_from_file
import Grid

def solving_algorithm(grid):
     s = solving_flags.solving_flag(grid)   
     for row in range(0,9):
            for col in range(0,9):
                if(s.grid[row][col] == 0):
                    s.check_row(row)
                    s.check_col(col)
                    s.check_sqr(row,col)
                    s.check_one(row,col)                 
                    
                else:
                    continue
     return s.grid
def check_if_solved(grid):
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    grid = solving_algorithm(grid)
    return grid

        
    
   
                 
#grid = read_from_file.read_game_file()     
#Grid.draw_grid(grid)
#Grid.draw_grid_from_file(check_if_solved(grid))

