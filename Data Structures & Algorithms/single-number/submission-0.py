class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                num_set.remove(num)

        for num in num_set:
            return num
        