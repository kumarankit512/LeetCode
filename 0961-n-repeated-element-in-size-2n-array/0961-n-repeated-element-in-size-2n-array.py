class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        '''
        Procedure:
        1) Create an empty set to keep track of seen numbers
        2) Iterate through the array
        3) For each number:
            - If in set 
                - return nums
            - else 
                - add it to the set
        '''

        seen = set()
        
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        #Time Complexity: O(n)
        #Space Complexity: O(n)