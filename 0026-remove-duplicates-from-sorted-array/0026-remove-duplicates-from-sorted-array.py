class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        '''
        Procedure:
        1) Initialize a pointers:
            -> i = 0 which represents index of the last unique element
        2) Create a while loop to iterate through the array 'nums'
            -> Use another pointer j starting from index 1 and move through the array
        3) Compare elements
            -> if nums[j] != nums[i] 
                -> that means we found a new unique element
            -> Move i forward (i += 1) and copy that unique element to nums[i] = nums[j]
        4) Repeat the process until we reach the end of the array
        5) Return the number of unique elements
            -> return i + 1
        '''

        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

#Time Complexity: O(n)
#Space Complexity: O(1)