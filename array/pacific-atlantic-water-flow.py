class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #m*n rect island, borders pacific and stantic ocean
        # pacific touched island left and top edge
        # atlantic touches right and bottom
        # island = square cells 
        # heights[r][c] height obver sea level at coordinate r,c 
        # if negh cheight <= curr height, water can flow from any cell adjacent to ocean 
        # retrun 2d grid where re = ri,ci rainwater flow cell to both pacific and atantic ocean 

        # check for each cell can it reach the atlantic(right and bottom) and pacific ocean(top and left), if yes add to result
        # cell can only ove where adj element has height less or eq to them 

        #brute force - go to every position, and check if it can flow in diff direction using dfs/bfs 
        # time = O(n*m )^2

        #optimized way
        # start from pacific ocean, and check nodes that border it ,they can reach pacific ocean 
        # starting from these nodes, figure out which other nodes inside can reach pacific ocean 
        # do the same with atantic ocean, start from the boundary nodes and go back in 
        # now find common between both and return those 
        #we're not gonna revisit same nodes 
        # so time = O(n*m)
        # since we're starting from border and going in, 
        # the rule that water can flow in if adj nodes are less than you will be reversed and we'll check which nodes are bigger 

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        #helper function dfs 
        def dfs(r,c,visit, prevHeight):

            #check if it's out of bounds or if it's height is valid or if it's already in visit 
            if((r,c) in visit
               or r<0 or c<0
               or r==ROWS or c==COLS
               or heights[r][c] < prevHeight):
               return 
            
            visit.add((r,c))

            #run dfs in all 4 directions 
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        # check first rows and last row and run dfs 
        for c in range(ROWS):
            dfs(0,c,pac, heights[0][c])
            dfs(ROWS-1,c,atl, heights[ROWS-1][c])  

        # check first col and last col and run dfs 
        for r in range(COLS):
            dfs(r,0,pac, heights[r][0])
            dfs(r,COLS-1,atl, heights[r][COLS-1])

        
        res =[]

        #go through each node and check if it's in both sets       
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
