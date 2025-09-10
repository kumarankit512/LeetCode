class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        '''
        Given:
        1) Number of gifts
        2) K, which is the time in seconds

        We are using a heap because we want to find the max number of remaining gifts afer k seconds. We also have to use a priority queue because we wannt to prioritize the PILE with the max number of gifts.

        Pseudo:
        1. Heapify the given array list
        2. Loop through the end of the heap
        3. Find the pile with max number of gifts
        4. Take the square root of the pile
        5. Perform an inplace operation on the pile
        6. Once you loop through the entire heap, return the sum 
        '''

        # nums = []
        # for n in gifts:
        #     nums.append(-n)
        # heapify(nums)

        nums = [-num for num in gifts]
        heapify(nums)
        
        while k > 0:
            largest_pile = -heappop(nums)
            temp = int(sqrt(largest_pile))
            heappush(nums, -temp)
            k -= 1
        return -sum(nums)

#Time Complexity: O(n + k log n) because we heapify the array and perform heappop and heappush at each iteration.
#Space Complexity: O(1)