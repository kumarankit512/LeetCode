# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        Procedure:
        1) Use a binary search because each call to guess(num) tells us whether the target is higher, lower, or equal
        2) Initialize two pointers, left and right
        3) While left <= right:
            - Compute mid = (left + right) // 2
            - Call guess(mid)
            - If it returns 0: we found the number -> return mid.
            - If it returns -1: the target is lower -> move search to left half -> right = mid - 1
            - If it returns 1: the target is higher -> move search to right half -> left = mid + 1
        '''

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid + 1

#Time Complexity: O(log n)
#Space Complexity: O(1)