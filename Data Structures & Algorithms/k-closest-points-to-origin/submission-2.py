class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap=[]
        res=[]
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = x**2 + y**2
            maxHeap.append((-distance, x, y))
        heapq.heapify(maxHeap)
        while len(maxHeap)>k:
            heapq.heappop(maxHeap)
        while len(maxHeap):
            res.append([maxHeap[0][1], maxHeap[0][2]])
            heapq.heappop(maxHeap)
        return res