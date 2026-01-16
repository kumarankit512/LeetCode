class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        '''
        Procedure:
        1) Add field boundaries
            -> Horizontal fences: add 0 and n
            -> Vertical fences: add 0 and m
        2) Sort the fences
        3) Find all the gaps to find the distance between the fences
            -> For every pair of fences: 
                -> gap = fence[j] - fence[i]   (j > i)
        4) Find common gaps
            -> A square is possible only when the same distance exists in both directions
        5) Calculate the area
        '''

        MOD = 10**9 + 7

        # Add boundaries
        hFences = hFences + [1, m]
        vFences = vFences + [1, n]

        # Sort the fences
        hFences.sort()
        vFences.sort()

        # Find all horizontal gaps (heights)
        horizontal_gaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                horizontal_gaps.add(hFences[j] - hFences[i])

        # Find all vertical gaps (widths)
        vertical_gaps = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                vertical_gaps.add(vFences[j] - vFences[i])

        # Find the largest common gap
        max_side = 0
        for gap in horizontal_gaps:
            if gap in vertical_gaps:
                max_side = max(max_side, gap)

        # Return result
        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD

        # Time Complexity: O(H^2 + V^2)
        # Space Complexity: O(H^2 + V^2)