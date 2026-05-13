class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''.join(str(len(word)) + '#' + word for word in strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        # 1.Initialize res & i
        result = []
        i = 0
        # 2.Loop
        while i < len(s):
            # 2.1. Small loop to move j
            j = i
            while s[j] != '#':
                j += 1
            # 2.2. Find length
            length = int(s[i : j])
            # 2.3. Find word then append it into result
            word = s[j+1 : j+1+length]
            result.append(word)
            # 2.4. i new step
            i = j + 1 + length
        # 3.Return result
        return result







            
