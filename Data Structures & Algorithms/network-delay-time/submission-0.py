class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Build adjacency list:
        # edges[u] = [(v, time), ...]
        edges = collections.defaultdict(list)

        for source, destination, travel_time in times:
            edges[source].append((destination, travel_time))

        # Min-heap:
        # (total_time, node)
        #
        # Always process the node we can reach
        # in the shortest amount of time so far.
        min_heap = [(0, k)]

        # Nodes whose shortest time has been finalized.
        visited = set()

        total_time = 0

        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)

            # We already found the shortest path to this node.
            if current_node in visited:
                continue

            visited.add(current_node)

            # This is the shortest time needed to reach this node.
            total_time = current_time

            # Try reaching all neighbors through this node.
            for neighbor, travel_time in edges[current_node]:

                if neighbor not in visited:
                    new_time = current_time + travel_time

                    # Add the possible path to the heap.
                    # The heap will give us the smallest one next.
                    heapq.heappush(
                        min_heap,
                        (new_time, neighbor)
                    )

        # If we reached every node, the answer is the
        # longest shortest-path time.
        # Otherwise, some node is unreachable.
        return total_time if len(visited) == n else -1
