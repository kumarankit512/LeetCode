class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        Procedure:
        1) Initialize two pointers
            - left = 0 (start of array)
            - right = len(s) - 1 (end of array)
        2) Swap characters
            - While left < right:
            - Swap s[left] and s[right]
            - Increment left
            - Decrement right
        3) Stop when pointers meet
            - Once left >= right, the array is fully reversed
        '''
        
        left = 0 
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

#Time Complexity: O(n)
#Space Complexity: O(1)