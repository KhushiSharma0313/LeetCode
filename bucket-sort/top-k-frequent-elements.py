class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #time = O(n)
        # array nums, int k 
        #return k most frequent elements 
        # example => 1,1,12,2,3, k =2, so return 2 most freq items output => 1,2
        # brute force 
        # take the element and it's freq and map them 
        #sort them from most freq to least
        # tim = O(nlogn)
        # if we do max heap 
        # so enter this in our heap 
        # then pop k times 
        # so it's klogn not n logn 

        #optimized sol = bucket sort 
        # itd only be O(n) if our values were bounded
        # but this is unbounded and top k values are still not clear
        # so we'll use an customzed bucket sort 
        # here key would be number of times it occured
        # and val would be list of values which occured this many times 
        #bound for key here would me max elements in the array, since count of occurences can't exceed that
        # to know topk, start from end of key array, max occureing to least, and k values from it 
        #so scan through it O(n) times 
        # so in worse case, if one key has list with all values, we'll iterate through them until we have k values
        #that's still O(n) 
        # so there's input array and hashmap for counting, so memory is also O(n)

        #hashmap for maintaining count of array 
        count = {} 

        res = []

        #array for frquency 
        freq = [[] for i in range(len(nums)+1)]

        #calculate count 
        for n in nums:
            #get values already or default to 0
            count[n] = 1 + count.get(n,0)
        
        #map freq to nums elements 
        for n,c in count.items():
            # the number is gonna be the index of frequency
            freq[c].append(n)
        
        #add top k value to our result 
        #iterating through freq in desc order, since we want most frequent first 
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                
                if len(res) ==k:
                    return res
        
        
        



        