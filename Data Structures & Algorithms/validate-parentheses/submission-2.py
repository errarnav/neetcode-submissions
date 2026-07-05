class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        corr = {')': '(', ']': '[', '}': '{'}

        for bracket in s:
            
            if bracket not in corr:  # its an opening bracket
                stack.append(bracket)
            else: # its a closing bracket
                if not stack:
                    return False
                
                if stack[-1] != corr[bracket]:
                    return False
                stack.pop()

        return len(stack) == 0