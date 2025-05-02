class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #array = nums, find contiguous subarray with max sum and return sum 
        # keep in mind it has both positive and negative numbers

        #O(n^3)
        #  brute force = compute sum of each subarray, so go from each element, create it's sub array with everyother element and compute sum 
        # pseudo code 
        # for ( i to n-1) - for each index 
        # for( j = i to n-1) - for computing this element go through each remaining element 
        # for(k = i to j) - to compute sum of each subarray 

        #O(n^2)
        # to save repepated work, instead of calculating sum of each sub array
        # we can calculate sum of one sub array, and just keep adding new elements to it 
        # current sum + current element = new sum 
        #pseudo code
        # for (i to n-1)- index of all elements
        # for (j = i to n -1) - for remaining elements 
        # current sum + num[j]

        # time = O(n)
        #do we have to compute every sub array starting from each element 
        # ignore negative number prefix of positive , since they're not imp for max sum
        # up until a point if total sum is negative ignore that
        # if at a point, prefix/ or sum if positive keep going, 
        #it's like sliding window 
        # keep incremeting right pointer, but fix the left pointer when we find prev to be positive 
        #left pointer only shifted when prefix is neagtive 

        maxSum = nums[0] #we gave it a value instead of 0, since this array also has negative value and is non empty
        currSum = 0

        for n in nums:

            # if prefix / sum until this point is negative, don't consider it and set it to 0
            if currSum <0:
                currSum = 0 
            
            currSum += n 
            maxSum = max(maxSum, currSum)
        return maxSum

        