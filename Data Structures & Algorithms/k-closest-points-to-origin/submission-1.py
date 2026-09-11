class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap) 

        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(minHeap, (distance, x, y))
            

        res = []
        
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res