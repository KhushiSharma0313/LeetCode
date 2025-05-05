class MedianFinder:

    #median = middle val of ordered int list 
    # median finder class initilaizse median finder object 
    # add num adds int num from data stream to data strcut
    # find median retruns median of elements so far
    # 

    #design data structure that can store numbers which is not constant
    # then find median 

    #brute force 
    #obvisous = insert in order 
    # if our array is always sorted, it;s easier to find median 
    #how to insert in order -> check each element, so every time O(n) operation 

    # but we're gonna use a heap, and divide in two subsets, where l <= r 
    # size of l and r are approx equal, only diff one
    # heap is similar to array, adding and removing element is O(logn) operation 
    # 2 tpyes -> max heap(find max is O(1)) and min heap (find min in O(1))
    # so small heap will be max heap, large heap will be min heap 
    # because median = max of small heap + min of larg heap // 2
    #what if sizes are unequal -> whicever heap has larger size get value from there 
    # by default add first element in small heap 
    # if heaps len have diff more than 1, transfer max from small heap or min from large heap 
    # keep checking if small heap elements <= large heap by taking max of small heap and comparing with min of large heap
    # if not true, tranfer 



    def __init__(self):
        #data structure is max heap for small and min heap for large 
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        #add num by default to small 
        heapq.heappush(self.small, -1* num)

        #elements of small > elements of large, push them to large 
        if(self.small and self.large and 
           -1* self.small[0] > self.large[0]):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)

        # if there's a size difference 
        if(len(self.small) > len(self.large) +1):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)

        if(len(self.large) > len(self.small) +1):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

        

    def findMedian(self) -> float:

        #median in small
        if(len(self.small)>len(self.large)):
            return self.small[0]

        #median in large 
        if(len(self.small) < len(self.large)):
            return self.large[0]

        if(len(self.small) == len(self.large)):
        #avg of max from small and min from large as median 
            return (-self.small[0]+ self.large[0]) /2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()