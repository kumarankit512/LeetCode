class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        '''
        Procedure:
        1) Check compatibility:
            -> If str1 + str2 != str2 + str1, return ""
                -> This means they don’t share a common repeating pattern
        2) Find GCD
            -> Compute g = gcd(len(str1), len(str2))
        3) Return substring
            -> The common divisor string will be str1[:g]
        '''

        #If concatenations are not equal, there’s no common base string
        if str1 + str2 != str2 + str1:
            return ""
        
        #Helper function to compute GCD of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        #Find GCD of the lengths
        gcd_length = gcd(len(str1), len(str2))
        
        #The GCD string will be the prefix of str1 with length gcd_length
        return str1[:gcd_length]

#Time Complexity: O(m + n)
#Space Complexity: O(1)