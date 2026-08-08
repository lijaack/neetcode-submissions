# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Keep merging pairs of lists until only one remains
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(self.merge_two_lists(list1, list2))

            lists = merged_lists

        return lists[0]

    def merge_two_lists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach whatever is left
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
