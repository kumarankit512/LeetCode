class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        '''
        Procedure:
        1) If k is divisible by 2 or 5, return -1.
        2) Use % to avoid large numbers
            -> mod = 1 % K (this represents the number “1”)
            -> length = 1

        Example: 
        k = 3
        1 -> remainder = 1
        11 -> remainder = (110 + 1) % 3 = 2
        111 -> remainder = (210 + 1) % 3 = 0

        answer = 3
        '''

        if k % 2 == 0 or k % 5 == 0: 
            return -1

        mod = 1 % k
        length = 1

        while mod != 0:
            mod = (mod * 10 + 1) % k
            length += 1
        
        return length

#Time Complexity: O(k)
#Space Complexity: O(1)