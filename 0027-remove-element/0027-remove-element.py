class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        1) Use two pointers:
            - One pointer i to iterate over the array
            - Another pointer k to mark the position where the next "valid" element should go
        2) Iterate through the array:
            - For each element nums[i]:
            - If it is not equal to val:
            - Place it at nums[k].
            - Increment k.

        3) At the end
            - After the loop, k will represent the number of elements that are not equal to val.
            - Return k.
        '''

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

#Time Complexity: O(n)
#Space Complexity: O(1)