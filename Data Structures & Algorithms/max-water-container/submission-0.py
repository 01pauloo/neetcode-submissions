class Solution:
    def maxArea(self, heights: List[int]) -> int:
        contain_max = 0
        l, r = 0, len(heights)-1
        while l < r:
            surf = min(heights[l],heights[r]) * (r-l)
            contain_max = max(contain_max, surf)
            if heights[l] < heights[r]:
                l +=1
            else:
                
                r-=1
        
        return contain_max
                