class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0
        for n in nums:
            res = res ^ n
        return res

#Time Complexity: O(n)
#Space Complexity: O(1)