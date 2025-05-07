
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # approach is similar to merge sort 
        # k => k/2 => k/4 ... 1 list (O(nlogn))
        #helper function 
        def mergeList(l1,l2):
            dummy = ListNode()
            curr = dummy 

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1 
                 

            if l2:
                curr.next = l2 
                

            return dummy.next 

                #edge case
        if not lists or len(lists) ==0:
            return None
        
        # merge lists until 1  
        while len(lists) >1:
            res = []
            for i in range(0,len(lists),2):
                next_list = lists[i+1] if i+1 in range(len(lists)) else None
                res.append(mergeList(lists[i], next_list))
            
            lists = res 
        
        return lists[0]


            



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next







        #for linked list with only one node, imagine a merge sort/divide and conquer type algo 
        #brute force 
        #first sort first two node, then add one and sort it and so on
        # this is not super effiecient, as we have k lists and every time we're merging it take k*n time 

        # instead merge 2 linked lists at a time, then merge 2 and so on
        # so from k linked list we went to k/2 linked list to k/4 to k/8 until 1
        #height of this tree is log k
        #each layer have n, n/2, n/4 .... nodes
        # so time complexiy is nlogk

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            
#         def mergeList(l1,l2):
#             dummy = ListNode()
#             tail = dummy 

#             while l1 and l2:
#                 if l1.val < l2.val:
#                     tail.next = l1
#                     l1 = l1.next
#                 else:
#                     tail.next = l2
#                     l2 = l2.next 
#                 tail = tail.next 
            
#             if l1:
#                 tail.next = l1
            
#             if l2:
#                 tail.next = l2
            
#             return dummy.next

#         #edge case
#         if not lists or len(lists) ==0:
#             return None


#         #we want to merge lists until there's only one list  
#         while len(lists) > 1:
#             res = []
#             #iterate through pairs of linked list 
#             for i in range(0,len(lists),2):
#                 l1 = lists[i]
#                 l2 = lists[i+1] if i+1 < len(lists) else None #next list only valid if it's in bounds 
#                 #add merge sorted listed in the result 
#                 res.append(mergeList(l1,l2))
#             lists = res 

#         return lists[0]

        