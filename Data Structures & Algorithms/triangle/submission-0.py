class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(len(triangle) - 2, -1, -1):
            for c in range(len(triangle[r])):
                # Add the minimum of the two reachable nodes directly below
                triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c + 1])
        
        # The top node now contains the minimum total path sum
        return triangle[0][0]