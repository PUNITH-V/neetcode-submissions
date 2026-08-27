class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     left = 0
     result = 0
     max_freq =0
     count ={}
     for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1
        max_freq = max(max_freq, count[s[right]])
        length = right -left +1
        while length - max_freq > k:
            count[s[left]] -=1
            left+=1
            length = right -left +1
        result = max(result, length)
     return result
