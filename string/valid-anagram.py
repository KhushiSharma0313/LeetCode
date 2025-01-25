class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter is a data structure which is a hashmap that counts the occurences itself, so the sol below can be written in one line
        return Counter(s) == Counter(t)

# #hash table 
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s)!= len(t):
#             return False
#         countS, countT = {}, {}

#         #Formation of hashmaps counting occurences of each character in both strings
#         #we're using get() to avoid key error, so that if the key doesn't exist we return 0
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i],0)
#             countT[t[i]] = 1 + countT.get(t[i],0)
        
#         #Checking if occurence of each charachter(which is value here) and each chcaracter(which is key here) are equal in both strings, if not return false
#         for c in countS:
#             if countS[c] != countT.get(c, 0):
#                 return False
#         return True




#brute force and sorting
#time complexity = O(nlogn+ mlogm)
#space complexity = O(1) or O(n) depending on sorting technique
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False 
        
#         return sorted(s) == sorted(t)
        