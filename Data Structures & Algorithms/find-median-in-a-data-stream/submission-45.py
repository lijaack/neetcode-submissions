class MedianFinder:

    def __init__(self):
        self.leftHeap=[]
        self.rightHeap=[]

    def addNum(self, num: int) -> None:
        leftLen=len(self.leftHeap)
        rightLen=len(self.rightHeap)
        leftMax=-self.leftHeap[0] if self.leftHeap else 0
        rightMin=self.rightHeap[0]if self.rightHeap else 0
        if num >= leftMax and num <= rightMin:
            if rightLen >= leftLen:
                heapq.heappush(self.leftHeap,-num)
            else:
                heapq.heappush(self.rightHeap,num)
        elif num >= leftMax and num >= rightMin:
            heapq.heappush(self.rightHeap, num)
        elif num <= leftMax and num <= rightMin:
                heapq.heappush(self.leftHeap,-num)
        if abs(len(self.leftHeap)-len(self.rightHeap)) > 1:
            if len(self.leftHeap)>len(self.rightHeap):
                hold=heapq.heappop(self.leftHeap)
                heapq.heappush(self.rightHeap, -hold)
            else:
                hold=heapq.heappop(self.rightHeap)
                heapq.heappush(self.leftHeap, -hold)





    def findMedian(self) -> float:
        median = int()

        if abs(len(self.leftHeap)-len(self.rightHeap)) >= 1:
            if len(self.leftHeap)>len(self.rightHeap):
                median = -(self.leftHeap[0])
            else:
                median = self.rightHeap[0]
        else:
            median = (-(self.leftHeap[0] if self.leftHeap else 0)+self.rightHeap[0]if self.rightHeap else 0)/2
        return median
        