class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #time - O(n), memory - O(n) due to set 
        # string s, longest substring without duplicate
        # substring - contiguous non empty set of string 
        #e.g. = s "abcabcbb" output = 3
        #we need substring so we can't sort them
        # brute force - checking each substring, if it doesn't have duplicate, and return max 
        # when we check substring starting at char a, if we find it has duplicate, we don't need to go any further
        #use sliding window 
        # we can use set for knowing duplicate, since it only contains unique character 
        # 

        #declare a set 
        charSet = set()
        res = 0
        #left pointer starting at index 0
        l = 0

        if len(s) == 0:
            return 0

        #iterating through right pointer in string 

        for r in range(len(s)):
            #until there's char already in set, you keep moving left pointer and interating it 
            # 
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])

            res = max(res,len(charSet))
        return res