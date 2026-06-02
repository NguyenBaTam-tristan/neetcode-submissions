class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        n = len(temps)
        res = [0]*n
        for i in range(n):
            while stack and temps[i] > temps[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i)
        return res




        