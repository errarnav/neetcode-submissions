"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda i: i.start)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = 0

        s = 0
        e = 0
        res = 0


        while s < len(intervals):

            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                count -= 1
                e += 1

            res = max(count, res)

        return res
