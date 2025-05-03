class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #n ppiles of bananas 
        # ith pile has piles[i] bananas 
        # guards come back in h hours 
        # bananas per hour eating speed of k
        # each hour choose pile, eats k banana from pile
        # if pile has less than k, eat alll of them 
        # eat slowly but finish all
        #return minimum k so she can eat bananas within h hours 
        # piles = [3,6,7,11] h =8
        # start with min of array, because below that is not possible, 
        #binary search sol

        #max koko can eat entire pile in one hours 
        # h must be greater than equal to len(P) to eat all bananas 
        #return when koko can fnish all piles min k 

        #brute force =>start with k=1, keep going until she can finish all bananas 
        #max for k = max element in piles 
        # if we do k max, hours it will take us will be less than h cause h >= len(P) and in this case hours will be len(P)
        #start fron k =1 to k max, stop when we eat bananas less than eq to h hours 
        #time = O(max(P)*P) interating through P for each val of k 
        # if we find k using binary search instead of linear search time = O(log(max(P)*P)
        #apprach for binary search
        #form an array for k => k -1 to k max
        # l = k[0], r = k[n], mid = l+r//2
        # check for mid to eat all bananas in less than eq hours than h 
        # divide mid to each number in piles and round up and add them, that's number of hours 
        # if hours < h move binary search in left part of k, otherwise right part 
        # when we shift our left or right pointer, we leave the other part behined and not gonna be onsider everrr

        #left and right pointer for k values possible 
        l, r = 1, max(piles)
        #result max possible value is maxp
        res = max(piles)
        #hours gonna take initially is 0 

        # if(len(piles)==0):
        #     return 0


        while l <= r:
            k = (l+r)//2
            hour = 0
            
            #now interate through each pile to calculate number of hours 
            for p in piles:
                hour += math.ceil(p/k)
            
            #if we find the k where we can complete bananas in given hours 
            if hour<=h:
                    res = min(k,res)
                    #move pointet to left part
                    r = k-1
            else:
                l = k+1 
            
        return res



        