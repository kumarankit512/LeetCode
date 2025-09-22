class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        '''
        1) Count frequencies
            - Use a hash map to store the frequency of each number in the array
        2) Find maximum frequency
            - Traverse the frequency map to find the highest frequency value
        3) Count elements with max frequency:
            - For each number in the array, if its frequency equals the maximum frequency, add that frequency to the answer
        '''
        #Count frequencies of each element in the array
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        #Find the maximum frequency
        max_count = 0
        for value in count.values():
            if value > max_count:
                max_count = value

        #Add up all elements that have this max frequency
        result = 0
        for value in count.values():
            if value == max_count:
                result += value

        return result

#Time Complexity: O(n)
#Space Complexity: O(n)