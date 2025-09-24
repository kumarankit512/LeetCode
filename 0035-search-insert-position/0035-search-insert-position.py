class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Procedure:

        1) Since the array is sorted, use binary search.
        2) Initialize two pointers:
            - left = 0
            - right = len(nums) - 1
        3) While left <= right:
            - Find mid = (left + right) // 2
            - If nums[mid] == target, return mid (found exact position).
            - If nums[mid] < target, move left = mid + 1
            - Else (when nums[mid] > target), move right = mid - 1
        4) If loop ends, left will be the position where the target should be inserted.
            - Return left.
        '''

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

#Time Complexity: O(log n)
#Space Complexity: O(1)