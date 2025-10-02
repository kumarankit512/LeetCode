class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        exchange = numExchange

        while empty >= exchange:
            empty -= exchange
            drunk += 1
            empty += 1
            exchange += 1

        return drunk

#Time Complexity: O(n)
#Space Complexity: O(1)