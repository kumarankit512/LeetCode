class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Sorting Solution: 
        # nums.sort()
        # return nums[len(nums) // 2]  

        #Time Complexity: O(n log n)
        #Space Complexity: O(1)
    

        # Optimized Approach: Use a hash map, using the key and val, we itterate through the array and increment the val at key each time we see that val in the array and at the end return the key with the highest val. 
        count = 0
        temp = nums[0]
        for num in nums:
            if count == 0:
                temp = num
            if num == temp:
                count += 1
            else:
                count -= 1
        return temp

        # Time Complexity: O(n)
        # Space Complexity: O