#hash table 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(s) == set(t)

#brute force and sorting
#time complexity = O(nlogn+ mlogm)
#space complexity = O(1) or O(n) depending on sorting technique
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False 
        
#         return sorted(s) == sorted(t)
        