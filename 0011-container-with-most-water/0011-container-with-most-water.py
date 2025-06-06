class Solution(object):
    def maxArea(self, height):
        totalArea = 0
        l, r = 0, len(height) - 1

        while l < r:
         area = (r - l) * min(height[l], height[r])
         totalArea = max(totalArea, area) 

         if height[l] < height[r]:
            l += 1
         else:
            r -= 1

        return totalArea 
        