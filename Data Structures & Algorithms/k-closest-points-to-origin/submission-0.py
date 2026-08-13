class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        res=[]
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = x**2 + y**2
            minHeap.append((-distance, x, y))
        heapq.heapify(minHeap)
        while len(minHeap)>k:
            heapq.heappop(minHeap)
        while len(minHeap):
            res.append([minHeap[0][1], minHeap[0][2]])
            heapq.heappop(minHeap)
        return res