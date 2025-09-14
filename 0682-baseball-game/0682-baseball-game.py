class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        Procedure:
        - Use a stack to keep track of valid scores.
        - Iterate through each operation:
            - If operation is an integer -> push it into the stack.
            - If "+" -> push the sum of the last two scores from the stack.
            - If "D" -> push double the last score from the stack.
            - If "C" -> pop the last score from the stack.
        - At the end, sum all values in the stack and return it.
        '''

        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)

#Time Complexity: O(n)
#Space Complexity: O(n)