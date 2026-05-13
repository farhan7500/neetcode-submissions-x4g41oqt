class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        result = nums[0]

        while i <= j:
            if nums[i] <= nums[j]:
                result = min(result, nums[i])
                break

            mid = (i + j) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[i]:
                i = mid + 1
            else:
                j = mid - 1
        return result
                

        
        