class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # brute force - check each window for each element 
        # we can use sliding window = O(n) and add it to hashset = O(k)

        #hasset to check duplicate 
        window = set()
        #left pointer
        l = 0

        # iterating through nums with right pointer
        for r in range(len(nums)):
            #if window is too big shift left pointer 
            if r - l > k:
                window.remove(nums[l])
                l +=1
            
            if nums[r] in window:
                return True 
            window.add(nums[r])

        return False

        