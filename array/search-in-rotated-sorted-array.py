class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = sorted in asceding order, distinct 
        # nums possible rotated, with unknown pivot 1<=k<=len
        #exmple 0,1,2,4,5,6,7 to become 4,5,6,7,0,1,2 rotated by pivot index 3
        # after rotatedm and integer target, return index of target, if in nums otherise -1
        # example = [4,5,6,7,0,1,2], target = 0
        #time = O(logn)

        #brute force way would be linear search
        # intiuition is like binary search, but since this is not sorted, and rotated after sorted, how to unrotate it 

        #when sorted, left side > righside and both sides are sorted 
        # for binary search => left, right, middle and left <= right 
        # if we're in left sorted portion
        # and our target is in the middle, eliminage left portion 
        #if our target is less than middle, 2 conditions 
        # if it's less than nums[0] then it's not in left portion, run binary search in right part
        # if it's greater than or equal to nums[0],then run binary search in right part before middle 
        # 
        #if we're in right sorted part 
        # if target is middle return that
        # if target is greater than middle
        # if target <nums[n] run binary search in right part 
        # if target > nums[n] run binary search in left part 
        # if target is smaller than middle, move to left, don't worry about parts, just move to left
        
        #for the entire array we have left right and middle pointer
        #to check if middle is left part and which is right part
        # if L <= M, left part otherwise right part

        #left and right pointer indexes of array 
        l, r = 0, len(nums) -1

        #condition for binary search left is less than equal to right 
        while l<=r:
            m = (l+r) //2

            #if middle value is target 
            if target == nums[m]:
                return m #return index of target
            
            # check which portion is middle in 

            #middle is in left part 
            if nums[m] >= nums[l]:
                # if target is more than middle move to right part, or if target is less than leftmost eleemnt of left part, move to right part, since both are sorted 
                if target > nums[m] or target < nums[l]:
                    l = m +1
                #target is in left part 
                else: 
                    r = m-1 

            #middle in right part 
            else:
                #if tartet is less than mid or it's greater than rightmost val of right part, then it's in left part 
                if target < nums[m] or target > nums[r]: 
                    r = m-1 
                #it's in right part 
                else:
                    l = m+1
        
        #if it doesn't statisy these cond, it's not here
        return -1





