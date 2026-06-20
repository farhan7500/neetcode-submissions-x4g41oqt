class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = Counter(tasks)
        max_heap = [-n for n in count_map.values()]
        heapq.heapify(max_heap)

        queue = deque()
        time = 0
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time