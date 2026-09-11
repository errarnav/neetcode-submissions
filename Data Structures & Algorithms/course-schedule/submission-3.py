class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        crs = {i: [] for i in range(numCourses)}
        for course, prq in prerequisites:
            crs[course].append(prq)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if crs[course] == []:
                return True

            visit.add(course)
            for prereq in crs[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)

            crs[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True
        

