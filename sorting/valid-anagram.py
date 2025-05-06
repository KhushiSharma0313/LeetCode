# anagram = both words contain same letters 
# brute force = take element from one string and go over other string to check if it matches 
# sorting them and then checking if they match => yes O(nlogn)
# same letters and count of letters is equal 
# hasmap to map count of letter to actual letters, and if they match then anagram 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # key is char, and value is count 
        sMap = {} #hashmap for string s to map count to char 
        tMap = {} #hashmap for string t to map count to char 

        # if unequal length of string, not anagrams 
        if len(s) != len(t):
            return False 

        #filling the hashmap 
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i],0)
            tMap[t[i]] = 1 + tMap.get(t[i],0)
        
        #check if both hashmap match by iteratng through each value 
        for i in sMap:
            if sMap[i] != tMap.get(i,0):
                return False
        
        return True

# #we build a hashmap, where key = the char, value = occurence, and if both match, it's anamgram
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if(len(s) != len(t)):
#             return False
#         countS, countT = {}, {} #hashmaps 

# #filling the hapshmap with key of char and value of occurence in s and t 
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i],0) #get is lookup function, if not found defaut is 0
#             countT[t[i]] = 1 + countT.get(t[i],0) 
        
#         #check if both hashmaps match
#         for c in countS:
#             if countS[c] != countT.get(c,0):
#                 return False 
#         return True
        

# #hashmap 
# # class Solution:
# #     def isAnagram(self, s: str, t: str) -> bool:
# #         # Counter is a data structure which is a hashmap that counts the occurences itself, so the sol below can be written in one line
# #         return Counter(s) == Counter(t)

# # #hash table 
# # time complexity = O(s+t), since we're iterating through both hashmaps
# # space compleixty = O(s+t), since we're building 2 hashmaps size of s and t 
# # class Solution:
# #     def isAnagram(self, s: str, t: str) -> bool:
# #         if len(s)!= len(t):
# #             return False
# #         countS, countT = {}, {}

# #         #Formation of hashmaps counting occurences of each character in both strings
# #         #we're using get() to avoid key error, so that if the key doesn't exist we return 0
# #         for i in range(len(s)):
# #             countS[s[i]] = 1 + countS.get(s[i],0)
# #             countT[t[i]] = 1 + countT.get(t[i],0)
        
# #         #Checking if occurence of each charachter(which is value here) and each chcaracter(which is key here) are equal in both strings, if not return false
# #         for c in countS:
# #             if countS[c] != countT.get(c, 0):
# #                 return False
# #         return True


# #brute force and sorting
# #time complexity = O(nlogn+ mlogm)
# #space complexity = O(1) or O(n) depending on sorting technique
# # class Solution:
# #     def isAnagram(self, s: str, t: str) -> bool:
# #         if len(s) != len(t):
# #             return False 
        
# #         return sorted(s) == sorted(t)
        