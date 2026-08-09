# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        currDummy=dummy

        #hold k length nodes
        hold = head 
        currHold=hold
        #k counter
        currK = 1
        while currHold and currHold.next:
            currHold=currHold.next
            currK+=1
            if currK == k:
                temp=currHold.next
                currHold.next = None
                reversedGroup = self.reverseGroup(hold)
                
                currDummy.next=reversedGroup
                while currDummy.next:
                    currDummy=currDummy.next
                hold=temp
                currHold=hold
                currK=1

        if(hold):
            currDummy.next=hold
        return dummy.next

    def reverseGroup(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
