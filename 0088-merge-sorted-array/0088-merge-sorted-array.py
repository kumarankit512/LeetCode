class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Initialize three pointers:
        # i points to the last element in the initial portion of nums1.
        # j points to the last element in nums2.
        # k points to the last position of nums1, where the merged element will be placed.
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Iterate until all elements of nums2 are placed in nums1.
        while j >= 0:
            # If nums1's current element is greater than nums2's current element,
            # place nums1's element at position k and move pointer i to the left.
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            # Otherwise, place nums2's element at position k and move pointer j to the left.    
            else:
                nums1[k] = nums2[j]
                j -= 1
            # Move pointer k to the left, as we have placed an element in nums1[k].
            k -= 1