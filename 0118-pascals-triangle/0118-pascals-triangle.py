class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # if numRows < 1:
        #     return []

        res = []
        for i in range(numRows):
            row = []
            num = i
            for j in range(i + 1):
                if j == i or j == 0:
                    row.append(1)
                else:
                    num = res[i - 1][j - 1] + res[i - 1][j]
                    row.append(num)
            res.append(row)
        
        return res
        
        #Time Complexity: O(n^2)
        #Space Complexity: O(n^2)