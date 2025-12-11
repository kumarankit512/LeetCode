class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        Brute Force Method:
            Given:
            1) Array of integers 'nums' and 'target'
            2) Return the indices of the two numbers that add up to 'target'
            3) Can return the answer in any order

            Procedure:
            1) Initialize a variable for the length of nums
            2) Use two while loops 
                -> for i in range(n) -> Starts at index 0
                    -> for j in range(i + 1, n) -> Starts at index 1
            3) Check if the value at i and j add up to the 'target'
            4) If we find a pair, return the indices 
        '''

        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        #Time Complexity -> O(n^2)
        #Space Complexity -> O(1)