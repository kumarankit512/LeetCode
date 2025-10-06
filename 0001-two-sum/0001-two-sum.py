class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

# Time Complexity -> O(n^2) -> Brute Force

        # A = []
        # for i, num in enumerate(nums):
        #     A.append([num, i])
        
        # A.sort()
        # i, j = 0, len(nums)- 1
        # while i < j:
        #     sum = A[i][0] + A[j][0]
        #     if sum == target:
        #         return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
        #     elif sum < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []

# Time Complexity -> O(n log (n)) -> Sorting
# Space Complexity: O(n)
    
        mp = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in mp:
                return [mp[complement], i]
            mp[n] = i

#Hash Map Solution:
# Time Complexity: O(n) 
# Space Complexity: O(n)