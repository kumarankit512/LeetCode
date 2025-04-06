class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  
            return []
       
        result = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"  
        }
       
        for digit in digits:
            temp = []
            for s in result:
                for c in digitToChar[digit]:
                    temp.append(s + c)
            result = temp
        return result