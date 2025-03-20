class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

# Time Complexity -> O(n^2) -> Brute Force
# Space Complexity -> O(1)

        mp = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in mp:
                return [mp[complement], i]
            mp[n] = i

# Time Complexity: O(n) -> Hash Map
# Space Complexity: O(n)