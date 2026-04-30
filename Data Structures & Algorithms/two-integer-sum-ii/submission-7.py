class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            actual_sum = numbers[i] + numbers[j]
            if actual_sum == target:
                return [i + 1, j + 1]
            elif actual_sum > target:
                j -= 1
            else:
                i += 1

        