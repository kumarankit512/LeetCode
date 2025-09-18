class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.map = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            self.map[taskId] = (priority, userId)
            self.heap.append((-priority, -taskId))
        
        heapq.heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId))
    
    def edit(self, taskId: int, newPriority: int) -> None:
        self.map[taskId] = (newPriority, self.map[taskId][1])
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.map[taskId]
        
    def execTop(self) -> int:
        while self.heap:
            negatedPriority, negatedTaskId = heapq.heappop(self.heap)
            priority, taskId = abs(negatedPriority), abs(negatedTaskId)
        
            if taskId in self.map and self.map[taskId][0] == priority:
                userId = self.map[taskId][1]
                del self.map[taskId]
                return userId
        return -1
        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()