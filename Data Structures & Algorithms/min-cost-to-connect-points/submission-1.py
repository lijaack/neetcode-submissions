class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Start Prim's algorithm from point 0
        node = 0

        # Cheapest known cost to connect each point
        # Start with infinity because we haven't found any connections yet
        dist = [float("inf")] * n

        # Track which points are already connected
        visited = [False] * n

        edges = 0
        result = 0

        # Need exactly n - 1 edges to connect n points
        while edges < n - 1:
            # Add current node to our connected group
            visited[node] = True

            # Find the next cheapest unvisited point
            next_node = -1

            for i in range(n):
                if visited[i]:
                    continue

                # Manhattan distance from current node to point i
                cur_dist = (
                    abs(points[i][0] - points[node][0]) +
                    abs(points[i][1] - points[node][1])
                )

                # Keep the cheapest way we've found to connect point i
                dist[i] = min(dist[i], cur_dist)

                # Pick the unvisited point with the smallest connection cost
                if next_node == -1 or dist[i] < dist[next_node]:
                    next_node = i

            # Add the cheapest connection to our total
            result += dist[next_node]

            # Move to that newly connected point
            node = next_node
            edges += 1

        return result