class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #when we visited island 1st, we need to look for its adjacent piece being land too 
        # for that we'll use bfs 
        #
        if not grid: # if it's not a grid
            return 0
        
        rows, cols = len(grid), len(grid[0]) #defining rows and cols 
        visit = set() #for visited elements 
        islands = 0 #to count n.o of islands 

        def bfs(r,c): #iterative algo
            q = collections.deque() #declaring a queue, since we need data struc to store visited nodes
            visit.add((r,c)) #add the node in visit set 
            q.append((r,c)) #add node in queue too 

            while q: #while q is not empty
                row, col = q.pop() #if we do pop instead of pop left it will become dfs, iterative 
                directions = [[1,0],[-1,0],[0,1],[0,-1]] #dir for right, left, up, down 
                for dr, dc in directions: 
                    r = row+dr
                    c= col+dc
                    if(r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == "1" and
                       (r,c) not in visit):
                       q.append((r,c))
                       visit.add((r,c)) 

        for r in range(rows): #iterate r in rows
            for c in range(cols): #iterate c in cols
                if(grid[r][c] == "1") and (r,c) not in visit: #if its a land and if it hasn't been visited already 
                    bfs(r,c) # run bfs algorithm on it 
                    islands +=1 #iterate through the loop 
        return islands 

        