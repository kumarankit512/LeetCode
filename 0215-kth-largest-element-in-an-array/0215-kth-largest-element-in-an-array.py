class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Given:
        1) integer array of 'nums'
        2) integer 'k'

        Procedure:
        - Given an integer array of 'nums' we need to find the kth largest element 'k'. 

        For example:
        nums = [1, 5, 5, 6, 3, 2] and k = 1
        Output: 6

        Output is 6 because we have to find the 1st largest number in the array 'nums' if k was 2 the output would be 5 since thats the 2nd largest number inside the array. 

        Pseudo:
        1. Create a heap
        2. Loop through the array to get each value as we loop (each time the code runs, the previous integer moves down the array)
        3. If the length of the heap is greater than k, we remove the smallest element from the heap
        4. Return the value at index 0 in the heap
        '''
        
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
