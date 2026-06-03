class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        index = []

        for i in range(len(temperatures)):
            if len(index) == 0:
                index.append(i)
            else:
                while len(index) > 0 and temperatures[i] > temperatures[index[-1]]:
                    distance = i - index[-1]
                    res[index[-1]] = distance
                    index.pop()

                index.append(i)

        
        return res