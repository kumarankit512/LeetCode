class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        Three Pointer Solution:
        Procedure:
        1) Initialize the starting position for each pointer
        2) Compare elements from the end
            -> While both i >= 0 and j >= 0
                -> If nums1[i] > nums2[j] -> place nums1[i] at nums1[k]
                -> Else -> place nums2[j] at nums1[k]
                -> Move the pointer that had the larger element
                -> Move k back
        3) If nums2 still has leftover elements
            -> Copy them into nums1
        '''

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

            #Time Complexity: O(m + n)
            #Space Complexity: O(1)