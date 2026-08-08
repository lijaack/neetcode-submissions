# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast,slow= head,head
        while fast and slow:
            if fast == None:
                return False
            if fast.next:
                fast=fast.next.next  
            else: return False
            slow=slow.next
            if fast==slow:
                return True

        return False