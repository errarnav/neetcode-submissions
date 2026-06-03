class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num, c in count.items():
            freq[c].append(num)
        results_list = []
        for i in range(len(freq) - k, 0, -1):
            for number in freq[i]:
                results_list.append(number)
                if len(results_list) == k:
                    return results_list
                
