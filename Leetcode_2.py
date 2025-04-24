import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
         # Adjacency List
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-Heap to Expand the Shortest Path
        heap = [(0, k)]  # (current_time, node)
        shortest = {}  # node -> shortest time from k

        while heap:
            time, node = heapq.heappop(heap)
            if node in shortest:
                continue
            shortest[node] = time
            for nei, t in graph[node]:
                if nei not in shortest:
                    heapq.heappush(heap, (time + t, nei))

        return max(shortest.values()) if len(shortest) == n else -1
        