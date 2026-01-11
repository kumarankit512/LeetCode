class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        '''
        One line approach however, it uses extra space for split()
        '''
        # return len(s.strip().split()[-1])

        #Time Complexity: O(n)
        #Space Complexity: O(n)

        '''
        Optimized Solution

        Procedure:
        1) Edge cases:
            - The string may have trailing spaces
            - There may be multiple spaces between words
            - The string is guaranteed to contain at least one word
        2) Remove trailing spaces
        3) Traverse the string from the end
            - Start counting characters from the last character
            - Stop when you encounter a space
        4) Return the count
        5)
        '''

        s = s.rstrip()   # Remove trailing spaces
        length = 0
        
        # Count characters of the last word
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            length += 1
        
        return length

        #Time Complexity: O(n)
        #Space Complexity: O(1)