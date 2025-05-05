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

        #if we use dfs, it's not gonna work cause it counts when each orange becomes rotten
        # but oranges are rotten simultaneosly not one by one 
        # we are using BFS, cause we can just count the layers
        # since we're running bfs on multiple nodes, it's multi sources bfs 
        # to know if its possible or not, keep track of fresh oranges before running bfs, then 
        # then after bfs, if we have positive number of oranges, means it's not possible
        #we're only gonna visit each node once, so time = O(n*m)

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        #iterating through each node 
        for r in range(ROWS):
            for c in range(COLS):
                #check if it's fresh 
                if grid[r][c] ==1:
                    fresh +=1
                #check if its rotten to run bfs on it 
                if grid[r][c] ==2:
                    q.append([r,c])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # if queue is empty or fresh is empty, loop will not run 
        while q and fresh >0:
            # go through each element in the q 
            for i in range(len(q)):
                r,c = q.popleft()

                #check its adjacent nodes
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c 

                    # check if these coordinate has fresh oranges or it's out of bounds 
                    if (row == ROWS or row<0 or col<0 or col == COLS or grid[row][col] !=1):
                        continue 
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -=1
            time +=1

        return time if fresh == 0 else -1 

        