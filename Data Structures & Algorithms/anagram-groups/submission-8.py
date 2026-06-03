class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        
        for string in strs:
            freq = [0] * 26

            for char in string:
                freq[ord(char) - ord('a')] += 1
        
            if tuple(freq) not in hashMap:
                hashMap[tuple(freq)] = []
            
            hashMap[tuple(freq)].append(string)

        return list(hashMap.values())