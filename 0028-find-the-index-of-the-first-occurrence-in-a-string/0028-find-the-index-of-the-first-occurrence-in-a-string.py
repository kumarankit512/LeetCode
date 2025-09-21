class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        1) Check the lengths of both the strings, if needle is longer than 'haystack', return -1 immediately
        2) Iterate through the string 'haystack'
            - Loop from index 0 to len(haystack) - len(needle)
            - For each starting index i, check if the substring haystack[i : i+len(needle)] matches needle
        3) If match a match is found, return the index i
        4) If no match found, return -1
        '''

        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i

        return -1
#Time Complexity: O(n * m)
#Space Complexity: O(1)