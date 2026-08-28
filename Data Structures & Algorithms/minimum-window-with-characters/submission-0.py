class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c,0)+1
        left =0
        have =0
        min_len = float('inf')
        min_start = 0
        window = {}

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have+=1
            while have == len(need):
                current_len = right -left +1
                if current_len < min_len:
                    min_len = current_len
                    min_start = left
                window[s[left]] -=1
                if window[s[left]] == 0:
                    del window[s[left]] 
                if s[left] in need and window.get(s[left],0) < need[s[left]]:
                    have -=1
                left+=1
        if min_len == float('inf'):
            return ""
        else:
            return s[min_start:min_start+min_len]