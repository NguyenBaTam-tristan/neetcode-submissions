class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_lst = []
        for num in nums:
            if num in my_lst:
                return True
            my_lst.append(num)
        return False
s = Solution()
print(s.hasDuplicate([1, 2, 3, 3]))
        