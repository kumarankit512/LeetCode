class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        1) Initialize pointers
            - Set two indices i and j starting at 0 for word1 and word2
            - Use a result list to collect characters.
        2) Iterate through both strings
            - While i < len(word1) and j < len(word2)
            - Append word1[i] to result
            - Append word2[j] to result
            - Increment both i and j
        3) Handle leftovers
            - If word1 still has characters left, append them
            - If word2 still has characters left, append them
        4) Return result
            - Join the result list into a single string and return it
        '''

        i = 0 
        j = 0
        result = []

        # Merge alternately while both have characters
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append leftovers
        if i < len(word1):
            result.append(word1[i:])
        if j < len(word2):
            result.append(word2[j:])

        return "".join(result)

#Time Complexity: O(n + m) where n = len(word1) and  m = len(word2) -> O(n)
#Space Complexity: O(n + m) -> O(n)