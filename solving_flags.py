#imports
import Grid

class solving_flag:
    row_flags = []
    col_flags = []
    sqr_flags = []
    one_flags = []
    
    offset_row = 0
    offset_col = 0
    update_num = 0
    grid = []

    def __init__(self,grid):
        
        offset_row = 0
        offset_col = 0
        update_num = 0
        
        self.grid = grid
        
        self.row_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.col_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.sqr_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.one_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #returns  all non zero values in a given row
    def check_row(self, row):
        self.row_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        check= False
        #for row in range(0,9):
        for col in range(0,9):
            if not ((self.grid[row][col] == 0)):                      
                self.row_flags[col] = self.grid[row][col]
            if(col==8):
                check = True
        if(check):
            check = False
            #return self.row_flags
            
    #returns all non zero values in a given col 
    def check_col(self, col):
        self.col_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        check = False
        #for row in range(0,9):
        for row in range(0,9):
            if not ((self.grid[row][col] == 0)):                      
                self.col_flags[row] = self.grid[row][col]
            if(row==8):
                check = True
        if(check):
            check = False
            #return self.col_flags


    #returns non zero values in a given sqr
    def check_sqr(self, row, col):
        self.sqr_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        sqr = self.check_num(row, col)
        for row in range(0,3):
            for col in range(0,3):
                new_row = row + self.offset_row
                new_col = col + self.offset_col
                if not ((self.grid[new_row][new_col] == 0)):
                    self.sqr_flags[self.check_v(row, col)-1] = self.grid[new_row][new_col]

    #checks for possbile caditates for given point
    def check_one(self,row,col):
        temp = 0
        self.one_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        #returns the possible values for given
        #print(self.sqr_flags)
        for i in range(1,10):
            for j in range(0,9):
                if(self.row_flags[j] == i):
                    #print(i,"row",self.row_flags[j])
                    break
                elif(self.col_flags[j] == i):
                    #print(i,"col",self.col_flags[j])
                    break
                elif(self.sqr_flags[j] == i):
                    #print(i,"sqr",self.sqr_flags[j])
                    break
                elif(j==8):
                    #print(i,"pos")
                    self.one_flags[i-1] = 1
                    self.update_num  = i
                    break
        count = 0
        for k in range(0,9):
                if(self.one_flags[k] == 1):
                    count = count+1
                if(k == 8):
                    if(count == 1):
                       #print(self.update_num )
                        self.update_grid(row,col)
        return self.grid
                              

    def update_grid(self,row,col):
        self.grid = Grid.update_grid2(row,col,self.update_num ,self.grid)
        
    def check_num(self, row, col):
        
        if((0<=row<3)&(0<=col<3)):
            
            self.offset_row = 0
            self.offset_col = 0
            sqr = 1
        
            return sqr
            
        elif((0<=row<3)&(3<=col<6)):
            
            self.offset_row = 0
            self.offset_col = 3
            sqr = 2
            
            return sqr
            
        elif((0<=row<3)&(6<=col<9)):

            self.offset_row = 0
            self.offset_col = 6
            sqr = 3
            
            return sqr
            
        elif((3<=row<6)&(0<=col<3)):

            self.offset_row = 3
            self.offset_col = 0
            sqr = 4
            
            return sqr
            
        elif((3<=row<6)&(3<=col<6)):

            self.offset_row = 3
            self.offset_col = 3
            sqr = 5
            
            return sqr
            
        elif((3<=row<6)&(6<=col<9)):

            self.offset_row = 3
            self.offset_col = 6
            sqr = 6
            
            return sqr
            
        elif((6<=row<9)&(0<=col<3)):

            self.offset_row = 6
            self.offset_col = 0
            sqr = 7
            
            return sqr
            
        elif((6<=row<9)&(3<=col<6)):

            self.offset_row = 6
            self.offset_col = 3
            sqr = 8
            
            return sqr
            
        elif((6<=row<9)&(5<=col<9)):

            self.offset_row = 6
            self.offset_col = 6
            sqr  = 9
            
            return sqr

    def check_v(self, row, col):
        
        if((row ==0)&(col==0)):
            
            sqr = 1
        
            return sqr
            
        elif((row ==0)&(col==1)):
            
            sqr = 2
            
            return sqr
            
        elif((row ==0)&(col==2)):

            sqr = 3
            
            return sqr
            
        elif((row ==1)&(col==0)):

            sqr = 4
            
            return sqr
            
        elif((row ==1)&(col==1)):

            sqr = 5
            
            return sqr
            
        elif((row ==1)&(col==2)):

            sqr = 6
            
            return sqr
            
        elif((row ==2)&(col==0)):

            sqr = 7
            
            return sqr
            
        elif((row ==2)&(col==1)):

            sqr = 8
            
            return sqr
            
        elif((row ==2)&(col==2)):

            sqr  = 9
            
            return sqr





            
        
    #def check_one():

        
    
