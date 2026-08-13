class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timer = 0
        q=deque()
        heap = []
        
        counts = Counter(tasks)
        heap = [(-count, task) for task, count in counts.items()]
        heapq.heapify(heap)
        while heap:
            count, task = heapq.heappop(heap)
            count +=1
            if count < 0 :
                q.append([tuple([count,task]),timer+n+1])
            timer+=1

            while q and q[0][1] <=  timer:
                heapq.heappush(heap,q.popleft()[0])
            
            while not heap and q:
                timer+=1
                while q and q[0][1] <= timer:
                    heapq.heappush(heap,q.popleft()[0])
        return timer