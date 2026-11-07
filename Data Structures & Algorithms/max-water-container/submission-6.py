class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum_area = 0

        while left < right:
            current_area = min(heights[left], heights[right]) * (right - left)
            maximum_area = max(maximum_area, current_area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maximum_area

        