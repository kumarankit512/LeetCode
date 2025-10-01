class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

#Brute Force
        # nums.sort()
#Time Complexity: O(n log n)
#Space Complexity: O(1) or O(n) depending on the type of sorting algorithm


#Three Pointer Approach
        '''
        Procedure:
        1) Initialize three pointers
            - low = 0
            - mid = 0
            - high = n - 1 
        2) While mid <= high:
            - If nums[mid] == 0:
                - Swap nums[low] and nums[mid]
                - Increment both low and mid
            - Else if nums[mid] == 1:
                - increment mid
            - Else if nums[mid] == 2:
                - Swap nums[mid] and nums[high]
                - Decrement high
        3) End when mid > high     
        '''

        low = 0
        mid = 0 
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
#Time Complexity: O(n)
#Space Complexity: O(1)