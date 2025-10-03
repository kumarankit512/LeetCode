class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        '''
        Procedure: 
        1) If heightMap is empty or m < 3 or n < 3, return 0 (no inner space to trap water)
        2) Initialize
            - visited[m][n] all False
            - A min-heap heap
            - Push all boundary cells (all edges) into heap as (height, i, j) and mark them visited
        3) Process heap:
            - While heap not empty:
                - Pop (h, x, y) (the current lowest boundary)
                - For each 4-neighbor (nx, ny):
                    - If not visited:
                        - Mark visited
                        - If heightMap[nx][ny] < h -> water += h - heightMap[nx][ny].
                        - Push (max(heightMap[nx][ny], h), nx, ny) into heap (this neighbor becomes a new boundary with an updated effective height)
        4) Return the accumulated water
        '''

        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        maxWater = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            height, x, y = heapq.heappop(heap)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    
                    # If neighbor is lower, trap water
                    maxWater += max(0, height - heightMap[nx][ny])
                    
                    # Update neighbor's boundary height
                    heapq.heappush(heap, (max(heightMap[nx][ny], height), nx, ny))
        
        return maxWater

#Time Complexity: O(m * n * log(m * n))
#Space Complexity: O(m * n)