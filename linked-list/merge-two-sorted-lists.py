# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force approach 
        # 1 and 1 -> 1 get in list3
        # 1 -> 3 -> 1 in list 3
        #2,3 -> 2 in l3
        #  
        # optimized approach 
        # 1, 1 & 2,3 & 4,4
        # 1,1, 2,3 & 4,4, 
        # 1,1,2,3,4,4
        # n -> n/2 -> n/4 => logn 
        dummy = ListNode()
        curr = dummy 

        #when both lists exist
        while list1 and list2: 

            # list 1 element is smaller 
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            #list 2 node is smaller
            else: 
                curr.next = list2
                list2 = list2.next 
            curr = curr.next 
        
        #when list2 is empty 
        if list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next 

        #when list1 is empty 
        if list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next 
        
        return dummy.next



        # #create new sorted list
        # #create them usign the linked list given not its copies 

        # #avoid edge case by adding a dummy node to your output, since initially your output is empty
        # #for each index compare values from l1 and l2, whichever one is smaller is intserted in l3
        # # bigger one gets compared by val from another list next index 
        # #if there are no values left in l2, insert all elements from l2 and viceversa 

        # #divide and conquer algo
        # #also used in sorting algos 
        # dummy = ListNode()
        # tail = dummy 

        # #when both lists are non empty
        # while list1 and list2:
        #     #if val from l1 is less insert that in our linked list
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         #interating to next node 
        #         list1 = list1.next 
        #         #if list2 node is less 
        #     else: 
        #         tail.next = list2
        #         list2 = list2.next 
        #     tail = tail.next 

        # #if only elements from list 1 is left, you can add them directly to tail, since it's already sorted
        # if list1:
        #     tail.next = list1
        # elif list2:
        #     tail.next = list2

        # return dummy.next           

