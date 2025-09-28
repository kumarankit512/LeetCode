class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        Procedure:
        1) Use two pointers
            - One pointer at the start -> left = 0
            - One pointer at the end -> right = len(s) - 1
        2) Check characters
            - While left < right:
                - If s[left] is not alphanumeric -> move left forward.
                - If s[right] is not alphanumeric -> move right backward.
                - Otherwise, compare s[left] and s[right]
                    - If they are different -> return False
                    - Else -> move both pointers inward
        3) Return result
            - If the loop completes without mismatches -> return True
        '''

        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

#Time Complexity: O(n)
#Space Complexity: O(1)