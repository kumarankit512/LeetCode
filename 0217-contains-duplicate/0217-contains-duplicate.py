class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]: 
        #             return True
        # return False

#Brute Force -> TLE
#Time Complexity: O (n^2) 
#Space Complexity: O(1)

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

#Time Complexity: O(n log n) -> because of sorting
#Space Complexity: O(1)
