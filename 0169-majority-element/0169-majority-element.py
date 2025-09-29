class Solution:
    def majorityElement(self, nums: List[int]) -> int:

# Sorting Solution: 
        # nums.sort()
        # return nums[len(nums) // 2]  

#Time Complexity: O(n log n)
#Space Complexity: O(1)

        # Boyer–Moore Majority Vote Algorithm: We keep track of a candidate element (temp) and a counter. As we iterate through the array:
        #If the counter is 0, set the current element as the new candidate.
        #If the current element matches the candidate, increment the counter; otherwise, decrement it. At the end, the candidate is the majority element.
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

#Time Complexity: O(n)
#Space Complexity: O(1)