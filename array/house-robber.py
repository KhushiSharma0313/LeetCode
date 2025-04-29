class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp - bottom up approach 
        #we'll start at nums[0], and nums[1], then we'll loop from 2 to n
        #decide max between nums[i] + dp pf alter, or dp of next element 
        #return dp of last element 
        if(len(nums) == 0):
            return 0
        elif(len(nums)==1):
            return nums[0]
        elif(len(nums)==2):
            return max(nums[0],nums[1])
        
        n = len(nums)
        dp = [0]*n #declare array with 0s and size n

        #base cases
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        #return last element of dp
        return dp[n]
        



        # brute force, for each way there's 2 decisions, rob or not to rob 
        # if we rob 1, then we'll 3, otherwise we'll rob 2, if we rob 2 then we'll rob 1, and max of these decisions
        # if  we go out of bounds, we get 0, our base case
        # we can do recursion, and choose max of num[i] + dfs[i+2], dfs[i+1]
        