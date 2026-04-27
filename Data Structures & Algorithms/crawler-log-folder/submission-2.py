class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for l in logs:
            if l[1] == '.':
                if l[1] == '.': res = max(0, res-1)
            elif l[0] != '.':
                res += 1
        return res


        