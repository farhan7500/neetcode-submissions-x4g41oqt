class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize a list of len(nums) elements, each element is an empty list
        count_list: list = []
        for _ in nums:
            count_list.append([])

        # Get a count of each element in the list and place it in the (n - 1)th index
        num_count_map: dict[int, int] = Counter(nums)
        for key, value in num_count_map.items():
            count_list[value - 1].append(key)

        # Traverse the list in reverse order
        #   If the element is a non-empty list, add it to result until result length is k
        result = []
        for idx in range(len(count_list) - 1, -1, -1):
            if count_list[idx] and len(result) < k:
                result.extend(count_list[idx])

        # return the result
        return result
        