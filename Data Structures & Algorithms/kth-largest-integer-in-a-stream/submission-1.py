import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # Store the numbers as our min-heap
        # and remember k (for example, k = 3)
        self.minHeap = nums
        self.k = k

        # Convert nums into a min-heap.
        # The SMALLEST number will always be at index 0.
        #
        # Example:
        # nums = [1, 2, 3, 3]
        # after heapify, the heap contains the same values
        # but is organized as a min-heap.
        heapq.heapify(self.minHeap)

        # We only want to keep the k largest numbers.
        #
        # If k = 3 and we have 4 numbers:
        # [1, 2, 3, 3]
        #
        # Remove the smallest (1):
        # [2, 3, 3]
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:

        # Add the new number to the min-heap.
        heapq.heappush(self.minHeap, val)

        # If we now have more than k numbers,
        # remove the SMALLEST one.
        #
        # Example:
        # [2, 3, 3] + 5
        # → [2, 3, 3, 5]
        #
        # Too many numbers, so remove 2:
        # → [3, 3, 5]
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Because we ALWAYS keep only the k largest numbers,
        # the smallest number inside the heap is the kth largest
        # number overall.
        #
        # heap[0] = smallest value in the min-heap
        return self.minHeap[0]