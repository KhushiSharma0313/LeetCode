# using a hashset since it only has unique elements 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False



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
        
        