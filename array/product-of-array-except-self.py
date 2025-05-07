class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for prod apart from itself we need to take product of prefix and postfix 
        # then multiply together and that's prod except itself 
        prefix = 1 #  by default it's 1 for every element 
        res = [1] *len(nums)

        # left to right interable to calculate prefix   
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        # right to left, to calculate postfix 
        for j in range(len(nums)-1, -1, -1):
            #res already has prefix, now multiply by postfix
            res[j]  *= postfix 
            postfix *= nums[j]

        return res



# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # answer[i] = prod of all elements except self - fit in 32 bit int 
#         # run in O(n) without division operation 
#         # example = 1,2,3,4 output = 24, 12, 8, 6
#         # using division operator = take prduct of all elements, then divide with each element to teir answer[i]
#         # so other way 
#         # take prod of value before i, and prod of value after i, then multiply together 
#         # so use prefix prod and postfix prod and compute them in O(n)
#         # for prefix, go left to right and multiply by its left neighbour and vice versa for postfix 
#         # prefix of leftmost and rightmost val is the 1 
#         # output = multiply prefix of value before it and postfix of value after it 
#         # now this time = O(n) but memory is O(n) also 

#         #optimized 
#         # so instead we could do memory = O(1)
#         # so don't use prefix or postfix arry and compute it all in output array 
#         # 2 passes in our input array 
#         # first run is computing prefix, now prefix[i] will be sotred in output[i+1], and 
#         # since 1st value doesn't have prefix, output[0] will be empty 
#         # now 2nd pass compute postfix and postfix[i] = output[i-1] ( multiply this val to existing val in array )

#         # result array 
#         res = [1] *len(nums)
#         prefix = 1
#         # to calculate prefix 
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *=nums[i]

#         postfix =1
#         #calculate postfix 
#         for i in range(len(nums)-1, -1, -1):
#             res[i] *= postfix #multipling with values exisiting 
#             postfix *= nums[i] 
        
#         return res

