class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #declaring rows and cols 
        ROWS, COLS = len(grid), len(grid[0])
        island = 0 # counting how many islands total
        visit = set() # we don't revisit a node
        directions = [[1,0],[-1,0],[0,1],[0,-1]]  

        #helper function to run dfs recursively 
        def dfs(r,c):
            if (r,c) in visit:
                return 
            visit.add((r,c))
            
            #run dfs on its neighbours 
            for dr,dc in directions:
                # rows and col of next element 
                row = dr + r
                col = dc + c
                if (row in range(ROWS) and col in range(COLS)
                    and (row,col) not in visit 
                    and grid[row][col] == "1") :
                    dfs(row,col)
            

        #run dfs on each
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visit and grid[i][j] == "1":
                    dfs(i,j)
                    island +=1

        return island 

        




# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # we go to 1, then look in all direction, if in any direction it has 1, we go there and so on
#         # when no direction has 1, it's one island
#         # then we look at remaining 1s
#         # to not lose track of islands and reount, we'll store the visited ones in a set 
#         # it's basically dfs 

#         island = 0
#         visited = set() # for 1s that are visited 
#         rows = len(grid)
#         cols = len(grid[0])

#  #helper function dfs, taking coordinates as input 
#         def dfs(r,c):
#             if (r,c) in visited:
#                 return 
#             visited.add((r,c))
#             directions = [[1,0],[0,1],[-1,0],[0,-1]] # up, right, down, left

#             # dr to move in row, dc to move in col 
#             for dr, dc in directions:
#                 nr = dr + r # adding direction in row coord, moving up or down 
#                 nc = dc + c # adding direction in col coord, moving  left or right 

#                 if(nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1"):
#                     dfs(nr,nc) #running dfs recursivley until all 1s visited 

#         # point to point and run dfs if it's 1 and not visited
#         for r in range(rows):
#             for c in range(cols):
#                 if((r,c) not in visited and grid[r][c] == "1"):
#                     dfs(r,c)
#                     island +=1

#         return island






        


        # #when we visited island 1st, we need to look for its adjacent piece being land too 
        # # for that we'll use bfs 
        # #
        # if not grid: # if it's not a grid
        #     return 0
        
        # rows, cols = len(grid), len(grid[0]) #defining rows and cols 
        # visit = set() #for visited elements 
        # islands = 0 #to count n.o of islands 

        # def bfs(r,c): #iterative algo
        #     q = collections.deque() #declaring a queue, since we need data struc to store visited nodes
        #     visit.add((r,c)) #add the node in visit set 
        #     q.append((r,c)) #add node in queue too 

        #     while q: #while q is not empty
        #         row, col = q.popleft() # pop leftmost cell from queue
        #          #if we do pop instead of pop left it will become dfs, iterative 
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]] #dir for right, left, up, down 
        #         for dr, dc in directions: # dr and dc are 1 and 2nd value of each direction pair
        #             r = row+dr #move in rows
        #             c= col+dc #move in cols 
        #             if(r in range(rows) and #check if row is in bound 
        #                c in range(cols) and #check if col is in bound 
        #                grid[r][c] == "1" and #check if it's land 
        #                (r,c) not in visit): #if its visited or not 
        #                q.append((r,c))
        #                visit.add((r,c)) 

        # for r in range(rows): #iterate r in rows
        #     for c in range(cols): #iterate c in cols
        #         if(grid[r][c] == "1") and (r,c) not in visit: #if its a land and if it hasn't been visited already 
        #             bfs(r,c) # run bfs algorithm on it 
        #             islands +=1 #iterate through the loop 
        # return islands 

        