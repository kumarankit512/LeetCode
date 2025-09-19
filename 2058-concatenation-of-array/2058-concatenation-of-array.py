class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        Procedure:
        - Initialize an empty array 'ans' of size 2 * n
        - Iterate through each index i from 0 to n - 1
            - Set ans[i] = nums[i]
            - Set ans[i + n] = nums[i]
        - After finishing the loop, return res
        '''

        n = len(nums)
        ans = [0] * (2 * n)
        
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans

#Time Complexity: O(n)
#Space Complexity: O(n)