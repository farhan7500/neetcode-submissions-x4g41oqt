class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if candidate is None:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count += 1
                else:
                    if count == 1:
                        candidate = num
                    else:
                        count -= 1

        return candidate
        