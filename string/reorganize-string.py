class Solution:
    def reorganizeString(self, s: str) -> str:
        #time = O(nlogn)
        #space = O(n)
        # approach 1 - use hashmap since we're counting the occurences 
        # start with most frequent character 
        # then keep arranging based on occurences and cycle through
        # this won't work cause if we don't most occurence twise, it will arrage same character together 
        # so first do most occurence, then put it on hold, check prev element, and do element diff than that

        # if we just do hashmap , then it'll take O(n^2) time to go through most occurence and then keeping track of prev
        #space will be O(26) if just characcters otherwise will be O(n)
        # to optimize this, we can store it in a heap, and max heap can have most occurences at first to pop out 
        #since python doesn't have by default max heap, we;ll use min heap, negate the occurences, and increment instead of decrement 

        count = Counter(s) #using in built data structure of hashmap, which counts occurnece of char
        maxHeap = [[-cnt, char] for char,cnt in count.items() ] # declaring max heap in list comprehension, getting values from counter and negating the count 

        #heapify this into min heap , this takes O(n)
        heapq.heapify(maxHeap)

        #declare elements 
        prev = None
        res = ""

        #we want to max occurences until either prev is null or heap is null
        while prev or maxHeap:

            #if string is invalid, we're gonna have values in our prev, but not in our heap, cause the condition does not match 
            if prev and not maxHeap:
                return ""

            #pop most occurence char 
            cnt, char = heapq.heappop(maxHeap)
            res += char #add this char to result string
            cnt +=1 #increment count since this is min heap and our occurnece are negative 

            #if prev already had a value, add it back to the heap so we don't override it 
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None # set it back to non 

            # if count is 0, we're not gonna add it back to the heap
            if cnt !=0:
                prev = [cnt, char]
        
        return res




        