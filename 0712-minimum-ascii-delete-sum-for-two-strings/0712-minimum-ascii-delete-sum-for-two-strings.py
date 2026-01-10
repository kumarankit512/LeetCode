class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        '''
        DP Approach

        Procedure:
        1) Get the length of the string
        2) Create the dp table
        3) Handle base case (If s2 is empty)
            - If s2 is exhausted (j == n), we must delete all remaining characters in s1
        4) Handle Base Case (If s1 Is Empty)
            - If s1 is exhausted (i == m), we must delete all remaining characters in s2
        5) Complete the dp table
        6) Check if the characters match
            - If characters are equal, no deletion needed
            - Else, Delete s1[i] or Delete s2[j] -> Choose the cheaper one
        7) Return the Final Answer
        '''

        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])

        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])

        # Fill DP table
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )

        return dp[0][0]

        #Time Complexity: O(m x n)
        #Space Complexity: O(m x n)
