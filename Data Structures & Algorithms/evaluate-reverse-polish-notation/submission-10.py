class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ref = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token not in ref:
                stack.append(int(token))
            
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    new = a + b
                
                elif token == '-':
                    new = a - b
                
                elif token == '*':
                    new = a * b

                else:
                    new = int(a / b)

                stack.append(new)

        return stack[0]
        