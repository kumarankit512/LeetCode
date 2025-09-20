class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        1) Edge Case
            - If the list is empty -> return ""
            - If the list has only one string -> return that string
        2) Pick a baseline
            - Assume the first string in the array is the prefix candidate
        3) Iterate over other strings
            - For each string in the list, compare it with the current prefix
            - Check characters one by one until they differ or we reach the end of one string
            - Update the prefix to only the matching portion
            - If at any point the prefix becomes empty, return ""
        4) Return result
            - After comparing all strings, return the final prefix.
        '''

        if not strs:
            return ""

        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref_len > 0 and pref != s[:pref_len]:
                pref_len -= 1
                pref = pref[:pref_len]

            if pref_len == 0:
                return ""

        return pref
