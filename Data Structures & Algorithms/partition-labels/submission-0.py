class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        loc = {}
        for i in range(len(s)):
            if s[i] in loc:
                loc[s[i]].append(i)
            else:
                loc[s[i]] = [i]


        intervals = []
        for key, value in loc.items():
            intervals.append([value[0], value[-1]])

        intervals.sort()

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        new = []
        for interval in res:
            new.append(interval[1] - interval[0] + 1)

        return new
            
