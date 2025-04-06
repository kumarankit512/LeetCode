class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sum = [nums[i], nums[j], nums[k]]
                        res.add(tuple(sum))
        return [list(r) for r in res]
    
# Time Complexity: O(n^3)
# Space Complexity: O(k) k is the number of triplets