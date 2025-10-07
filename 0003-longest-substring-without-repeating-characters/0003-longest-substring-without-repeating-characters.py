class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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

