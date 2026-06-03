class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for string in strs:
            sorted_tuple = tuple(sorted(string))

            if sorted_tuple not in hashMap:
                hashMap[sorted_tuple] = []
            
            hashMap[sorted_tuple].append(string)
        
        return list(hashMap.values())