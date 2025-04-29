class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #brute force way is to basically make a decision tree for two strings, when they don;t match
        # then if they don't match, either go i+1 or j+1, whichever one has max matches ,go to that way
        # if they do match, then move in bth strings 

        def dfs(i,j):
            if i==len(text1) or j == len(text2): #base case - if the pointer is at the end, then return 0
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i+1,j+1) # +1 cause it matches
            else:
                return max(dfs(i+1,j),dfs(i,j+1))
        return dfs(0,0)
        