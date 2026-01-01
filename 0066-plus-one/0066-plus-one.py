class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        '''
        Procedure:
        1) Iterate backwards, starting from the last digit
        2) Add 1 to the last digit
        3) If the sum is less than 10
            - Update the digit and return the array
        4) If the sum is 10 or greater
            - Set the current digit to 0
            - Carry 1 to the next more significant digit
        5) If you reach the beginning of the array and still have a carry (For Example: [9,9,9] -> [0,0,0] with carry 1)
            - Insert 1 at the beginning of the array
        6) Return the updated array
        '''

        n = len(digits)

        for i in range(n - 1, -1, -1):
            digits[i] += 1 

            if digits[i] < 10:
                return digits

            digits[i] = 0

        return [1] + digits

        #Time Complexity: O(n)
        #Space Complexity: O(n)