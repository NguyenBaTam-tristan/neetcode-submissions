class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_t = {}
        dict_s = {}
        for ch in t:
            if ch not in dict_t:
                dict_t[ch] = 1
            else:
                dict_t[ch] += 1
        for ch in s:
            if ch not in dict_s:
                dict_s[ch] = 1
            else:
                dict_s[ch] += 1
        return dict_t == dict_s
s = Solution()
print(s.isAnagram("racecar","carrace"))



        