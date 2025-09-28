class Solution:
    def validPalindrome(self, s: str) -> bool:

        '''
        Procedure:
        1) Use two pointers
            - One pointer at the start -> left = 0
            - One pointer at the end -> right = len(s) - 1
        2) While left < right:
            - If characters match -> move both pointers inward
            - If characters don’t match:
                - Try skipping one character either s[left] or s[right]
                - Check if the remaining substring is a palindrome
                - If either works -> return True
                - Otherwise -> return False
        3) If loop ends with no mismatches -> return True
        '''

        def isPalindrome(l, r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Skip either left or right character
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        return True

#Time Complexity: O(n)
#Space Complexity: O(1)
