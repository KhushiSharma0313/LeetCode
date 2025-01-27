class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach should be that 
        # to find diff for each number in array
        # then lookup that number in hashmap of the array, if it exists append to array, 
        # if not move on to next number
        result = {} # val: index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in result:
                return [result[diff], i]
            result[nums[i]] = i
        return





# #time complexity = O(n^2)
# #space complexity = O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # taking 1 number, then going to next number and checking if 1+2 = target or not, 
#         # check till 2nd last number only, and check with last number out of the loop
#         result = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     result.append(i)
#                     result.append(j)
#         return result
      