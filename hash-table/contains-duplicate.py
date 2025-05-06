# brute force
# taking one element going through the enitre array O(n^2)
# 1,1,1,2,2,3,3,4,4 => index 1 and go till index n-1 and check element before it 
# O(nlogn)
# set() has unique values 
# go through entire array and check if this is in set, and if it return truem and if not 
# add to to set and return false 
# time = O(n), space = O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)




# #hash set length 
# #time complexity = O(n)
# #space complexity = O(n)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)


# #hash set 
# #time complexity = O(n)
# #space complexity = O(n)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True 
#             seen.add(num)
#         return False


# #sorting 
# # time complexity = O(nlogn)
# # space complexity = O(1) or O(n) depending on sorting algo
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return False 
#         nums.sort()
#         if len(nums) == 2:
#             if nums[0] == nums[1]:
#                 return True 
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False
        

# #brute force 
# #time complexity = O(n^2)
# #space complexity = O(1)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#             return False
        
        