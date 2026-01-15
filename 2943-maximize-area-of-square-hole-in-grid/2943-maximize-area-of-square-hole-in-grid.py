class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        '''
        Procedure:

        1) Sort hBars and vBars
        2) Count the longest run of consecutive numbers in each
        3) Add 1 to each run to get the gap size
        4) Square the minimum of the two gaps
        '''

        hBars.sort()
        max_h = cur = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            max_h = max(max_h, cur)
        max_h += 1
        
        # Vertical bars
        vBars.sort()
        max_v = cur = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            max_v = max(max_v, cur)
        max_v += 1
        
        side = min(max_h, max_v)
        return side * side

        #Time Complexity: O(h log h + v log v)
        #Space Complexity: O(1)
