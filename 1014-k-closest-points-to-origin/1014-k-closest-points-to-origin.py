class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Given:
        1) Array of 'points'
        2) points[i] = [xi, yi] represents a point on the x-y plane
        3) interger 'k' 
        4) The distance between two points is "Euclidean distance" which is √(x1 - x2)2 + (y1 - y2)2)

        Procedure:
        - Given an array of points we have to find a point 'k' which is closest to the origin (0, 0). The distance between X-Y is Euclidean distance.
        '''

        minHeap = []
        for x, y in points:
            dist = (x ** 2 + y ** 2)
            minHeap.append([dist, x, y])
        
        heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

#Time Complexity: O(n + k log n)
#Space Complexity: O(n + k)
        
