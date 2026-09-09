class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for src, target, time in times:
            edges[src].append((target,time))
        
        min_heap = [(0,k)] 
        #n= length
        visited = set()
        total_time = 0
        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)
            total_time = current_time
            for target,time in edges[current_node]:
                new_time = time + current_time
                heapq.heappush(min_heap,(new_time,target))

        return total_time if len(visited) == n else -1
                