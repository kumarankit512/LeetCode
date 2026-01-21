class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
        Procedure:
        1) Convert the arrays to sets in order to remove the duplicates
        2) Find the intersection
        3) Convert the result back to a list
        '''

        set1 = set(nums1)
        set2 = set(nums2)
        
        #Find the intersection
        common_elements = set1 & set2
        
        #Convert result to list and return
        return list(common_elements)

        #Time Complexity: O(n + m)
        #Space Complexity: O(n + m)