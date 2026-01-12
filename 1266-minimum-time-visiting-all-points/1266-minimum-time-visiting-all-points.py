class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        '''
        Given: 
        A list of points on a 2D plane
        Start at the first point and must visit all points in order

        We can move:
            -> Horizontally (x ± 1)
            -> Vertically (y ± 1)
            -> Diagonally (x ± 1, y ± 1)
        Each move takes 1 second
        We have to compute the minimum time required to visit all the points in sequence

        Procedure:
        1) Initialize total_time = 0
        2) Loop through the points from index 1 to n-1
        3) For each pair of consecutive points:
            - Compute dx = abs(x2 - x1)
            - Compute dy = abs(y2 - y1)
            - Add max(dx, dy) to total_time
        4) Return total_time
        '''

        total_time = 0
        
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            
            total_time += max(abs(x2 - x1), abs(y2 - y1))
        
        return total_time

        #Time Complexity: O(n)
        #Space Complexity: O(1)