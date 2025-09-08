class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        '''
        Conditions:
        1) Each a should have a corresponding b - Satisfies the 2nd condition
        2) b cannot have a corresponding a - Satisfies the 1st condition 
            - Return -1 if it does
        '''

        for judge in range(1, n + 1):
            trusting = True
            trusted_upon = 0

            for a, b in trust:
                if a == judge:
                    trusting = False
                if b == judge:
                    trusted_upon += 1
                    
            # If this person trusts no one, and all the other people trust them, then they are the judge.
            if trusting and trusted_upon == n - 1:
                return judge
        return -1

#Brute Force Soluion:
#Time Complexity: O(n * m)
#Space Complexity: O(1)