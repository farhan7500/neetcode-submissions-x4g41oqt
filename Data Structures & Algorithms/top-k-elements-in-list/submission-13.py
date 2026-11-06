class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrence_list = [[] for _ in range(len(nums) + 1)]

        count_map = Counter(nums)

        for key, value in count_map.items():
            occurrence_list[value].append(key)

        result = []

        for el in range(len(occurrence_list) - 1, 0, -1):
            if el and len(result) < k:
                result.extend(occurrence_list[el])

        return result
