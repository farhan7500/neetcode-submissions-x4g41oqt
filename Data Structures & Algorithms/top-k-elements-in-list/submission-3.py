class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for num in nums:
            try:
                nums_dict[num] += 1
            except KeyError:
                nums_dict[num] = 1

        element_count_list = []
        for i in range(len(nums)):
            element_count_list.append([])

        for key, value in nums_dict.items():
            element_count_list[value - 1].append(key)

        result = []
        for element in element_count_list[::-1]:
            if len(element) != 0:
                result.extend(element)
                if len(result) >= k:
                    return result
        return None

        
                
        