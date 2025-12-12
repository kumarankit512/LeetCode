class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''
        Brute Force Approach: (TLE)

        Procedure:
        1) Pick every possible starting index i
        2) For each start, try every ending index j ≥ i
        3) Compute the subarray sum from i to j
        4) Track the maximum sum found
        5) Return max_sum
        '''

        # max_sum = float('-inf')
        # n = len(nums)

        # for i in range(n):
        #     current_sum = 0
        #     for j in range(i, n):
        #         current_sum += nums[j]  # accumulate instead of recomputing
        #         max_sum = max(max_sum, current_sum)

        # return max_sum

        #Time Complexity: O(n^2)
        #Space Complexity: O(1)

        '''
        Kadane's Algorithm:

        Procedure:
        1) Initialize two variables 
        2) Loop through each number n in the array
            -> If current_sum is negative, reset it to 0
            -> Add the current number to current_sum
            -> Update the global maximum
        3) After processing all numbers, return max_sum
        '''

        max_sum = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sum = max(max_sum, current_sum)

        return max_sum

        #Time Complexity: O(n)
        #Space Complexity: O(1)