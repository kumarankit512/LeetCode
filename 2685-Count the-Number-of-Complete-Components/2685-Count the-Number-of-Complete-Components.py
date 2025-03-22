class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.visited = set()

        def dfs(node, component_nodes):
            self.visited.add(node)
            component_nodes.add(node)
            for nei in adj[node]:
                if nei not in self.visited:
                    dfs(nei, component_nodes)
        
        components = 0
        for i in range(n):
            if i not in self.visited:
                component_nodes = set()
                dfs(i, component_nodes)
                len_components = len(component_nodes)
                expected_edges = len_components * (len_components-1) //2
                actual_edges = 0
                for u in component_nodes:
                    for j in adj[u]:
                        if j in component_nodes:
                            actual_edges += 1

                if actual_edges//2 == expected_edges:
                    components+=1

        return components

#Time Complexity: O(V + E)
#Space Complexity: O(V + E)