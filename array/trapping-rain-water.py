class Solution:
    def trap(self, height: List[int]) -> int:
        #time = O(n)
        # height = 0,1,0,2
        # to trap water it must have boundaries on both sides
        # height of trap water = min(max(left boundary), max(right boundary)) - height of current boundary 
        # if height is negative, we can't hold water here
        # 2 approaches to solve the prob

        #1st approach, memory = O(n)
        #form the array of height and store info like maxleft and maxright for each element - O(n) time 
        #then store min(L,R)
        #water we can trap = min(l,r) - h[i] >= 0
        #add them all of each element of array and return

        #2nd approach, ,memory = O(1), using two pointer 
        # l =0, r = n-1
        # keeping track of maxL and maxR for each pointer 
        # shift the pointer that has smaller max value 
        # since it's prev position was smaller than right pointer, it's min(l,r) 
        # so intead of taking min(l,r) we're just gonna take max of whichever side is less, move it, and then 
        # maxl or maxr - current position height
        #if maxleft = maxright, shift anyone 
        

        #edge case 
        if not height:
            return 0
        #declaring variables
        res= 0 
        n = len(height)
        #two pointers 
        l,r = 0, n-1
        #max of both sides
        maxLeft, maxRight = height[l], height[r]

        while l < r: 
            #if maxleft is less we'll move left pointer, update maxleft and add trapp water in result 
            if maxLeft < maxRight:
                l+=1 
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            #if maxright is less, do the same for right pointer
            else:
                r-=1
                maxRight =max(maxRight, height[r])
                res += maxRight - height[r]

        return res


        