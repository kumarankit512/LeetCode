class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        '''
        Procedure:
        - Iterate through each item in prices from left to right.
        - For each item prices[i]:
            - Look at the items to its right (prices[j], where j > i).
            - Find the first one such that prices[j] <= prices[i].
            - If found, subtract prices[j] from prices[i] and record the discounted price.
            - If not found, just keep prices[i] as it is.
        - Return the resulting array.
        '''

        #Brute Force Approach:
        # n = len(prices)
        # result = prices[:]
        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if prices[j] <= prices[i]:
        #             result[i] -= prices[j]
        #             break
        # return result

#Time Complexity: O(n^2)
#Space Complexity: O(n)

        #Optimized Solution using a Stack:
        stack = []
        n = len(prices)

        for i in range(n):
            # while stack has items and current price <= price at top index
            while stack and prices[i] <= prices[stack[-1]]:
                index = stack.pop()
                prices[index] -= prices[i]  # apply discount
            stack.append(i)  # push current index to stack

        return prices

#Time Complexity: O(n)
#Space Complexity: O(n)