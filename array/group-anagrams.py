class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # how to know if multiple words are anagrams
        # n(mlogm)
        # nat, tan => same letters and same count of letters 
        # count a bc... value = list of strings 
        # key count[1,0,1] size = 26
        # list = strings 

        res = defaultdict(list) # key is count and value is string 

        #iterating through each word
        for s in strs:
            count = [0]*26 
            #iterating through each letter 
            for c in s:
                #index letters a to z as 0,1...26
                count[ord(c) - ord("a")] += 1
                #it matches the count, so it has been appended
            res[tuple(count)].append(s)
        
        return list(res.values())
             




# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # group together anagrams any order 
#         # how to know anagrams, if we take both words and sort them and they're same they're anagrams 
#         # sorting take O(nlogn)
#         # and we need to do this m times = number of strings 
#         # total = O(mnlogn )

#         # better?
#         # use hashmap where key is count from a to z 
#         # value is strings who match this count, they're anagrams together 

#         # time = O(m*n*26) where m = number of strings, n = len of each word, 26 = range of hashmap 

#         res = defaultdict(list)

#         for s in strs:
#             #index from  0 to 25 for each alphabet
#             count = [0] * 26

#             for c in s:
#                 count[ord(c) - ord("a")] +=1 #index from 0 to 25 for lowerccase alphabet 
            
#             #add the string with this particular count 
#             res[tuple(count)].append(s) 
            
#         return list(res.values())


        