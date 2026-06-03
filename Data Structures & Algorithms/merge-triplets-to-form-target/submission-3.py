class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a, b, c = False, False, False
        p, q, r = target[0], target[1], target[2]
        for x, y, z in triplets:
            if x > p or y > q or z > r:
                continue
            if x == p:
                a = True
            if y == q:
                b = True
            if z == r:
                c = True

        return (a and b and c)
            