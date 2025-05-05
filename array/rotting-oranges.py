class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # m*n grid
        # three values - 0: empty
        # 1: fresh orange
        # 2: rotten orange 
        # fresh orange 4 direc adjacent rotten -> becomes rotten 
        # min minutes until no cell has fresh orange, if not possible = -1 

        # example -> 
        # 2, we check it's adj, if it's 1 we turn them to 2, and increase the count now again check 2 it's a

        ROWS, COLS = len(grid), len(grid[0])
        minute = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    if r+1 >ROWS or r-1<0:
                        break 
                    if c+1> COLS or c-1<0:
                        break
                    grid[r+1][c] == 2 if grid[r+1][c] ==1 else 0
                    grid[r-1][c] == 2 if grid[r-1][c] ==1 and r-1 >0 else 0
                    grid[r][c+1] == 2 if grid[r][c+1] ==1 and c+1 < COLS else 0
                    grid[r][c-1] == 2 if grid[r][c-1] ==1 and c-1 > 0 else 0

                minute +=1
        
        return minute
        