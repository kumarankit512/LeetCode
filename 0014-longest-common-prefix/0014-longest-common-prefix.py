class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)
        for s in strs[1:len(strs)]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[0:pref_len]
        return pref
    
# Time Complexity: O(n * m)
# Space Complexity: O(1)