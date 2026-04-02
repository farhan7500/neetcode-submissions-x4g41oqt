class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a map for number:occurance
        num_map = {}
        occurance_list = []
        for num in nums:
            occurance_list.append([])
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        # Populate the list based on occurance
        for num, occurance in num_map.items():
            occurance_list[occurance-1].append(num)

        result_list = []
        current = 0
        while current != k:
            current_top = occurance_list.pop()
            if len(current_top) != 0:
                result_list.extend(current_top)
                current += len(current_top)
        return result_list
