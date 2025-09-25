class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Procedure:
        1) Handle trivial case
            - If x == 0 or x == 1, return x.
        2) Set binary search range
            - Left = 1
            - Right = x // 2 -> because sqrt(x) <= x/2 when x > 1
        3) Binary search loop
            - While left <= right:
                - Compute mid = (left + right) // 2
                - If mid * mid == x -> return mid.
                - If mid * mid < x -> move left = mid + 1 (keep track of mid as a possible answer).
                - Else -> move right = mid - 1.
        4) Return answer
            - When the loop ends, right will be the floor of sqrt(x)
        '''

        if x == 0 or x == 1:
            return x

        left = 1
        right = x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

#Time Complexity: O(log x)
#Space Complexity: O(1)
