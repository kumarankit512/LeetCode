class Solution:
    def numOfWays(self, n: int) -> int:
        
        '''
        Given:
            - No two adjacent cells in the same row can have the same color.
            - No two adjacent cells in the same column can have the same color
            - Return the number of valid ways mod 10^9 + 7

        Procedure:
        1) Count ways for the first row
        Type A (ABA):
            Choose color for A → 3 ways
            Choose color for B → 2 ways
            Total: 3 × 2 = 6
        Type B (ABC):
            Choose 3 distinct colors → 3 × 2 × 1 = 6

        2)Transition between rows
            For every new row, count how many ways it can follow the previous row:
            
            From previous ABA row
                New ABA rows → 3 ways
                New ABC rows → 2 ways

            From previous ABC row
                New ABA rows → 2 ways
                New ABC rows → 2 ways

        3) Dynamic Programming Update
            For each row from 2 to n:
            Take modulo 10⁹ + 7 at every step.
        '''

        MOD = 10**9 + 7
        
        # Base case: first row
        same = 6  # ABA pattern
        diff = 6  # ABC pattern
        
        for _ in range(2, n + 1):
            new_same = (same * 3 + diff * 2) % MOD
            new_diff = (same * 2 + diff * 2) % MOD
            same, diff = new_same, new_diff
        
        return (same + diff) % MOD

        #Time Complexity: O(n)
        #Space Complexity: O(1)