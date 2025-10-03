class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        maxWater = 0
        while l < r:
            if maxLeft <= maxRight:
                l = l + 1
                maxLeft = max(maxLeft, height[l])
                maxWater += maxLeft - height[l]
            else:
                r = r - 1
                maxRight = max(maxRight, height[r])
                maxWater += maxRight - height[r]
        return maxWater

#Time complexity: O(n)
#Space complexity: O(1)
