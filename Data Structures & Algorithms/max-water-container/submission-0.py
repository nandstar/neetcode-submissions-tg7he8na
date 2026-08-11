class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right,maxwater=0,len(heights)-1,0
        while left<right:
            res=(right-left)*min(heights[left],heights[right])
            maxwater=max(maxwater,res)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxwater


        




        