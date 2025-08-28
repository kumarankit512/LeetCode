class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        result = []

        #Edge case to check for an empty list. Return result if list is empty
        if not nums:
            return result
        
        start = nums[0]
        
        for i in range(1, len(nums) + 1):
            
            # Condition: either we've reached the end of nums,
            # OR the current number is NOT consecutive to the previous one
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                
                # If the range has only one number, add single number as a string
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    # If the range has multiple numbers take the current range (start...last number before the break), format it as a string like start->end, and add it to the result list.
                    result.append(f"{start}->{nums[i - 1]}")
                
                # Reset 'start' for the next potential range, if not at the end
                if i < len(nums):
                    start = nums[i]
        return result