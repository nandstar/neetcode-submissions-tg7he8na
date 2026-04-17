class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            premap[crs].append(preq)
        visited=set()
        def dfs(crs):
            if premap[crs]==[]:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for i in premap[crs]:
                if not dfs(i):
                    return False
            visited.remove(crs)
            premap[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            