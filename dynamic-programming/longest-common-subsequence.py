#dp - bottom up 
# there's a grid of text 1 and text 2
# we start at the bottom of the grid
# then see if char matches, if yes we move diagonally in the grid
# if no match, we either move right or down
#we are sotring them in a grid so space is O(m*n)
#and we are check each element in grid so nested for loop so time compl = O(m*n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1)+1)] #plus one so that we have a base case 

        #going reverse, since we need to know at the top dp[0][0], what's max len 
        for i in range(len(text1) -1,-1,-1):
            for j in range(len(text2) -1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1] #1 + cause it matched
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


#time complexity = O(2^(m+n))
#space complexity = O(m+n)
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         #brute force way is to basically make a decision tree for two strings, when they don;t match
#         # then if they don't match, either go i+1 or j+1, whichever one has max matches ,go to that way
#         # if they do match, then move in bth strings 

#         def dfs(i,j):
#             if i==len(text1) or j == len(text2): #base case - if the pointer is at the end, then return 0
#                 return 0
#             if text1[i] == text2[j]:
#                 return 1 + dfs(i+1,j+1) # +1 cause it matches
#             else:
#                 return max(dfs(i+1,j),dfs(i,j+1))
#         return dfs(0,0)
        