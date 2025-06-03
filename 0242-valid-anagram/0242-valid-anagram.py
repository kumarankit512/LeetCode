class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

        # Time Complexity: O(n)
        # Space Complexity: O(n)  