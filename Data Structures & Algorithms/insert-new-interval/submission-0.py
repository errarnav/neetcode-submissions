class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        res = []

        for i in range(len(intervals)):
            newIntervalStart = newInterval[0]
            newIntervalEnd = newInterval[1]
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]


            if curr_start > newIntervalEnd:
                res.append(newInterval)
                return res + intervals[i:]


            elif newIntervalStart > curr_end:
                res.append([curr_start, curr_end])


            else:
                newInterval = [min(newIntervalStart, curr_start), max(newIntervalEnd, curr_end)]
            

        res.append(newInterval)
        return res


