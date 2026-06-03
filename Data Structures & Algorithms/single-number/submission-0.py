class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = set()

        for num in nums:
            if num in visited:
                visited.remove(num)
            else:
                visited.add(num)

        
        for i in visited:
            elem = i

        return i