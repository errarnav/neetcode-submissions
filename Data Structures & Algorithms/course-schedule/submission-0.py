class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {i: [] for i in range(numCourses)}
        print(reqs)

        for crs, prq in prerequisites:
            reqs[crs].append(prq)

        print('post update: ', reqs)

        visit = set()

        def dfs(crs):

            if reqs[crs] == []:
                return True

            visit.add(crs)
            
            for prereq in reqs[crs]:
                if prereq in visit or not dfs(prereq):
                    return False

                reqs[prereq] = []
            
            reqs[crs] = []
            visit.remove(crs)

            return True

        
        for course in reqs:
            if not dfs(course):
                return False

        return True