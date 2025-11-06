# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # n = mountainArr.length()
    
        # for i in range(n):
        #     if mountainArr.get(i) == target:
        #         return i
        
        # return -1

#Brute Force Approach -> Linear Solution
#Time Complexity: O(n)
#Space Complexity: O(1)

        n = mountainArr.length()
    
        #Find the peak element
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        
        # Helper function with binary search for ascending part
        def binary_search_increasing(left, right):
            while left <= right:
                mid = (left + right) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # Helper function with binary search for descending part
        def binary_search_decreasing(left, right):
            while left <= right:
                mid = (left + right) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    left = mid + 1  # reversed comparison
                else:
                    right = mid - 1
            return -1

        #Search in increasing side
        index = binary_search_increasing(0, peak)
        if index != -1:
            return index

        #Search in decreasing side
        return binary_search_decreasing(peak + 1, n - 1)