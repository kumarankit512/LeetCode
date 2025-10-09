class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        '''
        Procedure:
        1) Start from the last digit
            - Because when you add 1, it might cause a carry only near the end
        2) Add 1 to the last digit
        3) If the sum is less than 10
            - Update the digit and return the array
        4) If the sum is 10 or greater
            - Set the current digit to 0
            - Carry 1 to the next more significant digit
        5) Continue this process moving leftward through the array
        6) If you reach the beginning of the array and still have a carry (For Example: [9,9,9] -> [0,0,0] with carry 1)
            - Insert 1 at the beginning of the array
        7) Return the updated array
        '''

        n = len(digits)

        # tart from the last digit
        for i in range(n - 1, -1, -1):
            digits[i] += 1 

            if digits[i] < 10:
                return digits   #No carry, return result

            digits[i] = 0       #Carry over to the next digit

        #If all digits were 9, add 1 at the beginning
        return [1] + digits

#Time Complexity: O(n)
#Space Complexity: O(1)