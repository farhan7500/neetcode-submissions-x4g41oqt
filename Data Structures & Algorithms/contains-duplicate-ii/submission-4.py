class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        num_set =set()

        for right in range(len(nums)):
            if right - left > k:
                num_set.remove(nums[left])
                left += 1
            if nums[right] in num_set:
                return True
            num_set.add(nums[right])
        return False

nums = [1,2,3,1]
k = 3
s = Solution()
print(s.containsNearbyDuplicate(nums, k))
