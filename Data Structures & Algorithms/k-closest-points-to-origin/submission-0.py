import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        maxHeap = []
        heapq.heapify(maxHeap)

        for i in points:
            x = i[0]
            y = i[1]
            dist = x**2 + y**2
            dist = -1 * dist
            
            print(x, y, dist)
            heapq.heappush(maxHeap, [dist, x, y])

            while len(maxHeap) > k:
                heapq.heappop(maxHeap)

        
        for i in maxHeap:
            res.append([i[1], i[2]])

        return res


