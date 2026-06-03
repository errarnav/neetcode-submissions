
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        reqs = {i: [] for i in range(numCourses)}

        for crs, prq in prerequisites:
            reqs[crs].append(prq)

        print(reqs)

        res = []

        cycle = set()
        visited = set()

        def dfs(crs):

            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)

            for prq in reqs[crs]:
                if dfs(prq) == False:
                    return False

            res.append(crs)
            cycle.remove(crs)
            visited.add(crs)

            return True

        for crs in reqs:
            if not dfs(crs):
                return []

        return res
            



