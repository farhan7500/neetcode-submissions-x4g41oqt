import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_list = []
        for i in range(len(nums)):
            result_list.append([])

        num_map = {}
        for num in nums:
            try:
                num_map[num] += 1
            except KeyError:
                num_map[num] = 1

        for key, value in num_map.items():
            result_list[value-1].append(key)

        total = k
        result = []
        for el_list in result_list[::-1]:
            if len(el_list) != 0:
                if len(el_list) == total:
                    return el_list
                else:
                    result.extend(el_list)
                    if len(result) == total:
                        return result
