class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        Procedure:
        1) Initialize two counters, 'five' and 'ten' to keep track of $5 and $10 bills
        2) Loop through the array 'bills' 
            -> If bill == 5:
                -> You don’t need to give change, just increment five
            -> If bill == 10:
                -> Check whether you need to return any change 
                    -> If yes -> decrement five by 1, increment ten by 1
                    -> If no -> return False
            -> If bill == 20:
                -> You need to give back $15
                -> Use one $10 + one $5 bill (greedy choice)
                    -> If possible -> decrement ten and five
                    -> Else if you have at least three $5 bills -> decrement five by 3
                    -> Else -> return False
        4) If you finish processing all customers, return True
        '''

        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            #Check for bills > 10        
            else:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

#Time Complexity: O(n)
#Space Complexity: O(1)