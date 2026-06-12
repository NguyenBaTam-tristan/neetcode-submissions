class Solution:
    def maxArea(self, h: List[int]) -> int:
        left = 0
        right = len(h) - 1
        max_record = 0
        while left <= right:
            record = min(h[right], h[left]) * (right - left)
            max_record = max(max_record, record)
            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
        return max_record




        