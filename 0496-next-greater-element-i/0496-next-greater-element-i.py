class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

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


