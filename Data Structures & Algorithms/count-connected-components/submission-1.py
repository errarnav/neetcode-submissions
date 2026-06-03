class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(n)}

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        print(graph)
        
        visited = set()

        def dfs(node):

            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)


        count = 0
        for node in graph:
            if node not in visited:
                count += 1
                dfs(node)

        return count
