class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merged = []
        intervals.sort(key = lambda x: x[0])
        merged.append(intervals[0])
	    
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            prevMergeStart, prevMergeEnd = merged[-1]
            if prevMergeEnd < start:
                merged.append(intervals[i])
            else:
                prevMergeEnd = max(end, prevMergeEnd)
                merged[-1][1] = prevMergeEnd
        return merged

#Time Complexity: O(n log n)
#Space Complexity: O(1)