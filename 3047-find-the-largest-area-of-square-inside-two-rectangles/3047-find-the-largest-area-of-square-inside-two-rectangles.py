class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        '''
        Goal: Find the largest possible square that can fit inside the overlapping region of the two rectangles, and return its area

        Procedure:
        1) Iterate through the n number of triangles 
        2) Compute the intersection of two triangles
        3) Check if intersection exists
            -> If no overlap -> skip this pair
        4) Find the largest sqaure inside the interaction
        4) Return the maximum area found
            -> If there is no valid square, return 0

        For Example:
        rect1 = [1, 1, 5, 5]
        rect2 = [3, 3, 7, 7]

        Intersection = [3, 3, 5, 5]
        Width = 2, Height = 2
        Largest square side = 2
        Area = 4
        '''

        n = len(bottomLeft)
        max_area = 0

        #Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                #Compute intersection
                left = max(bottomLeft[i][0], bottomLeft[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                right = min(topRight[i][0], topRight[j][0])
                top = min(topRight[i][1], topRight[j][1])

                #Check if intersection exists
                if right > left and top > bottom:
                    #Find the largest square
                    side = min(right - left, top - bottom)
                    max_area = max(max_area, side * side)

        return max_area

        #Time Complexity: O(n^2)
        #Space Complexity: O(1)