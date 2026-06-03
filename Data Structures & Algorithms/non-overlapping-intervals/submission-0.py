class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort()

        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start >= output[-1][1]:
                output.append([start, end])

            else:
                res += 1
                if end > output[-1][1]:
                    continue
                else:
                    output.append([start, end])

        return res