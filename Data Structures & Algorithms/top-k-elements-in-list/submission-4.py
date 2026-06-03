class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for integer in nums:
            count[integer] = 1 + count.get(integer, 0)

        freq = [[] for i in range(len(nums) + 1)]
        
        for integer, countt in count.items():
            freq[countt].append(integer)

        final = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                final.append(num)
                if len(final) == k:
                    return final
