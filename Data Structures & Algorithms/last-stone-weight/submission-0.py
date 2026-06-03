class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = abs(heapq.heappop(stones))
            second_stone = abs(heapq.heappop(stones))

            if first_stone > second_stone:
                new = first_stone - second_stone
                heapq.heappush(stones, -new)

        stones.append(0)

        return -stones[0]