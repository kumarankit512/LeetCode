class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = 10000
        sum = 0
        for id, x in enumerate(s):
            curr = romanNum[x]
            sum = sum + curr
            if prev < curr:
                sum = sum - prev - prev
            prev = curr
        return sum

#Time Complexity: O(n)
#Space Complexity: O(1)