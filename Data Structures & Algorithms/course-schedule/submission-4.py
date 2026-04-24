class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)

        print(graph)


        visited = set()
        
        def dfs(node):
            if node in visited: return False 
            if graph[node]==[]: return True
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    return False
                else:
                    if not dfs(nei): return False
            visited.remove(node)
            return True
        
        for i in graph:
            if i not in visited:
                if not dfs(i):
                    return False
        return True
        
        
        
        # graph = {i:[] for i in range(numCourses)}
        # for i in prerequisites:
        #     if i[0] in graph:
        #         graph[i[0]].append(i[1])
        #     else:
        #         graph[i[0]] = [i[1]]
        # visited = set()
        # def dfs(crs):
            
        #     if crs in visited:
        #         return False
        #     if graph[crs] == []:
        #         return True
        #     visited.add(crs)
        #     for pre in graph[crs]:
        #         if not dfs(pre):
        #             return False
        #     visited.remove(crs)
        #     graph[crs] = []
        #     return True
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True

            
            
        # graph = {i: [] for i in range(numCourses)}
        # for i in prerequisites:
        #     if i[0] in graph:
        #         graph[i[0]].append(i[1])
        #     else:
        #         graph[i[0]] = [i[1]]
        # print(graph)

        # visiting = set()
        # def dfs(crs):
        #     if crs in visiting:
        #         return False
        #     if graph[crs]==[]:
        #         return True
        #     visiting.add(crs)
        #     for pre in graph[crs]:
        #         if not dfs(pre):
        #             return False
        #     visiting.remove(crs)
        #     graph[crs] = []
        #     return True
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True
            

            