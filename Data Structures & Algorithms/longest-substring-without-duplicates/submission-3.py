class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left =0
        right =0
        max_len =0
        seen = set()
        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                length = right- left +1
                max_len = max(length, max_len)
                right+=1
            else:
                seen.remove(s[left])
                left+=1
        return max_len
