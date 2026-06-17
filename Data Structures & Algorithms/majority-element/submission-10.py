class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        for num in nums:
            if candidate is None:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            elif count == 1:
                candidate = num
            else:
                count -= 1

        return candidate
        