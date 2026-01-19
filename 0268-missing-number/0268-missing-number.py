class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        '''
        Sorting Approach

        Procedure:
        1) Sort the array nums
        2) Iterate through the array from index 0
        3) At each index i:
            -> if nums[i] != i then i is the missing number -> return i
        4) If no mismatch is found:
            -> The missing number must be n (the largest value)
        '''

        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

        #Time Complexity: O(n log n)
        #Space Complexity: O(1)
