class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ref = {}
        for task in tasks:
            ref[task] = ref.get(task, 0) + 1

        maxHeap = [-i for i in ref.values()]
        heapq.heapify(maxHeap)

        q = collections.deque()

        minutes = 0
        while maxHeap or q:
            minutes += 1

            if q:
                if q[0][1] == minutes:
                    task, readyTime = q.popleft()
                    heapq.heappush(maxHeap, task)

            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task != 0:
                    q.append([task, minutes + 1 + n])
            
        return minutes
