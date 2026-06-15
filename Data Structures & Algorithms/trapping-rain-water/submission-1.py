class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        start = 0
        end = len(height) - 1
    
        def find_start_and_end(start, end):
                for h in range(len(height) - 1):
                    if height[start] < height[start + 1]:
                        start += 1
                    else:
                        break
                for h in range(len(height) - 1, -1 ,-1):
                    if height[end] < height[end-1]:
                        end -= 1
                    else:
                        break
                return start, end
        
        max_val = -1
        max_index = -1 
        def find_highest(max_val, max_index):
            for h in range(len(height)):
                if height[h] > max_val:
                    max_val = height[h]
                    max_index = h
            return max_val, max_index

        posible_range = find_start_and_end(start, end)
        max_info = find_highest(max_val, max_index)

        slow_left = posible_range[0]
        fast_left = posible_range[0] + 1
        
        while slow_left < fast_left and fast_left <= max_info[1]:
            if height[slow_left] > height[fast_left]:
                total_water -= height[fast_left]
                fast_left += 1
            else:
                total_water += (fast_left - slow_left - 1) * height[slow_left]
                slow_left = fast_left
                fast_left += 1
        
        slow_right = posible_range[1]
        fast_right = posible_range[1] - 1

        while slow_right > fast_right and fast_right >= max_info[1]:
            if height[slow_right] > height[fast_right]:
                total_water -= height[fast_right]
                fast_right -= 1
            else:
                total_water += (slow_right - fast_right - 1) * height[slow_right]
                slow_right = fast_right
                fast_right -= 1
        
        return total_water
                


        
        