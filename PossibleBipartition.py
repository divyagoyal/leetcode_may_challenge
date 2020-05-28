class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:       
        graph = defaultdict(list)
        color = {}

        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(element, c ^ 1) for element in graph[node])

        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        return all(dfs(node)
                           for node in range(1, N+1)
                           if node not in color)

        
