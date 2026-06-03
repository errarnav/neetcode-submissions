class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1

        
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                new_val = heapq.heappop(maxHeap) # most freq element
                new_val = new_val + 1 # now processed
                if new_val < 0: # needs some more processing to do 
                    q.append([new_val, time + n]) # append it to our cooldown queue


            if q and q[0][1] == time:
                elem = q.popleft()[0]
                heapq.heappush(maxHeap, elem)
        
        return time
            