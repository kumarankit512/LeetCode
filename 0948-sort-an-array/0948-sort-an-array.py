class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        Procedure:
        1) Split the array into two halves
        2) Use the divide and conquer method:
            - Recursively sort the left half.
            - Recursively sort the right half.
        3) Merge the two sorted halves into a single sorted array
            - Compare the first elements of both halves.
            - Append the smaller one to the result.
            - Continue until all elements from both halves are merged.
        3) Return the merged sorted array.
        '''

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Add remaining elements
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result
        
        return mergeSort(nums)

#Time Complexity: O(n log n)
#Space Complexity: O(n)