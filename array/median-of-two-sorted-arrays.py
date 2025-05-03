class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # take two sorted array, maybe diff sizes
        # merge them together and keep the sorting
        # now return median, if odd the middle eleemnt, if not both element's avg 
        # do it in O(log(m+n)) time 

        #if someone wants log algo, use a binary search cause even merging them is gonna take n time, which ain't ideal 
        # median is when both sides it has equal elements 
        # left partition size = right parition size 
        #if total is even
        #  divide in left and right partiton, take rightmost val of left part and leftmost val of right part and take avg
        #how to do that without merging 
        # find left partition from array 1 and 2, 
        # a1 = n1--|---m1
        #a2 = n2--|---m2
       

        #for len of leftpart of a1 = 0 + n/2 and then round down , and that's the index of our median  
        #now left part is  to median 
        # then half = len(m+n)/2 round down for half 
        # so len of left partition in array2 = half - len(leftpart(array1))
        #how to know if they're correct 
        # we want them to be in order 
        # values in left part in a1 and a2 are goona be less than values to their right 
        # to know that coolectively right part of a1 and a2 is greater than left part

        # take rightmost val of leftpart in a1, and compare with leftmost val of rightpart in a2  and vice versa 
        # if not true then update l and r pointers, l = 1 + middle value
        #now recompute the median
        # now update left part and right part accordingly same steps but diff values 

        #if len is odd
        # to find the median = min(leftmost val of right part in a1, a2)
        #if len is even median = avg(max value in left part, min val in right part)
        # so take max of left part from a1 and a2 i.e max between rightmst val in left part 
        #min of right part in a1 and s2, min 
        A,B = nums1, nums2
        total = len(nums1) + len(nums2) #total length of combined array
        half = total // 2 #half for knowing number of elements in both left and right partition 

        #make sure A is smaller array than b
        if len(A) > len(B):
            #swap 
            A,B = B, A
        
        l, r = 0, len(A) -1 

        #while this is true, which it is, because every array will have a median 
        while True:
            #index of median of A 
            i = (l+r) //2
            #index of median of B
            j = half - i -2 #since both i and j are index and they're starting at 0, -1 for both of them 

            #check if partition is correct

            # A left partition's rightmost element 
            Aleft = A[i] if i >=0 else float("-infinity") # if it's out of bounds of array 

            #A right partition's leftmost element 
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")

            # B left partition's rightmost element
            Bleft = B[j] if j >=0 else float("-infinity") # if it's out of bounds of array 

            #B right partition left most element 
            Bright = B[j+1] if (j+1) < len(B) else float("infinity") # if it's out of bounds of array 

            
            #partition is correct 
            if Aleft<= Bright and Aright >= Bleft:

                #odd = min of leftmost val in right part in a and b 
                if total % 2:
                    return min(Aright, Bright)
                
                #even => nedian = avg of max value of left part and min in right part 
                return (max(Aleft,Bleft) + min(Aright,Bright) ) /2
            
            #partition is not correct 
            #left partition too big 
            elif Aleft > Bright:
                r = i-1
            #right partition too big 
            else:
                l = i+1





        