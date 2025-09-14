class Solution:
    def minOperations(self, logs: List[str]) -> int:
        '''
        Procedure:
        - Start at depth 0 (main folder).
        - Iterate through each log in the list:
            - If the log is "../" → decrease depth by 1 (but depth cannot go below 0).
            - If the log is "./" → do nothing.
            - If the log is "x/" → increase depth by 1 (move into subfolder).
        - After processing all logs, the depth value represents how far you are from the main folder.
        - At the end Return depth
        '''

        stack = []
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log != "./":
                stack.append(log)
        return len(stack)