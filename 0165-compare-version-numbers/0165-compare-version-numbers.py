class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        Procedure:
        1) Split both the version strings into parts by "."
        2) Compare each part as an integer in left-to-right order
            - If one part is greater, return 1 (first is larger)
            - If one part is smaller, return -1 (second is larger)
            - If equal, move to the next part
        3) If loop ends without finding a difference, return 0
        '''

        v1 = version1.split(".")
        v2 = version2.split(".")

        while len(v1) < len(v2):
            v1.append("0")
        while len(v2) < len(v1):
            v2.append("0")

        # Compare each number one by one
        for i in range(len(v1)):
            num1 = int(v1[i])
            num2 = int(v2[i])

            if num1 > num2:
                return 1
            if num1 < num2:
                return -1

        return 0

#Time Complexity: O(n + m)
#Space Complexity: O(n + m)