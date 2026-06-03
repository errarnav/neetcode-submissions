class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ref = {'+', '-', '/', '*'}

        for i in tokens:
            if i not in ref:
                stack.append(int(i))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                
                if i == '+':
                    new_val = a + b
                
                elif i == '-':
                    new_val = a - b

                elif i == '/':
                    new_val = int(a/b)
                
                else:
                    new_val = a*b

            
            
                stack.append(new_val)

        return stack[0]
