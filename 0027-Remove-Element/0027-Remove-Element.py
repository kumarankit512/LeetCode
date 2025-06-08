class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Get the initial size of the list.
        size = len(nums)
        # Initialize two pointers:
        # i will be used to iterate over the list.
        # j will point to the last valid element in the list (end of the list).
        i = 0
        j = size - 1
        # Iterate while i is less than or equal to j.
        # This ensures that all elements up to the end have been checked.
        while i <= j:
            # If the element at index i is equal to the target value val:
            if nums[i] == val:
                # Swap the element at index i with the element at index j.
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                # Remove the last element from the list using pop().
                # This effectively discards the element that equals val.
                nums.pop()
                # Decrement j because the size of the list has decreased.
                j -= 1
                # Use 'continue' to skip incrementing i in this case,
                # as the new element at index i needs to be checked.
                continue
            # Increment i if nums[i] is not equal to val.    
            i+=1
        return size