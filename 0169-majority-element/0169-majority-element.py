class Solution:
    def majorityElement(self, nums: List[int]) -> int:

# Sorting Solution: 
        nums.sort()
        return nums[len(nums) // 2]  

#Time Complexity: O(n log n)
#Space Complexity: O(1)
