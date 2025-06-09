class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                result = max(result, sell - buy)
        return result

        #Time Complexity: O(n^2) but TLE - Brute Force
        #Space Complexity: O(1)

        l = 0 
        r = 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
