class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#Brute Force
        nums.sort()
#Time Complexity: O(n log n)
#Space Complexity: O(1) or O(n) depending on the type of sorting algorithm