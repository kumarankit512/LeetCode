class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        '''
        Brute Force

        Procedure:
        1) Iterate through each number in the array 'nums'
        2) Find all the divisors
            - Loop d from 1 to √x
            - Add d
            - Add x // d (if different)
            - Stop if divisor count exceeds 4
        3) Check divisor count
            - Add 'sum' to the answer if the total number of divisors is exactly 4
        4) Return 'total_sum'
        '''

        total_sum = 0

        for x in nums:
            divisors = set()

            d = 1
            while d * d <= x:
                if x % d == 0:
                    divisors.add(d)
                    divisors.add(x // d)

                    if len(divisors) > 4:
                        break
                d += 1

            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum

        #Time Complexity: O(n * √m)
            #n = number of elements in nums  
            #m = maximum value in nums
        #Space Complexity: O(1)
