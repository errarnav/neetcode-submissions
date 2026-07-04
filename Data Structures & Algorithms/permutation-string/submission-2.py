class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            target[index] += 1

        l = 0
        count = [0] * 26
        
        for i in range(len(s1) - 1):
            index = ord(s2[i]) - ord('a')
            count[index] += 1

        for r in range(len(s1) - 1, len(s2), 1):
            index_to_add = ord(s2[r]) - ord('a')
            count[index_to_add] += 1
            
            if count == target:
                return True
            
            index_to_remove = ord(s2[l]) - ord('a')
            count[index_to_remove] -= 1
            l += 1
            

        return False


