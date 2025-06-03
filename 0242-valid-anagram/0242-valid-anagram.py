class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

        # Time Complexity: O(n log n)
        # Space Complexity: O(n) 