
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrence_list = []
        for idx in range(len(nums)):
            occurrence_list.append([])

        count_map = {}
        for num in nums:
            try:
                count_map[num] += 1
            except KeyError:
                count_map[num] = 1

        for key, value in count_map.items():
            occurrence_list[value - 1].append(key)

        result_list = []
        result_count = 0
        for idx in range(len(occurrence_list) - 1, -1, -1):
            if occurrence_list[idx]:
                if result_count != k:
                    result_list.extend(occurrence_list[idx])
                    result_count = len(result_list)
        return result_list
