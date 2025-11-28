class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        '''
        Given:
        1) An array of integers 'nums'
        2) Integer 'k'

        We have to find the maximum subarray sum such that:
            -> (subarray length) % k == 0
            -> Subarray must be contiguous
        
        Procedure:
        1) Compute a running prefix sum 'sum'
        2) For each index i, compute:
            -> rem = i % k
        3) Check what is the smallest prefix sum previously seen with the same remainder
        4) Update the answer
            -> ans = max(ans, sum - min_prefix[rem])
        5) Update the stored minimum prefix for this remainder:
            -> min_prefix[rem] = min(min_prefix[rem], sum)
        
        For Example:
        nums = [3, -2, 5, -1] 
        k = 2

        We compute prefix sums at each index i:
        i : 0  sum = 0
        i : 1  sum = 3
        i : 2  sum = 1
        i : 3  sum = 6
        i : 4  sum = 5

        Remainders (i % k):
        i = 0 -> rem = 0 -> prefix = 0
        i = 1 -> rem = 1 -> prefix = 3
        i = 2 -> rem = 0 -> prefix = 1
        i = 3 -> rem = 1 -> prefix = 6
        i = 4 -> rem = 0 -> prefix = 5

        Remainder 0 group: prefix sums = [0, 1, 5]
        Max difference = 5 − 0 = 5

        Remainder 1 group: prefix sums = [3, 6]
        Max difference = 6 − 3 = 3

        Final answer -> max(5, 3) = 5
        '''

        n = len(nums)
        prefix = 0
        ans = float('-inf')

        # min_prefix[r] = minimum prefix sum seen at indices whose i % k == r
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0  # prefix before processing any element

        for i in range(1, n + 1):
            prefix += nums[i - 1]
            rem = i % k

            # If we previously saw a prefix with the same remainder,
            # we can form a subarray whose length is divisible by k.
            ans = max(ans, prefix - min_prefix[rem])

            # Update the minimum prefix sum for this remainder group
            min_prefix[rem] = min(min_prefix[rem], prefix)

        return ans

#Time Complexity: O(n)
#Space Complexity: O(k)