class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        Brute Force Solution:
        Procedure:
        1) Build a new string with only alphanumeric characters in lowercase
        2) Reverse the cleaned string manually
        3) Compare the cleaned string with its reversed version
        '''

        # cleaned = ""

        # for c in s:
        #     if c.isalnum():
        #         cleaned += c.lower()
        
        # reversed_cleaned = ""
        # for i in range(len(cleaned)-1, -1, -1):
        #     reversed_cleaned += cleaned[i]
        
        # if cleaned == reversed_cleaned:
        #     return True
        # else:
        #     return False

        #Time Complexity: O(n)
        #Space Complexity: O(n)

        '''
        Two Pointer Solution:
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