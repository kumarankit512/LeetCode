class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        '''
        Procedure:
        1) Initialize two pointers
        2) Compute the are at each step:
            - The area is determined by the shorter line between height[l] and height[r], multiplied by the distance (r - l)
        3) Update maximum area:
            - Compare the current area with the stored maximum (res) and keep the larger one
        4) Move pointers strategically:
            - If height[l] <= height[r], increment l (because moving the shorter line may give a taller line, possibly increasing the area)
            - Else, decrement r
        5) Repeat until pointers meet:
            - Stop when l >= r
        6) Return the maximum area found
        '''

        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
