class RandomizedSet:

    def __init__(self):
        # randomized set object is initialized 
        # inserts val into set if not present, true if present, false 
        # remove item val from set if present, true if present otherwise false 
        # get random return random element from current set of elements 
        #(at least on elem exists wjen this method is called)
        # each element same prob of being returned 
        # each function O(1) time 

        # approach 
        # take insert and remove using data structure hash set 
        # check if val exist or not using hash set 
        # for get random, 
        # brute force - get indices of all elements and then use get random value using built in lib
        # but we can't get index in hashset, they're unordered
        # we can't just maintain a hashset, se need to maintain a list as well
        # when we add to hashset, also add to list 
        # but now for removing an element, in case of a list it'd take O(n) time instead of O(1) time 
        # how about we use hashmap instead, mapping each val to its index 
        # now for removing, we'll first copy last val from array and put it at index which is rempved
        # then delete last val from last position since that only takes O(1) time 
        # now update the mapping of hash map 

        #hashmap with values mapping to index in list 
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        # check if val exists or not 
        res = val not in self.numMap 

        # if it doesn't exist, insert 
        if res:
            #map value to index
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res
        

    def remove(self, val: int) -> bool:
        # check if val exists
        res = val in self.numMap 

        # if it exisits , we need to remove it 
        if res:
            # index of current value 
            idx = self.numMap[val]
            # last value in the list 
            lastVal = self.numList[-1]
            # copy last val from its positon to current val
            self.numList[idx] = lastVal 
            # removing last val from list since it takes O(1)
            self.numList.pop()
            # mapping new value to it's index in hashmap 
            self.numMap[lastVal] = idx
            # remove element from hashmap  
            del self.numMap[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()