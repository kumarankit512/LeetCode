class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        '''
        Procedure:
        1) Initialize two counters 
            curr -> Tracks the current streak
            max_count -> Track the maximum streak
        2) Traverse the array 
            -> increment 'curr' if the next element is 1 and update 'max_count' 
            -> reset the 'max_count' if the next element is a 0
        3) Return the result after we traverse the entire array
        '''

        curr = 0
        max_count = 0

        for num in nums:
            if num == 1:
                curr += 1
                max_count = max(max_count, curr)
            else:
                curr = 0
        return max_count

        #Time Complexity: O(n)
        #Space Complexity: O(1)
