class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        '''
        Procedure:
        1) Build row by row up to rowIndex
            -> For each row i from 1 to rowIndex:
                Append 1 at the end
                Update middle elements from right to left
        2) Update the elements from right to left 
            -> For j from i-1 down to 1
        3) Return the final row
        '''

        row = [1]

        for i in range(1, rowIndex + 1):
            row.append(1)
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row

        #Time Complexity: O(n^2)
        #Space Complexity: O(n)