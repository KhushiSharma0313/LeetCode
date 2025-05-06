class TimeMap:
    # time base ds, sotre multiple val for same key at diff time 
    #and retireve key val at certain time stamp 
    # initialize ds
    # sotres key with val at timestamp 
    # returns s

    # key value pair like hasmap 
    # values are multiple, each value is pair with val and timestamp 
    # implement this using hashmap, key will be keys, and values will be list of vals 
    # for key find the key, then iterate throug the timestamps to find correct val 
    # if you don't find exact match for time, return the recent one which is closest and less than val itself 
    # time = O(1), set in hashamp is constant since we're setting it at the end of list
    # and for get we might need to scan through a list which is O(n)
    # we could do binary search, but then we'll need it to be sorted with takes O(nlogn) time
    # timestamp are going to be in increasing order 
    # so if we add timestamp at the end, it'll be sorted by default 
    # so we'll go binary search 

    def __init__(self):
        # hasmap where key is string, and value: tuple or pair or value and timestamp 
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #check if key exists 
        if key not in self.map:
            self.map[key] = [] #assign an empty list here 
        
        #append the values 
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # declare the string 
        res = ""
        #value of this key 
        val = self.map[key]
        # run binary search on this value to find exact or closer timestamp 
        l, r = 0, len(val) -1

        while l <=r:
            m = (l+r) //2
            #found the exact value 
            if val[m][1] == timestamp:
                res = val[m][0] # this is the value associated with timestamp 
                return res 
            elif val[m][1] < timestamp:
                res = val[m][0] # closer to timestamp, so valid value 
                l = m+1 
            else:
                #invalid value 
                r = m -1 
        
        return res 

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)