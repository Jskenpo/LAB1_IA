from collections import deque
import heapq

class QueueFIFO:
    def __init__(self):
        self.queue = deque()

    def empty(self) -> bool:
        return len(self.queue) == 0
    
    def first(self):
        return self.queue[0]

    def remove_first(self):
        return self.queue.popleft()
    
    def insert(self, element):
        self.queue.append(element)

class QueueLIFO:
    def __init__(self):
        self.queue = []

    def empty(self) -> bool:
        return len(self.queue) == 0
    
    def first(self):
        return self.queue[-1]

    def remove_first(self):
        return self.queue.pop()
    
    def insert(self, element):
        self.queue.append(element)  
        return self.queue

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def empty(self) -> bool:
        return len(self.queue) == 0
    
    def first(self):
        return self.queue[0]

    def remove_first(self):
        return heapq.heappop(self.queue)
    
    def insert(self, element):
        heapq.heappush(self.queue, element)
    


