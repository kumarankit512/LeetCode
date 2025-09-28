class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        '''
        Procedure:
        1) Find three lengths from the array that can form a valid triangle and have the largest perimeter
        2) Find the largest perimeter of a triangle:
            - Sort the array in descending order
            - Iterate through consecutive triplets: check if they form a valid triangle
            - The first valid triplet found will give the maximum perimeter
        3) If no valid triangle exists -> return 0
        '''

        # n = len(nums)
        # max_perimeter = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             a, b, c = sorted([nums[i], nums[j], nums[k]])
        #             if a + b > c:
        #                 max_perimeter = max(max_perimeter, a + b + c)
        # return max_perimeter

#Brute Force Approach -> Time Limit Exceeded
#Time Complexity: O(n^3)
#Space Complexity: O(1)

        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0

#Time Complexity: O(n log n)
#Space Complexity: O(1)