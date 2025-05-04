# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #brute force, is doing comparisions of one node from l1 to every node until lk
        # O(nk)
        # can we do better 
        # 1,4,5 [1,3,4], [2,6], [7,8,9]
        # 1,4,5 with 1,3,4, then [2,6] [7,8,9]
        # we start from k lists -> k/2 lists -> k/4 lists .... 
        # time = nlogK

        #helper function to merge 2 lists 
        def mergeList(l1, l2):
            dummy = ListNode()
            curr = dummy 

            #when both lists are not empty
            while l1 and l2:
                #when l1 node is smaller
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                #when l2 node is smaller
                else:
                    curr.next = l2
                    l2 = l2.next 
                
                curr = curr.next 
            
            #if l2 is empty 
            if l1:
                curr.next = l1
                curr = curr.next

            #if l1 is empty 
            if l2:
                curr.next = l2
                curr = curr.next
            
            return dummy.next 

        

        if not lists or len(lists) == 0:
            return None

        #do this until we have one list 
        while len(lists) >1:
            res = []
            #compare listi, list i+1
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                res.append(mergeList(l1,l2)) 
            
            lists = res
 
        
        return lists[0]
        












        # #for linked list with only one node, imagine a merge sort/divide and conquer type algo 
        # #brute force 
        # #first sort first two node, then add one and sort it and so on
        # # this is not super effiecient, as we have k lists and every time we're merging it take k*n time 

        # # instead merge 2 linked lists at a time, then merge 2 and so on
        # # so from k linked list we went to k/2 linked list to k/4 to k/8 until 1
        # #height of this tree is log k
        # #each layer have n, n/2, n/4 .... nodes
        # # so time complexiy is nlogk

                
        # def mergeList(l1,l2):
        #     dummy = ListNode()
        #     tail = dummy 

        #     while l1 and l2:
        #         if l1.val < l2.val:
        #             tail.next = l1
        #             l1 = l1.next
        #         else:
        #             tail.next = l2
        #             l2 = l2.next 
        #         tail = tail.next 
            
        #     if l1:
        #         tail.next = l1
            
        #     if l2:
        #         tail.next = l2
            
        #     return dummy.next

        # #edge case
        # if not lists or len(lists) ==0:
        #     return None


        # #we want to merge lists until there's only one list  
        # while len(lists) > 1:
        #     res = []
        #     #iterate through pairs of linked list 
        #     for i in range(0,len(lists),2):
        #         l1 = lists[i]
        #         l2 = lists[i+1] if i+1 < len(lists) else None #next list only valid if it's in bounds 
        #         #add merge sorted listed in the result 
        #         res.append(mergeList(l1,l2))
        #     lists = res 

        # return lists[0]

        