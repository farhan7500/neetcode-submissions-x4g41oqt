class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        left = right = 0

        num_set = set()

        while right < len(nums):

            if nums[right] in num_set:
                return True

            # Add incoming
            num_set.add(nums[right])

            if right - left + 1 > k:
                num_set.remove(nums[left])
                left += 1



            right += 1
        
        return False

        