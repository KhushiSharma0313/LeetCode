# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # non empty non neg linked list -> digits in reverse order
        # sum them and return linked list 
        # example - [2,4,3], [5,6,4] = [7,0,8] 342 + 456
        # need to know how you sum numbers -> sum them or take carry 
        # interate through both nodes and add them to new linked list node 
        # if res greater than 9, add carry to next node
        # if linked list are of diff lenght, assume it's a zero for all remaining nodes where they don't have node from 2nd linked list 
        # if you have a carry, but no remaining nodes, create a node for the carry 

        #new linked list 
        dummy = ListNode()
        curr = dummy 

        #carry for addition 
        carry = 0

        # until either linked list is empty, or if it has carry but no node remaining, create another node just for carry 
        while l1 or l2 or carry:

            #values of both lists 
            v1 = l1.val if l1 else 0 # if l1 is null put 0 as its value 
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry 

            #what if this value is larger than 10 
            carry = val // 10 
            val = val%10

            #update pointers
            curr = curr.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        
        return dummy.next