class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_area=0
        while left < right:
            current_height = min(heights[left], heights[right])
            current_width = right - left
            current_area = current_height*current_width
            if current_area > max_area:
                max_area = current_area
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_area