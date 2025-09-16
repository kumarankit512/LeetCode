import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        #
        # [] -> stack

        #[6, 4] ->  LCM(stack.pop(), stack.pop())
        #[12]
        #[12, 3] -> 
        # [12]
        # [12, 2] -> do GCD first -> pop back both -> DO LCM and push back into the stack
        # [12]
        #[12, 7] 
        #[12, 7, 6, 2]
        #  [12, 7] -> o GCD first -> pop back both -> DO LCM and push back into the stack
        #[12, 7, 6] -> final answer


        # [a]
        # [a,b] (a,b coprime)
        # [a,b,c] (b,c not coprime) -> [a,d] (a,d not coprime) -> [z]
        # [z,e]
        def gcd(n1,n2):
            return math.gcd(n1,n2)
        def lcm(n1,n2):
            return math.lcm(n1,n2)
        # nums = [6,4,3,2,7,6,2]
        # stack = []
        # [ 6 ]
        # [ 6, 4 ]
        # [ 12 ]
        # [ 12, 3 ]
        # [ 12 ]
        # [ 12, 2 ]
        # [ 12 ]
        # [ 12, 7 ]
        # [12, 7, 6 ]
        # [ 12, 7, 6, 2]
        # [ 12, 7, 6]
        stack = []
        for i in range(len(nums)):
            stack.append(nums[i])
            while stack and len(stack) > 1:
                first = stack.pop()
                second = stack.pop()
                if gcd(first, second) > 1:
                    temp = lcm(first, second)
                    stack.append(temp)
                else:
                    stack.append(second)
                    stack.append(first)
                    break
        return stack
            
            
                
                
            
            
        
        