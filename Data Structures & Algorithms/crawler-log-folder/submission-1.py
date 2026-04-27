class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for l in logs:
            if l[0] == '.':
                if l[1] == '.': res = max(0, res-1)
            else:
                res += 1
        return res


        