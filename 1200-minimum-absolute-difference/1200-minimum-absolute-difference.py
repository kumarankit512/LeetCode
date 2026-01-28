class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        '''
        Sorting Approach

        Procedure:
        1) Sort the array to bring close numbers next to each other
        2) Find the minimum difference between adjacent elements
        3) Collect all pairs with that minimum difference and add pairs where the difference equals the minimum
        4) Return the result
        '''

        arr.sort()
        
        #Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        
        #Collect all pairs with the minimum difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
        
        return result

        #Time Complexity: O(n log n)
        #Space Complexity: O(1)