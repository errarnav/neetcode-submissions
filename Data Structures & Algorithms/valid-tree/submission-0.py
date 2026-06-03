class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        print(graph)
        
        
        visited = set()

        

        def dfs(node, prev):

            if node in visited:
                return False


            visited.add(node)

            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
                