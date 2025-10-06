class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        if numFriends == 1:
            return word
        
        n = len(word)
        max_len = n - numFriends + 1
        res = " "

        for i in range(len(word)):
            strs = word[i : i + max_len]  
            if strs > res:
                res = strs
        return res

#Time Complexity: O(n^2)
#Space Complexity: O(n)