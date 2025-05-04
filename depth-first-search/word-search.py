class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # m*n grid board
        # string word
        # return true is exists 
        # word can be done from letter -> seq adjacent, where adjacent are horizontal or vertical 
        # example => abce, sfcs, adee, word = abcced, 

        # looking for path which makes this word 
        # use brute force way to backtrack 
        # so start from word[0] look for it in grid then look it's neighbours
        #left, right, up down, if we find great, not move to next word 
        # we can't go back 
        # here we'll do this recursively, or dfs 

        ROWS, COLS = len(board), len(board[0])

        #to know if a char is already visited 
        path = set()
        
        #we will go through each element using dfs and i is index of word 
        def dfs(r,c,i):

            if i ==len(word):
                return True 

            if (r<0 or c<0 # if row or col is out of bounds
                or r>=ROWS or c>=COLS
                or word[i] !=board[r][c]  # if it doesn match word 
                or (r,c) in path): # if it's already in path 
                return False 
            
            #it means this char matches word
            path.add((r,c))

            #run dfs in all four directions for next letter in word
            res = (dfs(r+1,c,i+1) or 
                    dfs(r-1,c,i+1) or 
                    dfs(r,c+1,i+1) or 
                    dfs(r,c-1,i+1))
            
            #if any of dfs is true it's gonna return true 
            return res
        
        #run dfs on all elements in grid
        for r in range(ROWS):
            for c in range (COLS):
                if dfs(r,c,0):
                    return True
        return False
