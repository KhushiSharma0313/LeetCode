#approach 
#hashmap, to store key value pair and keep track of key value pair 
# for value in hashmap, it points to the value of node instead of storing the value
#i want to keep track of most used and least used value of cache 
# i want to use doubly linked list 
# i want it to start with lru node and end with mru node, to keep track of them 
# whenever using get, i wanna move that to prev of mru so that it's mru
#whichever one was there swaps with it 
# for put, if capacity is less, remove lru next node, lru point to lru next to next now
# also update key of lru to now this new node's key and update it's value so it points to new node
#then the node is added at mru prev position, and mru prev is now this node's prev

class Node:
    def __init__(self,key,val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #hashmap 

        #lru = left, mru = right
        self.left, self.right = Node(0,0), Node(0,0) #initializing with no values
        #nodes must be connected to each other, so new node ocmes in between you guys 
        self.left.next = self.right
        self.right.prev = self.left
    
    #helper function to remove node in doubly linked list
    def remove(self,node):
        prev, nxt = node.prev, node.next  
        prev.next, nxt.prev = nxt, prev
    
    #helper function to insert nodes at rightmost postion before right pointer
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #removing key from current position 
            self.insert(self.cache[key]) #inserting it so it becomes mru 
            return self.cache[key].val #returning the value of key 
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #removing the exisiting key to make the key val pair 
        self.cache[key] = Node(key,value) #create new node with key val pair 
        self.insert(self.cache[key]) #since its doubly linked list, inserting value in the linked list 

        #remove lru from list and delete from hash map if capacity is less than cache len 
        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]



        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)