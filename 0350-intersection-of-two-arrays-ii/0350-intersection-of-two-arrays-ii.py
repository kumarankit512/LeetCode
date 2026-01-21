class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        '''
        Hash map approach

        Procedure:
        1) Count frequencies of elements in nums1
        2) Iterate through nums2
            -> If the element exists in the map and count > 0:
                -> Add it to the result
                -> Decrease the count
        3) Return the result list
        '''

        #Count frequency of elements in nums1
        freq = Counter(nums1)
        
        result = []
        
        #Iterate through nums2
        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        
        #Return result
        return result

        #Time Complexity: O(n + m)
        #Space Complexity: O(n)