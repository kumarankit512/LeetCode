class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # We first check if the elements exist in both arrays -> nums1[i] == nums2[j] and if it does we find the next greater element on the right. If there are no more elements in the array or no next greater element we return -1 else we return the next greatest element closest to the current element.

        result = []
        for i in range(len(nums1)):
            found = False
            nge = -1

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            nge = nums2[k]
                            found = True
                            break
                    break
            result.append(nge)
        return result
        
# Brute Force Soltion:
# Time Complexity: O(m * n)
# Space Complexity: O(m)

