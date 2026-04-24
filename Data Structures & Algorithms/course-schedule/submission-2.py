class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for i in prerequisites:
            if i[0] in graph:
                graph[i[0]].append(i[1])
            else:
                graph[i[0]] = [i[1]]
        print(graph)

        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if graph[crs] and graph[crs]==[]:
                return True
            visiting.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            graph[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            

            