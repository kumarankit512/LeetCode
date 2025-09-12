class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Thought Process:
        - Given an array of CPU 'tasks' which consists of letters from A to Z
        - A number 'n' which represents the number of gaps allowed
            - After processing a task there must be 'n' gaps before the same task can be processed again
        - Return an int which represents the min number of CPU intervals (time) to complete all tasks

        Pseudo:
        1) Loop through the array to identify the number of tasks and its frequency
            - Use a hashmap to store each char frequency
        2) Heapify the list
        3) Loop through the list to find the char with max freq
            - Subtract the freq by 1
        3) Keep going until we have processed all the tasks in the list
        '''

        # mp = {}
        # for task in tasks:
        #     if task not in mp:
        #         mp[task] = 0
        #     mp[task] += 1
        
        #In-built python function to keep track of all the tasks instead of having to create the whole hashmap
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapify(maxHeap)

        time = 0
        q = deque() #Pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

#Time Complexity: O(n)
#Space Complexity: O(1)