class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = []
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            res.append(trip)

        loc = {target[0]: [], target[1]: [], target[2]: []}
        for i in range(3):
            elem = target[i]
            for k in range(len(res)):
                if res[k][i] == elem:
                    loc[elem].append(k)

        for list1 in loc.values():
            if not list1:
                return False

        return True
        

