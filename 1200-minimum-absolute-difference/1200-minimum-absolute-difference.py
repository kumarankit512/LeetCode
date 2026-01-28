class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float('inf')
        res = []
        arr.sort()
        for i in range(1, len(arr)):
            currDiff = abs(arr[i] - arr[i - 1])
            if currDiff < minDiff:
                minDiff = currDiff
                res = [[arr[i - 1], arr[i]]]
            elif currDiff == minDiff:
                res.append([arr[i - 1], arr[i]])
        return res