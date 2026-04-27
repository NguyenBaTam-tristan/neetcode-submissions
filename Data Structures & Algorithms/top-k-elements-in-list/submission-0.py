class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else: freq[n] += 1
        items = list(freq.items())
        for i in range(len(items)):
            for j in range(i+1, len(items)):
                if items[j][1] > items[i][1]:
                    items[i], items[j] = items[j], items[i]
        return [k for k,v in items[:k]]
s = Solution()
print(s.topKFrequent([1,2,2,3,3,3],2))

        
        