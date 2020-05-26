# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None: return None;
        
        odd= head
        even = head.next
        evenHead = even
        
        while True:
            if odd==None or even==None or even.next==None:
                odd.next=evenHead
                break
            
            odd.next=even.next
            odd=even.next
            
            if odd.next==None: 
                even.next=None
                odd.next= evenHead
                break
            
            even.next = odd.next
            even=odd.next
        return head
        
