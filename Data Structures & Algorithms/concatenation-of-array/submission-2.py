class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums * 2
        # return nums + nums
        result = []
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)
        return result
        
        