import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        # Min-heap: (total_cost, current_city, stops)
        heap = [(0, src, 0)]
        
        while heap:
            cost, city, stops = heapq.heappop(heap)

            # If we reached destination within k stops
            if city == dst:
                return cost
            
            # If we still have stops left
            if stops <= k:
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost + price, neighbor, stops + 1))
        
        return -1
