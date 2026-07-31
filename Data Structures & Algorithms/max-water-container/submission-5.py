class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area: int = 0
        left: int = 0
        right: int = len(heights) - 1
        while left < right:
            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area
