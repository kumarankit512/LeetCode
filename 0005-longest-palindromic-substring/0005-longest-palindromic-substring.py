class Solution:
    def isPalindrome(self, s:str, i, j, pali):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i = i - 1
            j = j + 1
        i = i + 1
        j = j - 1   
        if (j - i + 1) > pali[1]:
            pali[0] = i
            pali[1] = j - i + 1

    def longestPalindrome(self, s: str) -> str:
        pali = [0, 0] #Start, length
        for i in range(len(s)):
            self.isPalindrome(s, i, i, pali)
            self.isPalindrome(s, i, i + 1, pali)
        return s[pali[0]: pali[0] + pali[1]]

#Time Complexity: O(n^2)
#Space Complexity: O(1)	