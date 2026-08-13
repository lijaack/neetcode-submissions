class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Turn stones into negative numbers so heapq acts like a max-heap
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:

            # Get the two heaviest stones
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            # Smash them
            if x != y:
                heapq.heappush(maxHeap, -(x - y))

        # Return the remaining stone
        return -maxHeap[0] if maxHeap else 0