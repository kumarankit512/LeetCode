class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Given:
        1) Two strings 's' and 't'
        2) return true if t is an anagram of s, else false

        Sorting Approach:
        Procedure:
        1) Firstly check if the length of both the strings are same
        2) Return false if the lengths are different
        3) Return sorted(s) == sorted(t)
        '''

        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

        #Time Complexity: O(n log n)
        #Space Complexity: O(n)