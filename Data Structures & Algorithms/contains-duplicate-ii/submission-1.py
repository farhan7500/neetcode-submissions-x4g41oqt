class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                num_set.remove(nums[left])
                left += 1
            if nums[right] in num_set:
                return True
            num_set.add(nums[right])

        return False
