class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        q=collections.deque()
        rows,cols=len(grid),len(grid[0])
        perimeter=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    q.append([r,c])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q :
            row,col=q.popleft() 
            for dr,dc in directions:
                r,c=row+dr,col+dc
                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                    perimeter+=1
        return perimeter