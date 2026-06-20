class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []
        for point in points:
            distance = (point[0] ** 2) + (point[1] ** 2)
            dist_list.append([distance, point])
        heapq.heapify(dist_list)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(dist_list)[1])
        return result
