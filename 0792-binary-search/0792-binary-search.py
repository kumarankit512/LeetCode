class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1) Initialize two pointers one at the left and one at the right 
        2) While left <= right:
            - Find the middle index -> mid = (left + right) // 2
            - If nums[mid] == target -> return mid (target has been found)
            - If nums[mid] < target -> move search to the right half -> left = mid + 1.
            - Else (nums[mid] > target) -> move search to the left half -> right = mid - 1.
        3) If not found, return -1.
        '''

        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # search in the right half
            else:
                right = mid - 1  # search in the left half

        return -1

#Time Complexity: O(log n)
#Space Complexity: O(1)