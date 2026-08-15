class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i))+ '#'+ i
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = s[i:j]
            res.append(s[j+1:j+1+int(length)])
            i = j+1+int(length)
        return res