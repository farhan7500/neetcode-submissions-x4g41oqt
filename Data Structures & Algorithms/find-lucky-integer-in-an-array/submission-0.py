class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count_map = {}
        result = -1
        for num in arr:
            try:
                count_map[num] += 1
            except KeyError:
                count_map[num] = 1
        for key, value in count_map.items():
            if key == value:
                result = max(result, key)
        return result
        