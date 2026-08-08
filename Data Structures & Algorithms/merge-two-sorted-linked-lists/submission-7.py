# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1
        newList = ListNode()
        newListHead=newList
        while list1 or list2:
            if list2 is None or (list1 and list1.val < list2.val):
                newList.next = list1
                list1=list1.next
            else:
                newList.next=list2
                list2=list2.next
            newList=newList.next

        return newListHead.next