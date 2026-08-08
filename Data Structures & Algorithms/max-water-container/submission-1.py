class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0
        max_left_h = 0
        max_right_h = 0
        while left < right :
            max_left_h = max(heights[left], max_left_h)
            max_right_h = max(heights[right], max_right_h)
            length = min (max_left_h, max_right_h)
            area = length * (right - left )
            max_area = max(area, max_area)

            if heights[left] < heights[right] :
                left += 1
            else :
                right -= 1
        return max_area