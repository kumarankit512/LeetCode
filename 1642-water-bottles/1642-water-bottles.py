class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        '''
        Procedure:
        1) Initialize 3 instances
            - drunk = 0 (total bottles drunk)
            - full = numBottles (initial full bottles)
            - empty = 0 (initial empty bottles)
        2) While you have full bottles:
            - Drink all full bottles -> add them to drunk
            - Add those bottles to empty
            - Exchange as many empty bottles as possible:
                - new_full = empty // numExchange
                - empty = (empty % numExchange) + new_full
            - Set full = new_full
        3) Repeat until no more full bottles remain
        4) Return drunk
        '''

        drunk = 0
        full = numBottles
        empty = 0
        
        while full > 0:
            # Drink all full bottles
            drunk += full
            empty += full
            
            # Exchange empty bottles for new full bottles
            full = empty // numExchange
            empty = empty % numExchange
        
        return drunk

#Time Complexity: O(n)
#Space Complexity: O(1)