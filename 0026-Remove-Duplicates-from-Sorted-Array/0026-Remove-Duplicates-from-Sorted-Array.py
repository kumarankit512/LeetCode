class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0 # pointer for the place of the next unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1 
                nums[i] = nums[j]
        return i + 1
        
#Time Complexity: O(n)
#Space Complexity: O(1)