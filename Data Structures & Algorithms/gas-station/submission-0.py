class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for i in range(len(gas)):
            visit = set()
            reserve = 0
            index = i
            while index not in visit:
                reserve += gas[index]
                if cost[index] > reserve:
                    break
                else:
                    visit.add(index)
                    reserve -= cost[index]
                    index += 1
                if index >= len(gas):
                    index = 0
            
            if len(visit) == len(gas):
                return i
            
        return -1