class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        '''
        Given:
        1) Integer array 'nums'
        2) return true if an element appears twice
        3) return false if every element is distinct

        Brute Force:
        Procedure:
        1) Initialize a variable n for len(nums)
        2) Use two while loops one starts at index 0 and the other at 1
        3) Compare the values at both index
        4) Return true if value matches
        5) Return false if value is different
        '''

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]: 
                    return True
        return False

        #Time Complexity: O(n^2) 
        #Space Complexity: O(1)

        '''
        Sorting Approach:
        Procedure:
        1) Sort the array
        2) Loop through the array
        3) Compare the values at the current index and prev index
        4) Return true if value matches
        5) Return false if value is different
        '''

        n = len(nums)
        nums.sort()
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False

        #Time Complexity: O(n log n)
        #Space Complexity: O(1)