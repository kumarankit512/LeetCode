class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = defaultdict(int)
        # for n in nums:
        #         freq[n] += 1
        # sorted_items = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        # top_k = [i[0] for i in sorted_items[:k]] 
        
        # return top_k

        #Time Complexity: O(n log n)
        #Space Complexity: O(n)

        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res

	    #Time Complexity: O(n log n)
        #Space Complexity: O(n)