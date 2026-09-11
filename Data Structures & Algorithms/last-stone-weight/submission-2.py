class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = abs(heapq.heappop(maxHeap))
            stone2 = abs(heapq.heappop(maxHeap))

            if stone1 > stone2:
                heapq.heappush(maxHeap, -(stone1 - stone2))

            print(stone2 - stone1)

        maxHeap.append(0)
        return -maxHeap[0]