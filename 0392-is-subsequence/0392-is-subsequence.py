class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        Approach:
        - We can solve this problem using a two-pointer technique to check whether s is a subsequence of t. 

        1) Pointer Initialization:
            - Initialize two pointers, one for s and one for t
        2) Iterate over t
            - Move pointer j over each character of string t.
            - Whenever a character t[j] matches the character s[i], increment i to move to the next character in s
        3) Check if all characters of s are matched
            - If i reaches the length of s before j finishes iterating through t, it means all characters of s have been found in t in order, so return true
            - If j reaches the end of t and i has not reached the end of s, then return false
        '''

        if not s:
            return True

        i = 0 
        j = 0
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1

            if i == len(s):
                return True

        return False

#Time Complexity: O(n)
#Space Complexity: O(1)