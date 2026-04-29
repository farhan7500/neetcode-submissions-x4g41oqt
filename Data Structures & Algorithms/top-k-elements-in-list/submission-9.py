class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                # Create an occurrence map
        count_map = Counter(nums)

        # Create a list with len(nums) elements and assign empty list to
        # all the indices
        bucket_list = []
        for i in range(len(nums)):
            bucket_list.append([])


        # Iterate through counter map and populate the list
        # with following rules
        # 1. The value is the (index - 1)
        # 2. The key is appended to the list value in the list
        for key, value in count_map.items():
            bucket_list[value - 1].append(key)


        # Iterate backwards and fetch the first k elements
        result_list = []
        for idx in range(len(bucket_list) - 1, -1, -1):
            if len(result_list) == k:
                break
            for el in bucket_list[idx]:
                result_list.append(el)
                if len(result_list) == k:
                    break

        return result_list
        