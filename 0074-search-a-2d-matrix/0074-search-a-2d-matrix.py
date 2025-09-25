class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        low = 0
        high = ROWS - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                break
        row = (low + high) // 2
        left = 0
        right = COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

#Time Complexity: O(log ROWS + log COLS)
#Space Complexity: O(1) 