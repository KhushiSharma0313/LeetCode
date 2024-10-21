/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        // l3 initial head is 0(dummy)
        //l1 and l2 
        // value = l1(v) + l2(v)
        // carry = value/10 - 
        // l3(next) = value%10 - 
        // all nodes in list becomes  equal to their next
        // l1 or l2
        // value = l1(v) or l2(v)
        // carry = value/10
        //l3(v) = value % 10 
        //if carry -> l3(v) = carry
        // return l3 head(0 dummy) next

        ListNode* l3 = new ListNode(0);
        int value;
        int carry = 0;
        ListNode* head = l3; 

        while(l1 && l2)
        {
            value = l1->val + l2->val + carry;
            carry = value/10;
            l3->next = new ListNode(value%10);
            l1 = l1->next;
            l2 = l2-> next;
            l3 = l3->next;
        }
        while(l1)
        {
            value = l1->val + carry;
            carry = value/10;
            l3->next = new ListNode(value%10);
            l1 = l1->next;
            l3 = l3->next;
        }
        while(l2)
        {
            value = l2->val + carry;
            carry = value/10;
            l3->next = new ListNode(value%10);
            l2 = l2->next;
            l3 = l3->next;
        }

        if(carry)
        {
            l3->next = new ListNode(carry);
            l3 = l3->next;
        }

        return head-> next;

        
    }
};