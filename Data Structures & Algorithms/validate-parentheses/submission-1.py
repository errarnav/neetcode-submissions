class Solution:
    
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ']': '[', ')': '('}
        stack = []

        for i in s:
            if i in pairs: # then we know it is a closing bracket
                if len(stack) == 0 or stack[-1] != pairs[i]:
                    return False
                else:
                    stack.pop()

            else: # we know that it is an opening bracket, so just append
                stack.append(i)


        return len(stack) == 0