class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Procedure:
        - Create a hash map to store the last index of each number.
        - Iterate through the array with index i:
            - If nums[i] is already in the map and the distance i - map[nums[i]] <= k, return True.
            - Otherwise, update the map with nums[i] = i
        - If no such pair is found after looping, return False.
        '''

        lastIndex = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in lastIndex:
                if i - lastIndex[num] <= k:
                    return True
            lastIndex[num] = i   # update last index of this number
        return False

#Time Complexity: O(n)
#Space Complexity: O(n)