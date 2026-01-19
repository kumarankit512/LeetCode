class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        '''
        Procedure:
        1) Initialize the result list
            -> Create an empty list triangle to store all rows
        2) Build rows one by one
            -> For each row i from 0 to numRows - 1:
                -> Create a list of size i + 1 filled with 1s for each position j inside the row (excluding first and last)
        3) Append the row
            -> Add the constructed row to triangle
        4) Return the result
        '''

        triangle = []

        for i in range(numRows):
            #Start each row with 1s
            row = [1] * (i + 1)

            #Fill the inner elements
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle
        
        #Time Complexity: O(numRows^2)
        #Space Complexity: O(numRows^2)