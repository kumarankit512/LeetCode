class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        '''
        One line approach however, it uses extra space for split()
        
        '''
        return len(s.strip().split()[-1])

        #Time Complexity: O(n)
        #Space Complexity: O(n)