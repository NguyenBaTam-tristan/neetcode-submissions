class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        result = []
        for num in nums:
            if num != 0:
                prod *= num
            else: 
                zero_count += 1
        if zero_count > 1: return [0] * len(nums)
        for num in nums:
            if zero_count == 1:    
                if num != 0:
                    result.append(0)
                else: 
                    result.append(prod)
            elif zero_count == 0:
                result.append(prod // num)
        return result 
             



        