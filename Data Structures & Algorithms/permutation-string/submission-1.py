class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):

            return False

        s1_freq_list = [0]*26
        for i in s1:
            index = ord(i) - 97
            s1_freq_list[index] += 1
        
        l = 0
        r = len(s1) - 1

        curr_freq_list = [0]*26
        for i in range(l , r + 1, 1):
            index = ord(s2[i]) - 97
            curr_freq_list[index] += 1
        
        while r < len(s2):
            
            if curr_freq_list == s1_freq_list:
                return True

            else:
                index = ord(s2[l]) - 97
                curr_freq_list[index] -= 1
                r += 1
                l += 1
                if r < len(s2):
                    new_index = ord(s2[r]) - 97
                    curr_freq_list[new_index] += 1
                else:
                    continue
        
        return False

                
