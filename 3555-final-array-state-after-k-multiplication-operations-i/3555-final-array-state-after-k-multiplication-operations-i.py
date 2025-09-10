class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        '''
        Given:
        1) Array 'nums
        2) integer 'k'
        3) integer 'multiplier'

        Given the array 'nums' we have to perform an operation 'k' number of times. We have to take the minimum value 'x' in the array and multiply it with the 'multiplier' however if a value appears twice in the array we take the value that appears first. In the end we return the final array. 

        Pseudo:
        1. Heapify the given array list
        2. Loop through the array to find the minimum value 'x'
        3. Mutiply the minimum value 'x' with the 'multiplier'
        5. Perform an inplace operation to replace the minimum value 'x' with x * multiplier
        6. return the array 
        '''

        # heap = [(num, i) for i, num in enumerate(nums)]
        # heapify(heap)

        heap = []
        for index in range(len(nums)):
            heap.append((nums[index], index))
        heapify(heap)
        
        while k > 0:
            min_val, index = heappop(heap)
            temp = min_val * multiplier
            #Update the value of array 'nums' at the current index with temp
            nums[index] = temp
            heappush(heap, (temp, index))
            k -= 1
        return nums

#Time Complexity: O(n + k log n)
#Space Complexity: O(1)