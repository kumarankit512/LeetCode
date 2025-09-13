class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''
        Procedure:
        - Given the array of integers 'arr' and integer 'k' we need to find least number of unique integers after removing 'k' elements. In other words, given the 'k' we have to remove 'k' numbers from the array and return the remaining types of unique numbers. 

        Psuedo:
        -> Brute Force Approach:
            - Sort the array
                -> sorted_list = sorted(arr)
            - Loop through the array
            - Remove the first few distinct 'k' elements from the array
            - Return the number of remaining distinct elements
        '''

        # Keep track of the frequency of each element
        freq = Counter(arr)
        
        #Sort the array based on the frequency of the values inside the array
        sorted_list = sorted(freq.values())
        
        #Remove the least frequent elements first
        removed = 0
        for count in sorted_list:
            if k >= count:
                k -= count
                removed += 1
            else:
                # Can't fully remove this element, stop
                break
        else:
            # If we finish the loop, all unique numbers are removed
            return 0
        
        # Subtract and return the number of fully removed elements
        return len(sorted_list) - removed

#Time Complexity: O(n log n)
#Space Comlexity: O(n)