// this is two pointer problem
 //dummy points to the head
 // first ptr will be the current node 
 //second ptr prev
 // until curr is not null
 // check if curr needs to be deleted 
 // if yes, then prev points to curr.next 
 //  if not then, prev moves to curr and curr moves curr.nxt 

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* curr = head;
        ListNode* prev = dummy;

        while(curr != nullptr)
        {
            if(curr->val == val)
            {
                prev->next = curr->next;
            }
            else 
            {
                prev = curr;
            }
            curr = curr->next;
        }

        return dummy->next;
    }
};
