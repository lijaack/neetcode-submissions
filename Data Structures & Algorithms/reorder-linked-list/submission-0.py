# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next 
        slow.next = None

        # Reverse the second half
        reverse = None
        while second:
            temp = second.next
            second.next = reverse
            reverse = second
            second = temp

        # Merge the two halves
        first = head
        second = reverse

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
