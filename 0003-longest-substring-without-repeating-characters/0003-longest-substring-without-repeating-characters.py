class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        1) Initialize 
            - Initialize two pointers; left and right
            - Create a set charSet to store the unique characters currently in the window
            - Initialize max_len = 0 to track the longest substring found
        2) While right is less than the length of s
            - Check if s[right] (the current character) is already in charSet
            - If it is, that means the current substring contains a duplicate
        3) While the current character s[right] is in charSet:
            - Remove s[left] from charSet to shrink the window from the left
            - Increment left by 1 to move the left boundary rightward
        4) Add the Current Character
            - Add s[right] to charSet (now it’s guaranteed to be unique in the window)
        5) Update the Maximum Length
            - Compute the current window length as right - left + 1
            - Update max_len = max(max_len, right - left + 1)
        6) Move the Right Pointer
            - Increment right to expand the window and check the next character
        7) Return the Result
            - After the loop ends, return max_len
        '''

        # max_len = 0
        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i, len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         max_len= max(max_len, j - i + 1)
        # return max_len
        # Time Complexity: O(n^2)

        left = 0
        right = 0
        max_len = 0
        charSet = set()
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
    
#Time Complexity: O(n)
#Space Complexity: O(min(n, k))
