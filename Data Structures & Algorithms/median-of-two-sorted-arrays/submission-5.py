class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left = 0
        right = len(A) - 1

        while True:
            # Partition A
            i = (left + right) // 2

            # Partition B so the left side has half the elements
            j = half - i - 2

            # Values immediately around the partitions
            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i + 1 < len(A) else float("inf")

            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j + 1 < len(B) else float("inf")

            #A[7,8,9,12,17]
            #B[5,6,10,19,20,23]
            # Correct partition
            if A_left <= B_right and B_left <= A_right:

                # Odd number of elements
                if total % 2:
                    return min(A_right, B_right)

                # Even number of elements
                left_max = max(A_left, B_left)
                right_min = min(A_right, B_right)

                return (left_max + right_min) / 2

            # A's partition is too far right
            elif A_left > B_right:
                right = i - 1

            # A's partition is too far left
            else:
                left = i + 1